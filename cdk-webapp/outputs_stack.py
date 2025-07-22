from aws_cdk import (
    Stack,
    CfnOutput,
    aws_elasticloadbalancingv2 as elbv2,
    aws_s3 as s3,
    aws_rds as rds,
    aws_secretsmanager as secretsmanager
)
from constructs import Construct

class OutputsStack(Stack):
    def __init__(
        self,
        scope: Construct,
        id: str,
        alb: elbv2.ApplicationLoadBalancer,
        bucket: s3.Bucket,
        rds_instance: rds.DatabaseInstance,
        rds_secret: secretsmanager.ISecret,
        **kwargs
    ):
        super().__init__(scope, id, **kwargs)

        CfnOutput(self, "LoadBalancerDNS", value=alb.load_balancer_dns_name)
        CfnOutput(self, "S3BucketName", value=bucket.bucket_name)
        CfnOutput(self, "RDSEndpoint", value=rds_instance.db_instance_endpoint_address)
        CfnOutput(self, "RDSSecretArn", value=rds_secret.secret_arn)
