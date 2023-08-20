from todoist_api_python.api import TodoistAPI

api = TodoistAPI("0123456789abcdef0123456789")

try:
    projects = api.get_projects()
    print(projects)
except Exception as error:
    print(error)