import json
from dataclasses import dataclass

@dataclass
class FirewallRule:
    """
    Rules for firewall filtering
    """
    id: int
    type: str
    value: str
    reason: str
    active: bool
    priority: int

    def to_dict(self):
        return {
            "id": self.id,
            "type": self.type,
            "value": self.value,
            "reason": self.reason,
            "active": self.active,
            "priority": self.priority,
        }

    def to_json(self):
        return json.dumps(self.to_dict())

    @classmethod
    def from_dict(cls, data: dict):
        return cls(**data)


    @dataclass
    class FirewallRequest:
        ip: str
        port: int
        protocol: str
        path: str
        method: str













