# app/db/models/product.py
import uuid
from datetime import datetime

from sqlalchemy import Boolean, DateTime, Numeric, String, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class Product(Base):
    __tablename__ = "products"

    # প্রাইমারি কি (UUID)
    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    # প্রোডাক্টের নাম (টাইটেল)
    title: Mapped[str] = mapped_column(
        String(200),
        index=True,
        nullable=False,
    )

    # প্রোডাক্টের বিবরণ
    description: Mapped[str | None] = mapped_column(
        String(1000),
        nullable=True,
    )

    # দাম (দশমিক সংখ্যা সাপোর্ট করার জন্য Numeric)
    price: Mapped[float] = mapped_column(
        Numeric(10, 2),
        nullable=False,
    )

    # প্রোডাক্ট কি বিক্রির জন্য প্রস্তুত?
    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )

    # 🔥 মাইক্রোসার্ভিস কনসেপ্ট: কোন ইউজার এই প্রোডাক্ট অ্যাড করেছে তার ID
    created_by: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        nullable=False,
    )

    # তৈরি ও আপডেটের সময়
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )