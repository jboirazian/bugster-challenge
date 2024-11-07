from fastapi import FastAPI, HTTPException
from pydantic import ValidationError
from modules.event_validator import  EventsData

app = FastAPI()


@app.post("/api/v1/events")
async def events(events: EventsData):
    try:
        # We enter here if the request body validation is successful
        for event in events.events:
            # We then iterate over every event sent and append it to the database
            print(event.properties.journey_id)
        
        return {"message": "Validation successful"}
    except ValidationError as e:
        # Custom handling for validation errors
        raise HTTPException(status_code=400, detail="Invalid event data")


@app.get("/api/v1/stories")
async def stories():
    return {"message": "Hello World"}


@app.get("/api/v1/tests")
async def tests():
    return {"message": "Hello World"}