import os, sys
from pydub import AudioSegment

if(len(sys.argv) != 3):
    print(f"{sys.argv[0]} <audio file> <format>")
    sys.exit(1)

filename = sys.argv[1]
frm = sys.argv[2]
filepath = os.path.abspath(filename)
filebase = os.path.basename(filename)
if not(filename.endswith(str("." + frm))):
    track = AudioSegment.from_file(filename, filename[-3:])
    newname = filebase.replace(filebase[-3:], frm)
    track.export(newname, format=frm)
    print(f"{filebase} converted to {newname}")
