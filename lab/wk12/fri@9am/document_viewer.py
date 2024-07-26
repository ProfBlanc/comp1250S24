import os
from PIL import Image
from rich.console import Console
from rich.table import Table

app_root_dir = "docs/"
docs_listing = ""


def init():
    global docs_listing
    if not os.path.exists(app_root_dir):
        os.mkdir(app_root_dir)

    docs_listing = os.listdir(app_root_dir)


def display_doc(choice: str)->None:
    extension = choice.split(".")[-1]
    match extension:
        case "txt":
            print(open(app_root_dir + choice).read())
        case "bin":
            print(open(app_root_dir + choice).read())
        case "csv":
            content = open(app_root_dir + choice).readlines()
            console = Console()
            table = Table()
            for column in content[0].strip().split(","):
                table.add_column(column)

            print(content, content[1], content[1].split(","), "IND" , *content[1].split(","))
            for line in content[1:]:
                data = line.strip().split(",")
                row = data[:5]
                row.append(",".join(data[5:]).replace('"', ""))
                table.add_row(*row)

            console.print(table)

        case "jpg":
            image = Image.open(app_root_dir + choice)
            image.show()



def run():
    print("Enter one of the following documents and we will display the data\n")
    print("\n".join(docs_listing))
    choice = input("Enter your choice: ")
    display_doc(choice)
def main():
    init()
    print("Welcome to our Document Viewer")
    run()

if __name__ == '__main__':
    main()
