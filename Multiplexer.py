

#Computation of the Breakdown voltage for the 128 of SiPM arrays.
#Take the .txt of the x-y Table to read
#The code removes the first 2 lines and neglects ;
#Axel K.



import numpy as np
import os

from array import array


from ROOT import TH1F, TH2F, TCanvas, TGraph, TLegend, TF1, TMath, TMultiGraph
import ROOT
ROOT.gROOT.SetBatch(True)



#######################INITIALISATION#######################
import sys

param = sys.argv[1]
param =np.int(param)


Channel =[]
rq_list=[]
VBD=[]
OVint=[]
TypDCR=[]
deadchannel=[]
numberofdead=0

allgraph=TMultiGraph()
allgraphDCR=TMultiGraph()
allgraphRQ=TMultiGraph()
allgraphDeriv=TMultiGraph()

color=1



ConfigList="/Users/kuonen/Desktop/PhD/Setups/Multiplexer/Code/config_file.txt"
config=np.genfromtxt(ConfigList,skip_header=2,invalid_raise=False, dtype='string')
Name=config[0]
Output=config[1]
Nfiles=config[2]
Nfiles=Nfiles.astype(np.int)
Npixel=config[3]
Npixel=Npixel.astype(np.double)
Gain=config[4]
Gain=Gain.astype(np.double)
Vmin=config[5]
Vmin=Vmin.astype(np.double)
Vmax=config[6]
Vmax=Vmax.astype(np.double)
Vmin2=config[7]
Vmin2=Vmin2.astype(np.double)
Vmax2=config[8]
Vmax2=Vmax2.astype(np.double)
OVtyp=config[9]
OVtyp=OVtyp.astype(np.double)
T=config[10]
Breakdown=config[11:Nfiles+11]
Breakdown=Breakdown.astype(np.double)





#########################Function#######################################
def FindBreakdown(Volt,Current):
    Deriv=[0]
    for m in range(1,len(Volt)-2):
        Deriv.append(0)
        Deriv[m-1] = 1/((1/Current[m-1])*( (Current[m+2]-Current[m-1])/(Volt[m+2]-Volt[m-1])))
    return Deriv




def FindDCR(Volt,Current,Breakdown):
    Over=[0]
    DCR=[0]
        
    for l in range(1,Volt.size):
        Over.append(0)
        DCR.append(0)
        Over[l]=Volt[l]-Breakdown
        DCR[l]= Current[l]/(((Gain/3.5)*Over[l])*1.602e-19)
    return (DCR,Over)


###################### Help ##########################
if param == 0 :
    print "Give the Parameter like number of files, number of pixeles, V_BD, Gain, RQ ranges through the config_file"
    print "Use option 0 for Help, 1 for approximate breakdown calcutation, 2 for RQ, 3 for DCR, 4 to selecte a Channel we are interseted in, add the channel we are interested in. Example python Multiplexer.py 4 128 to look at channel 128"



    


    ###################### Main ##########################

elif param == 4 :
    
    ############ RQ Single ####################
    
        single = sys.argv[2]
        single =np.int(single)
        Signal='/Users/kuonen/Desktop/PhD/Setups/Multiplexer/Code/%s/Channel_%s.txt'% (Name,single)
        Volt=np.genfromtxt(Signal,usecols=0)
        Current=np.genfromtxt(Signal,usecols=1)*1e9
        
        ccrq_single=TCanvas()
        gPadrq = ccrq_single.cd()
        gPadrq.SetGrid()
        
        graph=TGraph(len(Volt),Volt,Current)
        graph.SetLineColor(color)
        function = ROOT.TF1("function", 'pol1',Vmin,Vmax)
        graph.Fit(function,"RQ")
        graph.Draw("AP")
        graph.GetXaxis().SetRangeUser(-5,0)
        graph.SetMarkerStyle(20)
        graph.SetMarkerSize(1)
        graph.SetMarkerColor(4)
        offset=function.GetParameter(0)
        slope=function.GetParameter(1)
        Rq = 1./(slope*1e-9)*Npixel*1e-3 ;
        ccrq_single.Update()
        ccrq_single.SaveAs('/Users/kuonen/Desktop/PhD/Setups/Multiplexer/Code/%s/RQ_%s.root' % (Output,single))
        ccrq_single.SaveAs('/Users/kuonen/Desktop/PhD/Setups/Multiplexer/Code/%s/RQ_%s.pdf' % (Output,single))
        fout = open("/Users/kuonen/Desktop/PhD/Setups/Multiplexer/Code/%s/RQ_%s.txt" % (Output,single),"w")
        fout.write("%s   %s \n" % (single, Rq))
        fout.close()
            
