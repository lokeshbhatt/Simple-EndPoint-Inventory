# Simple host inventory creation framework
- This documents details simple hosts inventory creation framework
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

![Alt text](https://github.com/lokeshbhatt/Simple-EndPoint-Inventory/blob/main/Inventory%20-%20how%20it%20works.JPG "Simple Inventory Collection - Technical Framework")
#
#
#
# Demonstrated use case
- AIX inventory creation
#
#
# Detailed Steps
### Step-1: Validate that passwordless authentication from jump-point to all end-points is working well
### Step-2: Copy AIXInventory.sh to all AIX end pointh
