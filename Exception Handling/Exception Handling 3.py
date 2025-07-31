#Handle FileNotFoundError Exception When Opening a File
try:
    with open('text.txt', 'r') as file:
        content = file.read()
except FileNotFoundError as e:
    print(f"Error: {e}. The file doesn't exist.")