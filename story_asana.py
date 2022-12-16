"""
approval_asana.py 
Created By: Alex Galvan
Program will get last note and place it in a custom flield
"""
from os import name
import asana
import logging
from pprint import pprint as pp
logging.basicConfig(filename = 'asana_log.log',level = logging.INFO, format ='%(asctime)s:%(levelname)s:%(message)s')
cred = '1/1111064222358483:98aad7b6d15fb22fb8283e174991fa14'
client = asana.Client.access_token(cred)
me = client.users.me()

def get_names(note):
    updated_note = note
    
    dict = {'https://app.asana.com/0/1120765509095916/list':'Neil Gregory',
                'https://app.asana.com/0/1120765650673038/list':'Nick Key',
                'https://app.asana.com/0/795229807353606/list':'Miranda Reaves',
                'https://app.asana.com/0/795229807353606/calendar':'Miranda Reaves',
                'https://app.asana.com/0/795229807353606/795229807353606':'Miranda Reaves',
                'https://app.asana.com/0/1120963410897111/list':'Caitlin Malone',
                'https://app.asana.com/0/1165882834333578/list':'Michael Vandemark',
                'https://app.asana.com/0/1164445702370188/list':'Jessica McKenney',
                'https://app.asana.com/0/13196939616157/list':'Todd Ferguson',
                'https://app.asana.com/0/13196939616157/13196939616157':'Todd Ferguson',
                'https://app.asana.com/0/1111567443702405/1111567443702405':'Drew Metcalfe',
                'https://app.asana.com/0/1111567443702405/list':'Drew Metcalfe',
                'https://app.asana.com/0/1111064120619414/list':'Alex Galvan',
                'https://app.asana.com/0/1200435787024410/list':'Jeren Joslin',
                'https://app.asana.com/0/1120963410897125/list':'Toria Howard',
                'https://app.asana.com/0/1201341477361320/list':'Liz Poe'
    }


    for key,value in dict.items():
        if key in note:
            updated_note = note.replace(key,value)
            break
    return(updated_note)


def get_tsk_stories(task_gid):
    #returns last comments added resource_subtype': 'comment_added'
    task_gid = task_gid
    sub_text_type = list(client.stories.get_stories_for_task(task_gid))
    comments_added = []
    for comment in sub_text_type:
        if comment['resource_subtype'] == 'comment_added':
            comments_added.append(comment)
    for comment in range(0,len(comments_added)):
        all_comments = list(comments_added)
        last_comment = all_comments[-1]['text']
    return(get_names(last_comment))

def get_inc_tsks():
#Returns a list of all incompleted task gids called incompleted_tasks
    project_gid = '1198513601388629'  
    tasks_in_proj = list(client.tasks.get_tasks_for_project(project_gid, {'opt_fields': 'completed'}))
    task_gid = []
    for task in tasks_in_proj:
        if task['completed'] == False:
            task_gid.append(task['gid'])
    return(task_gid)
def main():
    for tsk_gid in get_inc_tsks():
        try:
            client.tasks.update_task(tsk_gid,{'custom_fields':{'1201021503995606':get_tsk_stories(tsk_gid)}})
        except:
            pass
if __name__ =="__main__":
    main()










