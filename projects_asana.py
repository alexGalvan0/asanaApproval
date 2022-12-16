"""
projects_asana.py 
Created By: Alex Galvan
Program will add approved request into respected projects and sections.
"""
import asana
#Authentication 
cred = '1/1111064222358483:98aad7b6d15fb22fb8283e174991fa14'
client = asana.Client.access_token(cred)
me = client.users.me()

approved_sec_gid = '1198513601388630'
approved_sec_tsks = list(client.tasks.get_tasks_for_section(approved_sec_gid))

def add_sec (sec_gid,task_gid):
    # Add task into new Section
    result = client.sections.add_task_for_section(sec_gid, {'task': task_gid})

def check_notes (task_gid):
    #Get all approved task NOTES
    tsk_info = client.tasks.get_task(task_gid)
    type_of_req = tsk_info ['custom_fields'][1]['display_value']
    return(type_of_req)

def main (project_id):
    secs = list(client.sections.get_sections_for_project(project_id))
    for sec in range (0,len(secs)):
        dics =  secs[sec]
        names = (dics['name'])
        gids = (dics['gid'])
        #Check type of Req
        for approved_sec_tsk in range (0,len(approved_sec_tsks)):
            aprved_gids = approved_sec_tsks[approved_sec_tsk]['gid']
            answer = check_notes(aprved_gids) 
            #pprint(com_sec_names + answer)
            if answer == names :
                add_sec(gids,aprved_gids)
            else:
                pass
                

main('1199378946093870')#Comms
main('1199378946093873')#Des
main('1199378946093867')#Vid

