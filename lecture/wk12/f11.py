import zipfile

with zipfile.ZipFile("zip1.zip", "r") as zfile:
    print(zfile.namelist())
    print(zfile.infolist())
    for info in zfile.infolist():
        print(info.filename)
        print(info.file_size)
        print(info.compress_size)
        print(info.extract_version)
