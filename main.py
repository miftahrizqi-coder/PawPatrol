# main.py

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
from auth import create_access_token

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
    description="API Pet Shop, Adopsi Hewan, Produk, dan Grooming",
    version="2.0.0"
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

    return crud.create_user(
        db,
        user
    )


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
def get_user_by_id(
    user_id: int,
    db: Session = Depends(get_db)
):

    user = crud.get_user(
        db,
        user_id
    )

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
    user: schemas.UserUpdate,
    db: Session = Depends(get_db)
):

    updated = crud.update_user(
        db,
        user_id,
        user
    )

    if not updated:
        raise HTTPException(
            status_code=404,
            detail="User tidak ditemukan"
        )

    return updated


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
# CATEGORIES
# ======================================================

@app.post(
    "/categories",
    response_model=schemas.CategoryOut
)
def create_category(
    category: schemas.CategoryCreate,
    db: Session = Depends(get_db)
):
    return crud.create_category(
        db,
        category
    )


@app.get(
    "/categories",
    response_model=List[schemas.CategoryOut]
)
def get_categories(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    return crud.get_all_categories(
        db,
        skip,
        limit
    )


@app.get(
    "/categories/{category_id}",
    response_model=schemas.CategoryOut
)
def get_category_by_id(
    category_id: int,
    db: Session = Depends(get_db)
):

    category = crud.get_category(
        db,
        category_id
    )

    if not category:
        raise HTTPException(
            status_code=404,
            detail="Kategori tidak ditemukan"
        )

    return category


@app.put(
    "/categories/{category_id}",
    response_model=schemas.CategoryOut
)
def update_category(
    category_id: int,
    category: schemas.CategoryUpdate,
    db: Session = Depends(get_db)
):

    updated = crud.update_category(
        db,
        category_id,
        category
    )

    if not updated:
        raise HTTPException(
            status_code=404,
            detail="Kategori tidak ditemukan"
        )

    return updated


@app.delete("/categories/{category_id}")
def delete_category(
    category_id: int,
    db: Session = Depends(get_db)
):

    deleted = crud.delete_category(
        db,
        category_id
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
# ANIMALS
# ======================================================

@app.post(
    "/animals",
    response_model=schemas.AnimalOut
)
def create_animal(
    animal: schemas.AnimalCreate,
    db: Session = Depends(get_db)
):
    return crud.create_animal(
        db,
        animal
    )


@app.get(
    "/animals",
    response_model=List[schemas.AnimalOut]
)
def get_animals(
    skip: int = 0,
    limit: int = 100,
    kategori_id: Optional[int] = None,
    status: Optional[str] = None,
    db: Session = Depends(get_db)
):
    return crud.get_all_animals(
        db,
        skip,
        limit,
        kategori_id,
        status
    )


@app.get(
    "/animals/{animal_id}",
    response_model=schemas.AnimalOut
)
def get_animal_by_id(
    animal_id: int,
    db: Session = Depends(get_db)
):

    animal = crud.get_animal(
        db,
        animal_id
    )

    if not animal:
        raise HTTPException(
            status_code=404,
            detail="Hewan tidak ditemukan"
        )

    return animal


@app.put(
    "/animals/{animal_id}",
    response_model=schemas.AnimalOut
)
def update_animal(
    animal_id: int,
    animal: schemas.AnimalUpdate,
    db: Session = Depends(get_db)
):

    updated = crud.update_animal(
        db,
        animal_id,
        animal
    )

    if not updated:
        raise HTTPException(
            status_code=404,
            detail="Hewan tidak ditemukan"
        )

    return updated


@app.delete("/animals/{animal_id}")
def delete_animal(
    animal_id: int,
    db: Session = Depends(get_db)
):

    deleted = crud.delete_animal(
        db,
        animal_id
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
# PRODUCTS
# ======================================================

@app.post(
    "/products",
    response_model=schemas.ProductOut
)
def create_product(
    product: schemas.ProductCreate,
    db: Session = Depends(get_db)
):
    return crud.create_product(
        db,
        product
    )


@app.get(
    "/products",
    response_model=List[schemas.ProductOut]
)
def get_products(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    return crud.get_all_products(
        db,
        skip,
        limit
    )


@app.get(
    "/products/{product_id}",
    response_model=schemas.ProductOut
)
def get_product_by_id(
    product_id: int,
    db: Session = Depends(get_db)
):

    product = crud.get_product(
        db,
        product_id
    )

    if not product:
        raise HTTPException(
            status_code=404,
            detail="Produk tidak ditemukan"
        )

    return product


@app.put(
    "/products/{product_id}",
    response_model=schemas.ProductOut
)
def update_product(
    product_id: int,
    product: schemas.ProductUpdate,
    db: Session = Depends(get_db)
):

    updated = crud.update_product(
        db,
        product_id,
        product
    )

    if not updated:
        raise HTTPException(
            status_code=404,
            detail="Produk tidak ditemukan"
        )

    return updated


@app.delete("/products/{product_id}")
def delete_product(
    product_id: int,
    db: Session = Depends(get_db)
):

    deleted = crud.delete_product(
        db,
        product_id
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
# GROOMING SERVICES
# ======================================================

@app.post(
    "/grooming-services",
    response_model=schemas.GroomingServiceOut
)
def create_grooming_service(
    service: schemas.GroomingServiceCreate,
    db: Session = Depends(get_db)
):
    return crud.create_grooming_service(
        db,
        service
    )


@app.get(
    "/grooming-services",
    response_model=List[schemas.GroomingServiceOut]
)
def get_grooming_services(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    return crud.get_all_grooming_services(
        db,
        skip,
        limit
    )


@app.get(
    "/grooming-services/{service_id}",
    response_model=schemas.GroomingServiceOut
)
def get_grooming_service_by_id(
    service_id: int,
    db: Session = Depends(get_db)
):

    service = crud.get_grooming_service(
        db,
        service_id
    )

    if not service:
        raise HTTPException(
            status_code=404,
            detail="Layanan grooming tidak ditemukan"
        )

    return service


@app.put(
    "/grooming-services/{service_id}",
    response_model=schemas.GroomingServiceOut
)
def update_grooming_service(
    service_id: int,
    service: schemas.GroomingServiceUpdate,
    db: Session = Depends(get_db)
):

    updated = crud.update_grooming_service(
        db,
        service_id,
        service
    )

    if not updated:
        raise HTTPException(
            status_code=404,
            detail="Layanan grooming tidak ditemukan"
        )

    return updated


@app.delete("/grooming-services/{service_id}")
def delete_grooming_service(
    service_id: int,
    db: Session = Depends(get_db)
):

    deleted = crud.delete_grooming_service(
        db,
        service_id
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Layanan grooming tidak ditemukan"
        )

    return {
        "message": "Layanan grooming berhasil dihapus"
    }


# ======================================================
# ORDERS
# ======================================================

@app.post(
    "/orders",
    response_model=schemas.OrderOut
)
def create_order(
    order: schemas.OrderCreate,
    db: Session = Depends(get_db)
):
    return crud.create_order(
        db,
        order
    )


@app.get(
    "/orders",
    response_model=List[schemas.OrderOut]
)
def get_orders(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    return crud.get_all_orders(
        db,
        skip,
        limit
    )


@app.get(
    "/orders/{order_id}",
    response_model=schemas.OrderOut
)
def get_order_by_id(
    order_id: int,
    db: Session = Depends(get_db)
):

    order = crud.get_order(
        db,
        order_id
    )

    if not order:
        raise HTTPException(
            status_code=404,
            detail="Order tidak ditemukan"
        )

    return order


@app.patch(
    "/orders/{order_id}/status",
    response_model=schemas.OrderOut
)
def update_order_status(
    order_id: int,
    status: str,
    db: Session = Depends(get_db)
):

    updated = crud.update_order_status(
        db,
        order_id,
        status
    )

    if not updated:
        raise HTTPException(
            status_code=404,
            detail="Order tidak ditemukan"
        )

    return updated


# ======================================================
# ORDER PRODUCTS
# ======================================================

@app.post(
    "/order-products",
    response_model=schemas.OrderProductOut
)
def create_order_product(
    item: schemas.OrderProductCreate,
    db: Session = Depends(get_db)
):

    db_item = crud.create_order_product(
        db,
        item
    )

    if not db_item:
        raise HTTPException(
            status_code=400,
            detail="Produk gagal ditambahkan ke order"
        )

    return db_item


# ======================================================
# ANIMAL ADOPTIONS
# ======================================================

@app.post(
    "/animal-adoptions",
    response_model=schemas.AnimalAdoptionOut
)
def create_animal_adoption(
    adoption: schemas.AnimalAdoptionCreate,
    db: Session = Depends(get_db)
):

    db_adoption = crud.create_animal_adoption(
        db,
        adoption
    )

    if not db_adoption:
        raise HTTPException(
            status_code=400,
            detail="Adopsi gagal"
        )

    return db_adoption


# ======================================================
# GROOMING BOOKINGS
# ======================================================

@app.post(
    "/grooming-bookings",
    response_model=schemas.GroomingBookingOut
)
def create_grooming_booking(
    booking: schemas.GroomingBookingCreate,
    db: Session = Depends(get_db)
):

    db_booking = crud.create_grooming_booking(
        db,
        booking
    )

    if not db_booking:
        raise HTTPException(
            status_code=400,
            detail="Booking grooming gagal"
        )

    return db_booking


@app.patch(
    "/grooming-bookings/{booking_id}/status",
    response_model=schemas.GroomingBookingOut
)
def update_grooming_booking_status(
    booking_id: int,
    status: str,
    db: Session = Depends(get_db)
):

    updated = crud.update_grooming_booking_status(
        db,
        booking_id,
        status
    )

    if not updated:
        raise HTTPException(
            status_code=404,
            detail="Booking tidak ditemukan"
        )

    return updated

# ======================================================
# AUTH
# ======================================================

@app.post(
    "/auth/register",
    response_model=schemas.UserOut
)
def register(
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

    return crud.create_user(
        db,
        user
    )


@app.post(
    "/auth/login",
    response_model=schemas.LoginResponse
)
def login(
    request: schemas.LoginRequest,
    db: Session = Depends(get_db)
):

    user = crud.login_user(
        db,
        request.email,
        request.password
    )

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Email atau password salah"
        )

    token = create_access_token({
        "sub": user.email
    })

    return {
        "access_token": token,
        "token_type": "bearer",
        "user": user
    }

# ======================================================
# CART ITEMS
# ======================================================
@app.post("/cart/add")
def add_to_cart(
    request: schemas.AddToCartRequest,
    db: Session = Depends(get_db)
):

    result = crud.add_to_cart(
        db,
        request.user_id,
        request.product_id,
        request.quantity
    )

    if result == "stok_habis":
        raise HTTPException(
            status_code=400,
            detail="Stok produk tidak cukup"
        )

    if not result:
        raise HTTPException(
            status_code=404,
            detail="Produk tidak ditemukan"
        )

    return {
        "message": "Produk berhasil ditambahkan ke cart",
        "cart_id": result.id
    }

@app.get("/cart/{user_id}")
def get_cart(
    user_id: int,
    db: Session = Depends(get_db)
):

    return crud.get_cart_items(
        db,
        user_id
    )

# ======================================================
# REMOVE FROM CART
# ======================================================

@app.delete("/cart/remove")
def remove_item_from_cart(
    user_id: int,
    product_id: int,
    db: Session = Depends(get_db)
):

    result = crud.remove_from_cart(
        db,
        user_id,
        product_id
    )

    if not result:
        raise HTTPException(
            status_code=404,
            detail="Item cart tidak ditemukan"
        )

    return {
        "message": "Item berhasil dihapus dari cart",
        "cart_total": result.total_harga
    }

# ======================================================
# UPDATE CART ITEM QUANTITY
# ======================================================

@app.put("/cart/update")
def update_cart_quantity(
    user_id: int,
    product_id: int,
    quantity: int,
    db: Session = Depends(get_db)
):

    result = crud.update_cart_item_quantity(
        db,
        user_id,
        product_id,
        quantity
    )

    if result == "invalid_quantity":
        raise HTTPException(
            status_code=400,
            detail="Quantity harus lebih dari 0"
        )

    if result == "stok_habis":
        raise HTTPException(
            status_code=400,
            detail="Stok produk tidak mencukupi"
        )

    if not result:
        raise HTTPException(
            status_code=404,
            detail="Item cart tidak ditemukan"
        )

    return {
        "message": "Quantity cart berhasil diupdate",
        "cart_total": result.total_harga
    }

@app.post("/cart/checkout/{user_id}")
def checkout_cart(
    user_id: int,
    db: Session = Depends(get_db)
):

    cart = crud.checkout_cart(
        db,
        user_id
    )

    if not cart:
        raise HTTPException(
            status_code=404,
            detail="Cart tidak ditemukan"
        )

    return {
        "message": "Checkout berhasil",
        "order_id": cart.id
    }