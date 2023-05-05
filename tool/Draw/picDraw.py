#!/usr/bin/python


import re
import os
import sys, getopt
import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib as mpl
import matplotlib.font_manager as font_manager
from matplotlib.ticker import FuncFormatter
from matplotlib.pyplot import MultipleLocator


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
                BaseTime = None
                continue
            if BaseTime == None:
                BaseTime = int(Items[0])
            Items = [(int(Items[0])-BaseTime)/3600, int (Items[1]), int (Items[2])]
            TpNodeList.append (TpNode (Items[0], Items[1], Items[2]))
    return TpNodeList

def GetAllLogs (DirName):
    LogFiles = []

    DirList = []
    DirList.append (DirName)

    while len (DirList) != 0:
        DirName = DirList.pop (0)
        FileList = os.listdir (DirName)
        for file in FileList:
            Path = os.path.join (DirName, file)
            if os.path.isdir (Path):
                DirList.append (Path)
                continue

            if Path.find ("PRTFuzz_perf.log") != -1:
                LogFiles.append (Path)

    return LogFiles

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

def StdCompute (TimeLine, Covs, Apps):
    Y = []
    Y.append(0)
    for I in range (1, len (TimeLine)):
        if Apps[I] == Apps[I-1]:
            Y.append (Y[-1])
            continue
        Y.append ((Covs[I]-Covs[I-1])/(Apps[I]-Apps[I-1]))
    Y[0] = Y [1]
    return Y

def SetLabelFrontSize (ax, size, tksize=10):
    ax.yaxis.label.set_size(size)
    ax.xaxis.label.set_size(size)
    ax.xaxis.set_tick_params(labelsize=tksize)
    ax.yaxis.set_tick_params(labelsize=tksize)

def SetYLabelColor (ax, c):
    ax.tick_params(axis='y', colors=c)
    ax.yaxis.label.set_color(c)

def SetYLabelRight (ax):
    ax.yaxis.tick_right()
    ax.yaxis.set_label_position("right")

def DrawRQ1 (Dir):
    print ("### RQ1: drawing Cov/AppNum over time line....")
    File = GetAllLogs (Dir)[0]
    TpNodeList = LoadInput (File)

    TimeLine = [v*8 for v in range (0, 16)]
    fig, (axCov, axStd) = plt.subplots(1, 2)

    # Cov over time and AppNum over time
    X = TimeLine
    print (X)

    Y = Covs = GetCovByTimeLine (TpNodeList, TimeLine)
    axCov.plot(X, Y, linewidth=2.0, color='black')
    #axCov.set_title('Block coverage over time', fontsize=10)
    axCov.grid(color = 'grey', linestyle = '--', linewidth = 0.5)
    axCov.set(ylabel="Number of basic blocks")
    #axCov.set(xlabel="Time (hour)")
    SetLabelFrontSize (axCov, 14)

    axApp = axCov.twinx()
    Y = Apps = GetAppNumByTimeLine (TpNodeList, TimeLine)
    axApp.plot(X, Y, linewidth=2.0, color='g')
    axApp.set(ylabel="Number of applications")
    #axApp.get_yticklabels()[0].set_color ('g')
    SetYLabelColor (axApp, 'g')
    SetLabelFrontSize (axApp, 14)


    # Cov/AppNum over time
    Y = StdCompute (TimeLine, Covs, Apps)
    print (Y)
    axStd.plot(X, Y, linewidth=2.0, color='black')
    axStd.grid(color = 'grey', linestyle = '--', linewidth = 0.5)
    axStd.set(ylabel="Per APP basic-block change / 8h")
    #axStd.set(xlabel="Time (hour)")
    SetYLabelRight (axStd)
    SetLabelFrontSize (axStd, 14)

    axStd.text(-48, -0.2, "Time (hour)", fontsize=14)

    
    fig.set_figwidth(8)
    fig.set_figheight(4)

    plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=0.3, hspace=None)
    plt.savefig(Dir+'/PIC_RQ1', bbox_inches='tight', pad_inches=0, dpi=300)
    plt.close()
    return

