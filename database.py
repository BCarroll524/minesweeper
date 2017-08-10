from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

class Highscores(Base):
	__tablename__ = 'highscores'

	id = Column(Integer, primary_key = True)
	name = Column(String(80), nullable = False)
	score = Column(Integer, nullable = False)

	@property
	def serialize(self):
		return {
			'name' : self.name,
			'score' : self.score,
			'id' : self.id
		}

engine = create_engine('sqlite:///highscores.db')
Base.metadata.create_all(engine)