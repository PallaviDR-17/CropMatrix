from sqlalchemy.orm import Session
from database import SessionLocal
from models import User
from auth import hash_password


router = APIRouter(prefix="/users", tags=["Users"])


def get_db():
    db = SessionLocal()
        try:
        yield db
        finally:
    db.close()


@router.post("/register")
def register(username: str, password: str, db: Session = Depends(get_db)):
user = User(username=username, password=hash_password(password))
db.add(user)
db.commit()
return {"message": "User registered"}