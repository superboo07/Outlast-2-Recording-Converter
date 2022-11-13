# Outlast 2 recording file exporter
# Doesn't support audio

recording = open(input("file name / path: "), "rb") # Open OL2 file (doesn't work on precompiled ones, only ones the game has made for some reason)
export = recording.read().split(b'\xff\xd8\xff\xe0') # Split by every jpeg header
x = 1
for i in export:
    if x > 1:
        with open("./export/" + str(x - 1) + ".jpg", 'wb') as f:
            f.write(b'\xff\xd8\xff\xe0' + i) # Readd jpeg header and write to frame
    x = x + 1
