# main.py

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional

import models
import schemas
import crud

from database import SessionLocal, engine


# ======================================================
# CREATE TABLE
# ======================================================

models.Base.metadata.create_all(bind=engine)


# ======================================================
# FASTAPI APP
# ======================================================

app = FastAPI(
    title="Pet Shop API",
    description="API Pet Shop, Adopsi Hewan, dan Grooming",
    version="1.0.0"
)


# ======================================================
# DATABASE SESSION
# ======================================================

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


# ======================================================
# ROOT
# ======================================================

@app.get("/")
def root():
    return {
        "message": "Pet Shop API Running"
    }


# ======================================================
# USERS
# ======================================================

@app.post(
    "/users",
    response_model=schemas.UserOut
)
def create_user(
    user: schemas.UserCreate,
    db: Session = Depends(get_db)
):

    cek_email = crud.get_user_by_email(
        db,
        user.email
    )

    if cek_email:
        raise HTTPException(
            status_code=400,
            detail="Email sudah digunakan"
        )

    return crud.create_user(db, user)


@app.get(
    "/users",
    response_model=List[schemas.UserOut]
)
def get_users(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    return crud.get_all_users(
        db,
        skip,
        limit
    )


@app.get(
    "/users/{user_id}",
    response_model=schemas.UserOut
)
def get_user(
    user_id: int,
    db: Session = Depends(get_db)
):

    user = crud.get_user(db, user_id)

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User tidak ditemukan"
        )

    return user


@app.put(
    "/users/{user_id}",
    response_model=schemas.UserOut
)
def update_user(
    user_id: int,
    user: schemas.UserCreate,
    db: Session = Depends(get_db)
):

    db_user = crud.update_user(
        db,
        user_id,
        user
    )

    if not db_user:
        raise HTTPException(
            status_code=404,
            detail="User tidak ditemukan"
        )

    return db_user


@app.delete("/users/{user_id}")
def delete_user(
    user_id: int,
    db: Session = Depends(get_db)
):

    deleted = crud.delete_user(
        db,
        user_id
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="User tidak ditemukan"
        )

    return {
        "message": "User berhasil dihapus"
    }


# ======================================================
# KATEGORI HEWAN
# ======================================================

@app.post(
    "/kategori-hewan",
    response_model=schemas.KategoriHewanOut
)
def create_kategori_hewan(
    kategori: schemas.KategoriHewanCreate,
    db: Session = Depends(get_db)
):
    return crud.create_kategori_hewan(
        db,
        kategori
    )


