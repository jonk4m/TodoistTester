# General Notes 

Thermal printer is $50 from adafruit, $2 for a 50'x2.25" roll

curl -X GET https://api.todoist.com/rest/v2/tasks?filter=today -H "Authorization: Bearer "

the e9a97... Bearer number is your token found under settings->developer

change the "filter=today" to "filter=overdue" to get your overdue tasks

## Examples

### Get User's Projects 
from todoist_api_python.api import TodoistAPI

api = TodoistAPI("0123456789abcdef0123456789")

try:
    projects = api.get_projects()
    print(projects)
except Exception as error:
    print(error)

### Get JSON List of User's tasks for Today 

### Get JSON List of USer's overdue tasks for Today

