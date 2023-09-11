# Fix SRT subtitle timing issues
is your subtitle timing incorrect.
hard code the time with srt-stf

## Install
- Simply clone the repository
- Install `python3`
- Installing with the Script (tested only in Linux)
    - then run the following
        ```sh
        sudo ./install.sh
        ```
    - to uninstall run 
        ```sh
        sudo ./uninstall.sh
        ```
- Or just simply symlink the `__main__.py` file to a path which is in your executable path
    - In linux
        ```bash
        ln -s "$(pwd)/__main__.py" /bin/srt-stf
        #                                   ^
        # [A path which is in the executables]
        ```
- Running (without installing) using `python` on `Windows/Mac/Linux`
    - first move into the directory you have downloaded the code to
        ```
        cd srt-subtitle-time-fix
        ```
    - Then run the following
        ```
        python . [-h] [--negative] [--encoding ENCODING] --file FILE --out OUT --time TIME
        ```
## Usage
-   ```
    usage: srt-stf [-h] [--negative] [--encoding ENCODING] --file FILE --out OUT --time TIME

    options:
    -h, --help            show this help message and exit
    --negative, -n        Subtracts the time from the subtitle file making the subtitles appear sooner
    --encoding ENCODING, -e ENCODING
                            The preferred encoding for the file (default is utf-8, which may not work with some files)
    --file FILE, -f FILE  path to the current subtitle.srt file
    --out OUT, -o OUT     output file name
    ```
- examples:
    ```
    # to delay the subtitle by 29 seconds
    $ srt-stf -f <input_file_name>.srt -t <TIME> -o <output_file_name>.srt
    $ srt-stf -f track.srt -t 00:00:29,000 -o out.srt -e utf-8
    #                HOURS-----|  |  |   | 
    #                MINUTES------|  |   | 
    #                SECONDS---------|   | 
    #                MILLISECONDS--------|

    # if you wanna play the subtitle 29 seconds sooner. Just add the '-n' flag to the command
    $ srt-stf -f track.srt -t 00:00:29,000 -o out.srt -n
    ```