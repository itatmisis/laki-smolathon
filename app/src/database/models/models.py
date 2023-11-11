from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    Float,
    String,
    Boolean,
    TIMESTAMP
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text

from .base import Base


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    first_name = Column(String)
    last_name = Column(String)
    login = Column(String, unique=True)
    password = Column(String)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))

    note = relationship('Notes', back_populates='user')
    # location = relationship('Locations', secondary='notes', back_populates='user')


class Notes(Base):
    __tablename__ = 'notes'
    id = Column(Integer, primary_key=True)
    id_user = Column(Integer, ForeignKey('users.id')) # primary_key=True)
    id_location = Column(Integer, ForeignKey('locations.id')) # primary_key=True)
    text_reaction = Column(String, nullable=True)
    photo = Column(String, nullable=True)
    marked_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    user = relationship('Users', back_populates='note')
    location = relationship('Locations', back_populates='note')


class Locations(Base):
    __tablename__ = 'locations'
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    id_category = Column(Integer, ForeignKey('category.id'))
    name = Column(String)
    description = Column(String)
    address = Column(String)
    coord_x = Column(Float)
    coord_y = Column(Float)

    note = relationship('Notes', back_populates='location')
    # user = relationship('Users', secondary='notes', back_populates='location')


class Categories(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    name = Column(String)


class Events(Base):
    __tablename__ = 'events'
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    id_category = Column(Integer, ForeignKey('category.id'))
    name = Column(String)
    description = Column(String)
    address = Column(String)
    coord_x = Column(Float)
    coord_y = Column(Float)

    event_date = Column(String)
    price = Column(String)
    link = Column(String)
