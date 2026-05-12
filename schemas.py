# schemas.py

from pydantic import BaseModel
from typing import Optional
from datetime import date


# ======================================================
# USER
# ======================================================

class UserBase(BaseModel):
    nama: str
    email: str
    alamat: Optional[str] = None


class UserCreate(UserBase):
    pass


class UserOut(UserBase):
    id: int

    class Config:
        from_attributes = True


# ======================================================
# KATEGORI HEWAN
# ======================================================

class KategoriHewanBase(BaseModel):
    nama_kategori: str


class KategoriHewanCreate(KategoriHewanBase):
    pass


class KategoriHewanOut(KategoriHewanBase):
    id: int

    class Config:
        from_attributes = True


# ======================================================
# HEWAN
# ======================================================

class HewanBase(BaseModel):
    nama_hewan: str
    umur: int
    foto: Optional[str] = None
    status: str
    id_kategori: int
    id_user: Optional[int] = None


class HewanCreate(HewanBase):
    pass


class HewanUpdate(BaseModel):
    nama_hewan: Optional[str] = None
    umur: Optional[int] = None
    foto: Optional[str] = None
    status: Optional[str] = None
    id_kategori: Optional[int] = None
    id_user: Optional[int] = None


class HewanOut(BaseModel):
    id: int
    nama_hewan: str
    umur: int
    foto: Optional[str]
    status: str

    kategori: Optional[KategoriHewanOut]
    user: Optional[UserOut]

    class Config:
        from_attributes = True


# ======================================================
# PRODUK
# ======================================================

class ProdukBase(BaseModel):
    nama_produk: str
    harga: int
    stok: int
    gambar: Optional[str] = None


class ProdukCreate(ProdukBase):
    pass


class ProdukUpdate(BaseModel):
    nama_produk: Optional[str] = None
    harga: Optional[int] = None
    stok: Optional[int] = None
    gambar: Optional[str] = None


class ProdukOut(ProdukBase):
    id: int

    class Config:
        from_attributes = True


# ======================================================
# GROOMING
# ======================================================

class GroomingBase(BaseModel):
    nama_layanan: str
    harga: int
    deskripsi: Optional[str] = None


class GroomingCreate(GroomingBase):
    pass


class GroomingUpdate(BaseModel):
    nama_layanan: Optional[str] = None
    harga: Optional[int] = None
    deskripsi: Optional[str] = None


class GroomingOut(GroomingBase):
    id: int

    class Config:
        from_attributes = True


# ======================================================
# TRANSAKSI
# ======================================================

class TransaksiBase(BaseModel):
    id_user: int

    id_produk: Optional[int] = None
    id_grooming: Optional[int] = None
    id_hewan: Optional[int] = None

    tanggal: date
    total: int

    jenis_transaksi: str
    status_pembayaran: str


class TransaksiCreate(TransaksiBase):
    pass


class TransaksiUpdate(BaseModel):
    id_produk: Optional[int] = None
    id_grooming: Optional[int] = None
    id_hewan: Optional[int] = None

    total: Optional[int] = None
    jenis_transaksi: Optional[str] = None
    status_pembayaran: Optional[str] = None


class TransaksiOut(BaseModel):
    id: int

    tanggal: date
    total: int

    jenis_transaksi: str
    status_pembayaran: str

    user: Optional[UserOut]
    produk: Optional[ProdukOut]
    grooming: Optional[GroomingOut]
    hewan: Optional[HewanOut]

    class Config:
        from_attributes = True