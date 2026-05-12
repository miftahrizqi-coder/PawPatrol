# crud.py

from sqlalchemy.orm import Session
from typing import Optional
import models
import schemas


# ==========================================
# USERS
# ==========================================

def get_user(db: Session, user_id: int):
    return db.query(models.Users).filter(
        models.Users.id == user_id
    ).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.Users).filter(
        models.Users.email == email
    ).first()


def get_all_users(
    db: Session,
    skip: int = 0,
    limit: int = 100
):
    return db.query(models.Users)\
        .offset(skip)\
        .limit(limit)\
        .all()


def create_user(
    db: Session,
    user: schemas.UsersCreate
):
    db_user = models.Users(**user.dict())

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


def update_user(
    db: Session,
    user_id: int,
    user: schemas.UsersCreate
):
    db_user = get_user(db, user_id)

    if db_user:
        db_user.nama = user.nama
        db_user.email = user.email
        db_user.password = user.password
        db_user.alamat = user.alamat

        db.commit()
        db.refresh(db_user)

    return db_user


def delete_user(db: Session, user_id: int):
    db_user = get_user(db, user_id)

    if db_user:
        db.delete(db_user)
        db.commit()
        return True

    return False


# ==========================================
# KATEGORI HEWAN
# ==========================================

def get_kategori_hewan(
    db: Session,
    kategori_id: int
):
    return db.query(models.KategoriHewan).filter(
        models.KategoriHewan.id == kategori_id
    ).first()


def get_all_kategori_hewan(
    db: Session,
    skip: int = 0,
    limit: int = 100
):
    return db.query(models.KategoriHewan)\
        .offset(skip)\
        .limit(limit)\
        .all()


def create_kategori_hewan(
    db: Session,
    kategori: schemas.KategoriHewanCreate
):
    db_kategori = models.KategoriHewan(**kategori.dict())

    db.add(db_kategori)
    db.commit()
    db.refresh(db_kategori)

    return db_kategori


def update_kategori_hewan(
    db: Session,
    kategori_id: int,
    kategori: schemas.KategoriHewanCreate
):
    db_kategori = get_kategori_hewan(db, kategori_id)

    if db_kategori:
        db_kategori.nama_kategori = kategori.nama_kategori

        db.commit()
        db.refresh(db_kategori)

    return db_kategori


def delete_kategori_hewan(
    db: Session,
    kategori_id: int
):
    db_kategori = get_kategori_hewan(db, kategori_id)

    if db_kategori:

        # cek apakah kategori dipakai hewan
        cek_hewan = db.query(models.Hewan).filter(
            models.Hewan.id_kategori == kategori_id
        ).count()

        if cek_hewan > 0:
            return False

        db.delete(db_kategori)
        db.commit()

        return True

    return False


# ==========================================
# HEWAN
# ==========================================

def get_hewan(
    db: Session,
    hewan_id: int
):
    return db.query(models.Hewan).filter(
        models.Hewan.id == hewan_id
    ).first()


def get_all_hewan(
    db: Session,
    skip: int = 0,
    limit: int = 100,
    kategori_id: Optional[int] = None,
    status: Optional[str] = None
):

    query = db.query(models.Hewan)

    if kategori_id:
        query = query.filter(
            models.Hewan.id_kategori == kategori_id
        )

    if status:
        query = query.filter(
            models.Hewan.status == status
        )

    return query.offset(skip).limit(limit).all()


def create_hewan(
    db: Session,
    hewan: schemas.HewanCreate
):
    db_hewan = models.Hewan(**hewan.dict())

    db.add(db_hewan)
    db.commit()
    db.refresh(db_hewan)

    return db_hewan


def update_hewan(
    db: Session,
    hewan_id: int,
    hewan: schemas.HewanCreate
):
    db_hewan = get_hewan(db, hewan_id)

    if db_hewan:
        db_hewan.nama_hewan = hewan.nama_hewan
        db_hewan.umur = hewan.umur
        db_hewan.foto = hewan.foto
        db_hewan.status = hewan.status
        db_hewan.id_kategori = hewan.id_kategori
        db_hewan.id_user = hewan.id_user

        db.commit()
        db.refresh(db_hewan)

    return db_hewan


def delete_hewan(
    db: Session,
    hewan_id: int
):
    db_hewan = get_hewan(db, hewan_id)

    if db_hewan:
        db.delete(db_hewan)
        db.commit()

        return True

    return False


# ==========================================
# PRODUK
# ==========================================

def get_produk(
    db: Session,
    produk_id: int
):
    return db.query(models.Produk).filter(
        models.Produk.id == produk_id
    ).first()


