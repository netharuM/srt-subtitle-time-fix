#!/bin/python3

# SRT time fixer github:@netharuM/srt-subtitle-time-fix
from srt import srt_time
from srt import srt_data
import argparse


def main(args):
    srt_file_name = args.file
    encoding = args.encoding

    extra_time = srt_time()
    extra_time.from_str(args.time)

    srt_file_obj = srt_data()
    with open(srt_file_name, 'rb') as srt_file:
        try:
            srt_file_obj.parse_from_str(srt_file.read().decode(encoding))
        except UnicodeDecodeError:
            print(f"Error: The encoding ('{encoding}') cannot decode the file")
            print(
                'Please provide the --encoding/-e argument with the encoding that the file is using')
            print('  Ex:')
            print(
                f'     srt-stf -f {srt_file_name} -t {args.time} -o {args.out} -e [encoding the file is using]')
            print(
                f'     srt-stf -f {srt_file_name} -t {args.time} -o {args.out} -e latin-1')
            print(
                f'     srt-stf -f {srt_file_name} -t {args.time} -o {args.out} -e utf-8')
            exit(1)

    if not args.negative:
        for s in srt_file_obj.sequences:
            s.sub_beginning_time += extra_time
            s.sub_ending_time += extra_time
    else:
        for s in srt_file_obj.sequences:
            s.sub_beginning_time -= extra_time
            s.sub_ending_time -= extra_time

    with open(args.out, "wb") as final_file:
        final_file.write(srt_file_obj.to_str_file().encode(encoding))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='srt-stf')
    parser.add_argument(
        '--negative', '-n', help='Subtracts the time from the subtitle file making the subtitles appear sooner', action='store_true')
    parser.add_argument('--encoding', '-e', type=str,
                        help="The preferred encoding for the file (default is utf-8, which may not work with some files)",
                        default='utf-8')
    parser.add_argument('--file', '-f', type=str,
                        help="path to the current subtitle.srt file",
                        required=True)
    parser.add_argument('--out', '-o', type=str, help='output file name',
                        required=True)
    parser.add_argument(
        '--time', '-t', type=str, help='Time to be changed in the format of HH:MM:SS,mmm mmm=Milliseconds HH=hours MM=minutes SS=seconds',
        required=True)

    args = parser.parse_args()
    main(args)
