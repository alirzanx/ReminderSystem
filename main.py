from id_generator import IDGenerator
from reminders import SimpleReminder, MeetingReminder, DailyRoutineReminder
from manager import ReminderManager

if __name__ == "__main__":
    gen = IDGenerator()
    manager = ReminderManager()

    r1 = SimpleReminder("Buy bread", "18:30", gen.next_id())
    r2 = MeetingReminder("Team meeting", "14:00", gen.next_id(), ["Ali", "Sara"])
    r3 = DailyRoutineReminder("Workout", "07:00", gen.next_id(), True)

    manager.add_reminder(r1)
    manager.add_reminder(r2)
    manager.add_reminder(r3)

    print("Reminders list:", manager.list_reminders())

    manager.execute_all()

    found = manager.find_by_id(2)
    if found:
        print("Found reminder:", found.remind())

    manager.remove_reminder(1)
