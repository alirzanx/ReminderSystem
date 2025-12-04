from dataclasses import dataclass

@dataclass
class Reminder:
    title: str
    time: str
    reminder_id: int

    def remind(self):
        raise NotImplementedError("Subclasses must implement remind()")
