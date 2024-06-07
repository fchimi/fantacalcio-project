from sqlalchemy.orm import Session
from sqlalchemy import select

def main(args):
    session = Session(engine)

    stmt = select(User).where(User.name.in_(["spongebob", "sandy"]))

    for user in session.scalars(stmt):
        print(user)