# models.py
from sqlalchemy import Column, Integer, String, Date, ForeignKey, Enum
from sqlalchemy.orm import relationship
from database import Base
import enum


# =========================
# ENUM STATUS
# =========================
class StatusHewan(str, enum.Enum):
    tersedia = 'tersedia'
    diadopsi = 'diadopsi'


class StatusPembayaran(str, enum.Enum):
    pending = 'pending'
    lunas = 'lunas'
    gagal = 'gagal'


# =========================
# TABEL USERS
# =========================
class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nama = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    alamat = Column(String(255), nullable=True)

    # Relasi
    hewan = relationship('Hewan', back_populates='user', lazy='selectin')
    transaksi = relationship('Transaksi', back_populates='user', lazy='selectin')


# =========================
# TABEL KATEGORI HEWAN
# =========================
class KategoriHewan(Base):
    __tablename__ = 'kategori_hewan'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nama_kategori = Column(String(50), unique=True, nullable=False)

    # Relasi
    hewan = relationship('Hewan', back_populates='kategori', lazy='selectin')


# =========================
# TABEL HEWAN
# =========================
class Hewan(Base):
    __tablename__ = 'hewan'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nama_hewan = Column(String(100), nullable=False)
    umur = Column(Integer, nullable=False)
    foto = Column(String(255), nullable=True)

    status = Column(
        Enum(StatusHewan),
        default=StatusHewan.tersedia
    )

    id_kategori = Column(Integer, ForeignKey('kategori_hewan.id'))
    id_user = Column(Integer, ForeignKey('users.id'), nullable=True)

    # Relasi
    kategori = relationship('KategoriHewan', back_populates='hewan')
    user = relationship('Users', back_populates='hewan')


# =========================
# TABEL PRODUK
# =========================
class Produk(Base):
    __tablename__ = 'produk'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nama_produk = Column(String(100), nullable=False)
    harga = Column(Integer, nullable=False)
    stok = Column(Integer, default=0)
    gambar = Column(String(255), nullable=True)

    # Relasi
    transaksi = relationship('Transaksi', back_populates='produk', lazy='selectin')


# =========================
# TABEL GROOMING
# =========================
class Grooming(Base):
    __tablename__ = 'grooming'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nama_layanan = Column(String(100), nullable=False)
    harga = Column(Integer, nullable=False)
    deskripsi = Column(String(255), nullable=True)

    # Relasi
    transaksi = relationship('Transaksi', back_populates='grooming', lazy='selectin')


# =========================
# TABEL TRANSAKSI
# =========================
class Transaksi(Base):
    __tablename__ = 'transaksi'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)

    id_user = Column(Integer, ForeignKey('users.id'))
    id_produk = Column(Integer, ForeignKey('produk.id'), nullable=True)
    id_grooming = Column(Integer, ForeignKey('grooming.id'), nullable=True)

    tanggal = Column(Date, nullable=False)
    total = Column(Integer, nullable=False)

    status_pembayaran = Column(
        Enum(StatusPembayaran),
        default=StatusPembayaran.pending
    )

    # Relasi
    user = relationship('Users', back_populates='transaksi')
    produk = relationship('Produk', back_populates='transaksi')
    grooming = relationship('Grooming', back_populates='transaksi')