############################### IV Single####################

            
        ccIV_single=TCanvas()
        gPadIV = ccIV_single.cd()
        gPadIV.SetGrid()
        gPadIV.SetLogy()
        graphIV=TGraph(len(Volt),Volt,Current)
        graphIV.SetLineColor(color)
        graphIV.Draw("AP")
        graphIV.GetXaxis().SetRangeUser(52,63)
        graphIV.GetYaxis().SetRangeUser(0.1,1e3)
        graphIV.SetMarkerStyle(20)
        graphIV.SetMarkerSize(1)
        graphIV.SetMarkerColor(4)

        ccIV_single.Update()
        ccIV_single.SaveAs('/Users/kuonen/Desktop/PhD/Setups/Multiplexer/Code/%s/IV_%s.root' % (Output,single))
        ccIV_single.SaveAs('/Users/kuonen/Desktop/PhD/Setups/Multiplexer/Code/%s/IV_%s.pdf' % (Output,single))

###############################VBD Single####################


        Deriv=FindBreakdown(Volt,Current)
        Deriv=np.array(Deriv)


        ccderiv = TCanvas()
        gPadDe = ccderiv.cd()
        gPadDe.SetGrid()
        function2 = ROOT.TF1("function", 'pol1',Vmin2,Vmax2)
        graphDeriv_single=TGraph(len(Deriv),Volt,Deriv)
        graphDeriv_single.Fit(function2,"RQ")
        offset=function2.GetParameter(0)
        slope=function2.GetParameter(1)
        VBD=-offset/slope
        graphDeriv_single.SetLineColor(4)
        graphDeriv_single.Draw("AL")
        graphDeriv_single.GetXaxis().SetRangeUser(46,56)
        #graphDeriv_single.GetYaxis().SetRangeUser(-1.5,2.5)
        ccderiv.Update()
        ccderiv.SaveAs('/Users/kuonen/Desktop/PhD/Setups/Multiplexer/Code/%s/Deriv_%s.root' % (Output,single))
        ccderiv.SaveAs('/Users/kuonen/Desktop/PhD/Setups/Multiplexer/Code/%s/Deriv_%s.pdf' % (Output,single))
        fout = open("/Users/kuonen/Desktop/PhD/Setups/Multiplexer/Code/%s/VBD_%s.txt" % (Output,single),"w")
        fout.write("%s   %s \n" % (single, VBD))
        fout.close()


########################### DCR Single ######################

        (DCR,Over)=FindDCR(Volt,Current*1e-9,Breakdown[single-1])
        overlist =Over
        DCRlist = DCR
        DCR=np.array(DCR)
        Over=np.array(Over)
        ccDCR = TCanvas()
        gPadDCR = ccDCR.cd()
        gPadDCR.SetGrid()
        gPadDCR.SetLogy()
        graphDCR_single=TGraph(len(Over),Over,DCR*1e-3)
        graphDCR_single.SetLineColor(4)
        graphDCR_single.Draw("AL")
        graphDCR_single.GetXaxis().SetRangeUser(0.1,8)
        #graphDCR_single.GetYaxis().SetRangeUser(0.1,1e5)
        graphDCR_single.GetXaxis().SetTitle("#DeltaV[V]")
        graphDCR_single.GetYaxis().SetTitle("DCR [kHz]")
        ccDCR.Update()
        ccDCR.SaveAs('/Users/kuonen/Desktop/PhD/Setups/Multiplexer/Code/%s/DCR_%s.root' % (Output,single))
        ccDCR.SaveAs('/Users/kuonen/Desktop/PhD/Setups/Multiplexer/Code/%s/DCR_%s.pdf' % (Output,single))

        OVint =min(Over, key=lambda x:abs(x-OVtyp))
        index=overlist.index(OVint)
        TypDCR = DCR[index]*1e-3
        fout = open("/Users/kuonen/Desktop/PhD/Setups/Multiplexer/Code/%s/DCR_%s.txt" % (Output,single),"w")
        fout.write("%s  %s  %s\n" % (single, OVint, TypDCR))
        fout.close()


    ######################## Plot the files ########################

