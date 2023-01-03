from sqlalchemy import Column, Integer, String, Boolean
from database import Base

class Songs(Base):
    __tablename__= "bodosong"

    id = Column(Integer, primary_key=True, index = True)
    char = Column(String)
    song_title = Column(String)
    lyric = Column(String)
    # song_num = Column(Integer)
    # favorite = Column(Boolean)
