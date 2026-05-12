
# schemas.py

from pydantic import BaseModel
from typing import Optional


# =========================
# USER
# =========================

class UserBase(BaseModel):
    nama: str
    email: str
    alamat: str


class UserCreate(UserBase):
    pass


class UserOut(UserBase):
    id_user: int

    class Config:
        from_attributes = True


# =========================
# KATEGORI HEWAN
# =========================

class KategoriHewanBase(BaseModel):
    nama_kategori: str


class KategoriHewanCreate(KategoriHewanBase):
    pass


class KategoriHewanOut(KategoriHewanBase):
    id_kategori: int

    class Config:
        from_attributes = True


# =========================
# HEWAN
# =========================

class HewanBase(BaseModel):
    nama_hewan: str
    umur: int
    foto: str
    status: str
    id_kategori: int
    id_user: Optional[int] = None


class HewanCreate(HewanBase):
    pass


class HewanOut(BaseModel):
    id_hewan: int
    nama_hewan: str
    umur: int
    foto: str
    status: str

    kategori: Optional[KategoriHewanOut]
    pemilik: Optional[UserOut]

    class Config:
        from_attributes = True


# =========================
# PRODUK
# =========================

class ProdukBase(BaseModel):
    nama_produk: str
    harga: int
    stok: int
    gambar: str


class ProdukCreate(ProdukBase):
    pass


class ProdukOut(ProdukBase):
    id_produk: int

    class Config:
        from_attributes = True


# =========================
# GROOMING
# =========================

class GroomingBase(BaseModel):
    nama_layanan: str
    harga: int
    deskripsi: str


class GroomingCreate(GroomingBase):
    pass


class GroomingOut(GroomingBase):
    id_grooming: int

    class Config:
        from_attributes = True


# =========================
# TRANSAKSI
# =========================

class TransaksiBase(BaseModel):
    id_user: int
    id_produk: Optional[int] = None
    id_grooming: Optional[int] = None
    tanggal: str
    total: int
    status_pembayaran: str


class TransaksiCreate(TransaksiBase):
    pass


class TransaksiOut(BaseModel):
    id_transaksi: int
    tanggal: str
    total: int
    status_pembayaran: str

    user: Optional[UserOut]
    produk: Optional[ProdukOut]
    grooming: Optional[GroomingOut]

    class Config:
        from_attributes = True