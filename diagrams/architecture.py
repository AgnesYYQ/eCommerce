from diagrams import Diagram, Cluster
from diagrams.aws.network import Route53, CloudFront
from diagrams.aws.security import WAF
from diagrams.aws.storage import S3
from diagrams.aws.compute import Lambda, ECS
from diagrams.aws.database import Dynamodb, RDS, ElastiCache
from diagrams.aws.integration import SQS, SNS, Eventbridge
from diagrams.aws.security import Cognito
from diagrams.aws.analytics import AmazonOpensearchService, Analytics

# Custom nodes for microservices
from diagrams.generic.blank import Blank
from diagrams.aws.network import APIGateway

with Diagram("eCommerce AWS Architecture", show=False, filename="architecture_diagram", outformat="png"):

    route53 = Route53("Route 53")
    cloudfront = CloudFront("CloudFront")
    waf = WAF("WAF")
    s3 = S3("S3 Static Assets")
    apigw = APIGateway("API Gateway")
    cognito = Cognito("Cognito")
    lambda_fn = Lambda("Lambda")
    ecs = ECS("ECS/Fargate")
    dynamodb = Dynamodb("DynamoDB")
    rds = RDS("Aurora/RDS")
    elasticache = ElastiCache("ElastiCache")
    sqs = SQS("SQS")
    sns = SNS("SNS")
    eventbridge = Eventbridge("EventBridge")
    opensearch = AmazonOpensearchService("OpenSearch")
    personalize = Analytics("Personalize")

    # Microservice nodes (using Lambda icons for each)
    order_svc = Lambda("Order Service")
    notification_svc = Lambda("Notification Service")
    analytics_svc = Lambda("Analytics Service")

    route53 >> cloudfront >> waf >> apigw
    cloudfront >> s3
    apigw >> [lambda_fn, ecs, cognito]
    lambda_fn >> [dynamodb, elasticache, sqs, sns, opensearch, personalize]
    ecs >> [rds, elasticache, sqs, sns, opensearch, personalize]
    sqs >> eventbridge
    eventbridge >> [order_svc, notification_svc, analytics_svc]
    # Response flows back to API Gateway
    order_svc >> apigw
    notification_svc >> apigw
    analytics_svc >> apigw
