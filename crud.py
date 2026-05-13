# crud.py

from sqlalchemy.orm import Session
from typing import Optional
from models import StatusOrder

import models
import schemas


# ======================================================
# USERS
# ======================================================

def get_user(db: Session, user_id: int):
    return db.query(models.Users).filter(
        models.Users.id == user_id
    ).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.Users).filter(
        models.Users.email == email
    ).first()


def get_all_users(db: Session, skip=0, limit=100):
    return db.query(models.Users)\
        .offset(skip)\
        .limit(limit)\
        .all()


def create_user(
    db: Session,
    user: schemas.UserCreate
):

    db_user = models.Users(
    nama=user.nama,
    email=user.email,
    password_hash=user.password,
    alamat=user.alamat,
)

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


def update_user(db: Session, user_id: int, user: schemas.UserUpdate):
    db_user = get_user(db, user_id)

    if not db_user:
        return None

    data = user.model_dump(exclude_unset=True)

    for k, v in data.items():
        setattr(db_user, k, v)

    db.commit()
    db.refresh(db_user)

    return db_user


def delete_user(db: Session, user_id: int):
    db_user = get_user(db, user_id)

    if not db_user:
        return False

    db.delete(db_user)
    db.commit()

    return True

def login_user(
    db: Session,
    email: str,
    password: str
):

    user = db.query(models.Users).filter(
        models.Users.email == email
    ).first()

    if not user:
        return None

    if password != user.password_hash:
        return None

    return user
# ======================================================
# CATEGORIES
# ======================================================

def get_category(db: Session, category_id: int):
    return db.query(models.Categories).filter(
        models.Categories.id == category_id
    ).first()


def get_all_categories(db: Session, skip=0, limit=100):
    return db.query(models.Categories)\
        .offset(skip)\
        .limit(limit)\
        .all()


def create_category(db: Session, category: schemas.CategoryCreate):
    db_obj = models.Categories(**category.model_dump())

    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)

    return db_obj


def update_category(db: Session, category_id: int,
                    category: schemas.CategoryUpdate):

    db_obj = get_category(db, category_id)

    if not db_obj:
        return None

    data = category.model_dump(exclude_unset=True)

    for k, v in data.items():
        setattr(db_obj, k, v)

    db.commit()
    db.refresh(db_obj)

    return db_obj


def delete_category(db: Session, category_id: int):
    db_obj = get_category(db, category_id)

    if not db_obj:
        return False

    count = db.query(models.Animals).filter(
        models.Animals.kategori_id == category_id
    ).count()

    if count > 0:
        return False

    db.delete(db_obj)
    db.commit()

    return True


# ======================================================
# ANIMALS
# ======================================================

def get_animal(db: Session, animal_id: int):
    return db.query(models.Animals).filter(
        models.Animals.id == animal_id
    ).first()


def get_all_animals(
        db: Session,
        skip=0,
        limit=100,
        kategori_id: Optional[int] = None,
        status: Optional[str] = None
):
    query = db.query(models.Animals)

    if kategori_id:
        query = query.filter(
            models.Animals.kategori_id == kategori_id
        )

    if status:
        query = query.filter(
            models.Animals.status_adopsi == status
        )

    return query.offset(skip).limit(limit).all()


def create_animal(db: Session, animal: schemas.AnimalCreate):
    db_obj = models.Animals(**animal.model_dump())

    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)

    return db_obj


def update_animal(db: Session, animal_id: int,
                  animal: schemas.AnimalUpdate):

    db_obj = get_animal(db, animal_id)

    if not db_obj:
        return None

    data = animal.model_dump(exclude_unset=True)

    for k, v in data.items():
        setattr(db_obj, k, v)

    db.commit()
    db.refresh(db_obj)

    return db_obj


def delete_animal(db: Session, animal_id: int):
    db_obj = get_animal(db, animal_id)

    if not db_obj:
        return False

    db.delete(db_obj)
    db.commit()

    return True


# ======================================================
# PRODUCTS
# ======================================================

def get_product(db: Session, product_id: int):
    return db.query(models.Products).filter(
        models.Products.id == product_id
    ).first()


def get_all_products(db: Session, skip=0, limit=100):
    return db.query(models.Products)\
        .offset(skip)\
        .limit(limit)\
        .all()


def create_product(db: Session, product: schemas.ProductCreate):
    db_obj = models.Products(**product.model_dump())

    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)

    return db_obj


def update_product(db: Session, product_id: int,
                   product: schemas.ProductUpdate):

    db_obj = get_product(db, product_id)

    if not db_obj:
        return None

    data = product.model_dump(exclude_unset=True)

    for k, v in data.items():
        setattr(db_obj, k, v)

    db.commit()
    db.refresh(db_obj)

    return db_obj


def delete_product(db: Session, product_id: int):
    db_obj = get_product(db, product_id)

    if not db_obj:
        return False

    db.delete(db_obj)
    db.commit()

    return True


