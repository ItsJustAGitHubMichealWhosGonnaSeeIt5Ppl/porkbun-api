from dataclasses import dataclass

@dataclass
class Ping:
    acccount: str
    status: str
    yourIp: str
    xForwardedFor: str
    credentialsValid: bool
    requestId: str
    
    @classmethod
    def from_json(cls, mapping: dict[str]):
        return Ping(**mapping)
    
