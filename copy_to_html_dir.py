import os
from datetime import datetime

#Edit this string to point to your output dir

web_folder = '/eos/user/v/vmilosev/www/'
input_folder = '/eos/user/v/vmilosev/SWAN_projects/Hinv-Plotting/work_200303/'


today = datetime.now()
#Production_title = 'Production_'+today.strftime("%b_%d_%Y_%H%M%S")
Production_title = 'Production_'+today.strftime("%b_%d_%Y")
output_location = web_folder + Production_title

Regions = ['Zmumu', 'Zee', 'Wmunu', 'Wenu', 'SR']
Categories = ['MTR', 'VTR']
Eras = ['2017', '2018']

print('Processin location: ' + input_folder)
print('-- Copying files to :' + output_location)

os.system('mkdir ' +  output_location)
os.system('cp index.php ' + output_location)

for era in Eras:
    for category in Categories:
        os.system('mkdir '+output_location+'/'+category+'_'+era)
        os.system('cp -r '+input_folder+'test_VBF_'+era+'_'+category+'_testing/Plots/*  '+ output_location+'/'+category+'_'+era+'/')
        os.system('cp index.php '+output_location+'/'+category+'_'+era+'/')
        for region in Regions:
            os.system('cp index.php '+output_location+'/'+category+'_'+era+'/'+region+'/')
