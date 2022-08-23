from dataclasses import dataclass

from models.base_entity import BaseEntity

@dataclass
class Place(BaseEntity):
    type: str = None
    tgn_id: str = None
