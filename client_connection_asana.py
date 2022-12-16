"""
client_connection_asana.py 
Created By: Alex Galvan
Program will run evrey few minuts and assign the "Read & 
connect with client" subtask and assign it to the assignee of the parent task
"""
from pprint import pprint as pp

import asana

cred = 'CRED'
client = asana.Client.access_token(cred)
me = client.users.me()




def getTaskIds():
#Get all approved tasks ID in the new request projects into a python list
    new_requests_project = '1198513601388629'
    tasks_in_proj = list(client.tasks.get_tasks_for_project(new_requests_project, {'opt_fields': 'completed'}))
    sample_tsk = client.tasks.get_task('1202193435648183')
   # pp(sample_tsk)

    for task in tasks_in_proj:
        try:
            if task['completed'] == False:
                task_gid = task['gid']

                custom_fields = client.tasks.get_task(task_gid,{'opt_fields':'custom_fields.enum_value'})
                approval_status = custom_fields['custom_fields'][3]['enum_value']['name']
                pp(approval_status)

                if approval_status == 'Approved':
                    #get task assignee
                    assignee = client.tasks.get_task(task_gid)['assignee']['name']
                    assignee_gid = client.tasks.get_task(task_gid)['assignee']['gid']
                    subtask_gid = list(client.tasks.get_subtasks_for_task(task_gid))
                    if subtask_gid[0]['name'] == 'Read & Connect with Client':
                        pp(subtask_gid)
        except:
            pass

getTaskIds()

