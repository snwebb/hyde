'''
Label and plot styling.
'''

import ROOT

def Styling(region = 'Zmumu', Experiment = "CMS", Status = "Work in Progress", Lumi_label = "41.9"):
    
    label = "SR" 
    
    if region == 'Zmumu':
        label = 'Z#rightarrow #mu#mu'
    if region == 'Zee':
        label = 'Z#rightarrow ee'
    if region == 'Wmunu':
        label = 'W#rightarrow #mu#nu'
    if region == 'Wenu':
        label = 'W#rightarrow e#nu'
    if region == 'SR':
        label == 'SR'
    if region == 'QCDCR':
        label == 'QCD CR'
        
    
    tex1 = ROOT.TLatex(0.16,0.96,"CMS")
    tex1.SetNDC()
    tex1.SetTextFont(61)
    tex1.SetTextSize(0.0375)
    tex1.SetLineWidth(2)
    tex2 = ROOT.TLatex(0.23,0.96,"Work in Progress")
    tex2.SetNDC()
    tex2.SetTextFont(52)
    tex2.SetTextSize(0.0285)
    tex2.SetLineWidth(2)
    tex3 = ROOT.TLatex(0.75,0.96, label+" L = "+Lumi_label+" fb^{-1}")
    tex3.SetNDC()
    tex3.SetTextFont(52)
    tex3.SetTextSize(0.0285)
    tex3.SetLineWidth(2) 
    
    return [tex1, tex2, tex3]
