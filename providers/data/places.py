from dataclasses import dataclass

from providers.data.base_entity import BaseEntity

@dataclass
class Place(BaseEntity):
    type: str = None
    tgn_id: str = None
