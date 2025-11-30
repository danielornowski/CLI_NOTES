import pytest
from database import Base
from database import engine as real_engine
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


TEST_DB = "sqlite:///:memory:"

test_engine = create_engine(TEST_DB, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = test_engine)

@pytest.fixture(scope="function")
def db_session():
    Base.metadata.create_all(bind = test_engine)
    session = TestingSessionLocal()
    try:
        yield session
    finally:
        session.close()
        Base.metadata.drop_all(bind=test_engine)
