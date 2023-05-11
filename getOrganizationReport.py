import json
import pingid

PROPERTIES_FILE = './pingid.properties'

req_body = {
   'fileType':'JSON',
   'clientData': 'NONE',
  }

pingid = pingid.PingIDDriver(PROPERTIES_FILE, verbose=False)
response_body = pingid.call('rest/4/getorgreport/do', req_body)
print(response_body)
#print('{0}Response{0}\n{1}\n'.format('='*20, json.dumps(response_body, indent=2)))
