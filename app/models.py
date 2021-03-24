from . import db
import random

class Property(db.Model):
    propertyid = db.Column(db.Integer, primary_key=True)
    title =  db.Column(db.String(80))    
    description = db.Column(db.String(255))
    no_of_rooms = db.Column(db.Integer)
    no_of_bathrooms = db.Column(db.Integer)   
    price = db.Column(db.Float)
    property_type = db.Column(db.String(80))
    location = db.Column(db.String(255))
    photo = db.Column(db.String(255))

