# manager.py
import logging
from logging.handlers import RotatingFileHandler  

class ReminderManager:
    def __init__(self):
        self.reminders = []

        self.logger = logging.getLogger("ReminderManager")
        self.logger.setLevel(logging.INFO)

        handler = RotatingFileHandler(
            "reminder.log", maxBytes=100 * 1024, backupCount=3, encoding="utf-8"
        )

        formatter = logging.Formatter("%(levelname)s - %(message)s")
        handler.setFormatter(formatter)

        if not self.logger.handlers:
            self.logger.addHandler(handler)

    def add_reminder(self, reminder):
        if not reminder.title or not reminder.time:
            self.logger.error("Reminder has empty title or time")
            return
        self.reminders.append(reminder)
        self.logger.info(f"Added reminder {reminder.title} (ID={reminder.reminder_id})")

    def remove_reminder(self, reminder_id):
        before = len(self.reminders)
        self.reminders = [r for r in self.reminders if r.reminder_id != reminder_id]
        after = len(self.reminders)
        level = logging.WARNING if before != after else logging.ERROR
        self.logger.log(level, f"Removed reminder ID={reminder_id}")

    def list_reminders(self):
        return [f"{r.reminder_id}: {r.title} at {r.time}" for r in self.reminders]

    def execute_all(self):
        for r in self.reminders:
            try:
                msg = r.remind()
                print(msg)
                self.logger.info(f"Executed reminder ID={r.reminder_id}: {msg}")
            except Exception as e:
                self.logger.error(f"Failed to execute reminder ID={r.reminder_id}: {e}")

    def find_by_id(self, reminder_id):
        for r in self.reminders:
            if r.reminder_id == reminder_id:
                return r
        return None
