from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

class User(BaseModel):
    id: str
    firstName: str
    lastName: str
    email: str
    isGuide: bool
    isAdmin: bool
    isStuff: bool

class Image(BaseModel):
    id: str
    url: str
    about: str

class Video(BaseModel):
    id: str
    url: str
    about: str

class PlaceDateTime(BaseModel):
    id: str
    url: datetime
    maxNum: int

class Place(BaseModel):
    id: str
    name: str
    cost: int
    description: str
    country: str
    city: str
    images: List[Image]
    videos: Optional[List[Video]]
    placeDateTimes: Optional[List[PlaceDateTime]]
    userId: str

class Reservation(BaseModel):
    id: str
    placeDateTimeId: str
    userId: str