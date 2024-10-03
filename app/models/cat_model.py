from app.database import Base
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy import ForeignKey


class Cats(Base):
    __tablename__ = 'cats'

    id: Mapped[int] = mapped_column(primary_key=True)
    color: Mapped[str] = mapped_column(nullable=False)
    months_old: Mapped[int] = mapped_column(nullable=False)
    descriptions: Mapped[str] = mapped_column(nullable=False)
    id_breed: Mapped[int] = mapped_column(ForeignKey('breed.id'))
    breed: Mapped['Breed'] = relationship(back_populates='cat')


class Breed(Base):
    __tablename__ = 'breed'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    cat: Mapped['Cats'] = relationship(back_populates='breed')
