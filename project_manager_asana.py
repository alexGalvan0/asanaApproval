"""
projectManager.py will assing task in asana to 
corresponfing team lead based on type of request 
chosen in one form to rule them all 
"""

#import dependancies
import asana
from pprint import pprint as pp

#global variables
cred = 'CRED'#caitlin creds
client = asana.Client.access_token(cred)

leads = {'caitlin':'1120963410897111',
        'nick':'1120765650673038',
        'drew':'1111567443702405'}

video = ['Video']
video_project_gid = '1199378946093867'
video_new_request_section_gid ='1201279191764834'

comms = ['Announcements','Calendar','Content Editing','Photography Needs','Social Media','Webpage']
comms_project_gid = '1199378946093870'
comms_new_request_section_gid = '1201279191764832'

design = ['Graphics','Product','Signage Needs']
design_project_gid = '1199378946093873'
design_new_request_section_gid = '1201279191764833'



# Construct an Asana Client
def main():

    section_gid ='1199385977779343' #New Request section in New reqeust project
    result = list(client.tasks.get_tasks_for_section(section_gid))
    
    for i in range(0,len((result))):
        try:
            task_gid = result[i]['gid']
            task_info = client.tasks.get_task(task_gid)
            type_of_request = task_info['custom_fields'][1]['text_value'] #gets the type of request custom feild

            if type_of_request in video:
                client.tasks.update_task(task_gid, {'assignee':leads['nick']})
                client.tasks.add_project_for_task(task_gid,{'project': video_project_gid})
                client.sections.add_task_for_section(video_new_request_section_gid,{'task':task_gid})

            if(type_of_request in design):
                client.tasks.update_task(task_gid, {'assignee':leads['caitlin']})
                client.tasks.add_project_for_task(task_gid,{'project': design_project_gid})
                client.sections.add_task_for_section(design_new_request_section_gid,{'task':task_gid})

            if(type_of_request in comms):
                client.tasks.update_task(task_gid, {'assignee':leads['drew']})
                client.tasks.add_project_for_task(task_gid,{'project': comms_project_gid})
                client.sections.add_task_for_section(comms_new_request_section_gid,{'task':task_gid})
        except:
            pass

if __name__ =="__main__":
	main()
