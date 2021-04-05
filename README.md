# Simple inventory creation framework
- This documents details simple inventory creation framework
- Although use case detailed is for AIX operating system, but same can be easily expanded to any end point 
#
#
# Use Case
1. You are an administrator and want to keep daily records of your hosts & other end-points configuration
2. You are a capacity manager and want to keep track of daily allocation of resources
#
#
# Requirements
- A central jump-point server/workstation with network reachability to end points
- Password less SSH configuration from central jump-point to end points
  -- Non-privileged user is fine  
- ksh at each AIX end point
- Python v3.6 at jump point server
#
#
# Technical Framework
Proposed frame work is primarily comprises of 3 stages,
1. Data Generation: End point inventory file generation
2. Data Gathering: All inventory files are gathered at one place
3. Data Parsing: Parsing of inventory files to generation single data file

![Alt text](https://github.com/lokeshbhatt/Simple-EndPoint-Inventory/blob/main/Inventory%20-%20how%20it%20works.JPG "Simple Inventory Creation - Technical Framework")
#
#
# Demonstrated use case
- AIX inventory creation
- AIX based central jump point server
- AIX based end points / LPARs
#
#
# Detailed Steps
## End-point  
- login with non-privileged user (cecuser in case of example below)  
- Create "Inventory" directory on each end point  
- Change to "Inventory" directory  
        $ cd /home/cecuser/Inventory  
- Copy "AIXInventory.sh" to all AIX end points  
        $ pwd  
        /home/cecuser/Inventory  
        $ ls  
        AIXInventory.sh  
- Edit crontab (crontab -e) to include following entry  
        00 00 * * * /home/cecuser/Inventory/AIXInventory.sh      #This initiates inventory data collection every mid night 0000 Hrs.  
#
## Central jumppoint
- AIX based central jumppoint is considered
- Install "python" and reuired libraries  
      $ curl -o aixtools.python.py36.3.6.12.0.I http://download.aixtools.net/tools/aixtools.python.py36.3.6.12.0.I  
      $ su -   
      # installp -d aixtools.python.py36.3.6.12.0.I -a all  
      # opt/bin/python3.6 --version   
      Python 3.6.12 
      # /opt/bin/pip3 install --upgrade pip  
      # /opt/bin/pip3 install xlsxwriter  
      # exit    
- Validate passwordless authentication from jump-point to all end-points
- Create & change to "Inventory" directory
- Create "hostlist" file (Single with hostname or IP addresses in each line without any spaces)  
      $ cat hostlist  
      p1263-pvm1  
      p1263-pvm2  
      p1263-pvm3  
- Copy "PullInventory-0.0.sh" to "Inventory" directory  
- Copy "CollateInventory-0.0.py" to "Inventory" directory  
    $ pwd  
    /home/cecuser/Inventory  
    $ ls  
    AIXInventory.sh          CollateInventory-0.0.py  PullInventory-0.0.sh     hostlist  
- Edit crontab (crontab -e) to include following entries,  
    00 00 * * * /home/cecuser/Inventory/AIXInventory.sh  
    00 01 * * * /home/cecuser/Inventory/PullInventory-0.0.sh  
    00 02 * * * /home/cecuser/Inventory/CollateInventory-0.0.py  
- Refer output file "Inventory_DD_MM_YYYY"
#
#
# Downloads
- [AIXInventory.sh](https://github.com/lokeshbhatt/Simple-EndPoint-Inventory/blob/main/AIXInventory_0.0.ksh)
- [PullInventory-0.0.sh](https://github.com/lokeshbhatt/Simple-EndPoint-Inventory/blob/main/PullInventory-0.0.sh)
- [CollateInventory-0.0.py](https://github.com/lokeshbhatt/Simple-EndPoint-Inventory)
- [aixtools.python.py36.3.6.12.0.I](http://download.aixtools.net/tools/aixtools.python.py36.3.6.12.0.I)
