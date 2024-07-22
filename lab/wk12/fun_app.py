"""
This will be a very, very limited document viewer & document compressor & document extractor

1) document viewer
Ask the user for a document that they would like to view
    E.G: hi.txt
         boo.bin
         foo.jpg
         bar.png
         f1.csv

Python will open this file (if it's found)

2)document compressor
The user will put a file extension & name, the program will gather all files with extension, compress those files to fileName.zip

3)document extractor
Display all .zip files
ask user which .zip file to extract
ask user to enter new location to extract zipped file.

"""
import os
import sys
from PIL import Image
import zipfile
from rich.console import Console
from rich.table import Table


supported_extensions = "bin csv txt png jpg".split(" ")
root_path = "data/"
def validate_extension(extension: str)->None:
    """
    Determines if the extension is part of our list of supported extensions. Exists program if not
    :param extension: targe extension
    """

    if "." in extension:
        extension = extension.split(".")[1]


    if extension not in supported_extensions:
        print("Sorry but", extension, "is not currently supported", file=sys.stderr)
        sys.exit("Exiting with Error!")


def get_all_docs():
    return os.listdir(root_path)
def document_viewer()->None:
    docs_found = get_all_docs()
    print("Here are the list of files\n")
    print("\n".join(docs_found))

    file_name = input("Enter one of the file names from above: ")

    if file_name in docs_found:
        get_extension = file_name.split(".")[1]
        validate_extension(get_extension)
        match get_extension:
            case "bin":
                content = open(root_path + file_name, "rb").read().decode()
                print(content)
            case "txt":
                content = open(root_path + file_name).read()
                print(content)
            case "jpg":
                Image.open(root_path + file_name).show()
            case "png":
                Image.open(root_path + file_name).show()
            case "csv":
                f = open(root_path + file_name)
                first_line = f.readline()

                headers = first_line.split(",")  # headers of .csv file

                console = Console()
                table = Table()
                for each_header_column in headers:
                    table.add_column(each_header_column)

                for lines in f.readlines():  # list line1,line2,line3
                    table.add_row(*lines.split(","))


                console.print(table)
    else:
        print(file_name, "was not found in our program", file=sys.stderr)

def document_compressor()->None:
    get_extension = input("Enter an extension that you'd like to compress")
    file_name = input("Enter the name of the zipped file")
    if not file_name.endswith(".zip"):
        file_name += ".zip"
    validate_extension(get_extension)
    docs_found = get_all_docs()
    hits = [x for x in docs_found if x.endswith(get_extension)]
    with zipfile.ZipFile(root_path + file_name, "w") as zf:
        for file in hits:
            zf.write(root_path + file)
    print("Mission complete!")


def document_extractor()->None:
    docs_found = get_all_docs()
    zip_files = [x for x in docs_found if x.endswith(".zip")]
    print("Here are all the zip files\n")
    print("\n".join(zip_files))
    answer = input("Enter a .zip file name")
    if not answer.endswith(".zip"):
        answer += ".zip"
    if answer not in zip_files:
        sys.exit("Desired .zip file not found!")
    new_location = input("Enter a new path location for " + answer)

    with zipfile.ZipFile(root_path + answer, "r") as zf:
        zf.extractall(root_path + new_location)


def launcher(choice: int)-> None:

    match choice:
        case 1:
            document_viewer()
        case 2:
            document_compressor()
        case 3:
            document_extractor()
        case _:
            print("Invalid Choice!", file=sys.stderr)

def main():
    print("Welcome to our app")
    choice = int(input("Choose from one of the following\n\n1)document viewer\n2)document compressor\n3)document extractor\n\nEnter Choice: "))
    launcher(choice)


if __name__ == '__main__':
    main()