@app.get(
    "/kategori-hewan",
    response_model=List[schemas.KategoriHewanOut]
)
def get_kategori_hewan(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    return crud.get_all_kategori_hewan(
        db,
        skip,
        limit
    )


@app.get(
    "/kategori-hewan/{kategori_id}",
    response_model=schemas.KategoriHewanOut
)
def get_kategori_by_id(
    kategori_id: int,
    db: Session = Depends(get_db)
):

    kategori = crud.get_kategori_hewan(
        db,
        kategori_id
    )

    if not kategori:
        raise HTTPException(
            status_code=404,
            detail="Kategori tidak ditemukan"
        )

    return kategori


@app.put(
    "/kategori-hewan/{kategori_id}",
    response_model=schemas.KategoriHewanOut
)
def update_kategori(
    kategori_id: int,
    kategori: schemas.KategoriHewanCreate,
    db: Session = Depends(get_db)
):

    updated = crud.update_kategori_hewan(
        db,
        kategori_id,
        kategori
    )

    if not updated:
        raise HTTPException(
            status_code=404,
            detail="Kategori tidak ditemukan"
        )

    return updated


@app.delete("/kategori-hewan/{kategori_id}")
def delete_kategori(
    kategori_id: int,
    db: Session = Depends(get_db)
):

    deleted = crud.delete_kategori_hewan(
        db,
        kategori_id
    )

    if not deleted:
        raise HTTPException(
            status_code=400,
            detail="Kategori tidak bisa dihapus"
        )

    return {
        "message": "Kategori berhasil dihapus"
    }


# ======================================================
# HEWAN
# ======================================================

@app.post(
    "/hewan",
    response_model=schemas.HewanOut
)
def create_hewan(
    hewan: schemas.HewanCreate,
    db: Session = Depends(get_db)
):
    return crud.create_hewan(
        db,
        hewan
    )


@app.get(
    "/hewan",
    response_model=List[schemas.HewanOut]
)
def get_hewan(
    skip: int = 0,
    limit: int = 100,
    kategori_id: Optional[int] = None,
    status: Optional[str] = None,
    db: Session = Depends(get_db)
):
    return crud.get_all_hewan(
        db,
        skip,
        limit,
        kategori_id,
        status
    )


@app.get(
    "/hewan/{hewan_id}",
    response_model=schemas.HewanOut
)
def get_hewan_by_id(
    hewan_id: int,
    db: Session = Depends(get_db)
):

    hewan = crud.get_hewan(
        db,
        hewan_id
    )

    if not hewan:
        raise HTTPException(
            status_code=404,
            detail="Hewan tidak ditemukan"
        )

    return hewan


@app.put(
    "/hewan/{hewan_id}",
    response_model=schemas.HewanOut
)
def update_hewan(
    hewan_id: int,
    hewan: schemas.HewanUpdate,
    db: Session = Depends(get_db)
):

    updated = crud.update_hewan(
        db,
        hewan_id,
        hewan
    )

    if not updated:
        raise HTTPException(
            status_code=404,
            detail="Hewan tidak ditemukan"
        )

    return updated


@app.delete("/hewan/{hewan_id}")
def delete_hewan(
    hewan_id: int,
    db: Session = Depends(get_db)
):

    deleted = crud.delete_hewan(
        db,
        hewan_id
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Hewan tidak ditemukan"
        )

    return {
        "message": "Hewan berhasil dihapus"
    }


# ======================================================
# PRODUK
# ======================================================

@app.post(
    "/produk",
    response_model=schemas.ProdukOut
)
def create_produk(
    produk: schemas.ProdukCreate,
    db: Session = Depends(get_db)
):
    return crud.create_produk(
        db,
        produk
    )


@app.get(
    "/produk",
    response_model=List[schemas.ProdukOut]
)
def get_produk(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    return crud.get_all_produk(
        db,
        skip,
        limit
    )


@app.get(
    "/produk/{produk_id}",
    response_model=schemas.ProdukOut
)
def get_produk_by_id(
    produk_id: int,
    db: Session = Depends(get_db)
):

    produk = crud.get_produk(
        db,
        produk_id
    )

    if not produk:
        raise HTTPException(
            status_code=404,
            detail="Produk tidak ditemukan"
        )

    return produk


@app.put(
    "/produk/{produk_id}",
    response_model=schemas.ProdukOut
)
def update_produk(
    produk_id: int,
    produk: schemas.ProdukUpdate,
    db: Session = Depends(get_db)
):

    updated = crud.update_produk(
        db,
        produk_id,
        produk
    )

    if not updated:
        raise HTTPException(
            status_code=404,
            detail="Produk tidak ditemukan"
        )

    return updated


@app.delete("/produk/{produk_id}")
def delete_produk(
    produk_id: int,
    db: Session = Depends(get_db)
):

    deleted = crud.delete_produk(
        db,
        produk_id
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Produk tidak ditemukan"
        )

    return {
        "message": "Produk berhasil dihapus"
    }


# ======================================================
# GROOMING
# ======================================================

@app.post(
    "/grooming",
    response_model=schemas.GroomingOut
)
def create_grooming(
    grooming: schemas.GroomingCreate,
    db: Session = Depends(get_db)
):
    return crud.create_grooming(
        db,
        grooming
    )


@app.get(
    "/grooming",
    response_model=List[schemas.GroomingOut]
)
def get_grooming(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    return crud.get_all_grooming(
        db,
        skip,
        limit
    )


@app.get(
    "/grooming/{grooming_id}",
    response_model=schemas.GroomingOut
)
def get_grooming_by_id(
    grooming_id: int,
    db: Session = Depends(get_db)
):

    grooming = crud.get_grooming(
        db,
        grooming_id
    )

    if not grooming:
        raise HTTPException(
            status_code=404,
            detail="Grooming tidak ditemukan"
        )

    return grooming


@app.put(
    "/grooming/{grooming_id}",
    response_model=schemas.GroomingOut
)
def update_grooming(
    grooming_id: int,
    grooming: schemas.GroomingUpdate,
    db: Session = Depends(get_db)
):

    updated = crud.update_grooming(
        db,
        grooming_id,
        grooming
    )

    if not updated:
        raise HTTPException(
            status_code=404,
            detail="Grooming tidak ditemukan"
        )

    return updated


@app.delete("/grooming/{grooming_id}")
def delete_grooming(
    grooming_id: int,
    db: Session = Depends(get_db)
):

    deleted = crud.delete_grooming(
        db,
        grooming_id
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Grooming tidak ditemukan"
        )

    return {
        "message": "Grooming berhasil dihapus"
    }


# ======================================================
# TRANSAKSI
# ======================================================

@app.post(
    "/transaksi",
    response_model=schemas.TransaksiOut
)
def create_transaksi(
    transaksi: schemas.TransaksiCreate,
    db: Session = Depends(get_db)
):

    db_transaksi = crud.create_transaksi(
        db,
        transaksi
    )

    if not db_transaksi:
        raise HTTPException(
            status_code=400,
            detail="Transaksi gagal"
        )

    return db_transaksi


@app.get(
    "/transaksi",
    response_model=List[schemas.TransaksiOut]
)
def get_transaksi(
    skip: int = 0,
    limit: int = 100,
    user_id: Optional[int] = None,
    status_pembayaran: Optional[str] = None,
    jenis_transaksi: Optional[str] = None,
    db: Session = Depends(get_db)
):
    return crud.get_all_transaksi(
        db,
        skip,
        limit,
        user_id,
        status_pembayaran,
        jenis_transaksi
    )


@app.get(
    "/transaksi/{transaksi_id}",
    response_model=schemas.TransaksiOut
)
def get_transaksi_by_id(
    transaksi_id: int,
    db: Session = Depends(get_db)
):

    transaksi = crud.get_transaksi(
        db,
        transaksi_id
    )

    if not transaksi:
        raise HTTPException(
            status_code=404,
            detail="Transaksi tidak ditemukan"
        )

    return transaksi


@app.patch(
    "/transaksi/{transaksi_id}/status",
    response_model=schemas.TransaksiOut
)
def update_status_transaksi(
    transaksi_id: int,
    status_pembayaran: str,
    db: Session = Depends(get_db)
):

    transaksi = crud.update_status_transaksi(
        db,
        transaksi_id,
        status_pembayaran
    )

    if not transaksi:
        raise HTTPException(
            status_code=404,
            detail="Transaksi tidak ditemukan"
        )

    return transaksi


@app.delete("/transaksi/{transaksi_id}")
def delete_transaksi(
    transaksi_id: int,
    db: Session = Depends(get_db)
):

    deleted = crud.delete_transaksi(
        db,
        transaksi_id
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Transaksi tidak ditemukan"
        )

    return {
        "message": "Transaksi berhasil dihapus"
    }