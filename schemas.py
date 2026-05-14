# schemas.py

from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime, date, time


# ======================================================
# USERS
# ======================================================

class UserBase(BaseModel):
    nama: str
    email: EmailStr
    alamat: Optional[str] = None


class UserCreate(UserBase):
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserUpdate(BaseModel):
    nama: Optional[str] = None
    email: Optional[EmailStr] = None
    alamat: Optional[str] = None


class UserOut(UserBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

# ======================================================
# LOGIN
# ======================================================

class LoginRequest(BaseModel):

    email: str

    password: str


class LoginResponse(BaseModel):

    access_token: str

    token_type: str

    user: UserOut


# ======================================================
# CATEGORIES
# ======================================================

class CategoryBase(BaseModel):
    nama_kategori: str


class CategoryCreate(CategoryBase):
    pass


class CategoryUpdate(BaseModel):
    nama_kategori: Optional[str] = None


class CategoryOut(CategoryBase):
    id: int

    class Config:
        from_attributes = True


# ======================================================
# ANIMALS
# ======================================================

class AnimalBase(BaseModel):
    nama_hewan: str
    umur: int
    harga: int
    deskripsi: Optional[str] = None
    foto: Optional[str] = None
    kategori_id: int


class AnimalCreate(AnimalBase):
    pass


class AnimalUpdate(BaseModel):
    nama_hewan: Optional[str] = None
    umur: Optional[int] = None
    harga: Optional[int] = None
    deskripsi: Optional[str] = None
    foto: Optional[str] = None
    status_adopsi: Optional[str] = None
    kategori_id: Optional[int] = None
    adopter_id: Optional[int] = None


class AnimalOut(BaseModel):
    id: int
    nama_hewan: str
    umur: int
    deskripsi: Optional[str]
    foto: Optional[str]

    status_adopsi: str

    created_at: datetime

    category: Optional[CategoryOut]

    adopter: Optional[UserOut]

    class Config:
        from_attributes = True


# ======================================================
# PRODUCTS
# ======================================================

class ProductBase(BaseModel):
    nama_produk: str
    deskripsi: Optional[str] = None
    harga: int
    stok: int
    foto: Optional[str] = None


class ProductCreate(ProductBase):
    pass


class ProductUpdate(BaseModel):
    nama_produk: Optional[str] = None
    deskripsi: Optional[str] = None
    harga: Optional[int] = None
    stok: Optional[int] = None
    foto: Optional[str] = None


class ProductOut(ProductBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


# ======================================================
# GROOMING SERVICES
# ======================================================

class GroomingServiceBase(BaseModel):
    nama_layanan: str
    harga: int
    deskripsi: Optional[str] = None


class GroomingServiceCreate(GroomingServiceBase):
    pass


class GroomingServiceUpdate(BaseModel):
    nama_layanan: Optional[str] = None
    harga: Optional[int] = None
    deskripsi: Optional[str] = None


class GroomingServiceOut(GroomingServiceBase):
    id: int

    class Config:
        from_attributes = True


# ======================================================
# ORDERS
# ======================================================

class OrderBase(BaseModel):
    total_harga: int


class OrderCreate(OrderBase):
    user_id: int


class OrderUpdate(BaseModel):
    total_harga: Optional[int] = None
    status: Optional[str] = None


class OrderOut(BaseModel):
    id: int

    total_harga: int

    status: str

    created_at: datetime

    user: Optional[UserOut]

    class Config:
        from_attributes = True


# ======================================================
# ORDER PRODUCTS
# ======================================================

class OrderProductBase(BaseModel):
    quantity: int
    harga: int
    order_id: int
    product_id: int


class OrderProductCreate(OrderProductBase):
    pass


class OrderProductUpdate(BaseModel):
    quantity: Optional[int] = None
    harga: Optional[int] = None


class OrderProductOut(BaseModel):
    id: int
    quantity: int
    harga: int
    product: Optional[ProductOut]

    class Config:
        from_attributes = True


# ======================================================
# ANIMAL ADOPTIONS
# ======================================================

class AnimalAdoptionBase(BaseModel):
    biaya_adopsi: int
    order_id: int
    animal_id: int


class AnimalAdoptionCreate(AnimalAdoptionBase):
    pass


class AnimalAdoptionUpdate(BaseModel):
    biaya_adopsi: Optional[int] = None
    status: Optional[str] = None


class AnimalAdoptionOut(BaseModel):
    id: int

    biaya_adopsi: int

    status: str

    animal: Optional[AnimalOut]

    class Config:
        from_attributes = True


# ======================================================
# GROOMING BOOKINGS
# ======================================================

class GroomingBookingBase(BaseModel):
    booking_date: date

    catatan: Optional[str] = None

    order_id: int

    user_id: int

    grooming_service_id: int


class GroomingBookingCreate(GroomingBookingBase):
    pass


class GroomingBookingUpdate(BaseModel):
    booking_date: Optional[date] = None
    catatan: Optional[str] = None
    status: Optional[str] = None


class GroomingBookingOut(BaseModel):
    id: int
    booking_date: date
    catatan: Optional[str]
    status: str
    user: Optional[UserOut]
    grooming_service: Optional[GroomingServiceOut]
    class Config:
        from_attributes = True

# ======================================================
# CART ITEMS
# =======================================================

class AddToCartRequest(BaseModel):
    user_id: int
    product_id: int
    quantity: int