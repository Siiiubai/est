import eel 
import json
import os
import sys

print("Script started")
print(f"Python version: {sys.version}")
#print(f"Eel version: {eel.__version__}")

# Get the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))
print(f"Current directory: {current_dir}")

# Set the web files folder
web_folder = os.path.join(current_dir, 'web')
print(f"Web folder: {web_folder}")

TODO_COUNT = 0

# Initialize eel with the absolute path
try:
    eel.init(web_folder)
    print("Eel initialized successfully")
except Exception as e:
    print(f"Error initializing Eel: {e}")

def read_data():
    with open('data.json', 'r') as file:
        return json.load(file)

def write_data(content):
    with open('data.json', 'w') as file:
        json.dump(content, file, indent=2)
    return content

@eel.expose
def create_todo(title):
    global TODO_COUNT
    TODO_COUNT += 1
    new_todo = {
        'id': TODO_COUNT,
        'title': title
    }
    content = read_data()
    content['todos'].append(new_todo)
    write_data(content)
    return new_todo

@eel.expose
def list_todos():
    return read_data()

@eel.expose
def delete_todo(id):
    global TODO_COUNT
    content = read_data()
    content['todos'] = [todo for todo in content['todos'] if todo['id'] != id]
    write_data(content)
    TODO_COUNT = len(content['todos'])

if not os.path.exists('data.json'):
    with open('data.json', 'w') as file:
        json.dump({'todos': []}, file)
else:
    content = read_data()
    TODO_COUNT = max([todo['id'] for todo in content['todos']], default=0)

# At the end of the file:
if __name__ == "__main__":
    html_file = os.path.join(web_folder, 'main.html')
    print(f"Looking for HTML file: {html_file}")
    if not os.path.exists(html_file):
        print(f"Error: {html_file} not found!")
    else:
        print(f"HTML file found. Attempting to start Eel...")
        try:
            eel.start('main.html', size=(800, 600), mode='edge')
        except Exception as e:
            print(f"Error starting Eel: {e}")
            print(f"Eel._start_args: {eel._start_args}")
