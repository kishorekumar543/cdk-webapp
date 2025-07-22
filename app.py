from aws_cdk import App, CfnOutput
from cdk_webapp.vpc_stack import VPCStack
from cdk_webapp.ecs_stack import ECSStack
from cdk_webapp.alb_stack import ALBStack
from cdk_webapp.s3_stack import S3Stack
from cdk_webapp.rds_stack import RDSStack
from cdk_webapp.outputs_stack import OutputsStack

app = App()

vpc_stack = VPCStack(app, "VPCStack")
ecs_stack = ECSStack(app, "ECSStack", vpc=vpc_stack.vpc)
alb_stack = ALBStack(app, "ALBStack", vpc=vpc_stack.vpc, service=ecs_stack.service)
s3_stack = S3Stack(app, "S3Stack")
rds_stack = RDSStack(app, "RDSStack", vpc=vpc_stack.vpc)

OutputsStack(app, "OutputsStack", alb=alb_stack.alb, bucket=s3_stack.bucket, rds_instance=rds_stack.db_instance, rds_secret=rds_stack.secret)

app.synth()
