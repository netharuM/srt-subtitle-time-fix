#!/bin/bash

echo "Installing srt-subtitle-time-fix (cmd: srt-stf)..."
echo ""
ln -s "$(pwd)/__main__.py" /bin/srt-stf
if [ $? -ne 0 ]; then
    
    echo "Error: Failed to install."
    
    exit 1
    
fi
echo "Symlinked __main__.py to /bin/srt-stf"
echo "__main__.py --> /bin/srt-stf"
echo ""
echo "use command srt-stf to run the program"
echo "Please do not delete this folder!!"
echo "use './unstall.sh' command to uninstall the program"