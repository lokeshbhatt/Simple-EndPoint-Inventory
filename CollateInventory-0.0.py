#!/opt/bin/python3.6
import os
import datetime
#######################################################################
#   CreateInventory
#   Developer: Lokesh Bhatt
#   (C) Copyright 2021 Lokesh Bhatt
#
#   - Collate all AIX inventory files present in current working directory
#     into a comma separated file (.csv)
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#########################################################################
#ChangeLog
#
# 0.0
#   - GA version
#########################################################################
#
#
ODIR="/home/cecuser/Inventory"

def PrepareInventoryFilesList() :
    if len(os.listdir()) == 0 :
        res = input("No files found in present working directory")
        exit(0)
    else :
        InventoryFileList = []
        for File in os.listdir() :
            if File.split(".")[-1] == "AIXInventory" :
                InventoryFileList.append(File)
    return(InventoryFileList)


def ValidateInputFileExistanceAndSize(FileName) : #Validating Input file existence in current working directory
    if (os.path.isfile(FileName)) and (os.path.getsize(FileName) > 0) :
        return(True)
    else:
        return(False)


def findpat(fname , pat) : #List all lines from file having pat as first word
        fname=fname.strip()
        pat = pat.strip()
        result=[]
        for line in open(fname,'r') :
                line=line.strip()
                thisline=line.split(',')
                if thisline[0]==pat :
                        if thisline[1] != '' and thisline[1] != 'START' and thisline[1] != 'END' :
                                result.append(thisline)
        return(result)

       
def findhostname(ThisFileName) :
        PatList=findpat(ThisFileName,'hostname')
        return(PatList[0][1])


def BaseIP(ThisFileName) :
        PatList=findpat(ThisFileName,'prtconf')
        for line in PatList :
                if line[1].count('\tIP Address: ') > 0 :
                        S=line[1].split(sep=': ')
                        return(S[1])

        
def findLPARName(ThisFileName) :
        PatList=findpat(ThisFileName,'lparstat_-i')
        for line in PatList :
                if line[1].count('Partition Name                             :') > 0 :
                        S=line[1].split(sep=' : ')
                        return(S[1])


def findLPARNo(ThisFileName) :
        PatList=findpat(ThisFileName,'lparstat_-i')
        for line in PatList :
                if line[1].count('Partition Number                           :') > 0 :
                        S=line[1].split(sep=' : ')
                        return(S[1])


def findMTM(ThisFileName) :
        PatList=findpat(ThisFileName,'prtconf')
        return(PatList[0][2])


def findSN(ThisFileName) :
        PatList=findpat(ThisFileName,'prtconf')
        S=(PatList[1][1]).split(':')
        return((S[1]).strip())


def findGen(ThisFileName) :
        PatList=findpat(ThisFileName,'prtconf')
        for line in PatList :
                if line[1].count('Processor Type: ') > 0 :
                        S=line[1].split(sep=': ')
                        return(S[1])
                    
def findClockSpeed(ThisFileName) :
        PatList=findpat(ThisFileName,'prtconf')
        S=(PatList[6][1]).split(':')
        return(((S[1]).split())[0].strip())

def findFW(ThisFileName) :
    PatList=findpat(ThisFileName,'prtconf')
    for line in PatList :
        if line[1].count('Platform Firmware level: ') > 0 :
            S=line[1].split(sep=': ')
            return(S[1])

def findConsoleIP(ThisFileName) :
        PatList=findpat(ThisFileName,'lsrsrc_-l_IBM.MCP')
        for line in PatList :
                if line[1].count('\tIPAddresses       = ') > 0 :
                        S=line[1].split(sep=' = ')
                        return((S[1].split('"'))[1])

def findProcs(ThisFileName) :
        PatList=findpat(ThisFileName,'lparstat_-i')
        for line in PatList :
                if line[1].count('Entitled Capacity                          :') > 0 :
                        S=line[1].split(sep=' : ')
                        return(S[1])


def findmem(ThisFileName) :
        PatList=findpat(ThisFileName,'lparstat_-i')
        for line in PatList :
                if line[1].count('Online Memory                              :') > 0 :
                        S=line[1].split(sep=' : ')
                        M=int(((S[1]).split())[0].strip())
                        return(M/1024)


def findOSLevel(ThisFileName) :
    PatList=findpat(ThisFileName,'oslevel_-s')
    return(PatList[0][1])


def finddate(ThisFileName) :
       PatList=findpat(ThisFileName,'date')
       S=PatList[0][1].split()
       return("-".join([S[2],S[1],S[5]]))

    
def ProcessListFile(InventoryFileList) :
    Inv = []
    Inv.append(['Hostname', 'BaseIP', 'ProcessingUnits', 'Memory(GB)', 'OSLevel', 'LPARName', 'LPARNo', 'TypeModel', 'ServerSN', 'Generation', 'ClockSpeed(MHz)', 'Firmware', 'ConsoleIP', 'CollectonTime', 'InventoryFilename'])
    #print('\nSTART :: Inventory file processing',  end="", sep="")
    for EachFileName in InventoryFileList:
        ThisFileName = EachFileName.rstrip().strip()
        ThisFileData = []
        if ValidateInputFileExistanceAndSize(ThisFileName):
            #print("\n\tProcessing file : ", ThisFileName, end="", sep="")
            ThisFileData.append(findhostname(ThisFileName))
            ThisFileData.append(BaseIP(ThisFileName))
            ThisFileData.append(findProcs(ThisFileName))
            ThisFileData.append(findmem(ThisFileName))
            ThisFileData.append(findOSLevel(ThisFileName))
            ThisFileData.append(findLPARName(ThisFileName))
            ThisFileData.append(findLPARNo(ThisFileName))
            ThisFileData.append(findMTM(ThisFileName))
            ThisFileData.append(findSN(ThisFileName))
            ThisFileData.append(findGen(ThisFileName))
            ThisFileData.append(findClockSpeed(ThisFileName))
            ThisFileData.append(findFW(ThisFileName))
            ThisFileData.append(findConsoleIP(ThisFileName))
            ThisFileData.append(finddate(ThisFileName))
            ThisFileData.append(ThisFileName)
        Inv.append(ThisFileData)
    return(Inv)


def List2CSV(Inv) :
    os.chdir(ODIR) 
    a= datetime.datetime.now()
    Prefix = str(a.day) + '_' + str(a.month) + '_' + str(a.year)
    CSVFileName = 'Inventory_' + Prefix + '.csv'
    OFH = open(CSVFileName, "w")
    for line in Inv:
        for word in line:
            print(word, end=",", sep=",", file=OFH)
        print(file=OFH) 
    OFH.close()
    return(CSVFileName)


def main():
    ToolName = os.path.basename(os.sys.argv[0])
    if ".py" in ToolName :
        ToolName = ToolName.replace(".py","")
    elif ".exe" in ToolName:
        ToolName = ToolName.replace(".exe","")

    CSVFileName = ToolName + ".csv"
    InventoryFileList = PrepareInventoryFilesList()
    Inv=ProcessListFile(InventoryFileList)
    OFileName=List2CSV(Inv)

if __name__=="__main__":
    main()
