from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, Field
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


class Songs(BaseModel):
    char: str = Field(min_length=1)
    song_title: str = Field()
    # song_num: int = Field()
    lyric: str = Field()
    # favorite: bool = Field()



@app.get("/")
def get_all_songs(db: Session = Depends(get_db)):
    return db.query(models.Songs).all()


