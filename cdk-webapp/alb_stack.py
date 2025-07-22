from aws_cdk import (
    Stack,
    aws_elasticloadbalancingv2 as elbv2,
    aws_ec2 as ec2,
    aws_ecs as ecs
)
from constructs import Construct

class ALBStack(Stack):
    def __init__(self, scope: Construct, id: str, vpc: ec2.Vpc, service: ecs.Ec2Service, **kwargs):
        super().__init__(scope, id, **kwargs)

        lb = elbv2.ApplicationLoadBalancer(self, "WebAppALB",
            vpc=vpc,
            internet_facing=True
        )

        listener = lb.add_listener("Listener", port=80)
        listener.add_targets("ECS", port=80, targets=[service])

        lb.connections.allow_from_any_ipv4(ec2.Port.tcp(80), "Allow HTTP")
        lb.connections.allow_from_any_ipv4(ec2.Port.tcp(443), "Allow HTTPS")

        self.alb = lb
