import pingid

PROPERTIES_FILE = './pingid.properties'

req_body = {
   'jobType':'USER_REPORTS',
   'clientData': 'NONE',
  }

pingid = pingid.PingIDDriver(PROPERTIES_FILE, verbose=True)
response_body = pingid.call('rest/4/createjob/do', req_body)