def LoadRQ2Data (File):
    DList = {}
    with open (File, 'r') as F:
        AllLines = F.readlines()
        for Line in AllLines:
            Items = ' '.join(Line.split ()).split()
            if not Items[0].isnumeric ():
                continue
            DList[Items[0]] = Items
    return DList

def GetOverComplexity (DList, Index):
    Data = []
    for compl, item in DList.items ():
        Data.append (item[Index])
    return Data

def DrawRQ2 (Dir):
    print ("### RQ2: drawing line of SSGEN.")
    DList = LoadRQ2Data (Dir+'/data.txt')

    XLabels = list (DList.keys())
    fig, (axTimes, axCodeSize) = plt.subplots(1, 2)

    # SS-gen
    SSTimes = GetOverComplexity (DList, 1)
    SSMems  = GetOverComplexity (DList, 2)

    # PY-gen
    PYTimes = GetOverComplexity (DList, 3)
    print (PYTimes)
    PYMems  = GetOverComplexity (DList, 4)
    PYSize  = GetOverComplexity (DList, 5)

    # Times & Memories
    X = XLabels
    axTimes.plot(X, SSTimes, linewidth=2.0, linestyle = '--', color='k', label='specification:time')
    axTimes.plot(X, PYTimes, linewidth=2.0, color='k', label='python:time')
    #axTimes.scatter (X, PYTimes, color='k')
    axTimes.grid(color = 'grey', linestyle = '--', linewidth = 0.5)
    axTimes.set(ylabel="Time cost (s)")
    #axTimes.set(xlabel="Specification size")
    axTimes.set_xticklabels(X, rotation=45)
    #axTimes.set_ylim ([0, 2750])
    axTimes.legend(bbox_to_anchor=(0.01, 0.99), loc="upper left", prop={"size": 12})
    SetLabelFrontSize (axTimes, 16, 12)
    axTimes.get_yticklabels()[9].set_color ('r')
    axTimes.get_xticklabels()[5].set_color ('r')

    axMems = axTimes.twinx()
    axMems.plot(X, SSMems, linewidth=2.0, color='g', linestyle = '--', label='specification:memory')
    axMems.plot(X, PYMems, linewidth=2.0, color='g', label='python:memory')
    #axMems.scatter (X, PYMems, color='b')
    axMems.set(ylabel="Memory usage (MB)")
    #axMems.set_ylim ([0, 300])
    axMems.legend(bbox_to_anchor=(0.01, 0.89), loc="upper left", prop={"size": 12})
    SetYLabelColor (axMems, 'g')
    SetLabelFrontSize (axMems, 16, 12)

    # Code size
    X = XLabels
    axCodeSize.plot(X, PYSize, linewidth=2.0, color='k')
    axCodeSize.grid(color = 'grey', linestyle = '--', linewidth = 0.5)
    axCodeSize.set(ylabel="Python code size (KLoC)")
    #axCodeSize.set(xlabel="Specification size")
    axCodeSize.set_xticklabels(X, rotation=45)
    SetLabelFrontSize (axCodeSize, 16, 12)
    SetYLabelRight (axCodeSize)
    axCodeSize.get_yticklabels()[5].set_color ('r')
    axCodeSize.get_xticklabels()[5].set_color ('r')

    axCodeSize.text(-2.5, -1.35, "Specification size", fontsize=16)

    fig.set_figwidth(12)
    fig.set_figheight(6)
    
    plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=0.25, hspace=None)
    plt.savefig(Dir+'/PIC_RQ2', bbox_inches='tight', pad_inches=0, dpi=300)
    plt.close()
    return

