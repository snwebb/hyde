import yaml

def CollectFromConfig(config_location = 'test.yaml'):
    with open(config_location, 'r') as ymlfile:
        cfg = yaml.load(ymlfile)
        
    for section in cfg:
        if section == "main_analysis":
            print("Main analysis section initiated, proceeding with the categorisation.")
            for option in cfg[section]:
                if option == 'MTR':
                    print("-- Creating plots for MTR category.")
                    if 'location' in cfg[section][option]:
                        location = cfg[section][option]['location']
                    else:
                        print("Error -- no location found. Please specify the location of input dataframes")
                        sys.exit(1)
                    if 'eras' in cfg[section][option]:
                        eras =  cfg[section][option]['eras']
                    else:
                        print("Error -- no eras found. Stopping the production, please add available eras to the config.")
                        sys.exit(1)
                    if 'regions' in cfg[section][option]:
                        regions = cfg[section][option]['regions']
                    else:
                        print("Error -- no regions specified. Stopping the production, please add at least one region to the config.")
                    if 'bkg_processes' in cfg[section][option].keys():
                        bkg_processes = cfg[section][option]['bkg_processes']
                    else:
                        bkg_processes = []
                    datasets = cfg[section][option]['datasets']
                    print("--- Looking for the dataframes in : "+location)
                    print("--- Running with the following eras: ")
                    for era in eras:
                        print('    - '+str(era))
                    print("--- Processing the following regions: ")
                    print(regions)
                    print ("--- Using the following processes: ")
                    for process in bkg_processes:
                        print('    - '+bkg_processes[process]['folder_name'])
                    print("--- Using the following datasets: ")
                    print('    - '+datasets['met'])
                    print('    - '+datasets['single_ele'])

                    return [location, eras, regions, bkg_processes, datasets]



def CollectFromConfigVariables(config_location = 'test_variables.yaml'):
    with open(config_location, 'r') as ymlfile:
        cfg = yaml.load(ymlfile)
        
    variables = []

    for variable in cfg:
        log = False
        if 'log' in cfg[variable]:
            log = cfg[variable]['log']
        variables.append([cfg[variable]['file_name'], cfg[variable]['histogram_name'], cfg[variable]['histogram_label'], cfg[variable]['weight'], cfg[variable]['weight'], cfg[variable]['rebin'], cfg[variable]['set_range'][0], cfg[variable]['set_range'][1], cfg[variable]['set_ratio_range'][0], cfg[variable]['set_ratio_range'][1], log])
     
    return variables
