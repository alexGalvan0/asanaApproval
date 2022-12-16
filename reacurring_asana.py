"""
projects_asana.py 
Created By: Alex Galvan
Program will delete attachetments evrey week on the announcement_gfx task in asana.
"""
import asana

#Authentication 
cred = 'CREDS'
client = asana.Client.access_token(cred)
me = client.users.me()


def main (name_of_task):
    design_weekly_tsks = '1199405096459889'
    tsks_weekly_dsg = list(client.tasks.get_tasks_for_section(design_weekly_tsks,{'opt_fields':'name'}))
    #Get all task gids off announcement gfx into a python list
    tsk_gids = []
    for tasks in range(0,len(tsks_weekly_dsg)):
        if tsks_weekly_dsg[tasks]['name'] == name_of_task:
            tsk_gids.append(tsks_weekly_dsg[tasks]['gid'])

    #Get new task announcement gfx task for the week's gid
    new_tsks = []
    for tsk_gid in tsk_gids:
        task_info = client.tasks.get_task(tsk_gid)
        if task_info['completed'] == False:
            new_tsks.append(task_info['gid'])

    #Get attachements from new task in the new_tsk python list called attachemt_gids
    attachemt_gids =[]
    for new_tsk in new_tsks:
        tsk_info = list(client.attachments.get_attachments_for_task(new_tsk))
        for num in range(0,len(tsk_info)):
            attachemt_gids.append(tsk_info[num]['gid'])
            
    for attachemt_gid in attachemt_gids:
        client.attachments.delete_attachment(attachemt_gid)

if __name__ =="__main__":
	main("Announcement GFX")
if __name__ =="__main__":
    main("Communion/Reflection GFX")