def DrawRQ3_1 (Dir):
    print ("### RQ3.1: drawing Cov/AppNum over time line with diff APP specifications....")

    TimeLine = [v*8 for v in range (0, 16)]
    fig, (axCov, axApp, axStd) = plt.subplots(1, 3)

    LineType = {'1':'-', '4':'-', '16':'-', '64':'-', '128':':', '256':':', '512':':', '1024':':'}
    ColorType = {'1':'k', '4':'g', '16':'r', '64':'b', '128':'k', '256':'g', '512':'r', '1024':'b'}

    AllLogs = GetAllLogs (Dir)
    AllLogs.sort ()
    for Log in AllLogs:
        Complexity = re.findall(r"-complex-(\d+?)/", Log)[0]
        LT = LineType[Complexity]
        CL = ColorType[Complexity]
        TpNodeList = LoadInput (Log)
        
        # Cov over time
        X = TimeLine
        Y = Covs = GetCovByTimeLine (TpNodeList, TimeLine)
        axCov.plot(X, Y, linewidth=2.0, color=CL, linestyle=LT, label='spec-' + str(Complexity))
        axCov.grid(color = 'grey', linestyle = '--', linewidth = 0.5)
        axCov.set(ylabel="Number of basic blocks")
        #axCov.set(xlabel="Time (hour)")
        axCov.legend(loc="upper left", prop={"size": 8})

        # AppNum over time
        Y = Apps = GetAppNumByTimeLine (TpNodeList, TimeLine)
        axApp.plot(X, Y, linewidth=2.0, color=CL, linestyle=LT, label='spec-' + str(Complexity))
        axApp.set(ylabel="Number of applications")
        axApp.legend(loc="upper left", prop={"size": 8})
        axApp.set(xlabel="Time (hour)")

        Y = StdCompute (TimeLine, Covs, Apps)
        axStd.plot(X, Y, linewidth=2.0, color=CL, linestyle=LT, label='spec-' + str(Complexity))
        axStd.grid(color = 'grey', linestyle = '--', linewidth = 0.5)
        axStd.set(ylabel="Per APP basic-block change / 8h")
        #axStd.set(xlabel="Time (hour)")
        axStd.legend(loc="upper left", prop={"size": 8})

    fig.set_figwidth(13)
    fig.set_figheight(4)

    plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=0.25, hspace=None)
    plt.savefig(Dir+'/PIC_RQ3-1_spec', bbox_inches='tight', pad_inches=0.01, dpi=300)
    plt.close()

def DrawRQ3_2 (Dir):
    print ("### RQ3.2: drawing Cov/AppNum over time line with diff Lv2Budget....")

    TimeLine = [v*8 for v in range (0, 16)]
    fig, (axCov, axApp, axStd) = plt.subplots(1, 3)

    LineType = {'10':'-', '30':'-', '60':'-', '90':'-', '180':':', '360':':'}
    ColorType = {'10':'k', '30':'g', '60':'b', '90':'b', '180':'g', '360':'b'}

    AllLogs = GetAllLogs (Dir)
    AllLogs.sort()
    for Log in AllLogs:
        print (Log)
        Budget = re.findall(r"-Budget-(\d+?)/", Log)[0]
        if not Budget in ['10', '90', '180', '360']:
            continue
        LT = LineType[Budget]
        CL = ColorType[Budget]

        TpNodeList = LoadInput (Log)
        
        # Cov over time
        X = TimeLine
        Y = Covs = GetCovByTimeLine (TpNodeList, TimeLine)
        axCov.plot(X, Y, linewidth=2.0, color=CL, linestyle=LT, label='budget-' + str(Budget))
        #axCov.set_title('Block coverage over time', fontsize=10)
        axCov.grid(color = 'grey', linestyle = '--', linewidth = 0.5)
        axCov.set(ylabel="Number of basic blocks")
        #axCov.set(xlabel="Time (hour)")
        axCov.legend(loc="lower right", prop={"size": 8})

        # AppNum over time
        Y = Apps = GetAppNumByTimeLine (TpNodeList, TimeLine)
        axApp.plot(X, Y, linewidth=2.0, color=CL, linestyle=LT, label='budget-' + str(Budget))
        #axApp.set_title('Application number over time', fontsize=10)
        axApp.grid(color = 'grey', linestyle = '--', linewidth = 0.5)
        axApp.set(ylabel="Number of applications")
        axApp.set(xlabel="Time (hour)")
        axApp.legend(loc="upper left", prop={"size": 8})

        Y = StdCompute (TimeLine, Covs, Apps)
        axStd.plot(X, Y, linewidth=2.0, color=CL, linestyle=LT, label='budget-' + str(Budget))
        axStd.grid(color = 'grey', linestyle = '--', linewidth = 0.5)
        axStd.set(ylabel="Per APP basic-block change / 8h")
        #axStd.set(xlabel="Time (hour)")
        axStd.legend(loc="upper right", prop={"size": 8})

    fig.set_figwidth(16)
    fig.set_figheight(4)
    
    plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=0.25, hspace=None)
    plt.savefig(Dir+'/PIC_RQ3-2_Lv2Budget', bbox_inches='tight', pad_inches=0.01, dpi=300)
    plt.close()

