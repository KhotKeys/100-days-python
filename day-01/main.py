import json
from pathlib import Path

DATA_FILE = Path(__file__).parent /"projects.json"

def load_projects():
    if not DATA_FILE.exists():
        return []

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError:
        backup = DATA_FILE.with_suffix(".json.bak")
        DATA_FILE.rename(backup)
        print(f"Projects. json was damange. Saved a copy as {backup.name} and started fresh.")
        return []

def save_projects(projects):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(projects, file, indent=2)

def show_menu():
    print("\n=== Project Tracker ===")
    print("1. Add a project")
    print("2. View projects")
    print("3. Mark a project as done")
    print("4. Delete a project")
    print("5. Quit")

def add_project(projects):
    name = input("Name: \n").strip()
    if not name:
        print("The project name can't be empty")
        return
    
    series = input("Series: \n").strip()
    academic_code = input("Academic Code: \n").strip()
    start_date = input("Start date (YYYY-MM-DD): \n").strip()
    end_date = input("End date (YYYY-MM-DD): \n").strip()

    project = {
        "name": name,
        "series": series,
        "academic_code": academic_code,
        "start_date": start_date,
        "end_date": end_date,
        "done": False,
    }

    projects.append(project)
    save_projects(projects)
    print(f"Added: {name}")

def view_projects(projects):
    if not projects:
        print("No project yet.")
        return
    
    for number, project in enumerate(projects, start=1):
        status = "[x]" if project["done"] else "[ ]"
        name = project["name"]
        series = project["series"]
        code = project["academic_code"]
        start = project["start_date"]
        end = project["end_date"]

        print(
            f"{number}. {status} {name} - {series} - {code} - {start} to {end}"
        )       

def ask_project_index(projects, action):
    if projects is None:
        print("There is no project yet.")
        return None

    view_projects(projects)
    answer = input(f"Which project you want to {action}?: \n").strip()

    try:
        number = int(answer)
    except ValueError:
        print("please enter a number")
        return None

    if number < 1 or number > len(projects):
        print(f"Please pick a number between 1 and {len(projects)}")
        return None
    
    return number - 1

def mark_done(projects):
    index = ask_project_index(projects, "Mark as done")

    if index is None:
        return

    project = projects[index]
    if project["done"]:
        print(f"{project["name"]} is already done!")
        return

    project["done"] = True
    save_projects(projects)
    print(f"Marked as done: {project["name"]} ")


def delete_project(projects):
    index = ask_project_index(projects, "Delete")

    if index is None:
        return

    name = projects[index]["name"]
    confirmation = input(f"Please delete this '{name}'? (y/n): \n").strip().lower()
    if confirmation != 'y':
        print("Delete cancelled.")
        return

    removed = projects.pop(index)
    save_projects(projects)
    print(f"Deleted: {removed['name']}")


def main():
    projects = load_projects()

    while True:
        show_menu()
        choice = input("Choose an option: \n").strip()

        if choice == "1":
            add_project(projects)
        elif choice == "2":
            view_projects(projects)
        elif choice == "3":
            mark_done(projects)
        elif choice == "4":
            delete_project(projects)
        elif choice == "5":
            print("Thank you for using the Project Tracker. Goodbye!")
            break
        else:
            print("Please, pick a number from 1 to 5.")

if __name__ == "__main__":
    main()