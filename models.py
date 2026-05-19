# models.py

from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    Enum,
    DateTime,
    Text,
    Date,
    Time
)

from sqlalchemy.orm import relationship
from database import Base

from datetime import datetime
import enum


# ======================================================
# ENUM STATUS ADOPSI
# ======================================================
class StatusAdopsi(str, enum.Enum):
    tersedia = "tersedia"
    pending = "pending"
    diadopsi = "diadopsi"


# ======================================================
# ENUM STATUS ORDER
# ======================================================
class StatusOrder(str, enum.Enum):
    pending = "pending"
    cart = "cart"
    paid = "paid"


# ======================================================
# ENUM STATUS BOOKING GROOMING
# ======================================================
class StatusBooking(str, enum.Enum):
    menunggu = "menunggu"
    diproses = "diproses"
    selesai = "selesai"
    dibatalkan = "dibatalkan"


# ======================================================
# TABEL USERS
# ======================================================
class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    nama = Column(String(100), nullable=False)

    email = Column(String(100), unique=True, nullable=False)

    password_hash = Column(String(255), nullable=False)

    alamat = Column(Text, nullable=True)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    # ==================================================
    # RELATIONSHIP
    # ==================================================
    animals = relationship(
        "Animals",
        back_populates="adopter",
        lazy="selectin"
    )

    orders = relationship(
        "Orders",
        back_populates="user",
        lazy="selectin"
    )

    grooming_bookings = relationship(
        "GroomingBookings",
        back_populates="user",
        lazy="selectin"
    )


# ======================================================
# TABEL CATEGORIES
# ======================================================
class Categories(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)

    nama_kategori = Column(
        String(100),
        unique=True,
        nullable=False
    )

    # ==================================================
    # RELATIONSHIP
    # ==================================================
    animals = relationship(
        "Animals",
        back_populates="category",
        lazy="selectin"
    )


# ======================================================
# TABEL ANIMALS
# ======================================================
class Animals(Base):
    __tablename__ = "animals"

    id = Column(Integer, primary_key=True, index=True)

    nama_hewan = Column(String(100), nullable=False)

    umur = Column(Integer, nullable=False)

    harga = Column(Integer, nullable=False)

    deskripsi = Column(Text, nullable=True)

    foto = Column(String(255), nullable=True)

    status_adopsi = Column(
        Enum(StatusAdopsi),
        default=StatusAdopsi.tersedia
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    # ==================================================
    # FOREIGN KEY
    # ==================================================
    kategori_id = Column(
        Integer,
        ForeignKey("categories.id")
    )

    adopter_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=True
    )

    # ==================================================
    # RELATIONSHIP
    # ==================================================
    category = relationship(
        "Categories",
        back_populates="animals"
    )

    adopter = relationship(
        "Users",
        back_populates="animals"
    )

    adoptions = relationship(
        "AnimalAdoptions",
        back_populates="animal",
        lazy="selectin"
    )


# ======================================================
# TABEL PRODUCTS
# ======================================================
class Products(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)

    nama_produk = Column(String(100), nullable=False)

    deskripsi = Column(Text, nullable=True)

    harga = Column(Integer, nullable=False)

    stok = Column(Integer, default=0)

    foto = Column(String(255), nullable=True)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    # ==================================================
    # RELATIONSHIP
    # ==================================================
    order_products = relationship(
        "OrderProducts",
        back_populates="product",
        lazy="selectin"
    )


# ======================================================
# TABEL GROOMING SERVICES
# ======================================================
class GroomingServices(Base):
    __tablename__ = "grooming_services"

    id = Column(Integer, primary_key=True, index=True)

    nama_layanan = Column(String(100), nullable=False)

    harga = Column(Integer, nullable=False)

    deskripsi = Column(Text, nullable=True)

    # ==================================================
    # RELATIONSHIP
    # ==================================================
    bookings = relationship(
        "GroomingBookings",
        back_populates="grooming_service",
        lazy="selectin"
    )


# ======================================================
# TABEL ORDERS
# ======================================================
class Orders(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)

    total_harga = Column(Integer, nullable=False)

    status = Column(
        Enum(StatusOrder),
        default=StatusOrder.paid    
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    # ==================================================
    # FOREIGN KEY
    # ==================================================
    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    # ==================================================
    # RELATIONSHIP
    # ==================================================
    user = relationship(
        "Users",
        back_populates="orders"
    )

    order_products = relationship(
        "OrderProducts",
        back_populates="order",
        lazy="selectin"
    )

    animal_adoptions = relationship(
        "AnimalAdoptions",
        back_populates="order",
        lazy="selectin"
    )

    grooming_bookings = relationship(
        "GroomingBookings",
        back_populates="order",
        lazy="selectin"
    )


# ======================================================
# TABEL ORDER PRODUCTS
# ======================================================
class OrderProducts(Base):
    __tablename__ = "order_products"

    id = Column(Integer, primary_key=True, index=True)

    quantity = Column(Integer, nullable=False)

    harga = Column(Integer, nullable=False)

    # ==================================================
    # FOREIGN KEY
    # ==================================================
    order_id = Column(
        Integer,
        ForeignKey("orders.id")
    )

    product_id = Column(
        Integer,
        ForeignKey("products.id")
    )

    # ==================================================
    # RELATIONSHIP
    # ==================================================
    order = relationship(
        "Orders",
        back_populates="order_products"
    )

    product = relationship(
        "Products",
        back_populates="order_products"
    )


# ======================================================
# TABEL ANIMAL ADOPTIONS
# ======================================================
class AnimalAdoptions(Base):
    __tablename__ = "animal_adoptions"

    id = Column(Integer, primary_key=True, index=True)

    biaya_adopsi = Column(Integer, nullable=False)

    # ==================================================
    # FOREIGN KEY
    # ==================================================
    order_id = Column(
        Integer,
        ForeignKey("orders.id")
    )

    animal_id = Column(
        Integer,
        ForeignKey("animals.id")
    )

    # ==================================================
    # RELATIONSHIP
    # ==================================================
    order = relationship(
        "Orders",
        back_populates="animal_adoptions"
    )

    animal = relationship(
        "Animals",
        back_populates="adoptions"
    )


# ======================================================
# TABEL GROOMING BOOKINGS
# ======================================================
class GroomingBookings(Base):
    __tablename__ = "grooming_bookings"

    id = Column(Integer, primary_key=True, index=True)

    booking_date = Column(
        Date,
        nullable=False
    )

    catatan = Column(Text, nullable=True)

    status = Column(
        Enum(StatusBooking),
        default=StatusBooking.menunggu
    )

    # ==================================================
    # FOREIGN KEY
    # ==================================================
    order_id = Column(
        Integer,
        ForeignKey("orders.id")
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    grooming_service_id = Column(
        Integer,
        ForeignKey("grooming_services.id")
    )

    # ==================================================
    # RELATIONSHIP
    # ==================================================
    order = relationship(
        "Orders",
        back_populates="grooming_bookings"
    )

    user = relationship(
        "Users",
        back_populates="grooming_bookings"
    )

    grooming_service = relationship(
        "GroomingServices",
        back_populates="bookings"
    )