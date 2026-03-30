# eCommerce Project Knowledge Base

## Summary of Architecture & Decisions

- **Cloud Provider:** AWS
- **Frontend:** React (scaffolded in `frontend/`)
- **Backend:** Microservices using FastAPI (Python), each in its own directory under `backend/`
- **Infrastructure as Code:** Terraform modules in `infra/terraform/`
- **Architecture Diagram:** Python script in `diagrams/architecture.py` (generates PNG for documentation)
- **Microservices Responsibilities:** Documented in `services/README.md`

## Multi-Region, High-Availability Enhancements (2026)
- **Route 53 (Global):** Latency-based routing and health checks direct users to the nearest healthy AWS region.
- **DynamoDB Global Tables:** Multi-region, multi-active replication for catalog, cart, and session data.
- **Aurora Global Database:** Orders and transactional data replicated across regions for fast failover.
- **S3 Cross-Region Replication:** Product images/assets are automatically copied to all regions for global access.
- **Stripe Integration:**
  - Frontend uses Stripe Elements for PCI-safe card entry.
  - Stripe redirects users to your “Success” page after payment.
  - Stripe sends a webhook to API Gateway, which puts the event in SQS and returns 200 OK.
  - Lambda processes SQS, updates Aurora, and triggers shipping.
  - Circuit breaker: If Stripe or DB is slow, Lambda retries SQS messages with exponential backoff; user is not blocked.
- **Event-Driven Microservices:** EventBridge routes events to Order, Notification, and Analytics services, which respond back to API Gateway/frontends.

## Summary Table
| Feature         | Standard (Single Region)      | Multi-Region (High Availability)      |
|-----------------|------------------------------|---------------------------------------|
| Database        | Regional DynamoDB / RDS      | Global Tables / Aurora Global         |
| User Latency    | High for distant users       | Low (nearest region)                  |
| Blast Radius    | Region outage = Down         | Region outage = Failover              |
| Complexity      | Low                          | High (consistency, failover logic)    |

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

## Multi-Region Infrastructure Example (Terraform)
- `infra/terraform/regions.tf` demonstrates how to:
  - Define multiple AWS regions for deployment
  - Set up DynamoDB Global Tables with replicas
  - Set up Aurora Global Database with primary and secondary clusters

## Stripe Payment Integration (Backend)
- `backend/payment/stripe_async.py` provides a FastAPI endpoint for Stripe webhooks:
  - Verifies Stripe signature
  - Immediately enqueues payment events to SQS for async processing
  - Designed for multi-region: deploy in each region, use region-local SQS queue
  - Supports failover by switching SQS_QUEUE_URL and AWS_REGION