def DrawRQ3_3 (Dir):
    print ("### RQ3.3: drawing Cov/AppNum over time line with typed/untyped....")

    TimeLine = [v*8 for v in range (0, 16)]
    fig, (axCov, axStd) = plt.subplots(1, 2)
    axApp = axCov.twinx()

    LineType = {'typed':'-', 'untyped':'--'}
    ColorType = {'typed':'k', 'untyped':'g'}

    AllLogs = GetAllLogs (Dir)
    for Log in AllLogs:
        Type = 'typed'
        if Log.find ("untyped") != -1:
            Type = 'untyped'
        
        LT = LineType[Type]
        CL = ColorType[Type]

        TpNodeList = LoadInput (Log)
        
        # Cov over time
        X = TimeLine
        Y = Covs = GetCovByTimeLine (TpNodeList, TimeLine)
        axCov.plot(X, Y, linewidth=2.0, color='k', linestyle=LT, label=Type)
        #axCov.set_title('Block coverage over time', fontsize=10)
        axCov.grid(color = 'grey', linestyle = '--', linewidth = 0.5)
        axCov.set(ylabel="Number of basic blocks")
        #axCov.set(xlabel="Time (hour)")
        axCov.legend(bbox_to_anchor=(0.01, 0.99), loc="upper left", prop={"size": 8})
        SetLabelFrontSize (axCov, 16, 12)

        # AppNum over time
        Y = Apps = GetAppNumByTimeLine (TpNodeList, TimeLine)
        axApp.plot(X, Y, linewidth=2.0, color='g', linestyle=LT, label=Type)
        #axApp.grid(color = 'grey', linestyle = '--', linewidth = 0.5)
        axApp.set(ylabel="Number of applications")
        axApp.legend(bbox_to_anchor=(0.01, 0.88), loc="upper left", prop={"size": 8})
        SetYLabelColor (axApp, 'g')
        SetLabelFrontSize (axApp, 16, 12)

        Y = StdCompute (TimeLine, Covs, Apps)
        axStd.plot(X, Y, linewidth=2.0, color='k', linestyle=LT, label=Type)
        axStd.grid(color = 'grey', linestyle = '--', linewidth = 0.5)
        axStd.set(ylabel="Per APP basic-block change / 8h")
        axStd.set(xlabel="   ")
        SetYLabelRight (axStd)
        axStd.legend(loc="upper left", prop={"size": 8})
        SetLabelFrontSize (axStd, 16, 12)

        axStd.text(-44, -5, "Time (hour)", fontsize=16)

    fig.set_figwidth(10)
    fig.set_figheight(4)
    
    plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=0.25, hspace=None)
    plt.savefig(Dir+'/PIC_RQ3-3_Typed', bbox_inches='tight', pad_inches=0.01, dpi=300)
    plt.close()

