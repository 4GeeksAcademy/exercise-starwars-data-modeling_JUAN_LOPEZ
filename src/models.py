import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float, DateTime, Text
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key = True)
    name = Column(String(250), nullable = False)
    email = Column(String(250), nullable = False)
    favorites = relationship("favorites")

class People(Base):
    __tablename__ = "people"

    iud = Column(Integer, primary_key= True)
    name = Column(String(250), nullable = False)
    height = Column(Integer, nullable = False)
    url = Column(String(400), nullable = False)
    mass = Column(Integer, nullable = True)
    hair_color = Column(String(100), nullable = True)
    skin_color = Column(String(100), nullable = True)
    eye_color = Column(String(100), nullable = True)
    birth_year = Column(String(100), nullable = True)
    gender = Column(String(100), nullable = True)
    favorites = relationship("favorites")


class Vehicle(Base):
    __tablename__ = "vehicle"

    iud = Column(Integer, primary_key = True)
    name = Column(String(200), nullable = False)
    model = Column(String(100), nullable = True)
    url = Column(String(200), nullable = False)
    vehicle_class = Column(String(50),nullable = True)
    manufacturer = Column(String(50), nullable = True)
    cost_in_credits = Column(Integer, nullable = True)
    lenght = Column(Float, nullable = True)
    crew = Column(Integer, nullable = True)
    max_atmosphering_speed = Column(Integer, nullable = True)
    cargo_capacity = Column(Integer, nullable = True)
    consumable = Column(String(100), nullable= True)
    favorites = relationship("favorites")



class Planet(Base):
    __tablename__ = "planet"

    iud = Column(Integer, primary_key = True)
    name = Column(String(300), nullable = False)
    url = Column(String(250), nullable = False)
    diameter = Column(Integer, nullable = True)
    rotation_period = Column(Integer, nullable =True)
    manufacturer = Column(String(50), nullable = True)
    orbital_period = Column(Integer, nullable = True)
    lenght = Column(Float, nullable = True)
    gavity = Column(Integer, nullable = True)
    population = Column(Integer, nullable = True)
    climate = Column(String(50), nullable = True)
    terrain = Column(String(50), nullable = True)
    surface_water = Column(Integer, nullable = True)
    favorites = relationship("favorites")


class Favorites(Base): 
    __tablename__ = "favorites"

    fav_id = Column(Integer, primary_key = True)
    People_uid = Column(Integer, ForeignKey("people.uid"))
    vehicle_uid = Column(Integer, ForeignKey("vehicle.uid"))
    planet_uid = Column(Integer, ForeignKey("planet.uid"))
    user_uid = Column(Integer, ForeignKey("user.id"))
    people = relationship("people")
    planet = relationship("planet")
    vehicle = relationship("vehicle")
    user = relationship("user")

    
## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
