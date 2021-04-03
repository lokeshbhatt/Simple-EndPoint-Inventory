# Simple host inventory creation framework
This documents details simple hosts inventory creation framework
#
#
# Use Case
1. You are an administrator and want to keep daily records of your hosts & other end-points configuration
2. You are a capacity manager and want to keep track of daily allocation of resources
#
#
# Requirements
- A jump-point/central server/workstation with network reachability to end points
- Password less SSH configuration (user from jump-point server should be able to connect to end points w/o requiring password) 
- ksh at each AIX end point
- Python v3.6 at jump point server
