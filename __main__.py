#!/bin/python3

# SRT time fixer github:@netharuM/srt-subtitle-time-fix

from srt import srt_time
from srt import srt_data
import argparse


def main(args):
    srt_file_name = args.file
    srt_file_obj = srt_data()
    srt_file = open(srt_file_name, "r")
    srt_file_obj.parse_from_str(srt_file.read())
    srt_file.close()

    extra_time = srt_time()
    extra_time.from_str(args.time)

    if not args.negative:
        for s in srt_file_obj.sequences:
            s.sub_beginning_time += extra_time
            s.sub_ending_time += extra_time
    else:
        for s in srt_file_obj.sequences:
            s.sub_beginning_time -= extra_time
            s.sub_ending_time -= extra_time

    final_file = open(args.out, "w")
    final_file.write(srt_file_obj.to_str_file())
    final_file.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='srt-stf')
    parser.add_argument(
        '--negative', '-n', help='Subtracts the time from the subtitle file making the subtitles appear sooner', action='store_true')
    parser.add_argument('--file', '-f', type=str,
                        help="path to the current subtitle.srt file")
    parser.add_argument('--out', '-o', type=str, help='output file name')
    parser.add_argument(
        '--time', '-t', type=str, help='Time to be changed in the format of HH:MM:SS,mmm mmm=Milliseconds HH=hours MM=minutes SS=seconds')

    args = parser.parse_args()
    if (args.file == None or args.out == None or args.time == None):
        print(
            'Insufficient arguments use --help to see args\n"-f,-o and -t" arguments are required')
        exit(1)
    main(args)
