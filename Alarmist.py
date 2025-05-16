# The Alarmist class name is a hilarious joke that makes everyone laugh.
# Aside from the hilarious joke, the class is responsible for managing alarms, setting them and checking if new alarms are allowed.
# Minutes past midnight is easier to use for checking overlaps than handling hours and minutes separately.
class Alarmist:
    def __init__(self):
        self.alarms = [660, 630]  # minutes past midnight (these examples are 11:00am and 10:30am)

    # Add a new alarm if it is not within 15 minutes of any existing alarm
    def addAlarm(self, minutes_past_midnight):
        if self.doesOverlapAnyAlarm(minutes_past_midnight):
            print("overlap detected. will not set alarm for {minutes_past_midnight}.")
        else:
            print("adding alarm for {minutes_past_midnight}")
            self.alarms.append(minutes_past_midnight)

    def doesOverlapAnyAlarm(self, newAlarm_minutes_past_midnight):
        # Avoid adding a new alarm within 15 minutes of any existing alarm
        # We have an unsorted array of existing alarm times, so we have to check all of them
       minimum_separation = 15
        for alarm in self.alarms:
            difference = abs(alarm - newAlarm_minutes_past_midnight)
            if difference < minimum_separation:
                return True
        return False

