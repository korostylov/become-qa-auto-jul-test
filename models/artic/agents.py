from dataclasses import dataclass

from models.artic.base_entity import BaseEntity

@dataclass
class Agent(BaseEntity):
    agent_type_title: str = None
    agent_type_id: str = None
