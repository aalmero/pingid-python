import sys, json
import pingid

PROPERTIES_FILE = './pingid.properties'

pingid = pingid.PingIDDriver(PROPERTIES_FILE, verbose=False)

def get_job_status(jobToken):
  req_body = {
     'jobToken': jobToken,
     'clientData': 'NONE',
    }
  
  return pingid.call('rest/4/getjobstatus/do', req_body)

#main logic
arguments = len(sys.argv) - 1
if arguments == 0:
  print('Usage: ' + __file__ + ' <jobToken>')
  exit()

jobToken = sys.argv[1]

response_body = get_job_status(jobToken)  

job = response_body['responseBody']
if (job['errorId'] == 200):
  status = job['jobResult']['status']
  if status == 'DONE':
    print('Job \'{0}\' succesfully completed.'.format(jobToken))
  else:
    print('Job \'{0}\' has not completed.'.format(jobToken))  
else:
  print('[!] Get Job Status Request Failed.')    
  