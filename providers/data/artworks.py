from dataclasses import dataclass

from providers.data.base_entity import BaseEntity

@dataclass
class Artwork(BaseEntity):
    artist_display: str = None
    place_of_origin: str = None
