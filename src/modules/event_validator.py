from pydantic import BaseModel, HttpUrl, Field
from typing import List
from datetime import datetime

class ElementAttributes(BaseModel):
    classAttributes: str = Field(alias="class")

class Properties(BaseModel):
    distinct_id: str
    session_id: str
    journey_id: str
    current_url: HttpUrl = Field(alias="$current_url")
    host: str = Field(alias="$host")
    pathname: str = Field(alias="$pathname")
    browser: str = Field(alias="$browser")
    device: str = Field(alias="$device")
    eventType: str
    elementType: str
    elementText: str
    elementAttributes: ElementAttributes
    timestamp: datetime
    x: int
    y: int
    mouseButton: int
    ctrlKey: bool
    shiftKey: bool
    altKey: bool
    metaKey: bool

class Event(BaseModel):
    event: str
    properties: Properties
    timestamp: datetime

class EventsData(BaseModel):
    events: List[Event]