from todoist_api_python.api import TodoistAPI

api = TodoistAPI("123456789")

try:
    projects = api.get_projects()
    for project in projects:
        # print(project.name)
        if project.name == 'Inbox': 
            print("found it, printing tasks")
            tasks = api.get_tasks(project_id = project.id)
            # print(tasks)
            for task in tasks:
                print(" - " + task.content)
except Exception as error:
    print(error)