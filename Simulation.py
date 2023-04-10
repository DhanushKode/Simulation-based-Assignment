import os

class File:
    def init(self, name, size):
        self.name = name
        self.size = size

class FileSystem:
    def init(self, total_space):
        self.total_space = total_space
        self.files = []

    def add_file(self, file):
        if self.get_free_space() < file.size:
            print("Error: Not enough free space to add file")
            return False
        self.files.append(file)
        print(f"File {file.name} ({file.size} KB) added successfully")
        return True

    def delete_file(self, name):
        for file in self.files:
            if file.name == name:
                self.files.remove(file)
                print(f"File {name} deleted successfully")
                return True
        print(f"Error: File {name} not found")
        return False

    def rename_file(self, old_name, new_name):
        for file in self.files:
            if file.name == old_name:
                file.name = new_name
                print(f"File {old_name} renamed to {new_name}")
                return True
        print(f"Error: File {old_name} not found")
        return False

    def move_file(self, name, new_location):
        for file in self.files:
            if file.name == name:
                if self.get_free_space() < file.size:
                    print("Error: Not enough free space to move file")
                    return False
                self.files.remove(file)
                self.add_file(File(new_location + file.name, file.size))
                print(f"File {name} moved to {new_location}")
                return True
        print(f"Error: File {name} not found")
        return False

    def get_free_space(self):
        used_space = sum([file.size for file in self.files])
        return self.total_space - used_space

    def print_files(self):
        print("Files in the file system:")
        for file in self.files:
            print(f"- {file.name} ({file.size} KB)")

while True:
    print('Select an option:')
    print('1. Create a new file')
    print('2. Delete an existing file')
    print('3. Rename an existing file')
    print('4. Move an existing file to a new location')
    print('5. Display the files in the file system')
    print('6. Exit')
    choice = input('Enter your choice: ')
    if choice == '1':
        name = input('Enter the name of the file: ')
        size = int(input('Enter the size of the file in bytes: '))
        if create_file(name, size):
            print('File created successfully')
        else:
            print('Not enough space in the file system to create the file')
    elif choice == '2':
        name = input('Enter the name of the file to delete: ')
        if delete_file(name):
            print('File deleted successfully')
        else:
            print('File not found')
    elif choice == '3':
        old_name = input('Enter the name of the file to rename: ')
        new_name = input('Enter the new name for the file: ')
        if rename_file(old_name, new_name):
            print('File renamed successfully')
        else:
            print('File not found')
    elif choice == '4':
        name = input('Enter the name of the file to move: ')
        new_location = input('Enter the new location for the file: ')
        if move_file(name, new_location):
            print('File moved successfully')
        else:
            print('File not found')
    elif choice == '5':
        print('Files in the file system:')
        display_files()
    elif choice == '6':
        break
    else:
        print('Invalid choice')
