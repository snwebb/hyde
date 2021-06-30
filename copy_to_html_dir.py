import os
from datetime import datetime

#Edit this string to point to your output dir
web_folder = '~/public_html/Production/'

var = ''
var = '20210630-UL-ElTrigSFs_VTRTrig'
input_folder = '/vols/cms/VBFHinv/'+var + '/'

#input_folder = '/home/hep/snwebb/invisible/Nick/analysis/'


today = datetime.now()
#Production_title = 'Production_'+today.strftime("%b_%d_%Y_%H%M%S")
#Production_title = 'Production_'+today.strftime("%b_%d_%Y")
Production_title = 'Production_'+today.strftime("%Y_%m_%d"+"_" + var)
output_location = web_folder + Production_title

Regions = ['Zmumu', 'Zee', 'Wmunu', 'Wenu', 'SR', 'QCDCR', "HFNoise"]
Categories = ['MTR', 'VTR']
Eras = ['2017', '2018']

print('Processing location: ' + input_folder)
print('-- Copying files to :' + output_location)

os.system('mkdir ' +  output_location)
os.system('cp index.php ' + output_location)

for era in Eras:
    for category in Categories:
        os.system('mkdir '+output_location+'/'+category+'_'+era)
        os.system('cp -r '+input_folder+'test_VBF_'+era+'_'+category+'_testing/Plots/*  '+ output_location+'/'+category+'_'+era+'/')
        os.system('cp index.php '+output_location+'/'+category+'_'+era+'/')
        for region in Regions:
            os.system('cp html/index_'+region+'_'+era+'_'+category+'.html ' + output_location + '/' +category+'_'+era+'/'+region+'/index.html')
            os.system('cp index.php '+output_location+'/'+category+'_'+era+'/'+region+'/')
