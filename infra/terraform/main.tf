terraform {
  required_version = ">= 1.3.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 5.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

module "network" {
  source = "terraform-aws-modules/vpc/aws"
  name   = var.project_name
  cidr   = var.vpc_cidr
  azs    = var.azs
  public_subnets  = var.public_subnets
  private_subnets = var.private_subnets
}

# Add more modules/resources for API Gateway, Lambda, ECS, Cognito, DynamoDB, RDS, ElastiCache, SQS, SNS, EventBridge, OpenSearch, Personalize, S3, CloudFront, WAF, Route53 as needed
