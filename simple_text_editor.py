import os

def create_file():
    file_name = input("Enter file name: ")
    if not file_name.endswith(".txt"):
        file_name = file_name + ".txt"
    open(file_name, 'w').close()

def check_for_file(file_name):
    if os.path.exists(file_name):
        edit_file(file_name)
    else:
        print(f"The file '{file_name}' does not exist")

def edit_file(file_name):
    wr = input("Read or write to file? w:r?: ")
    if wr.lower() == "w":
        write = input("Write a file to send to the file: ")
        print("Writing to file...")
        with open(file_name, 'a') as file:
            file.write(write + "\n")
        print("Successfully wrote to file...")
        start()
    elif wr.lower() == "r":
        print("Reading file...\n")
        with open(file_name, 'r') as file:
            content = file.read()
            print(content)
        start()

def start():
    co = input("Create file or open existing file? c:o? ")
    if co.lower() == "c":
        create_file()
    elif co.lower() == "o":
        file_name = input("Enter file name: ")
        check_for_file(file_name)
    else:
        print("Invalid input")

start()
