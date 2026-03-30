from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Notification(BaseModel):
    user_id: str
    message: str

@app.post("/notify")
def send_notification(notification: Notification):
    # Simulate sending notification
    return {"status": "sent", "user_id": notification.user_id}
