def show_menu():
    print("\n=== Project Tracker ===")
    print("1. Add a project")
    print("2. View projects")
    print("3. Mark a project as done")
    print("4. Delete a project")
    print("5. Quit")

def add_project(projects):
    name = input("Name: \n").strip()
    series = input("Series: \n").strip()
    academic_code = input("Academic Code: \n").strip()
    start_date = input("Start Date: \n").strip()
    end_date = input("End Date: \n").strip()
    title = f"{name} - {series} - {academic_code} - {start_date} - {end_date}".strip()

    if not title:
        print("The project title can't be empty")
        return

    project = {"title": title,"done": False}
    projects.append(project)
    print(f"Added: {title}")

def view_projects(projects):
    if not projects:
        print("No project yet.")
        return
    
    for number, project in enumerate(projects, start=1):
        status = "[X]" if project["done"] else "[ ]"
        print(f"{number}. {status} {project['title']}")

def main():
    projects = []

    while True:
        show_menu()
        choice = input("Choose an option: \n").strip()

        if choice == "1":
            add_project(projects)
        elif choice == "2":
            view_projects(projects)
        elif choice == "3":
            print("Mark done (COMING SOON)")
        elif choice == "4":
            print("Delete done (COMING SOON)")
        elif choice == "5":
            print("Thank you for using our service. Goodbyee!")
            break
        else:
            print("Please, pick from 1 to 5")

if __name__ == "__main__":
    main()