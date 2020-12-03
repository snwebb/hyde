'''
Main plotting procedure.
'''
import pandas as pd
from scripts.create_histogram import *
import ROOT
from ROOT import TCanvas, TH1F, TF1, TLegend, gPad, THStack, TColor
from scripts.styling import *
import math

class Properties():
    Name = 0
    HistName = 1
    AxisLabels = 2
    Weight = 3
    WeightError = 4
    Rebin = 5
    Axis_low = 6
    Axis_high = 7
    Ratio_Axis_low = 8
    Ratio_Axis_high = 9


groupBy = False

weight_names = ''
weight = 'weight_nominal::sumw'

def PlotVariables(output_dir, dataset_name, variable, weight_names, region, Location, Bkg_processes, Lumi, Lumi_label, category, LOG = False):
    
    
        bkg_names = []
        label_names = []
        for Bkg_process in Bkg_processes:
            if Bkg_process == 9:
                continue
            bkg_names.append(Bkg_processes[Bkg_process]['folder_name'])
            label_names.append([Bkg_processes[Bkg_process]['folder_name'], Bkg_processes[Bkg_process]['latex_name'], Bkg_processes[Bkg_process]['color'], 0])
       
        signal_name = [Bkg_processes[9]['folder_name']]  

        
        Scaling = False
        ScalingQCDCR = True

        #LOG = False
        
        
        c = []
        p1 = []
        p2 = []

        plot_count = 0

        data_hist = []
        data_for_ratio = []
        bkg_for_ratio = []
        signal_hist = []
        bkg_stack = []
        legend = []
        tex1 = []
        tex2 = []
        tex3 = []
        printing = False

        prefix = Location+"output_"+region+"_sh/"
        mc_prefix = prefix
        


        DATA = pd.read_csv(prefix+'/'+dataset_name+'/tbl_'+variable[Properties.Name]+weight_names+'.csv',comment='#')
        tmp1_name, tmp2 = variable[Properties.Name].split('--')


        data_hist.append(CreateHistogramNP(DATA, tmp1_name ,variable[Properties.HistName]+"_data",variable[Properties.AxisLabels],'n', 1, 1, variable[Properties.Rebin]))
        data_for_ratio.append(data_hist[plot_count].Clone())
        bkg_stack.append(THStack("Background","Full_Background"))
        if printing:
            print("Data", data_hist[plot_count].Integral())


        if ('W' in region) or ('Z' in region) or ('SR' in region) and not ("mindphi" in variable[Properties.Name].lower()):
            legend_args = (0.7, 0.55, 0.95, 0.91, '', 'NDC')
        else:
            legend_args = (0.18, 0.55, 0.55, 0.91, '', 'NDC') 

        if 'mindPhi' in variable[0] or ('electron' in variable[Properties.Name].lower() and 'phi' in variable[Properties.Name].lower()):
            legend_args = (0.18, 0.55, 0.55, 0.91, '', 'NDC') 

        if "QCDCR" in region:
            legend_args = (0.18, 0.65, 0.9, 0.91, '', 'NDC')

        #take legend parametrisation out of for loop later
        legend.append(TLegend(*legend_args))
        legend[plot_count].SetFillStyle(0)
        if "QCDCR" in region:
            legend[plot_count].SetNColumns(3)
        legend[plot_count].AddEntry(data_hist[plot_count], 'Data', 'p')

        if not(len(signal_name) == 0):
            SIGNAL = pd.read_csv(mc_prefix+'/'+signal_name[0]+'/tbl_'+variable[Properties.Name]+weight_names+'.csv',comment='#')
            signal_hist.append(CreateHistogramNP(SIGNAL, tmp1_name ,variable[Properties.HistName]+"_signal",variable[Properties.AxisLabels], variable[Properties.Weight], 1, Lumi, variable[Properties.Rebin]))
            if 'SR' in region:
                legend[plot_count].AddEntry(signal_hist[plot_count], 'VBF H#rightarrow Inv', 'l')


        for bkg_name in bkg_names:

            bkg_file = pd.read_csv(mc_prefix+'/'+bkg_name+'/tbl_'+variable[Properties.Name]+weight_names+'.csv',comment='#')

            color = 2
            addLeg = False
            if (groupBy):
                bkg_file = bkg_file.dropna().groupby(tmp1_name).sum()
                bkg_file.reset_index(inplace=True)

            #print bkg_name
            index_leg = [['','',0,0]]
            for label_name in label_names:
                if label_name[0] in bkg_name:
                   # print "In_check"
                    color = label_name[2]
                    if label_name[3] == 0:
                        #print bkg_name, label_name[0], "in label check"
                        addLeg = True
                        label_name[3] = 1
                        index_leg = label_name
                    break


            bkg_hist = CreateHistogramNP(bkg_file,tmp1_name,variable[Properties.HistName]+bkg_name+"_mc"+str(plot_count),variable[Properties.AxisLabels], variable[Properties.Weight], color, Lumi, variable[Properties.Rebin])        

            #Scaling
            if Scaling:
                if "DY" in bkg_name:
                    print("Scaling DY")
                    bkg_hist.Scale(1.15)
                if "WJETS" in bkg_name:
                    bkg_hist.Scale(1.171714)

            if ScalingQCDCR:
                if "2018" in Location:
                    if "QCDCR" in region:
                        print("Scaling QCDCR by 0.85")
                        bkg_hist.Scale(0.85)

                    
                    
            bkg_hist.GetXaxis().SetRangeUser(variable[Properties.Axis_low],variable[Properties.Axis_high]) #- Really strange!
            if 'mindPhi' in variable[Properties.Name]:
                if "QCDCR" in region:
                    bkg_hist.GetXaxis().SetRangeUser(0,2) 
            bkg_stack[plot_count].Add(bkg_hist)

            if  bkg_names.index(bkg_name) == 0:
                bkg_for_ratio.append(bkg_hist.Clone())
            else:
                bkg_for_ratio[plot_count].Add(bkg_hist)

            if addLeg:
                if not(bkg_hist.Integral()==0):
                   # print bkg_name, bkg_hist.Integral()
                    addLeg = False
                    legend[plot_count].AddEntry(bkg_hist, index_leg[1], 'f')
                else:
                    for label_name in label_names:
                        if label_name[0] in bkg_name:
                            label_name[3] = 0 # return to the state label_not_drawn, not elegant check. return to it after the EXO workdshop!
                            break


        #WORK IN PROGRESS

        printing = False
        c.append(ROOT.TCanvas("c"+str(plot_count),"2 Graphs",900,1000))
        p2.append(ROOT.TPad("p2","p3",0.,0.,1.,0.28)) 
        p2[plot_count].Draw();
        p2[plot_count].SetTopMargin(0.001);
        p2[plot_count].SetBottomMargin(0.3);
        p2[plot_count].SetGrid()

        p1.append(ROOT.TPad("p1","p1",0.,0.3,1.,1.))  
        p1[plot_count].Draw();
        p1[plot_count].SetBottomMargin(0.001);
        p1[plot_count].cd()

        data_hist[plot_count].SetLineColor(1)


        data_hist[plot_count].GetXaxis().SetRangeUser(variable[Properties.Axis_low], variable[Properties.Axis_high])

        if 'mindPhi' in variable[Properties.Name]:
            if "QCDCR" in region:
                data_hist[plot_count].GetXaxis().SetRangeUser(0,2) 



        if LOG:
            p1[plot_count].SetLogy(1)

            
        data_hist[plot_count].Draw("e1")

        bkg_stack[plot_count].Draw("hist same")
        bkg_for_ratio[plot_count].SetFillColor(1)
        bkg_for_ratio[plot_count].SetMarkerSize(0)
        bkg_for_ratio[plot_count].SetFillStyle(3018)
        bkg_for_ratio[plot_count].Draw("E2 same")

        if LOG:
            data_hist[plot_count].GetYaxis().SetRangeUser(0.2,1000*bkg_for_ratio[plot_count].GetMaximum())
        else:
            if data_hist[plot_count].GetMaximum() > bkg_for_ratio[plot_count].GetMaximum():
                data_hist[plot_count].GetYaxis().SetRangeUser(0.1,1.7*data_hist[plot_count].GetMaximum())
            else:
                data_hist[plot_count].GetYaxis().SetRangeUser(0,1.7*bkg_for_ratio[plot_count].GetMaximum())
            # if data_hist[plot_count].Integral() > 0:
            #     data_hist[plot_count].GetYaxis().SetRangeUser(0.1,1.7*bkg_for_ratio[plot_count].GetMaximum())
            #     if data_hist[plot_count].GetMaximum() > bkg_for_ratio[plot_count].GetMaximum():
            #         data_hist[plot_count].GetYaxis().SetRangeUser(0.1,1.7*data_hist[plot_count].GetMaximum())
        if 'mjj' in variable[Properties.Name] or 'nomu' in variable[Properties.Name].lower():
            if data_hist[plot_count].GetMaximum() >bkg_for_ratio[plot_count].GetMaximum():
                data_hist[plot_count].GetYaxis().SetRangeUser(0.1,1.3*data_hist[plot_count].GetMaximum())
                bkg_stack[plot_count].GetYaxis().SetRangeUser(0.1,1.3*data_hist[plot_count].GetMaximum())
            else:
                data_hist[plot_count].GetYaxis().SetRangeUser(0.1,1.3*bkg_for_ratio[plot_count].GetMaximum())
                bkg_stack[plot_count].GetYaxis().SetRangeUser(0.1,1.3*bkg_for_ratio[plot_count].GetMaximum())

                


        data_hist[plot_count].GetXaxis().SetLabelSize(0.1)
        data_hist[plot_count].GetYaxis().SetTitleOffset(1.15)
        data_hist[plot_count].GetXaxis().SetTitleSize(.12)

        #BLINDING
        # if 'mjj' in variable[Properties.Name]:
        #     if 'SR' in region:
        #         print("SR blinding")
        #         for i in range(1,data_hist[plot_count].GetNbinsX()+1):
        #             data_hist[plot_count].SetBinContent(i,0)
        #             data_hist[plot_count].SetBinError(i,0)
        #             data_for_ratio[plot_count] = data_hist[plot_count].Clone()
                

        data_hist[plot_count].Draw("e1 same")

        if not(len(signal_name)==0):
            signal_hist[plot_count].SetLineWidth(4)
            signal_hist[plot_count].SetFillStyle(0)
            if 'vtr' in category.lower():
                signal_hist[plot_count].Scale(1.5)
            else:
                signal_hist[plot_count].Scale(5)
            signal_hist[plot_count].Draw("hist same")

        #gPad.Draw()
        legend[plot_count].Draw()
        tex = Styling(region, "CMS",  "Work in Progress", Lumi_label)
        tex1.append(tex[0])
        tex2.append(tex[1])
        tex3.append(tex[2])

        tex1[plot_count].Draw("goff")      
        tex2[plot_count].Draw("goff")   
        tex3[plot_count].Draw("goff")   
        #gPad.Update();
        gPad.RedrawAxis();

        p2[plot_count].cd()
        #r = ROOT.TGraph(20); 
        #r.SetTitle("");
        data_for_ratio[plot_count].Divide(bkg_for_ratio[plot_count])
        data_for_ratio[plot_count].GetXaxis().SetRangeUser(variable[Properties.Axis_low], variable[Properties.Axis_high])
        data_for_ratio[plot_count].GetYaxis().SetRangeUser(variable[Properties.Ratio_Axis_low],variable[Properties.Ratio_Axis_high])

        if "QCDCR" in region:
            if 'vtr' in category.lower():
                data_for_ratio[plot_count].GetYaxis().SetRangeUser(0,3)

            if 'mindPhi' in variable[Properties.Name]:
                data_for_ratio[plot_count].GetXaxis().SetRangeUser(0,2) 

        # maximum = max([data_for_ratio[plot_count].GetBinContent(b)+data_for_ratio[plot_count].GetBinError(b) for b in range(1,data_for_ratio[plot_count].GetNbinsX()+1)])
        # minimum = min([data_for_ratio[plot_count].GetBinContent(b)-data_for_ratio[plot_count].GetBinError(b) for b in range(1,data_for_ratio[plot_count].GetNbinsX()+1)])
        # data_for_ratio[plot_count].SetMaximum(min(math.ceil(10*maximum)/10,2.49))
        # data_for_ratio[plot_count].SetMinimum(max(math.floor(10*minimum)/10,-0.49))
        #data_for_ratio[plot_count].GetYaxis().SetRangeUser(-0.49,2.49)

        data_for_ratio[plot_count].GetYaxis().SetTitle("Data / Pred.")
        data_for_ratio[plot_count].GetXaxis().SetTitleSize(.12)
        data_for_ratio[plot_count].GetYaxis().SetTitleSize(.12)
        data_for_ratio[plot_count].GetYaxis().SetTitleOffset(0.57)
        data_for_ratio[plot_count].GetYaxis().SetLabelSize(0.1)
        data_for_ratio[plot_count].GetXaxis().SetLabelSize(0.1)
        data_for_ratio[plot_count].Draw("P0")
        bkg_band = bkg_for_ratio[plot_count].Clone()
        bkg_band_d = bkg_for_ratio[plot_count].Clone()
        bkg_band.Divide(bkg_band_d)
        bkg_band.SetFillColor(1)
        bkg_band.SetMarkerSize(0)
        bkg_band.SetFillStyle(3018)
        bkg_band.Draw("E2 same")
#        c[plot_count].Draw()

        gPad.RedrawAxis();

        if not(LOG):
            c[plot_count].SaveAs(output_dir+"/"+tmp1_name+".pdf")
            c[plot_count].SaveAs(output_dir+"/"+tmp1_name+".png")
            c[plot_count].SaveAs(output_dir+"/"+tmp1_name+".C")
            c[plot_count].SaveAs(output_dir+"/"+tmp1_name+".root")
        else:
            c[plot_count].SaveAs(output_dir+"/"+tmp1_name+"_log.pdf")
            c[plot_count].SaveAs(output_dir+"/"+tmp1_name+"_log.png")
            c[plot_count].SaveAs(output_dir+"/"+tmp1_name+"_log.C")
            c[plot_count].SaveAs(output_dir+"/"+tmp1_name+"_log.root")


        plot_count+=1
        return True

