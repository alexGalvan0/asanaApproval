"""
approval_asana.py 
Created By: Alex Galvan
Program will notify once Creative Requests have been Approved.
"""
import asana
import sys
import logging
from pprint import pprint as pp 
logging.basicConfig(filename = 'asana_log.log',level = logging.INFO, format ='%(asctime)s:%(levelname)s:%(message)s')

# Construct an Asana Client
def main():
	#cred = open('creds.txt','r').read()
	cred = 'CREDS'
	client = asana.Client.access_token(cred)
	me = client.users.me()
	# Asana GIDs
	assigned_tag = '1198946033379088'
	ordered_tag = '1198923347472692' 
	new_requests_project = '1198513601388629'

	#get Gdids from New Requests Project
	tasks_in_proj = client.tasks.get_tasks_for_project(new_requests_project, {'opt_fields': 'completed'})

	not_cmpl_tsk = []
	for task in tasks_in_proj:
		if task['completed'] == False:
			not_cmpl_tsk.append(task['gid'])

	#get task info for not completed taskS
	for tasks in not_cmpl_tsk:
		try:
			tags = str((client.tasks.get_task(tasks,{'opt_fields':'tags.name'})['tags'][0:]))
			etas = (client.tasks.get_task(tasks,{'opt_fields':'custom_fields.text_value'})['custom_fields'][4]['text_value'])
			emails = (client.tasks.get_task(tasks,{'opt_fields':'custom_fields.text_value'})['custom_fields'][0]['text_value'])
			prject_name = (client.tasks.get_task(tasks,{'opt_fields':'name'})['name'])
			approvals = str((client.tasks.get_task(tasks)['custom_fields'][3]['enum_value']['name'])) 
			note = (client.tasks.get_task(tasks)['notes'].encode('utf-8'))
			#notes = note.decode('utf-8')
	#GmailAPI
			if ('Assigned' not in tags) and ('Approved' in approvals) :
				client.tasks.add_tag_for_task(tasks,{"tag": assigned_tag})
				# Getting gmail api to send Approved Email
				import smtplib
				smtp_object = smtplib.SMTP('smtp.gmail.com',587)
				smtp_object.ehlo()
				smtp_object.starttls()
				email = 'agalvan@southlandchristian.org'
				#gmcreds = open('gcred.txt','r').read()
				gmcreds = 'kzqjxrznnzlsfnnr'
				smtp_object.login(email,gmcreds)

				from_email_address = 'Alex Galvan'
				to_email_address = 'agalvan@southlandchristian.org',emails
				subject = 'Your Project "'+prject_name+'" has been approved!'
				messege = 'Your Creative request "'+prject_name+'" has been approved!'+\
				'\n'+'\n'+'If you have any questions, want to learn more about updates, or follow up in '+\
				'any other way on this project, please let me know.'+\
				'\n'+'We will reach out to you if we have any questions!'+note


				msg = 'Subject:' + subject + '\n' + messege				
				smtp_object.sendmail(from_email_address,to_email_address,msg)
				logging.info('Email has been sent to: '+emails+'for "'+prject_name+'" '+'request approval')
				logging.info('email sent')


			else:
				logging.info('Nothing needed to be sent')
		except:
			pass #print('Cannot read notes' + prject_name)
		finally:
			pass
if __name__ =="__main__":
	main()


