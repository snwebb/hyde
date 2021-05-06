import os

#location = '..//'
location = '/vols/cms/VBFHinv/20210324-V7-LeadEta2p9/'

MTR_SR_plots = [
'MetNoMu',
'leadingJet_mjj',
'leading_dEtajj',
'leading_dPhijj',
'MetNoLep_CleanJet_mindPhi',
'CentralEtaMTR',
'ForwardEtaMTR',
'Leading_jet_eta',
'Leading_jet_pt',
'Subleading_jet_eta',
'Subleading_jet_pt',
]

MTR_QCDCR_plots = [
'MetNoMu',
'leadingJet_mjj',
'leading_dEtajj',
'leading_dPhijj',
'MetNoLep_CleanJet_mindPhi',
'CentralEtaMTR',
'ForwardEtaMTR',
'Leading_jet_eta',
'Leading_jet_pt',
'Subleading_jet_eta',
'Subleading_jet_pt',
]

VTR_SR_plots = [
'MetNoMu',
'lMjj', 
'lMjj_leading_dEtajj',
'lMjj_leading_dPhijj',
'MetNoLep_CleanJet_mindPhi',
'CentralEtaVTR',
'ForwardEtaVTR',
'lMjj_Leading_jet_eta',
'lMjj_Leading_jet_pt',
'lMjj_Subleading_jet_eta',
'lMjj_Subleading_jet_pt',
]

VTR_QCDCR_plots = [
'MetNoMu',
'lMjj', 
'lMjj_leading_dEtajj',
'lMjj_leading_dPhijj',
'MetNoLep_CleanJet_mindPhi',
'CentralEtaVTR',
'ForwardEtaVTR',
'lMjj_Leading_jet_eta',
'lMjj_Leading_jet_pt',
'lMjj_Subleading_jet_eta',
'lMjj_Subleading_jet_pt',
]

MTR_Wmunu_plots = [
'MetNoMu',
'leadingJet_mjj', 
'leading_dEtajj',
'leading_dPhijj',
'MTmu_FAST',
'Leading_muon_pt',
'Leading_muon_eta',
'MetNoLep_CleanJet_mindPhi',
]

VTR_Wmunu_plots = [
'MetNoMu',
'lMjj', 
'lMjj_leading_dEtajj',
'lMjj_leading_dPhijj',
'MTmu_FAST',
'Leading_muon_pt',
'Leading_muon_eta',
'MetNoLep_CleanJet_mindPhi',
]


MTR_Wenu_plots = [
'MetNoMu',
'leadingJet_mjj', 
'leading_dEtajj',
'leading_dPhijj',
'MTe_FAST',
'Leading_electron_pt',
'Leading_electron_eta',
'MetNoLep_CleanJet_mindPhi',
]

VTR_Wenu_plots = [
'MetNoMu',
'lMjj', 
'lMjj_leading_dEtajj',
'lMjj_leading_dPhijj',
'MTe_FAST',
'Leading_electron_pt',
'Leading_electron_eta',
'MetNoLep_CleanJet_mindPhi',
]


MTR_Zmumu_plots = [
'MetNoMu',
'leadingJet_mjj', 
'leading_dEtajj',
'leading_dPhijj',
'Leading_muon_pt',
'Leading_muon_eta',
'diMuon_mass',
'MetNoLep_CleanJet_mindPhi',
]


VTR_Zmumu_plots = [
'MetNoMu',
'lMjj', 
'lMjj_leading_dEtajj',
'lMjj_leading_dPhijj',
'Leading_muon_pt',
'Leading_muon_eta',
'diMuon_mass',
'MetNoLep_CleanJet_mindPhi',
]

MTR_Zee_plots = [
'MetNoMu',
'leadingJet_mjj', 
'leading_dEtajj',
'leading_dPhijj',
'Leading_electron_pt',
'Leading_electron_eta',
'diElectron_mass',
'MetNoLep_CleanJet_mindPhi',
]


