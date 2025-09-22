import os
import time

class LazyTree:
    def __init__(self, root_path):
        if not os.path.isdir(root_path):
            raise ValueError(f"{root_path} is not a valid directory")
        self.root_path = os.path.abspath(root_path)

    def list_dir(self, path):
        try:
            items = os.listdir(path)
            items.sort()
            return items
        except PermissionError:
            return ["<Permission Denied>"]
        except FileNotFoundError:
            return ["<Not Found>"]

    def display_level(self, path, prefix=""):
        items = self.list_dir(path)
        for idx, item in enumerate(items):
            full_path = os.path.join(path, item)
            print(f"{prefix}[{idx}] {item}{'/' if os.path.isdir(full_path) else ''}")

    def run(self):
        current_path = self.root_path
        history = []

        while True:
            print("\nCurrent path:", current_path)
            self.display_level(current_path)
            print("\nOptions: [index] to open folder, 'c [index]' to copy path, '..' to go up, 'q' to quit")

            command = input("> ").strip()

            if command == "q":
                break
            elif command == "..":
                if history:
                    current_path = history.pop()
                else:
                    print("Already at root.")
            elif command.startswith("c "):
                try:
                    idx = int(command.split()[1])
                    items = self.list_dir(current_path)
                    if 0 <= idx < len(items):
                        full_path = os.path.join(current_path, items[idx])
                        print("Copied path:", full_path)
                    else:
                        print("Invalid index.")
                except ValueError:
                    print("Invalid command.")
            else:
                try:
                    idx = int(command)
                    items = self.list_dir(current_path)
                    if 0 <= idx < len(items):
                        selected = os.path.join(current_path, items[idx])
                        if os.path.isdir(selected):
                            history.append(current_path)
                            current_path = selected
                        else:
                            print(f"{selected} is not a folder.")
                    else:
                        print("Invalid index.")
                except ValueError:
                    print("Invalid command.")


if __name__ == "__main__":
    root = input("Enter root path: ").strip()
    time.sleep(1)
    tree = LazyTree(root)
    tree.run()
