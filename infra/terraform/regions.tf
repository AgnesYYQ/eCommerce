variable "regions" {
  description = "List of AWS regions for multi-region deployment"
  type        = list(string)
  default     = ["us-east-1", "eu-west-2"]
}

# Example: provider alias for secondary region
provider "aws" {
  alias  = "secondary"
  region = var.regions[1]
}

# DynamoDB Global Table example
resource "aws_dynamodb_table" "cart" {
  name           = "cart-global"
  billing_mode   = "PAY_PER_REQUEST"
  hash_key       = "user_id"
  attribute {
    name = "user_id"
    type = "S"
  }
  replica {
    region_name = var.regions[1]
  }
}

# Aurora Global DB example (primary cluster)
resource "aws_rds_global_cluster" "orders" {
  global_cluster_identifier = "orders-global"
}

resource "aws_rds_cluster" "orders_primary" {
  cluster_identifier      = "orders-primary"
  engine                 = "aurora-mysql"
  engine_mode            = "provisioned"
  master_username        = "admin"
  master_password        = "password"
  global_cluster_identifier = aws_rds_global_cluster.orders.id
  # ...other config...
}

# Aurora Global DB example (secondary cluster)
resource "aws_rds_cluster" "orders_secondary" {
  provider               = aws.secondary
  cluster_identifier     = "orders-secondary"
  engine                 = "aurora-mysql"
  engine_mode            = "provisioned"
  global_cluster_identifier = aws_rds_global_cluster.orders.id
  # ...other config...
}