VTR_Zee_plots = [
'MetNoMu',
'lMjj', 
'lMjj_leading_dEtajj',
'lMjj_leading_dPhijj',
'Leading_electron_pt',
'Leading_electron_eta',
'diElectron_mass',
'MetNoLep_CleanJet_mindPhi',
]


os.system("mkdir "+location+"/AN_plots/")

os.system("mkdir "+location+"/AN_plots/2017_MTR")
os.system("mkdir "+location+"/AN_plots/2017_MTR/Zmumu")
os.system("mkdir "+location+"/AN_plots/2017_MTR/Zee")
os.system("mkdir "+location+"/AN_plots/2017_MTR/Wmunu")
os.system("mkdir "+location+"/AN_plots/2017_MTR/Wenu")
os.system("mkdir "+location+"/AN_plots/2017_MTR/SR")
os.system("mkdir "+location+"/AN_plots/2017_MTR/QCDCR")

os.system("mkdir "+location+"/AN_plots/2018_MTR")
os.system("mkdir "+location+"/AN_plots/2018_MTR/Zmumu")
os.system("mkdir "+location+"/AN_plots/2018_MTR/Zee")
os.system("mkdir "+location+"/AN_plots/2018_MTR/Wmunu")
os.system("mkdir "+location+"/AN_plots/2018_MTR/Wenu")
os.system("mkdir "+location+"/AN_plots/2018_MTR/SR")
os.system("mkdir "+location+"/AN_plots/2018_MTR/QCDCR")

os.system("mkdir "+location+"/AN_plots/2017_VTR")
os.system("mkdir "+location+"/AN_plots/2017_VTR/Zmumu")
os.system("mkdir "+location+"/AN_plots/2017_VTR/Zee")
os.system("mkdir "+location+"/AN_plots/2017_VTR/Wmunu")
os.system("mkdir "+location+"/AN_plots/2017_VTR/Wenu")
os.system("mkdir "+location+"/AN_plots/2017_VTR/SR")
os.system("mkdir "+location+"/AN_plots/2017_VTR/QCDCR")

os.system("mkdir "+location+"/AN_plots/2018_VTR")
os.system("mkdir "+location+"/AN_plots/2018_VTR/Zmumu")
os.system("mkdir "+location+"/AN_plots/2018_VTR/Zee")
os.system("mkdir "+location+"/AN_plots/2018_VTR/Wmunu")
os.system("mkdir "+location+"/AN_plots/2018_VTR/Wenu")
os.system("mkdir "+location+"/AN_plots/2018_VTR/SR")
os.system("mkdir "+location+"/AN_plots/2018_VTR/QCDCR")


for MTR_Zmumu in MTR_Zmumu_plots:
    os.system("cp "+location+"/test_VBF_2017_MTR_testing/Plots/Zmumu/"+MTR_Zmumu+".pdf "+location+"/AN_plots/2017_MTR/Zmumu/")
    os.system("cp "+location+"/test_VBF_2018_MTR_testing/Plots/Zmumu/"+MTR_Zmumu+".pdf "+location+"/AN_plots/2018_MTR/Zmumu/")

for MTR_Zee in MTR_Zee_plots:
    os.system("cp "+location+"/test_VBF_2017_MTR_testing/Plots/Zee/"+MTR_Zee+".pdf "+location+"/AN_plots/2017_MTR/Zee/")
    os.system("cp "+location+"/test_VBF_2018_MTR_testing/Plots/Zee/"+MTR_Zee+".pdf "+location+"/AN_plots/2018_MTR/Zee/")

for MTR_Wmunu in MTR_Wmunu_plots:
    os.system("cp "+location+"/test_VBF_2017_MTR_testing/Plots/Wmunu/"+MTR_Wmunu+".pdf "+location+"/AN_plots/2017_MTR/Wmunu/")
    os.system("cp "+location+"/test_VBF_2018_MTR_testing/Plots/Wmunu/"+MTR_Wmunu+".pdf "+location+"/AN_plots/2018_MTR/Wmunu/")

