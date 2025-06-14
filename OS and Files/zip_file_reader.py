#!usr/bin/env/python3
import zipfile

def zip_read(filename):
    with zipfile.ZipFile(filename) as my_zip:
        for zipdetails in my_zip.infolist():
            yield zipdetails.filename

for filename in zip_read("music.zip"):
    print(filename)
