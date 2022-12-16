"""
newRequest_asasna.py 
Created By: Alex Galvan
Program will run evrey few minutes to acknowledge to the client that a request has been submitted
NOT IN PRODUCTION
"""
import asana
from pprint import pprint as pp 

cred = '1/1111064222358483:98aad7b6d15fb22fb8283e174991fa14'
client = asana.Client.access_token(cred)
me = client.users.me()


def sections(team_gid):
    #returns a list of sections from creative team
    projects = list(client.projects.get_projects_for_team(team_gid,{'opt_fields':'gid',
                                                                    'opt_fields':'name',
                                                                    'archived':False}))
    for project in projects:
        section = list(client.sections.get_sections_for_project(project['gid']))
        return(section)
sections('1120765093408562')









def newTsks():
    #returns types of requests from new requests sections in the new requests project.
    new_req_section_gid = '1199385977779343'
    new_reqs = list(client.tasks.get_tasks_for_section(new_req_section_gid,{'opt_fields':'gid'})) #list of new req gids

    for new_req in new_reqs:
        task_gid = new_req['gid']
        task = client.tasks.get_task(task_gid,{'opt_fields':'custom_fields.text_value'})
        pp(task['custom_fields'][1]['text_value'])


