from aws_cdk import (
    Stack,
    aws_rds as rds,
    aws_ec2 as ec2,
    aws_secretsmanager as secretsmanager,
)
from constructs import Construct

class RDSStack(Stack):
    def __init__(self, scope: Construct, id: str, vpc: ec2.Vpc, **kwargs):
        super().__init__(scope, id, **kwargs)

        db_credentials = rds.Credentials.from_generated_secret("dbadmin")

        self.db_instance = rds.DatabaseInstance(self, "WebAppDB",
            engine=rds.DatabaseInstanceEngine.postgres(
                version=rds.PostgresEngineVersion.VER_14_7
            ),
            vpc=vpc,
            credentials=db_credentials,
            instance_type=ec2.InstanceType.of(
                ec2.InstanceClass.BURSTABLE2, ec2.InstanceSize.MICRO
            ),
            multi_az=False,
            allocated_storage=20,
            max_allocated_storage=100,
            storage_encrypted=True,
            deletion_protection=False,
            publicly_accessible=False,
            vpc_subnets={"subnet_type": ec2.SubnetType.PRIVATE_WITH_EGRESS},
        )

        self.secret = self.db_instance.secret
