from app.database import Base
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy import ForeignKey, Date
import datetime


class Cat(Base):
    __tablename__ = 'cat'

    id: Mapped[int] = mapped_column(primary_key=True)
    color: Mapped[str] = mapped_column(nullable=False)
    birthdate: Mapped[datetime.date] = mapped_column(
        Date,
        nullable=False
    )
    descriptions: Mapped[str] = mapped_column(nullable=False)
    breed_id: Mapped[int] = mapped_column(ForeignKey(
        'breed.id',
        ondelete='CASCADE')
    )
    breed: Mapped['Breed'] = relationship(back_populates='cat')


class Breed(Base):
    __tablename__ = 'breed'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    cat: Mapped['Cat'] = relationship(back_populates='breed')
