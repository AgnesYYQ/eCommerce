# eCommerce Project Knowledge Base

## Summary of Architecture & Decisions

- **Cloud Provider:** AWS
- **Frontend:** React (scaffolded in `frontend/`)
- **Backend:** Microservices using FastAPI (Python), each in its own directory under `backend/`
- **Infrastructure as Code:** Terraform modules in `infra/terraform/`
- **Architecture Diagram:** Python script in `diagrams/architecture.py` (generates PNG for documentation)
- **Microservices Responsibilities:** Documented in `services/README.md`

## Key AWS Services Used
- Route 53 (DNS)
- CloudFront (CDN)
- S3 (static assets)
- WAF (web firewall)
- API Gateway (REST entrypoint)
- Cognito (user management)
- Lambda & ECS/Fargate (compute)
- DynamoDB (NoSQL)
- Aurora/RDS (relational DB)
- ElastiCache (caching)
- SQS/SNS/EventBridge (messaging/integration)
- OpenSearch (search)
- Personalize (recommendations)

## Decisions & Rationale
- **Microservices:** Each core domain (product, cart, order, payment, etc.) is a separate FastAPI service for scalability and maintainability.
- **Frontend:** React chosen for flexibility and ecosystem; can be deployed to S3/CloudFront.
- **Infra as Code:** Terraform for reproducible, versioned AWS infrastructure.
- **Documentation:** Architecture diagram is generated and linked in root and services README.

## Setup Steps
1. Generate the architecture diagram:
   ```bash
   pip install diagrams
   python diagrams/architecture.py
   ```
2. Start backend microservices (see each backend/*/README or main.py).
3. Start frontend:
   ```bash
   cd frontend
   npm install
   npm start
   ```
4. See root README.md for project navigation.

---

This file summarizes all major architectural and technical decisions for onboarding and future reference.
