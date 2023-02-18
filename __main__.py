from srt import srt_sequence
from srt import srt_time
import argparse


def main(args):
    srt_file_name = args.file
    srt_file = open(srt_file_name, "r")
    sequence_arr = srt_file.read().split('\n\n')
    srt_file.close()
    sequence_arr = [x for x in sequence_arr if x != '']

    def sequence_str_to_map(str):
        sequence = srt_sequence()
        sequence.from_str(str)
        return sequence

    sequences = list(map(sequence_str_to_map, sequence_arr))

    extra_time = srt_time()
    extra_time.from_str(args.time)

    if not args.negative:
        for s in sequences:
            s.sub_beginning_time += extra_time
            s.sub_ending_time += extra_time
    else:
        for s in sequences:
            s.sub_beginning_time -= extra_time
            s.sub_ending_time -= extra_time

    sequences_str = list(map(lambda sequence: sequence.to_str(), sequences))
    final_file_output = "\n\n".join(sequences_str)
    final_file = open(args.out, "w")
    final_file.write(final_file_output)
    final_file.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--negative', '-n', help='Subtracts the time from the subtitle file making the subtitles appear sooner', action='store_true')
    parser.add_argument('--file', '-f', type=str,
                        help="path to the current subtitle.srt file")
    parser.add_argument('--out', '-o', type=str, help='output file name')
    parser.add_argument(
        '--time', '-t', type=str, help='Time to be changed in the format of HH:MM:SS,mmm mmm=Milliseconds HH=hours MM=minutes SS=seconds')

    args = parser.parse_args()
    main(args)
