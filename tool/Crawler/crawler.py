#!/usr/bin/python


import csv
import os
import re
import requests
import sys, getopt
import pandas as pd
from time import sleep


class Issue():
    def __init__(self, ID, Status, Title, Label, SecLabel, Url, PatchUrl):
        self.ID = ID
        self.Title    = Title
        self.Status   = Status  
        self.Label    = Label
        self.SecLabel = SecLabel
        self.Url      = Url
        self.PatchUrl = PatchUrl
        
    def AppendWrite (self, FileName):
        IsNew = False
        if not os.path.exists (FileName):
            IsNew = True
        
        with open(FileName, 'a+', encoding='utf-8') as CsvFile:
            writer = csv.writer(CsvFile)      
            if IsNew == True:
                Header = ['ID', 'Status', 'Title', 'Label', 'Security-Label', 'Url', 'PatchUrl']
                writer.writerow(Header)
            Row = [self.ID, self.Status, self.Title, self.Label, self.SecLabel, self.Url, self.PatchUrl]
            writer.writerow(Row)


class Crawler():
    def __init__(self, Url, Dir='.'):

        self.IssueFile= Dir + "/Issues.csv"
        self.CmmtFile = Dir + "/Commits.csv"
        
        self.Username = "Daybreak2019"
        self.Password = ""
        
        self.Url = Url

        self.IssueMap = {}
        self.CmmtMap  = {}


    def LoadIssues (self):
        df = pd.read_csv(self.IssueFile)
        for index, row in df.iterrows():
            self.IssueMap ['ID'] = True

    def HttpCall(self, Url):
        Result = requests.get(Url,
                              auth=(self.Username, self.Password),
                              headers={"Accept": "application/vnd.github.mercy-preview+json"})
        if (Result.status_code != 200 and Result.status_code != 422):
            print("Status Code %s: %s, URL: %s" % (Result.status_code, Result.reason, Url))
            sleep(300)
            return self.HttpCall(Url)
        return Result.json()

    def Save (self):
        Header = ['commit', 'URL', 'Issue', 'tag']
        with open(self.FileName, 'w', encoding='utf-8') as CsvFile:       
            writer = csv.writer(CsvFile)
            writer.writerow(Header)  
            for Id, Repo in self.RepoList.items():
                row = [Repo.Id, Repo.Star, Repo.Langs, Repo.ApiUrl, Repo.CloneUrl, Repo.Descripe]
                writer.writerow(row)
        return

    def Appendix (self, Repo):
        IsNew = False
        if not os.path.exists (self.FileName):
            IsNew = True
        
        with open(self.FileName, 'a+', encoding='utf-8') as CsvFile:
            writer = csv.writer(CsvFile)      
            if IsNew == True:
                Header = ['id', 'Star', 'Languages', 'ApiUrl', 'CloneUrl', 'Description']
                writer.writerow(Header)
            Row = [Repo.Id, Repo.Star, Repo.Langs, Repo.ApiUrl, Repo.CloneUrl, Repo.Descripe]
            writer.writerow(Row)
        return

    def GetSecLabel (self, Label, Title, Description):
        
        Keywords = ['leak', 'slow', 'infinite', 'oom', 'out-of-memory', 'assertion', 'assert', 'overflow', 'deadlock', 'permission', 'crash', 'performance',
                    'hang', 'segmentation', 'endless', 'unhandled exception']

        Context = (Title + Description).lower()
        for key in Keywords:
            if Context.find (key) != -1:
                return key

        if Label.find ('security') != -1:
            return 'security'
        
        return ' '

    def GrabIssues (self):

        IssueStates = ['open', 'closed']
        for status in IssueStates:
    
            # trying to get issue lists
            pageNum = 0
            while True:
                Url = self.Url + "/issues?" + "per_page=100&page=" + str(pageNum) + "&state=" + status
                Result = self.HttpCall (Url)
                if (len (Result) == 0):
                    break

                print ("[%d] retrieve issue = %d" %(pageNum, len (Result)))
                pageNum += 1
                
                # iterate the list
                for issue in Result:
                    ID = issue['number']
                    if self.IssueMap.get (ID) != None:
                        continue
                    self.IssueMap[ID] = True
                    
                    Label  = ''
                    Description = ''
                    Labels = issue['labels']
                    for i in range (0, len (Labels)):
                        if Label != '':
                            Label += ','

                        CurLabel = Labels[i]
                        Label += CurLabel['name']

                        if CurLabel['description'] != None:
                            Description += CurLabel['description']

                    if Label.find ('bug') == -1 and Label.find ('security') == -1:
                        continue

                    Title = issue['title']
                    SecLabel = self.GetSecLabel (Label, Title, Description)

                    # get pullrequest
                    PatchUrl = ' '
                    if 'pull_request' in issue:
                        PullReq = issue['pull_request']
                        PatchUrl = PullReq['patch_url']
                        
                    curIssue = Issue(ID, issue['state'], Title, Label, SecLabel, issue['url'], PatchUrl)
                    curIssue.AppendWrite (self.IssueFile)

    def GrabCommits (self):
        pass

    def GrabMain (self):
        pass

def main(argv):
    Function   = 'issue'
    DefaultUrl = 'https://api.github.com/repos/python/cpython'

    try:
        opts, args = getopt.getopt(argv,"f:",["Function="])
    except getopt.GetoptError:
        print ("crawler.py -f <issue/commit>")
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-f", "--function"):
            Function = arg;
    
    if (Function == "issue"):
        Cl = Crawler(DefaultUrl)
        Cl.GrabIssues ()
    elif (Function == "commit"):
        Cl = Crawler(DefaultUrl)
        Cl.GrabCommits ()
    else:
        Cl = Crawler(DefaultUrl)
        
        Cl.GrabIssues ()
        Cl.GrabCommits ()

if __name__ == "__main__":
    main(sys.argv[1:])
    
