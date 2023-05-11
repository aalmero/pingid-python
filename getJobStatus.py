import pingid

PROPERTIES_FILE = './pingid.properties'

req_body = {
   'jobToken':'VQJSXFUMVAAAUAsBUAAAWgAFAAFeBgMAUVVRAAdSVAJVAwNV',
   'clientData': 'NONE',
  }

pingid = pingid.PingIDDriver(PROPERTIES_FILE, verbose=True)
response_body = pingid.call('rest/4/getjobstatus/do', req_body)

