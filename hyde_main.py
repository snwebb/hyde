#import stage
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import ROOT
from ROOT import TCanvas, TH1F, TF1, TLegend, gPad, THStack, TColor
import tdrstyle
import os.path
import os
from array import array
import yaml
import sys
import math
from scripts.collect_from_config import *
from scripts.convert_format import *
from scripts.create_histogram import *
from scripts.styling import *
from scripts.plot_variables import *

class Config():
    location = 0
    eras = 1
    regions = 2
    bkg_processes = 3
    datasets = 4
    
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'    

def IntroGreeting():
    f = open('hyde_logo.txt','r')
    for line in f:
        print bcolors.BOLD+bcolors.OKGREEN+line[:-1]+bcolors.ENDC
    print bcolors.OKBLUE+"Higgs to invisible Yields and Datatframe Extractor"+bcolors.ENDC
    print bcolors.OKBLUE+"-- 2019, Vukasin Milosevic "+bcolors.ENDC


IntroGreeting()
Input = CollectFromConfig('test.yaml')

Location = Input[Config.location]
Eras = Input[Config.eras]
Regions = Input[Config.regions]
Bkg_processes = Input[Config.bkg_processes]
Datasets = Input[Config.datasets]


variables = CollectFromConfigVairables('test_variables.yaml')
#print variables

'''
Plotting stage for the MTR category
'''

categories = ['MTR']
Lumi_label = Eras[2018]['lumi_for_label']
Lumi = Eras[2018]['lumi']

ROOT.gROOT.SetBatch()

for category in categories:
    print bcolors.OKBLUE+"Processing "+bcolors.ENDC+bcolors.OKGREEN+category+bcolors.ENDC
    location = Location+ "test_VBF_2018_"+category+"_testing/"
    Output_dir = location+"/Plots"
    os.system("mkdir "+Output_dir)

    for region in Regions:
        print bcolors.OKBLUE+"--Region: "+bcolors.ENDC+bcolors.OKGREEN+region+bcolors.ENDC
        output_dir =  Output_dir+ "/"+region
        os.system("mkdir "+output_dir)
        for variable in variables:
            print bcolors.OKGREEN+"----Processing: ", variable[0]+bcolors.ENDC
            if ("We" in region) or ("Zee" in region):
                dataset_name = Datasets['single_ele']
            else:
                dataset_name = Datasets['met']        
            test = PlotVariables(output_dir, dataset_name, variable, weight_names, region, location, Bkg_processes, Lumi, Lumi_label)
 
