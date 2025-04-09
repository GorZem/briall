from sqlalchemy import Column, Integer, String, Text, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Jewelry(db.Model):
    __tablename__ = 'jewelry'

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String, index=True)
    metal_id = Column(Integer, ForeignKey('metals.id'))
    description = Column(Text)
    main_image_id = Column(Integer, ForeignKey('images.id', ondelete='SET NULL'))
    main_title = Column(String)
    metal = relationship("Metal", backref="jewelry")  # Добавляем отношение к Metal
    images = relationship("Image", back_populates="jewelry", foreign_keys="[Image.jewelry_id]")
    stones = relationship("JewelryStone", back_populates="jewelry")

    @property
    def main_image(self):
        return next((img for img in self.images if img.is_main), None)

class Metal(db.Model):
    __tablename__ = 'metals'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    title = Column(String)

class Stone(db.Model):
    __tablename__ = 'stones'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    type = Column(String)
    jewelry = relationship("JewelryStone", back_populates="stone")

class JewelryStone(db.Model):
    __tablename__ = 'jewelry_stones'

    jewelry_id = Column(Integer, ForeignKey('jewelry.id'), primary_key=True)
    stone_id = Column(Integer, ForeignKey('stones.id'), primary_key=True)
    jewelry = relationship("Jewelry", back_populates="stones")
    stone = relationship("Stone", back_populates="jewelry")


class Image(db.Model):
    __tablename__ = 'images'

    id = Column(Integer, primary_key=True, index=True)
    jewelry_id = Column(Integer, ForeignKey('jewelry.id'))
    url = Column(String)
    is_main = Column(Boolean, default=False)
    jewelry = relationship("Jewelry", back_populates="images", foreign_keys=[jewelry_id])

# Создание базы данных
def init_db():
    db.create_all()
