from diagrams import Diagram, Cluster
from diagrams.aws.network import Route53, CloudFront
from diagrams.aws.security import WAF
from diagrams.aws.storage import S3
from diagrams.aws.compute import Lambda, ECS
from diagrams.aws.database import Dynamodb, RDS, ElastiCache, Aurora
from diagrams.aws.integration import SQS, SNS, Eventbridge
from diagrams.aws.security import Cognito
from diagrams.aws.analytics import AmazonOpensearchService, Analytics

# Custom nodes for microservices
from diagrams.aws.general import Users
from diagrams.onprem.client import Client
from diagrams.aws.network import APIGateway

with Diagram("eCommerce AWS Architecture", show=False, filename="architecture_diagram", outformat="png"):


    user = Users("Global Users")
    route53 = Route53("Route 53 (Global)")
    cloudfront = CloudFront("CloudFront (Global)")
    waf = WAF("WAF")
    s3 = S3("S3 (CRR)")
    apigw = APIGateway("API Gateway (Multi-Region)")
    cognito = Cognito("Cognito (Multi-Region)")
    lambda_fn = Lambda("Lambda")
    ecs = ECS("ECS/Fargate")
    dynamodb = Dynamodb("DynamoDB Global Table")
    aurora = Aurora("Aurora Global DB")
    elasticache = ElastiCache("ElastiCache")
    sqs = SQS("SQS (Payment Buffer)")
    sns = SNS("SNS")
    eventbridge = Eventbridge("EventBridge")
    opensearch = AmazonOpensearchService("OpenSearch")
    personalize = Analytics("Personalize")
    # Microservice nodes (using Lambda icons for each)
    order_svc = Lambda("Order Service")
    notification_svc = Lambda("Notification Service")
    analytics_svc = Lambda("Analytics Service")
    # Stripe integration
    stripe = Client("Stripe")

    user >> route53
    route53 >> cloudfront >> waf >> apigw
    cloudfront >> s3
    apigw >> [lambda_fn, ecs, cognito]
    lambda_fn >> [dynamodb, elasticache, sqs, sns, opensearch, personalize]
    ecs >> [aurora, elasticache, sqs, sns, opensearch, personalize]
    # Multi-region DBs (Global Table/Aurora Global DB replication shown conceptually)
    # In diagrams, cross-region replication is implied by naming and documentation.
    # Stripe async payment
    apigw << stripe
    stripe >> sqs
    sqs >> lambda_fn
    lambda_fn >> aurora
    # Event-driven microservices
    sqs >> eventbridge
    eventbridge >> [order_svc, notification_svc, analytics_svc]
    # Response flows back to API Gateway
    order_svc >> apigw
    notification_svc >> apigw
    analytics_svc >> apigw
