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
# Demonstrated use case
- AIX inventory creation
#
#
# Requirements
- A central jump-point server/workstation with network reachability to end points
- Password less SSH configuration from central jump-point to end points
  -- Non-privileged user is fine
- ksh at each AIX end point
- Python v3.6 at jump point server
- 
#
#
# Steps-1: Validating that passwordless authentication from jump-point to all end-points is working well
## Setup
