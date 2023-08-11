from typing import Union
from fastapi import FastAPI

import math

app = FastAPI()

# Basic example of a REST call without parameters
@app.get("/")
async def root():
    return {'example': 'This is an example', 'data': 0}

# Echo example
@app.get("/echo/")
async def echo(text: str):
    return {'echo': text}

# Haversine formula example in Python
def distance(origin, destination):
    lat1, lon1 = origin
    lat2, lon2 = destination
    radius = 6371 # km
    dlat = math.radians(lat2-lat1)
    dlon = math.radians(lon2-lon1)
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = radius * c
    return d

# REST API call for geo distance
@app.get("/distance/")
async def get_distance(lat1: float = 0.0, long1: float = 0.0,
                       lat2:float = 0.0 , long2: float = 0.0):
    d = distance((lat1, long1), (lat2, long2))
    return{'distance':  d}

