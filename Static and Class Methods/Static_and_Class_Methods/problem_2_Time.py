class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        current_hour = f"0{self.hours}" if int(self.hours) < 10 and self.hours != "00" else self.hours
        current_minute = f"0{self.minutes}" if int(self.minutes) < 10 and self.minutes != "00" else self.minutes
        current_second = f"0{self.seconds}" if int(self.seconds) < 10 and self.seconds != "00" else self.seconds
        return f"{current_hour}:{current_minute}:{current_second}"

    def next_second(self):
        self.hours = self.check_hour()
        self.minutes = self.check_minute()
        self.seconds = self.check_second()
        return self.get_time()

    def check_second(self):
        current_second = "00" if int(self.seconds) == Time.max_seconds else int(self.seconds) + 1
        return current_second

    def check_minute(self):
        current_minute = self.minutes
        if self.seconds == Time.max_seconds and self.minutes == Time.max_minutes:
            current_minute = "00"
        else:
            if self.seconds == Time.max_seconds:
                current_minute += 1
        return current_minute

    def check_hour(self):
        current_hour = self.hours
        if self.minutes == Time.max_minutes and self.seconds == Time.max_seconds:
            if self.hours == Time.max_hours:
                current_hour = "00"
            else:
                current_hour += 1

        return current_hour


t = Time(2, 58, 59)
print(t.get_time())
print(t.next_second())
