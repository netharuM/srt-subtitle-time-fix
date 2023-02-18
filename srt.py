class srt_time:
    def __init__(self):
        self.hours = 0
        self.milliseconds = 0
        self.minutes = 0
        self.seconds = 0

    def __add__(self, y):
        new_time = srt_time()
        new_time.minutes = self.minutes + y.minutes
        new_time.hours = self.hours + y.hours
        new_time.seconds = self.seconds + y.seconds
        new_time.milliseconds = self.milliseconds + y.milliseconds
        return new_time

    def __sub__(self, y):
        new_time = srt_time()
        new_time.minutes = self.minutes - y.minutes
        new_time.hours = self.hours - y.hours
        new_time.seconds = self.seconds - y.seconds
        new_time.milliseconds = self.milliseconds - y.milliseconds
        return new_time

    def from_str(self, sequence_time_str):
        t_split = sequence_time_str.split(',')
        time_arr = t_split[0].split(':')
        self.milliseconds = int(t_split[1])
        self.hours = int(time_arr[0])
        self.minutes = int(time_arr[1])
        self.seconds = int(time_arr[2])

    def to_str(self):
        hours_str = str(self.hours).zfill(2)
        minutes_str = str(self.minutes).zfill(2)
        seconds_str = str(self.seconds).zfill(2)
        milliseconds_str = str(self.milliseconds).zfill(3)
        time_str = "{}:{}:{},{}".format(
            hours_str, minutes_str, seconds_str, milliseconds_str)
        return time_str


class srt_sequence:
    def __init__(self):
        self.sequence_number = None
        self.sub_beginning_time = srt_time()
        self.sub_ending_time = srt_time()
        self.subtitle_arr = []

    def from_str(self, sequence):
        sub_item_arr = sequence.split('\n')
        self.sequence_number = sub_item_arr[0]
        sub_time = sub_item_arr[1].split(' --> ')
        beginning_time_str = sub_time[0]
        self.sub_beginning_time.from_str(beginning_time_str)
        ending_time_str = sub_time[1]
        self.sub_ending_time.from_str(ending_time_str)
        self.subtitle_arr = sub_item_arr[2:]

    def to_str(self):
        sub_lines = "\n".join(self.subtitle_arr)
        sequence_number_str = str(self.sequence_number)
        beginning_time_str = self.sub_beginning_time.to_str()
        ending_time_str = self.sub_ending_time.to_str()
        sub_sequence = "{}\n{}  -->  {}\n{}".format(
            sequence_number_str, beginning_time_str, ending_time_str, sub_lines)
        return sub_sequence
