from dataclasses import dataclass
from reminder_base import Reminder

@dataclass
class SimpleReminder(Reminder):
    def remind(self):
        return f"{self.title} : It is time"


@dataclass
class MeetingReminder(Reminder):
    participants: list

    def remind(self):
        return f"{self.title} - Participants: {', '.join(self.participants)} : Meeting Reminder"


@dataclass
class DailyRoutineReminder(Reminder):
    repeat_daily: bool

    def remind(self):
        status = "active" if self.repeat_daily else "inactive"
        return f"{self.title} (daily repeat {status}) : Daily Routine"
