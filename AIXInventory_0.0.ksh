#!/usr/bin/ksh
#
#OFNAME=`hostname``date +"_%d%m%Y_%H%M"".AIXInventory"`
OFNAME=`hostname`".AIXInventory"
ODIR='/home/cecuser/Inventory'                          #Change output directory variable to directory of your choice
#
aix_commands() {
cat <<- AIX_COMMANDS
        general,date,normal user
        general,uptime, normal user
        os,hostname,normal user
        os,uname_-aM,normal user
        os,oslevel_-s,normal user
        os,prtconf,normal user
        os,lscfg_-pv,normal user
        network,ifconfig_-a,normal user
        network,lsattr_-El_inet0,normal user
        network,netstat_-nr,normal user
        hw,lsslot_-c_slot,normal user
        hw,lsmcode,normal user
        hw,lsdev_-Cc_adapter,normal user
        hw,lsattr_-El_sys0,normal user
        hw,lparstat_-i,normal user
        hw,lsrsrc_-l_IBM.ManagementServer,
        hw,lsrsrc_-l_IBM.MCP
        storage,lspv,normal user
        storage,lspv_-u,normal user
        storage,lsdev_-Cc_disk,normal user
        storage,lsdev_-Cc_tape,normal user
        storage,lsvg,normal luser
        storage,lsvg_-o,normal user
        storage,lsfs,normal user
        storage,lsvg_-o_|_xargs_lsvg_-l,normal user             #NEW
        storage,lsvg_-o_|_xargs_lsvg_-p,normal user             #NEW
        storage,lspv_-u,normal user
        storage,df,normal user
        storage,df_-g,normal user
        virtual,echo_cvai_|_kdb,root user
        virtual,echo_vfcs_|_kdb,root user
AIX_COMMANDS
}
#
cd $ODIR
cat /dev/null > $OFNAME
#
aix_commands | grep -v "^$" | awk -F "," '{print $2}' | while read line
        do
#
        CM=`echo $line | tr "_" " "`
#
        printf "\nSTART\n" > TempCommandOutput
        eval $CM >> TempCommandOutput 2>&1
        printf "\nEND\n" >> TempCommandOutput
        sed -e "s/^/$line,/" TempCommandOutput >> $OFNAME
#
        if [ -f TempCommandOutput ];then
                rm TempCommandOutput
        fi
#
        done
