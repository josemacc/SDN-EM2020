import requests

r = requests.get('https://sandboxsdwan.cisco.com:8443/dataservice/device',
                 auth=('devnetuser', 'Cisco123!'), verify=False)

respuesta = r.json()['data']

#pprint(respuesta)

for dev in range(len(respuesta)):
    print("\n -----")
    print("Device: " + respuesta[dev]['host-name'])
    print("Type: " + respuesta[dev]['device-type'])
    print("Status: " + respuesta[dev]['status'])
