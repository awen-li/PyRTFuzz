#!/usr/bin/python


import csv
import os
import sys, getopt
import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib as mpl
import matplotlib.font_manager as font_manager
from matplotlib.ticker import FuncFormatter


class TpNode ():
    def __init__ (self, Time, Cov, AppNum):
        self.Time  = Time
        self.Cov = Cov
        self.AppNum = AppNum


def LoadInput (File='PRTFuzz_perf.log'):
    TpNodeList = []
    with open (File, 'r') as F:
        AllLines = F.readlines()
        BaseTime = None
        for Line in AllLines:
            Items = ' '.join(Line.split ()).split()
            if not Items[0].isnumeric ():
                continue
            if BaseTime == None:
                BaseTime = int(Items[0])
            Items = [(int(Items[0])-BaseTime)/3600, int (Items[1]), int (Items[2])]
            TpNodeList.append (TpNode (Items[0], Items[1], Items[2]))
    return TpNodeList

def GetCovByTimeLine (TpNodeList, TimeLine):
    CovList = {}
    for TN in TpNodeList:
        Time = int (TN.Time)
        if Time in TimeLine:
            CovList[Time] = TN.Cov

    CovList = list(CovList.values())
    while len (CovList) < len (TimeLine):
        CovList.append (CovList[-1])
    return CovList


def GetAppNumByTimeLine (TpNodeList, TimeLine):
    AnList = {}
    for TN in TpNodeList:
        Time = int (TN.Time)
        if Time in TimeLine:
            AnList[Time] = TN.AppNum
    AnList = list(AnList.values())
    while len (AnList) < len (TimeLine):
        AnList.append (AnList[-1])
    return AnList

def GetPicName (File):
    Index = File.rfind ('.')
    return File[0:Index]

def DrawRQ1 (File):
    TpNodeList = LoadInput (File)

    TimeLine = [v*4 for v in range (0, 19)]
    print (TimeLine)

    fig, (axCov, axApp) = plt.subplots(1, 2)

    # Cov over time
    X = TimeLine
    Y = GetCovByTimeLine (TpNodeList, TimeLine)
    print (Y)
    axCov.plot(X, Y, linewidth=2.0, color='red')
    #axCov.set_title('Block coverage over time', fontsize=10)
    axCov.grid(color = 'grey', linestyle = '--', linewidth = 0.5)
    axCov.set(ylabel="#Block-coverage")
    axCov.set(xlabel="Time (hour)")

    # AppNum over time
    Y = GetAppNumByTimeLine (TpNodeList, TimeLine)
    print (Y)
    axApp.plot(X, Y, linewidth=2.0, color='blue')
    #axApp.set_title('Application number over time', fontsize=10)
    axApp.grid(color = 'grey', linestyle = '--', linewidth = 0.5)
    axApp.set(ylabel="#Application")
    axApp.set(xlabel="Time (hour)")
    
    fig.set_figwidth(12)
    fig.set_figheight(4)
    
    PicName = GetPicName (File)
    plt.savefig(PicName)
    plt.close()
    
    return

def main(argv):
    Rq = ''

    try:
        opts, args = getopt.getopt(argv,"q:",["question="])
    except getopt.GetoptError:
        print ("picDraw.py -q <rq>")
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-q", "--question"):
            Rq = arg

    if Rq == '':
        print ("Rq = ", Rq, ", input invalid!!!!")
        return
    
    if Rq == 'rq1':    
        DrawRQ1 ('RQ1/GPU-cailab-FuzzResult-cpyfuzz-python3.9-48-covapp/FuzzResult/PRTFuzz_perf.log')

if __name__ == "__main__":
    main(sys.argv[1:])
    
