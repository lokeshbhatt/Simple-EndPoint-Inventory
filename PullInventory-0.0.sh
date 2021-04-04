#!/usr/bin/ksh
#
for h in `cat hostlist`
do
scp $h:/home/cecuser/Inventory/*.AIXInventory ./ >> PullInventory.log 2>&1
done