for MTR_Wenu in MTR_Wenu_plots:
    os.system("cp "+location+"/test_VBF_2017_MTR_testing/Plots/Wenu/"+MTR_Wenu+".pdf "+location+"/AN_plots/2017_MTR/Wenu/")
    os.system("cp "+location+"/test_VBF_2018_MTR_testing/Plots/Wenu/"+MTR_Wenu+".pdf "+location+"/AN_plots/2018_MTR/Wenu/")

for MTR_SR in MTR_SR_plots:
    os.system("cp "+location+"/test_VBF_2017_MTR_testing/Plots/SR/"+MTR_SR+".pdf "+location+"/AN_plots/2017_MTR/SR/")
    os.system("cp "+location+"/test_VBF_2018_MTR_testing/Plots/SR/"+MTR_SR+".pdf "+location+"/AN_plots/2018_MTR/SR/")

for MTR_QCDCR in MTR_QCDCR_plots:
    os.system("cp "+location+"/test_VBF_2017_MTR_testing/Plots/QCDCR/"+MTR_QCDCR+".pdf "+location+"/AN_plots/2017_MTR/QCDCR/")
    os.system("cp "+location+"/test_VBF_2018_MTR_testing/Plots/QCDCR/"+MTR_QCDCR+".pdf "+location+"/AN_plots/2018_MTR/QCDCR/")

for VTR_Zmumu in VTR_Zmumu_plots:
    os.system("cp "+location+"/test_VBF_2017_VTR_testing/Plots/Zmumu/"+VTR_Zmumu+".pdf "+location+"/AN_plots/2017_VTR/Zmumu/")
    os.system("cp "+location+"/test_VBF_2018_VTR_testing/Plots/Zmumu/"+VTR_Zmumu+".pdf "+location+"/AN_plots/2018_VTR/Zmumu/")

for VTR_Zee in VTR_Zee_plots:
    os.system("cp "+location+"/test_VBF_2017_VTR_testing/Plots/Zee/"+VTR_Zee+".pdf "+location+"/AN_plots/2017_VTR/Zee/")
    os.system("cp "+location+"/test_VBF_2018_VTR_testing/Plots/Zee/"+VTR_Zee+".pdf "+location+"/AN_plots/2018_VTR/Zee/")

for VTR_Wmunu in VTR_Wmunu_plots:
    os.system("cp "+location+"/test_VBF_2017_VTR_testing/Plots/Wmunu/"+VTR_Wmunu+".pdf "+location+"/AN_plots/2017_VTR/Wmunu/")
    os.system("cp "+location+"/test_VBF_2018_VTR_testing/Plots/Wmunu/"+VTR_Wmunu+".pdf "+location+"/AN_plots/2018_VTR/Wmunu/")

for VTR_Wenu in VTR_Wenu_plots:
    os.system("cp "+location+"/test_VBF_2017_VTR_testing/Plots/Wenu/"+VTR_Wenu+".pdf "+location+"/AN_plots/2017_VTR/Wenu/")
    os.system("cp "+location+"/test_VBF_2018_VTR_testing/Plots/Wenu/"+VTR_Wenu+".pdf "+location+"/AN_plots/2018_VTR/Wenu/")

for VTR_SR in VTR_SR_plots:
    os.system("cp "+location+"/test_VBF_2017_VTR_testing/Plots/SR/"+VTR_SR+".pdf "+location+"/AN_plots/2017_VTR/SR/")
    os.system("cp "+location+"/test_VBF_2018_VTR_testing/Plots/SR/"+VTR_SR+".pdf "+location+"/AN_plots/2018_VTR/SR/")

for VTR_QCDCR in VTR_QCDCR_plots:
    os.system("cp "+location+"/test_VBF_2017_VTR_testing/Plots/QCDCR/"+VTR_QCDCR+".pdf "+location+"/AN_plots/2017_VTR/QCDCR/")
    os.system("cp "+location+"/test_VBF_2018_VTR_testing/Plots/QCDCR/"+VTR_QCDCR+".pdf "+location+"/AN_plots/2018_VTR/QCDCR/")


