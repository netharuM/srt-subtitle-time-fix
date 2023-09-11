# SRT time fixer github:@netharuM/srt-subtitle-time-fix
# /srt.py --> SRT file datatype handlers

class srt_time:
    MILLISECONDS_PER_HOUR = 3600000
    MILLISECONDS_PER_MINUTE = 60000
    MILLISECONDS_PER_SECOND = 1000

    def __init__(self) -> None:
        self.inMilliseconds = 0

    def __add__(self, y):
        new_time = srt_time()
        new_time.inMilliseconds = self.inMilliseconds + y.inMilliseconds
        return new_time

    def __sub__(self, y):
        new_time = srt_time()
        new_time.inMilliseconds = self.inMilliseconds - y.inMilliseconds
        return new_time

    def from_str(self, sequence_time_str):
        t_split = sequence_time_str.split(',')
        time_arr = t_split[0].split(':')
        hours = int(time_arr[0])
        minutes = int(time_arr[1])
        seconds = int(time_arr[2])
        milliseconds = int(t_split[1])
        self.setFromDiffFormats(hours, minutes, seconds, milliseconds)

    def setFromDiffFormats(self, hours: int, minutes: int, seconds: int, milliseconds: int) -> int:
        inMillis = milliseconds
        inMillis += seconds * self.MILLISECONDS_PER_SECOND
        inMillis += minutes * self.MILLISECONDS_PER_MINUTE
        inMillis += hours * self.MILLISECONDS_PER_HOUR
        self.inMilliseconds = inMillis
        return inMillis

    def getHrsMinsSecsMils(self):
        inMillis = self.inMilliseconds
        milliseconds = inMillis % self.MILLISECONDS_PER_SECOND
        inMillis -= milliseconds
        seconds = (inMillis % self.MILLISECONDS_PER_MINUTE) / \
            self.MILLISECONDS_PER_SECOND
        inMillis -= seconds * self.MILLISECONDS_PER_SECOND
        minutes = (inMillis % self.MILLISECONDS_PER_HOUR) / \
            self.MILLISECONDS_PER_MINUTE
        inMillis -= minutes * self.MILLISECONDS_PER_MINUTE
        hours = inMillis / self.MILLISECONDS_PER_HOUR
        # wrapped in ints because the dividing always results in a float in python
        return (int(hours), int(minutes), int(seconds), milliseconds)

    def to_str(self):
        (hours, minutes, seconds, milliseconds) = self.getHrsMinsSecsMils()
        hours_str = str(hours).zfill(2)
        minutes_str = str(minutes).zfill(2)
        seconds_str = str(seconds).zfill(2)
        milliseconds_str = str(milliseconds).zfill(3)
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


class srt_data:
    def __init__(self):
        self.sequences = None

    def parse_from_str(self, srt_file_content: str):
        sequence_arr = srt_file_content.split('\n\n')
        sequence_arr = [x for x in sequence_arr if x != '']

        def sequence_str_to_map(str):
            sequence = srt_sequence()
            sequence.from_str(str)
            return sequence

        self.sequences = list(map(sequence_str_to_map, sequence_arr))

    def to_str_file(self) -> str:
        sequences_str = list(
            map(lambda sequence: sequence.to_str(), self.sequences))
        return "\n\n".join(sequences_str)
