''' Display controller and devices information using RESTAPI

Swapnasheel Sonkamble

'''

import requests
import json
import unicodedata
from subprocess import Popen, PIPE
import time


def getResponse(choice,url):
	response = requests.get(url)
	if(response.ok):
		jData = json.loads(response.content)
		if(choice == "ControllerInformation"):
			print "Controller Stats:"
			print "No of Switches: " + str(jData['# Switches'])
			print "No of Inter-switch links: " + str(jData['# inter-switch links'])
			print "No of Quarantine ports: " + str(jData['# quarantine ports'])
			print "No of hosts: " + str(jData['# hosts'])

		elif(choice == "SwitchRoles"):
			print "Switch Roles:"
			k=1			
			for i in jData:
				print "Switch {}: ".format(k) + str(jData[i])
				k = k+1

		elif(choice == "Flows"):
			print "Flow Stats:"
			j = 1
			for i in jData:
				print "Switch {}: ".format(j)
				print "Priority : " + str(jData[i]['flows'][0]['priority'])
				print "Byte Count : " + str(jData[i]['flows'][0]['byte_count'])
				print "Packet Count : " + str(jData[i]['flows'][0]['packet_count'])
				print "OF version : " + str(jData[i]['flows'][0]['version'])
				print "Actions : " + jData[i]['flows'][0]['instructions']['instruction_apply_actions']['actions']
				j = j+1
				print 

		elif(choice == "Firewall"):
			print "Firewall Status:"
			print jData['result']


#Run until keyboard Interuption 
while 1:
	try:
		print "\nSelect your option \n1. Display Controller Information \n2. Dislay Switch Roles \n3. Display Flow Information \n4. Display Firewall Status \n"
		option = input()
		if option == 1:			
			conInfo = "http://localhost:8080/wm/core/controller/summary/json"
			getResponse("ControllerInformation",conInfo)
		elif option == 2:
			switchRole = "http://localhost:8080/wm/core/switch/all/role/json"
			getResponse("SwitchRoles",switchRole)
		elif option == 3:
			flow = "http://localhost:8080/wm/core/switch/all/flow/json"
			getResponse("Flows",flow)
		elif option == 4:
			fwall = "http://localhost:8080/wm/firewall/module/status/json"
			getResponse("Firewall",fwall)

	except KeyboardInterrupt:
		break
		exit()



if __name__ == '__main__':
    Main()
