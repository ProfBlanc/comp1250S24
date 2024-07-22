import zipfile

with zipfile.ZipFile("zip1.zip", "r") as zfile:
    #zfile.extractall("unzipped")  # put where you want to extract all
    zfile.extract("db1.csv", "extracted")