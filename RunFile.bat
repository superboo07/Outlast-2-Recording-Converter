@echo off

rmdir /s /q .\export\
mkdir .\export\
python Recording-Ripper.py
ffmpeg -r 30 -f image2 -s 1280x720 -start_number 1 -i ./export/%%d.jpg -vframes 1000 -vcodec libx264 -crf 25  -pix_fmt yuv420p export.mp4
pause