# ======================================================
# GROOMING SERVICES
# ======================================================

def get_grooming_service(db: Session, service_id: int):
    return db.query(models.GroomingServices).filter(
        models.GroomingServices.id == service_id
    ).first()


def get_all_grooming_services(db: Session,
                              skip=0,
                              limit=100):
    return db.query(models.GroomingServices)\
        .offset(skip)\
        .limit(limit)\
        .all()


def create_grooming_service(
        db: Session,
        service: schemas.GroomingServiceCreate
):
    db_obj = models.GroomingServices(
        **service.model_dump()
    )

    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)

    return db_obj


def update_grooming_service(
        db: Session,
        service_id: int,
        service: schemas.GroomingServiceUpdate
):
    db_obj = get_grooming_service(db, service_id)

    if not db_obj:
        return None

    data = service.model_dump(exclude_unset=True)

    for k, v in data.items():
        setattr(db_obj, k, v)

    db.commit()
    db.refresh(db_obj)

    return db_obj


def delete_grooming_service(
        db: Session,
        service_id: int
):
    db_obj = get_grooming_service(db, service_id)

    if not db_obj:
        return False

    db.delete(db_obj)
    db.commit()

    return True


# ======================================================
# ORDERS
# ======================================================

def get_order(db: Session, order_id: int):
    return db.query(models.Orders).filter(
        models.Orders.id == order_id
    ).first()


def get_all_orders(db: Session,
                   skip=0,
                   limit=100):
    return db.query(models.Orders)\
        .offset(skip)\
        .limit(limit)\
        .all()


def create_order(db: Session,
                 order: schemas.OrderCreate):

    db_obj = models.Orders(
        user_id=order.user_id,
        total_harga=order.total_harga
    )

    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)

    return db_obj


def update_order_status(
        db: Session,
        order_id: int,
        status: str
):
    db_obj = get_order(db, order_id)

    if not db_obj:
        return None

    db_obj.status = status

    db.commit()
    db.refresh(db_obj)

    return db_obj


# ======================================================
# ORDER PRODUCT
# ======================================================

def create_order_product(
        db: Session,
        item: schemas.OrderProductCreate
):
    product = get_product(
        db,
        item.product_id
    )

    if not product:
        return None

    if product.stok < item.quantity:
        return None

    product.stok -= item.quantity

    db_obj = models.OrderProducts(
        **item.model_dump()
    )

    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)

    return db_obj


# ======================================================
# ANIMAL ADOPTION
# ======================================================

def create_animal_adoption(
        db: Session,
        adoption: schemas.AnimalAdoptionCreate
):
    animal = get_animal(
        db,
        adoption.animal_id
    )

    if not animal:
        return None

    if animal.status_adopsi == "diadopsi":
        return None

    animal.status_adopsi = "diadopsi"

    db_obj = models.AnimalAdoptions(
        **adoption.model_dump()
    )

    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)

    return db_obj


# ======================================================
# GROOMING BOOKING
# ======================================================

def create_grooming_booking(
        db: Session,
        booking: schemas.GroomingBookingCreate
):
    service = get_grooming_service(
        db,
        booking.grooming_service_id
    )

    if not service:
        return None

    bentrok = db.query(
        models.GroomingBookings
    ).filter(
        models.GroomingBookings.booking_date ==
        booking.booking_date,

        models.GroomingBookings.booking_time ==
        booking.booking_time
    ).first()

    if bentrok:
        return None

    db_obj = models.GroomingBookings(
        **booking.model_dump()
    )

    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)

    return db_obj


def update_grooming_booking_status(
        db: Session,
        booking_id: int,
        status: str
):
    booking = db.query(
        models.GroomingBookings
    ).filter(
        models.GroomingBookings.id == booking_id
    ).first()

    if not booking:
        return None

    booking.status = status

    db.commit()
    db.refresh(booking)

    return booking

# ======================================================
# CART
# ======================================================

def get_cart_by_user(
    db: Session,
    user_id: int
):
    return db.query(models.Orders).filter(
        models.Orders.user_id == user_id,
        models.Orders.status == StatusOrder.cart
    ).first()

