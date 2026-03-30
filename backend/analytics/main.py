from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Event(BaseModel):
    user_id: str
    event_type: str
    metadata: dict

@app.post("/event")
def track_event(event: Event):
    # Simulate event tracking
    return {"status": "tracked", "event_type": event.event_type}
