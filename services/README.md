# Microservices Breakdown

![Architecture Diagram](../diagrams/architecture_diagram.png)

## 1. User Service (Cognito)
- Handles user registration, authentication, and profile management.

## 2. Product Catalog Service
- Manages product listings, categories, inventory, and search (integrates with DynamoDB, OpenSearch).

## 3. Cart Service
- Manages user shopping carts (DynamoDB, ElastiCache for fast access).

## 4. Order Service
- Handles order creation, payment processing, and order history (Aurora/RDS).

## 5. Payment Service
- Integrates with payment gateways, processes transactions (Lambda or ECS).

## 6. Notification Service
- Sends emails, SMS, and push notifications (SNS, Lambda).

## 7. Recommendation Service
- Provides personalized product recommendations (Amazon Personalize).

## 8. Analytics Service
- Tracks user behavior, sales, and generates reports (EventBridge, OpenSearch).
