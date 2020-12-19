# Setup the weather app
#1. import dependencies 
import datetime as dt
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

# Setup the Database

engine = create_engine("sqlite:///hawaii.sqlite")

# Use automap_base() to put the database into classes and .prepare() to reflect the tables into SQLAlchemy
Base = automap_base()
Base.prepare(engine, reflect=True)

# Save our references to each table - Create a variable for each of the classes so we can reference them later

Measurement = Base.classes.measurement
Station = Base.classes .station

# Create a session link from Python to the Database

session = Session(engine)

# Create a flask application, being sure to pass __name__ in the app variable - we are putting the flask object into the app variable
app = Flask(__name__)

# Define our route - what to do when a user hits the index route - in this case this is the homepage - this is a static route
@app.route('/')
def welcome():
    return (
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')

# Create the precipitation route

@app.route('/api/v1.0/precipitation')
def precipitation():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    precipitation = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= prev_year).all()
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)