else :
    
    for i in range(1,Nfiles+1):
        
        Channel.append(0)
        Channel[i-1]=i
        Signal='/Users/kuonen/Desktop/PhD/Setups/Multiplexer/Code/%s/Channel_%s.txt'% (Name,Channel[i-1])
        Volt=np.genfromtxt(Signal,usecols=0)
        Current=np.genfromtxt(Signal,usecols=1)*1e9
        graph=TGraph(len(Volt),Volt,Current)
        graph.SetLineColor(color)
        
        
        if param == 2:
            function = ROOT.TF1("function", 'pol1',Vmin,Vmax)
            graph.Fit(function,"RQ")
            offset=function.GetParameter(0)
            slope=function.GetParameter(1)
            allgraph.Add(graph)
            rq_list.append(((1./(slope*1e-9))*Npixel)*1e-3) ;
            if color == 9:
                color=1
            color=color+1
        else :
            allgraph.Add(graph)
            if color == 9:
                color=1
            color=color+1

    ########## RQ computation ##################

    if param ==2 :
        
        RQ=np.array(rq_list)
        Channel = np.array(Channel)
        Channel =np.float_(Channel)
        ccrq=TCanvas()
        gPad2 = ccrq.cd()
        gPad2.SetGrid()
        ChannelRQ=TGraph(len(RQ),Channel,RQ)
        ChannelRQ.GetXaxis().SetTitle("Channel")
        ChannelRQ.GetYaxis().SetTitle("RQ[k#Omega]")
        ChannelRQ.GetYaxis().SetRangeUser(150,190)
        ChannelRQ.Draw("AP")
        ChannelRQ.SetMarkerStyle(20)
        ChannelRQ.SetMarkerSize(1)
        ChannelRQ.SetMarkerColor(4)
        ccrq.Update()
        ccrq.SaveAs('/Users/kuonen/Desktop/PhD/Setups/Multiplexer/Code/%s/RQ.root' % (Output))
        ccrq.SaveAs('/Users/kuonen/Desktop/PhD/Setups/Multiplexer/Code/%s/RQ.pdf' % (Output))
        fout = open("/Users/kuonen/Desktop/PhD/Setups/Multiplexer/Code/%s/RQ.txt" % (Output),"w")
        for q in range(1,len(Channel)+1):
            fout.write("%s   %s \n" % (Channel[q-1], RQ[q-1]))
        fout.close()

    ############ Plots ##################

    cc = TCanvas()
    gPad = cc.cd()
    gPad.SetGrid()
    allgraph.Draw("AL")
    if param ==2 :
        gPad = cc.cd
        allgraph.GetXaxis().SetRangeUser(-5,0)
    else :
        gPad.SetLogy()
        allgraph.GetXaxis().SetRangeUser(46,56)
        allgraph.GetYaxis().SetRangeUser(0.1,1e7)


    allgraph.GetXaxis().SetTitle("Volt [V]")
    allgraph.GetYaxis().SetTitle("Current [nA]")
    cc.Update()

    cc.SaveAs('/Users/kuonen/Desktop/PhD/Setups/Multiplexer/Code/%s/IV.root' % (Output))
    cc.SaveAs('/Users/kuonen/Desktop/PhD/Setups/Multiplexer/Code/%s/IV.pdf' % (Output))



    ######### Breakdown computation ############
    if param ==1 :
        color=1

        for p in range(1,Nfiles+1):
            
            VBD.append(0)
            Channel[p-1]=p
            
            Signal='/Users/kuonen/Desktop/PhD/Setups/Multiplexer/Code/%s/Channel_%s.txt' % (Name,Channel[p-1])
            Volt=np.genfromtxt(Signal,usecols=0)
            Current=np.genfromtxt(Signal,usecols=1) 
            Deriv=FindBreakdown(Volt,Current)
            Deriv=np.array(Deriv)
            Volt=np.array(Volt)
            function2 = ROOT.TF1("function", 'pol1',Vmin2,Vmax2)
            graphDeriv=TGraph(len(Deriv),Volt,Deriv)
            graphDeriv.Fit(function2,"RQ")
            offset=function2.GetParameter(0)
            slope=function2.GetParameter(1)
            VBD[p-1]=-offset/slope
            
            graphDeriv.SetLineColor(color)
            allgraphDeriv.Add(graphDeriv)
            if color == 9:
                color=1
            color=color+1

            if Current[50] <= 1e-8:
                deadchannel.append(p)
                numberofdead=numberofdead+1

        print "Number of dead channel =",numberofdead
        print "Channel number =", deadchannel
        VBD=np.array(VBD)
        cc3 = TCanvas()
        gPad3 = cc3.cd()
        gPad3.SetGrid()
        allgraphDeriv.Draw("AL")
        allgraphDeriv.GetXaxis().SetRangeUser(48,62)
        allgraphDeriv.GetYaxis().SetRangeUser(-3.5,3.5)
        cc3.Update()
        cc3.SaveAs('/Users/kuonen/Desktop/PhD/Setups/Multiplexer/Code/%s/Deriv.root' % (Output))
        cc3.SaveAs('/Users/kuonen/Desktop/PhD/Setups/Multiplexer/Code/%s/Deriv.pdf' % (Output))
        Channel = np.array(Channel)
        Channel = np.float_(Channel)
        ccvbd=TCanvas()
        gPad4 = ccvbd.cd()
        gPad4.SetGrid()
        ChannelVBD=TGraph(len(VBD),Channel,VBD)
        ChannelVBD.GetXaxis().SetTitle("Channel")
        ChannelVBD.GetYaxis().SetTitle("Breakdown Voltage [V]")
        ChannelVBD.Draw("AP")
        ChannelVBD.SetMarkerStyle(21)
        ChannelVBD.SetMarkerSize(1)
        ChannelVBD.SetMarkerColor(2)
        ccvbd.Update()
        ccvbd.SaveAs('/Users/kuonen/Desktop/PhD/Setups/Multiplexer/Code/%s/VBD.root' % (Output))
        ccvbd.SaveAs('/Users/kuonen/Desktop/PhD/Setups/Multiplexer/Code/%s/VBD.pdf'% (Output))
        fout = open("/Users/kuonen/Desktop/PhD/Setups/Multiplexer/Code/%s/VBD.txt" % (Output),"w")
        for q in range(1,len(Channel)+1):
            fout.write("%s   %s \n" % (Channel[q-1], VBD[q-1]))
        fout.close()


    ########## DCR Computation ############
    if param == 3:
        color=1
        for j in range(1,Nfiles+1):
            OVint.append(0)
            TypDCR.append(0)
            Signal='/Users/kuonen/Desktop/PhD/Setups/Multiplexer/Code/%s/Channel_%s.txt' % (Name,Channel[j-1])
            Volt=np.genfromtxt(Signal,usecols=0)
            Current=np.genfromtxt(Signal,usecols=1)
            (DCR,Over)=FindDCR(Volt,Current,Breakdown[j-1])
            DCRlist = DCR
            Overlist = Over
            OVint[j-1] =min(Over, key=lambda x:abs(x-OVtyp))
            index=Overlist.index(OVint[j-1])
            TypDCR[j-1] = DCR[index]*1e-6
      
            DCR=np.array(DCR)
            Over=np.array(Over)
            graphDCR=TGraph(len(Over),Over,DCR*1e-6)
            graphDCR.SetLineColor(color)
            allgraphDCR.Add(graphDCR)
            if color == 9:
                color=1
            color=color+1


        cc2 = TCanvas()
        gPad = cc2.cd()
        gPad.SetGrid()
        gPad.SetLogy()
        allgraphDCR.Draw("AL")
        allgraphDCR.GetXaxis().SetRangeUser(0.1,8)
        #allgraphDCR.GetYaxis().SetRangeUser(0.1,1e5)
        allgraphDCR.GetXaxis().SetTitle("#DeltaV[V]")
        allgraphDCR.GetYaxis().SetTitle("DCR [MHz]")
        cc2.Update()

        cc2.SaveAs('/Users/kuonen/Desktop/PhD/Setups/Multiplexer/Code/%s/DCR_%s.root' % (Output,T))
        cc2.SaveAs('/Users/kuonen/Desktop/PhD/Setups/Multiplexer/Code/%s/DCR_%s.pdf' % (Output,T))
        fout = open("/Users/kuonen/Desktop/PhD/Setups/Multiplexer/Code/%s/DCR_%s.txt" % (Output,T),"w")
        fout.write("Channel  Delta V [V]   DCR[MHz] \n")
        for n in range(1,len(Channel)+1):
            fout.write("%s  %s  %s \n" % (Channel[n-1], OVint[n-1],TypDCR[n-1]))
        fout.close()

        cc20= TCanvas()
        gPad20 = cc20.cd()
        gPad20.SetGrid()
        Channel = np.array(Channel)
        Channel = np.float_(Channel)
        TypDCR = np.array(TypDCR)
        ChannelDCR=TGraph(len(TypDCR),Channel,TypDCR)
        ChannelDCR.GetXaxis().SetTitle("Channel")
        ChannelDCR.GetYaxis().SetTitle("DCR at %sV [MHz]" % OVtyp)
        ChannelDCR.Draw("AP")
        ChannelDCR.SetMarkerStyle(21)
        ChannelDCR.SetMarkerSize(1)
        ChannelDCR.SetMarkerColor(2)
        cc20.Update()
        cc20.SaveAs('/Users/kuonen/Desktop/PhD/Setups/Multiplexer/Code/%s/DCR_Channel_%s.root' % (Output,T))
        cc20.SaveAs('/Users/kuonen/Desktop/PhD/Setups/Multiplexer/Code/%s/DCR_Channel_%s.pdf' % (Output,T))



