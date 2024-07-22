import zipfile

with zipfile.ZipFile("zip1.zip", "w") as zfile:
    zfile.write("db1.csv")
    zfile.write("db2.csv")
    zfile.write("db3.csv")