def add_to_cart(
    db: Session,
    user_id: int,
    product_id: int,
    quantity: int
):

    product = get_product(
        db,
        product_id
    )

    if not product:
        return None

    if product.stok < quantity:
        return "stok_habis"

    # =========================
    # CEK CART USER
    # =========================
    cart = get_cart_by_user(
        db,
        user_id
    )

    # =========================
    # BUAT CART BARU
    # =========================
    if not cart:

        cart = models.Orders(
            user_id=user_id,
            total_harga=0,
            status="cart"
        )

        db.add(cart)
        db.commit()
        db.refresh(cart)

    # =========================
    # CEK PRODUK SUDAH ADA?
    # =========================
    existing_item = db.query(
        models.OrderProducts
    ).filter(
        models.OrderProducts.order_id == cart.id,
        models.OrderProducts.product_id == product_id
    ).first()

    if existing_item:

        existing_item.quantity += quantity

        existing_item.harga = (
            existing_item.quantity *
            product.harga
        )

    else:

        cart_item = models.OrderProducts(
            order_id=cart.id,
            product_id=product_id,
            quantity=quantity,
            harga=product.harga * quantity
        )

        db.add(cart_item)

    # =========================
    # SIMPAN DULU ITEM
    # =========================
    db.commit()

    # =========================
    # HITUNG ULANG TOTAL
    # =========================
    items = db.query(
        models.OrderProducts
    ).filter(
        models.OrderProducts.order_id == cart.id
    ).all()

    total_harga = sum(
        item.harga for item in items
    )

    cart.total_harga = total_harga

    db.commit()
    db.refresh(cart)

    return cart

def get_cart_items(
    db: Session,
    user_id: int
):

    cart = get_cart_by_user(
        db,
        user_id
    )

    if not cart:
        return []

    return db.query(
        models.OrderProducts
    ).filter(
        models.OrderProducts.order_id == cart.id
    ).all()

# ======================================================
# REMOVE ITEM FROM CART
# ======================================================

def remove_from_cart(
    db: Session,
    user_id: int,
    product_id: int
):

    # =========================
    # CEK CART USER
    # =========================
    cart = get_cart_by_user(
        db,
        user_id
    )

    if not cart:
        return None

    # =========================
    # CEK ITEM DI CART
    # =========================
    cart_item = db.query(
        models.OrderProducts
    ).filter(
        models.OrderProducts.order_id == cart.id,
        models.OrderProducts.product_id == product_id
    ).first()

    if not cart_item:
        return None

    # =========================
    # HAPUS ITEM
    # =========================
    db.delete(cart_item)
    db.commit()

    # =========================
    # HITUNG ULANG TOTAL
    # =========================
    items = db.query(
        models.OrderProducts
    ).filter(
        models.OrderProducts.order_id == cart.id
    ).all()

    total_harga = sum(
        item.harga for item in items
    )

    cart.total_harga = total_harga

    db.commit()
    db.refresh(cart)

    return cart

# ======================================================
# UPDATE CART ITEM QUANTITY
# ======================================================

def update_cart_item_quantity(
    db: Session,
    user_id: int,
    product_id: int,
    quantity: int
):

    # =========================
    # VALIDASI QUANTITY
    # =========================
    if quantity <= 0:
        return "invalid_quantity"

    # =========================
    # CEK CART USER
    # =========================
    cart = get_cart_by_user(
        db,
        user_id
    )

    if not cart:
        return None

    # =========================
    # CEK PRODUK
    # =========================
    product = get_product(
        db,
        product_id
    )

    if not product:
        return None

    # =========================
    # CEK STOK
    # =========================
    if product.stok < quantity:
        return "stok_habis"

    # =========================
    # CEK ITEM DI CART
    # =========================
    cart_item = db.query(
        models.OrderProducts
    ).filter(
        models.OrderProducts.order_id == cart.id,
        models.OrderProducts.product_id == product_id
    ).first()

    if not cart_item:
        return None

    # =========================
    # UPDATE QUANTITY
    # =========================
    cart_item.quantity = quantity

    cart_item.harga = (
        quantity * product.harga
    )

    db.commit()

    # =========================
    # HITUNG ULANG TOTAL CART
    # =========================
    items = db.query(
        models.OrderProducts
    ).filter(
        models.OrderProducts.order_id == cart.id
    ).all()

    total_harga = sum(
        item.harga for item in items
    )

    cart.total_harga = total_harga

    db.commit()
    db.refresh(cart)

    return cart

def checkout_cart(
    db: Session,
    user_id: int
):

    cart = get_cart_by_user(
        db,
        user_id
    )

    if not cart:
        return None

    # =====================================
    # AMBIL SEMUA ITEM DALAM CART
    # =====================================
    cart_items = db.query(
        models.OrderProducts
    ).filter(
        models.OrderProducts.order_id == cart.id
    ).all()

    # =====================================
    # VALIDASI STOK
    # =====================================
    for item in cart_items:

        product = db.query(
            models.Products
        ).filter(
            models.Products.id == item.product_id
        ).first()

        if not product:
            return "produk_tidak_ditemukan"

        if product.stok < item.quantity:
            return "stok_tidak_cukup"

    # =====================================
    # KURANGI STOK
    # =====================================
    for item in cart_items:

        product = db.query(
            models.Products
        ).filter(
            models.Products.id == item.product_id
        ).first()

        product.stok -= item.quantity

    # =====================================
    # UPDATE STATUS ORDER
    # =====================================
    cart.status = models.StatusOrder.paid

    db.commit()
    db.refresh(cart)

    return cart