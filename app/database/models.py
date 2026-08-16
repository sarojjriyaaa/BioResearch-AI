"""
Database Models

Author: Riya Saroj
"""

from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    DateTime,
    ForeignKey
)

from sqlalchemy.orm import relationship

from datetime import datetime

from database.database import Base


class User(Base):

    __tablename__ = "users"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    username = Column(
        String,
        unique=True
    )

    email = Column(
        String,
        unique=True
    )

    password_hash = Column(
        String
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    researches = relationship(
        "ResearchHistory",
        back_populates="user"
    )


class ResearchHistory(Base):

    __tablename__ = "research_history"

    id = Column(
        Integer,
        primary_key=True
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    query = Column(
        Text
    )

    review = Column(
        Text
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    user = relationship(
        "User",
        back_populates="researches"
    )


class SavedPaper(Base):

    __tablename__ = "saved_papers"

    id = Column(
        Integer,
        primary_key=True
    )

    title = Column(Text)

    journal = Column(Text)

    year = Column(String)

    pmid = Column(String)

    abstract = Column(Text)