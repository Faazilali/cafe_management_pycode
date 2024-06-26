import os

def create(filename):
    try:
        with open(filename, 'x') as f:
            print(f"Your file {filename} is created successfully.")

    except FileExistsError:
        print(f"File with name {filename} already exist.")

def viewFile():
    files = os.listdir()
    if not files:
        print("No file found.")
    else:
        print("Files in directory:")
        for file in files:
            print(file)

def remove(filename):
    try:
        os.remove(filename)
        print("Your file is deleted sucessfully.")
    except FileNotFoundError:
        print(f"{filename} is not found.")

def read(filename):
    try:
        with open('sample.txt', 'r') as f:
            content = f.read()
            print(f"Content of file {filename}: \n{content} ")
    except FileNotFoundError:
        print("File not found.")

def edit(filename):
    try:
        with open('sample.txt', 'a') as f:
            content = input("Enter data to be added in file:")
            f.write(content)
            print(f"Content in {filename} added successfully.")
    except FileNotFoundError:
        print(f"{filename} is not found.")

def main():
    while True:
        print("File Management App")
        print("1. Create your file")
        print("2. View files")
        print("3. Delete file")
        print("4. Read file")
        print("5. Edit file")
        print("6. Exit")
        print("\n")

        choice = input("Enter your choice:")
        if choice == "1":
            filename = input("Enter your file name: ")
            create(filename)
            print("\n")

        elif choice == "2":
            viewFile()
            print("\n")
        
        elif choice == "3":
            filename = input("Enter the file to delete: ")
            remove(filename)
            print("\n")

        elif choice == "4":
            filename = input("Enter the file you want to read: ")
            read(filename)
            print("\n")

        elif choice == "5":
            filename = input("Enter the file you want to edit: ")
            edit(filename)
            print("\n")
        
        elif choice == "6":
            print("Closing the app....")
            print("\n")
        
        else:
            print("Enter the number between 1-6.")
            print("\n")

main()

