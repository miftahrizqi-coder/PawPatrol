# crud.py

from sqlalchemy.orm import Session
from typing import Optional

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


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.Users(
        nama=user.nama,
        email=user.email,
        password_hash=user.password,   # nanti diganti bcrypt
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