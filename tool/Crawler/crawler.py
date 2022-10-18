#!/usr/bin/python


import csv
import os
import re
import requests
import sys, getopt
import pandas as pd
from time import sleep


class Crawler():
    def __init__(self, Url, Dir='.'):
    	
        self.IssueFile= Dir + "/Issues.csv"
        self.CmmtFile = Dir + "/Commits.csv"
        
        self.Username = "wangtong0908"
        self.Password = ""
        
        self.Url = Url

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

    def GrabIssues (self):
        pass

    def GrabCommits (self):
        pass

    def GrabMain (self):
        pass

def main(argv):
    Function = 'issue'

    try:
        opts, args = getopt.getopt(argv,"f:",["Function="])
    except getopt.GetoptError:
        print ("crawler.py -f <issue/commit>")
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-f", "--function"):
            Function = arg;
    
    if (Function == "issue"):
        Cl = Crawler()
        Cl.GrabIssues ()
    elif (Function == "commit"):
        Cl = Crawler()
        Cl.GrabCommits ()
    elif
        Cl = Crawler()
        
        Cl.GrabIssues ()
        Cl.GrabCommits ()

if __name__ == "__main__":
    main(sys.argv[1:])
    
