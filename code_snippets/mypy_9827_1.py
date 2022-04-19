from typing import Dict, Literal, Optional, TypedDict

class HardwareMetadata(TypedDict):
    status: Literal["healthy", "degraded", "offline", "unavailable"]
    status_info: Optional[str]
    metadata: Dict[str, str]
