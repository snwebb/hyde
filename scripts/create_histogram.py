'''
Scripts to create TH1s from dataframes
'''

#Creating TH1 from input dataframe
import pandas as pd
from scripts.convert_format import *
from array import array
import ROOT
from ROOT import TCanvas, TH1F, TF1, TLegend, gPad, THStack, TColor
import math

def CreateHistogramNP_backup(df,column_name, name, label, variable='n', color=0, lumi =1, Rebin = 1):
    
    if type(color) == str:
        c1 = TColor()
        color = c1.GetColor(color)
 
            
    a = interval_from_string(df[column_name])
    nBins = len(a) - 2 #excluding under/overflow bins from plots
    
    bins = []  
    bins = a.left[1:] #excluding the underflow bin, but keeping the overflow as we want the last bin edge - which happens to be the left edge of the overflow bin
    d_bins = array('d', bins)
    

    if Rebin > 1: 
        if not(nBins % Rebin):
            print "Ok to rebin."
        else:
            print "Not ok to rebin -- using orginal binning scheme with ", nBins, " bins."
   # print nBins
   # print d_bins
    h_test = ROOT.TH1D("h_"+name,";"+label+";Events;;", nBins, d_bins)

    for i in range(1, nBins+1):
        h_test.SetBinContent(i, df[variable][i])
        if df[variable][i] > 0: 
            h_test.SetBinError(i, df[variable][i]/math.sqrt(df['n'][i]) )
        else:
            h_test.SetBinError(i, 0)
        if variable != 'n':
            h_test.SetBinContent(i, h_test.GetBinContent(i)*lumi)
            h_test.SetBinError(i,h_test.GetBinError(i)*lumi)        
                
    if color!=0 :
        h_test.SetFillColor(color)
        h_test.SetLineColor(color)
        
    h_test.GetXaxis().SetRangeUser(bins[0], bins[-1])
    
    return h_test




def CreateHistogramNP(df,column_name, name, label, variable='n', color=0, lumi =1, Rebin = 1):
    
    if type(color) == str:
        c1 = TColor()
        color = c1.GetColor(color)
 
            
    a = interval_from_string(df[column_name])
    nBins = len(a) - 2 #excluding under/overflow bins from plots
    
    bins = []  
    bins = a.left[1:] #excluding the underflow bin, but keeping the overflow as we want the last bin edge - which happens to be the left edge of the overflow bin
    d_bins = array('d', bins)
    
    
    Ok_to_rebin = False
    
    if Rebin > 1: 
        if not(nBins % Rebin):
    #        print "Ok to rebin."
            Ok_to_rebin = True
     #   else:
     #       print "Not ok to rebin -- using orginal binning scheme with ", nBins, " bins."

    h_test = ROOT.TH1D("h_"+name,";"+label+";Events;;", nBins, d_bins)
    
    
    if Ok_to_rebin:
        counter = 0
        value = 0
        N = 0
        
        h_test.Rebin(Rebin)
        
        for i in range(1, nBins+2): # has to go to N+1 in order to fill the last bin
            
            #print i 
            if (counter >= Rebin): 
              #  print "Bin rebinned", i/Rebin
              #  print "With value = ", value
             #   print 1.0*i/Rebin
                h_test.SetBinContent(i/Rebin, value)
                if N>0:
                    h_test.SetBinError(i/Rebin, value/math.sqrt(N))
                else:
                    h_test.SetBinError(i/Rebin, 0)
                
                if variable != 'n':
                    h_test.SetBinContent(i/Rebin, h_test.GetBinContent(i/Rebin)*lumi)
                    h_test.SetBinError(i/Rebin, h_test.GetBinError(i/Rebin)*lumi)  

                if (i < nBins+1):   
                    counter = 1
                    value = df[variable][i]
                    N = df['n'][i]
                     
                
            else:
              #  print "Counter will increase", counter 
              #  print "Value",  value
              #  print "N",  N
  
                value = value + df[variable][i]
                N = N + df['n'][i]
                counter = counter + 1                
                

                
            
        
        
    else:
    
        for i in range(1, nBins+1):
            h_test.SetBinContent(i, df[variable][i])
            if df[variable][i] > 0: 
                h_test.SetBinError(i, df[variable][i]/math.sqrt(df['n'][i]) )
            else:
                h_test.SetBinError(i, 0)
            if variable != 'n':
                h_test.SetBinContent(i, h_test.GetBinContent(i)*lumi)
                h_test.SetBinError(i,h_test.GetBinError(i)*lumi)        
                
    if color!=0 :
        h_test.SetFillColor(color)
        h_test.SetLineColor(color)
        
    h_test.GetXaxis().SetRangeUser(bins[0], bins[-1])
    
    return h_test



