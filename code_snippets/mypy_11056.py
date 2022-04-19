from dataclasses import dataclass


class Event:
    def __init_subclass__(cls):
        dataclass(cls)


class BaseEvent(Event):
    base_field: str


class SubEvent(BaseEvent):
    sub_field: str
    
    
SubEvent("base", "sub")
