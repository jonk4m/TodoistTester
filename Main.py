from todoist_api_python.api import TodoistAPI
import json

api = TodoistAPI("123456789876")

try:
    projects = api.get_projects()
    # Just print the entire JSON's for the projects
    # print(projects) 
    # print only the name strings of the projects 
    for project in projects:
        print(project.name)
except Exception as error:
    print(error)