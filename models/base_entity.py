from dataclasses import dataclass

@dataclass
class BaseEntity:
    id: str = None
    api_model: str = None
    api_link: str = None
    title: str = None
