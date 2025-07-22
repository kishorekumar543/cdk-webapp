from aws_cdk import (
    Stack,
    aws_ecs as ecs,
    aws_ec2 as ec2,
    aws_iam as iam,
    aws_autoscaling as autoscaling,
    aws_ecs_patterns as ecs_patterns,
)
from constructs import Construct

class ECSStack(Stack):
    def __init__(self, scope: Construct, id: str, vpc: ec2.Vpc, **kwargs):
        super().__init__(scope, id, **kwargs)

        cluster = ecs.Cluster(self, "WebAppCluster", vpc=vpc)

        asg = autoscaling.AutoScalingGroup(self, "EcsASG",
            vpc=vpc,
            instance_type=ec2.InstanceType("t3.micro"),
            machine_image=ecs.EcsOptimizedImage.amazon_linux2(),
            min_capacity=2,
            max_capacity=4
        )

        task_role = iam.Role(self, "TaskExecutionRole",
            assumed_by=iam.ServicePrincipal("ecs-tasks.amazonaws.com")
        )
        task_role.add_managed_policy(iam.ManagedPolicy.from_aws_managed_policy_name("AmazonS3ReadOnlyAccess"))
        task_role.add_managed_policy(iam.ManagedPolicy.from_aws_managed_policy_name("CloudWatchLogsFullAccess"))

        task_definition = ecs.Ec2TaskDefinition(self, "WebAppTaskDef", task_role=task_role)

        container = task_definition.add_container("WebAppContainer",
            image=ecs.ContainerImage.from_registry("nginx"),
            memory_limit_mib=256,
            cpu=256
        )
        container.add_port_mappings(ecs.PortMapping(container_port=80))

        service = ecs.Ec2Service(self, "WebAppService",
            cluster=cluster,
            task_definition=task_definition
        )

        self.service = service
        self.cluster = cluster
