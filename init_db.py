from databases import engine, Base

from models import User, Order  # noqa

Base.metadata.create_all(bind=engine)