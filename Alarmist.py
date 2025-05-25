class Alarmist:
    def __init__(self):
        self.alarms = [660, 630]  # minutes past midnight

    def checkAlarms(self, currentTime):
        currentMinutesPastMidnight = currentTime[3] * 60 + currentTime[4]
        print(f"Current minutes: {currentMinutesPastMidnight}")  # Debug print

        for alarm in self.alarms:
            print(alarm)
            if currentMinutesPastMidnight == alarm:
                print('Alarm triggered!')
                return True  # Immediately return if any alarm matches
        # Only return False after checking ALL alarms
        return False



    def addAlarm(self, minutes_past_midnight):
        if self.doesOverlapAnyAlarm(minutes_past_midnight):
            print(f"overlap detected. will not set alarm for {minutes_past_midnight}.")  # Added f-string
            return False
        else:
            print(f"adding alarm for {minutes_past_midnight}")  # Added f-string
            self.alarms.append(minutes_past_midnight)
            return True

    def doesOverlapAnyAlarm(self, newAlarm_minutes_past_midnight):
        minimum_separation = 15
        for alarm in self.alarms:
            difference = abs(alarm - newAlarm_minutes_past_midnight)
            if difference < minimum_separation:
                return True
        return False
