# CDK Web Application Stack

This project uses AWS CDK (Python) to deploy a basic web application infrastructure.

## Prerequisites
- AWS account
- AWS CLI configured
- Python 3.x
- AWS CDK installed


## Deployment

1. Install dependencies:
   ```bash
   python -m venv .venv && source .venv/bin/activate
   pip install --upgrade pip
   pip install -r requirements.txt
   npm install -g aws-cdk
   ```
   

2. Bootstrap cdk:
   ```bash
   cdk bootstrap
   ```

3. Deploy:
   ```bash
   cdk deploy
   ```

## Outputs
- ALB DNS Name: `ALBDNS`
- S3 Bucket Name: `S3BucketName`
