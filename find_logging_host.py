from netmiko import ConnectHandler
from getpass import getpass
import getpass
import re
import openpyxl

#######*****#######

Device_LIST  = open('inventory.txt')

user1 = input("Enter Username: ")
#pass1 = input("Enter Password: ")
pass1 = getpass.getpass("Enter Password: ")

wb = openpyxl.load_workbook('Device_logging_info.xlsx')
ws1 = wb.active
ws1.title = "Logging_info"

rowdata = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "AA", "AB", "AC", "AD"]

#err = ""
Logg = "logging"
cmd1 = "show run | i logging"

i = 2


for Host in Device_LIST:
	print("Reading Device info of " + Host.strip() + "")
	RTR = {
		'device_type': 'cisco_ios',
		'ip':   Host,
		'username': user1,
		'password': pass1
		}


	i += 1
	count = 0
	row = "A" + str(i)
	ws1[row] = Host
	output2 = ""

	try:
		net_connect = ConnectHandler(**RTR)
		output2 = net_connect.send_command(cmd1)

		if output2 != "":
			mylist = output2.rstrip('\n').split()

			col = 1
			for n in range(len(mylist)):
				if mylist[n].find(Logg) != -1:
					if mylist[n + 1] == "server":
						row = rowdata[col] + str(i)
						ws1[row] = mylist[n + 2]
						col += 1
						count = count + 1

					elif mylist[n + 1] == "host":
						row = rowdata[col] + str(i)
						ws1[row] = mylist[n + 2]
						col += 1
						count = count + 1


		if count == 0:
			row = rowdata[col] + str(i)
			ws1[row] = "Logging not configured"

		net_connect.disconnect()

	except:
		print("Couldn't login to " + Host.strip() + "\n")
		net_connect.disconnect()


wb.save("Device_logging_info.xlsx")

print('\nCompleted...!!!')

net_connect.disconnect()

# END...