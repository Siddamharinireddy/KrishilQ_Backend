from sqlalchemy import Column, String, Float, ForeignKey, DateTime, Enum, Date, JSON
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import uuid
import enum
from app.database import Base
from pydantic import BaseModel
from typing import Optional
from uuid import UUID



class CropStatus(str, enum.Enum):
    PLANNED = "planned"
    SOWING = "sowing"
    GROWING = "growing"
    HARVESTING = "harvesting"
    COMPLETED = "completed"


class Season(str, enum.Enum):
    KHARIF = "kharif"
    RABI = "rabi"
    ZAID = "zaid"

class CropCreate(BaseModel):
    farm_id: UUID
    crop_name: str           # Must match frontend key 'crop_name'
    season: Season           # Validates the enum string structure values
    area_acres: float        # Required numeric field validation
    crop_variety: Optional[str] = None
    actual_yield_kg: Optional[float] = None
    status: Optional[CropStatus] = CropStatus.PLANNED

class CropRecord(Base):
    __tablename__ = "crop_records"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    farm_id = Column(String(36), ForeignKey("farms.id"), nullable=False, index=True)
    crop_name = Column(String(100), nullable=False)
    crop_variety = Column(String(100), nullable=True)
    season = Column(Enum(Season), nullable=False)
    status = Column(Enum(CropStatus), default=CropStatus.PLANNED)
    sowing_date = Column(Date, nullable=True)
    expected_harvest_date = Column(Date, nullable=True)
    actual_harvest_date = Column(Date, nullable=True)
    area_acres = Column(Float, nullable=False)
    expected_yield_kg = Column(Float, nullable=True)
    actual_yield_kg = Column(Float, nullable=True)
    irrigation_schedule = Column(JSON, default={})
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    farm = relationship("Farm", back_populates="crop_records")
    advisories = relationship("Advisory", back_populates="crop_record")
