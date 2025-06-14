import zipfile

def see_zipfile(filer):
    with zipfile.ZipFile(filer) as zippy:
        for files in zippy.infolist():
            yield files
for names in see_zipfile("music.zip"):
    print(names)