def LoadFstl (path):
    Year2BugNum = {}
    with open (path, 'r') as F:
        AllLines = F.readlines()
        for Line in AllLines:
            Items = ' '.join(Line.split ()).split()
            if len (Items) == 0:
                continue
            Year2BugNum[Items[0]] = int (Items[1])
    Year2BugNum = dict(sorted (Year2BugNum.items()))
    return Year2BugNum

def LoadFstd (path):
    Md2BugNum = {}
    with open (path, 'r') as F:
        AllLines = F.readlines()
        for Line in AllLines:
            Items = ' '.join(Line.split ()).split()
            if len (Items) == 0:
                continue
            Md2BugNum[Items[0]] = int(Items[1])
    
    Md2BugNum = dict(sorted (Md2BugNum.items(), key=lambda x:x[1], reverse=True))
    return Md2BugNum

def DrawIssueStat (Dir):
    print ("### IssueStat: drawing stat of issues in CPython....")

    FSTL = Dir + '/StatByTimeLine.txt'
    FSTD = Dir + '/StatByDist.txt'

    Year2BugNum = LoadFstl (FSTL)
    Md2BugNum = LoadFstd (FSTD)

    # bugs over timeline
    TimeLine = list (Year2BugNum.keys())
    TimeLine = TimeLine[2::2]
    fig, ax = plt.subplots(1, 1)

    X = TimeLine
    print (X)
    Y = list (Year2BugNum.values())
    Y = Y[2::2]
    plt.ylim([1, 2000])
    plt.plot(X, Y, color='k')
    plt.xticks(['2002', ' ', '2006', ' ', '2010', ' ', '2014', ' ', '2018', ' ', '2022'])
    plt.grid(color = 'grey', linestyle = '--', linewidth = 0.5)
    plt.ylabel('#Bug')

    fig.set_figwidth(6)
    fig.set_figheight(3)  
    plt.savefig(Dir+'/StatByTimeLine', dpi=300)
    plt.close()

    # bugs by modules
    fig, ax = plt.subplots(1, 1)
    X = list (Md2BugNum.keys())[0:15]
    X = ['code', 'imp', 'string', 'dis', ' ', 'ssl', 'stat', 'socket', 'types', 'urllib', 'http', 'asyncio', 'email', 'ast', 'distutils']
    Y = list (Md2BugNum.values())[0:15]

    y_locator=MultipleLocator(500)
    ax.yaxis.set_major_locator(y_locator)
    ax.set_ylim ([0, 1500])
    
    ax.bar(X, Y, color='grey')
    print (X)
    ax.grid(color = 'grey', linestyle = '--', linewidth = 0.5)
    ax.set(ylabel="#Bug")
    ax.set_xticklabels(X, rotation=30)

    #plt.setp(ax.get_xticklabels(), rotation=30)
    

    fig.set_figwidth(8)
    fig.set_figheight(5)  
    plt.savefig(Dir+'/StatByDist', dpi=300) 
    plt.close()

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
    
    if Rq == 'rq1' or Rq == 'all':    
        DrawRQ1 ('RQ1')

    if Rq == 'rq2' or Rq == 'all':    
        DrawRQ2 ('RQ2')

    if Rq == 'rq3.1' or Rq == 'all':    
        DrawRQ3_1 ('RQ3.1')

    if Rq == 'rq3.2' or Rq == 'all':    
        DrawRQ3_2 ('RQ3.2')

    if Rq == 'rq3.3' or Rq == 'all':    
        DrawRQ3_3 ('RQ3.3')

    if Rq == 'stat' or Rq == 'all':
        DrawIssueStat ('../Crawler')

if __name__ == "__main__":
    main(sys.argv[1:])
    
