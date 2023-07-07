#!/usr/bin/python3

from base_model import BaseModel
from city import City
from user import User

class Place(BaseModel):
    """ """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []