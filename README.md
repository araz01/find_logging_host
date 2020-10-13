# find_logging_host

ProjectTask:
============
Create Python script that will login to a Cisco network devices, runs a command to get SysLog/Logging host IPs and parse out details to an excel spreadsheet.
its works for both Cisco ios and NX-OS.


Requirements:
=============
Use python 3, and make sure netmiko, openpyxl installed in the machine (Windows/Unix/MAC).

Device_logging_info.xlsx, find_logging_host_v1.py, inventory.txt has to be in the same folder.


inventory file should contain the IP address/ device name (including Domain or full DNS name) example included:

10.10.10.10
10.10.10.xx
xyz.ns.xxxx


Instructions:
=============
1. *don't open the spreadsheet during execution of the code.
2. to execute of code do following:
> python3 find_logging_host.py

3. once completed, open the spreadsheet for the output.
