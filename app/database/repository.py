"""
Database Operations

Author: Riya Saroj
"""

from database.database import SessionLocal
from database.models import (
    User,
    ResearchHistory,
    SavedPaper
)


def create_user(
    username,
    email,
    password
):

    db = SessionLocal()

    user = User(
        username=username,
        email=email,
    )

    from auth.password import hash_password
    password_hash=hash_password(password)
    password=password
    
    db.add(user)

    db.commit()

    db.close()


def save_research(
    user_id,
    query,
    review
):

    db = SessionLocal()

    history = ResearchHistory(
        user_id=user_id,
        query=query,
        review=review
    )

    db.add(history)

    db.commit()

    db.close()


def save_paper(
    paper
):

    db = SessionLocal()

    obj = SavedPaper(

        title=paper["title"],

        journal=paper["journal"],

        year=paper["year"],

        pmid=paper["pmid"],

        abstract=paper["abstract"]

    )

    db.add(obj)

    db.commit()

    db.close()

from auth.password import verify_password

def login_user(email, password):

    db = SessionLocal()

    user = db.query(User).filter(
        User.email == email
    ).first()

    if user is None:
        return None

    if verify_password(
        password,
        user.password_hash
    ):
        return user

    return None