def get_all_produk(
    db: Session,
    skip: int = 0,
    limit: int = 100
):
    return db.query(models.Produk)\
        .offset(skip)\
        .limit(limit)\
        .all()


def create_produk(
    db: Session,
    produk: schemas.ProdukCreate
):
    db_produk = models.Produk(**produk.dict())

    db.add(db_produk)
    db.commit()
    db.refresh(db_produk)

    return db_produk


def update_produk(
    db: Session,
    produk_id: int,
    produk: schemas.ProdukCreate
):
    db_produk = get_produk(db, produk_id)

    if db_produk:
        db_produk.nama_produk = produk.nama_produk
        db_produk.harga = produk.harga
        db_produk.stok = produk.stok
        db_produk.gambar = produk.gambar

        db.commit()
        db.refresh(db_produk)

    return db_produk


def delete_produk(
    db: Session,
    produk_id: int
):
    db_produk = get_produk(db, produk_id)

    if db_produk:
        db.delete(db_produk)
        db.commit()

        return True

    return False


# ==========================================
# GROOMING
# ==========================================

def get_grooming(
    db: Session,
    grooming_id: int
):
    return db.query(models.Grooming).filter(
        models.Grooming.id == grooming_id
    ).first()


def get_all_grooming(
    db: Session,
    skip: int = 0,
    limit: int = 100
):
    return db.query(models.Grooming)\
        .offset(skip)\
        .limit(limit)\
        .all()


def create_grooming(
    db: Session,
    grooming: schemas.GroomingCreate
):
    db_grooming = models.Grooming(**grooming.dict())

    db.add(db_grooming)
    db.commit()
    db.refresh(db_grooming)

    return db_grooming


def update_grooming(
    db: Session,
    grooming_id: int,
    grooming: schemas.GroomingCreate
):
    db_grooming = get_grooming(db, grooming_id)

    if db_grooming:
        db_grooming.nama_layanan = grooming.nama_layanan
        db_grooming.harga = grooming.harga
        db_grooming.deskripsi = grooming.deskripsi

        db.commit()
        db.refresh(db_grooming)

    return db_grooming


def delete_grooming(
    db: Session,
    grooming_id: int
):
    db_grooming = get_grooming(db, grooming_id)

    if db_grooming:
        db.delete(db_grooming)
        db.commit()

        return True

    return False


# ==========================================
# TRANSAKSI
# ==========================================

def get_transaksi(
    db: Session,
    transaksi_id: int
):
    return db.query(models.Transaksi).filter(
        models.Transaksi.id == transaksi_id
    ).first()


def get_all_transaksi(
    db: Session,
    skip: int = 0,
    limit: int = 100,
    user_id: Optional[int] = None,
    status_pembayaran: Optional[str] = None
):

    query = db.query(models.Transaksi)

    if user_id:
        query = query.filter(
            models.Transaksi.id_user == user_id
        )

    if status_pembayaran:
        query = query.filter(
            models.Transaksi.status_pembayaran == status_pembayaran
        )

    return query.offset(skip).limit(limit).all()


def create_transaksi(
    db: Session,
    transaksi: schemas.TransaksiCreate
):

    total_harga = 0

    # ======================
    # CEK PRODUK
    # ======================
    if transaksi.id_produk:

        produk = db.query(models.Produk).filter(
            models.Produk.id == transaksi.id_produk
        ).first()

        if not produk:
            return None

        if produk.stok <= 0:
            return None

        total_harga += produk.harga

        # kurangi stok
        produk.stok -= 1

    # ======================
    # CEK GROOMING
    # ======================
    if transaksi.id_grooming:

        grooming = db.query(models.Grooming).filter(
            models.Grooming.id == transaksi.id_grooming
        ).first()

        if not grooming:
            return None

        total_harga += grooming.harga

    db_transaksi = models.Transaksi(
        id_user=transaksi.id_user,
        id_produk=transaksi.id_produk,
        id_grooming=transaksi.id_grooming,
        tanggal=transaksi.tanggal,
        total=total_harga,
        status_pembayaran=transaksi.status_pembayaran
    )

    db.add(db_transaksi)
    db.commit()
    db.refresh(db_transaksi)

    return db_transaksi


def update_status_transaksi(
    db: Session,
    transaksi_id: int,
    status_pembayaran: str
):
    db_transaksi = get_transaksi(db, transaksi_id)

    if db_transaksi:
        db_transaksi.status_pembayaran = status_pembayaran

        db.commit()
        db.refresh(db_transaksi)

    return db_transaksi


def delete_transaksi(
    db: Session,
    transaksi_id: int
):
    db_transaksi = get_transaksi(db, transaksi_id)

    if db_transaksi:
        db.delete(db_transaksi)
        db.commit()

        return True

    return False