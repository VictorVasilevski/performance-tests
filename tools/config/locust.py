from pydantic import BaseModel


class LocustUserConfig(BaseModel):
    wait_time_min: float = 1.0
    wait_time_max: float = 3.0
