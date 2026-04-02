import boto3
import os
import redis
import sqlalchemy
from sqlalchemy import create_engine, text

# DynamoDB client
DYNAMODB_TABLE = os.getenv("DYNAMODB_TABLE", "products")
dynamodb = boto3.resource("dynamodb", region_name=os.getenv("AWS_REGION", "us-east-1"))
product_table = dynamodb.Table(DYNAMODB_TABLE)

def get_product_from_dynamodb(product_id):
    resp = product_table.get_item(Key={"id": product_id})
    return resp.get("Item")

# Aurora (MySQL) connection
AURORA_URI = os.getenv("AURORA_URI", "mysql+pymysql://user:password@host:3306/db")
engine = create_engine(AURORA_URI)

def get_order_from_aurora(order_id):
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM orders WHERE id=:id"), {"id": order_id})
        return result.fetchone()

# ElastiCache (Redis) connection
REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
redis_client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

def cache_product(product_id, product_data):
    redis_client.set(f"product:{product_id}", str(product_data), ex=3600)

def get_cached_product(product_id):
    return redis_client.get(f"product:{product_id}")

# S3 integration
S3_BUCKET = os.getenv("S3_BUCKET", "my-bucket")
s3 = boto3.client("s3")

def upload_image_to_s3(file_path, key):
    s3.upload_file(file_path, S3_BUCKET, key)

def get_image_url(key):
    return s3.generate_presigned_url('get_object', Params={'Bucket': S3_BUCKET, 'Key': key}, ExpiresIn=3600)
