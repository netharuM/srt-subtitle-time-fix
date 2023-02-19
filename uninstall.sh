#!/bin/bash
rm /bin/srt-stf
if [ $? -ne 0 ]; then
    
    echo "Error: Failed to uninstall."
    
    exit 1
    
fi
echo "Uninstalled!!"