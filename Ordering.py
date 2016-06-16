
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



ConfigList="/home/lphe/Multiplexer/config_file.txt"
config=np.genfromtxt(ConfigList,skip_header=2,invalid_raise=False, dtype='string')
Name=config[0]
Output=config[1]
Nfiles=config[2]
Nfiles=Nfiles.astype(np.int)



###################### Reordering ##########################

import os
dir = "/%s/" % Name
for filename in os.listdir("/%s/" % Name):
    if filename.startswith("Measure__1_1_3.txt"):
        os.rename(dir+"Measure__1_1_3.txt" , dir+"Channel_1.txt")
    if filename.startswith("Measure__1_1_4.txt"):
        os.rename(dir+"Measure__1_1_4.txt" , dir+"Channel_2.txt")
    if filename.startswith("Measure__1_1_1.txt"):
        os.rename(dir+"Measure__1_1_1.txt" , dir+"Channel_3.txt")
    if filename.startswith("Measure__1_1_2.txt"):
        os.rename(dir+"Measure__1_1_2.txt" , dir+"Channel_4.txt")
    if filename.startswith("Measure__1_1_7.txt"):
        os.rename(dir+"Measure__1_1_7.txt" , dir+"Channel_5.txt")
    if filename.startswith("Measure__1_1_8.txt"):
        os.rename(dir+"Measure__1_1_8.txt" , dir+"Channel_6.txt")
    if filename.startswith("Measure__1_1_5.txt"):
        os.rename(dir+"Measure__1_1_5.txt" , dir+"Channel_7.txt")
    if filename.startswith("Measure__1_1_6.txt"):
        os.rename(dir+filename , dir+"Channel_8.txt")
    if filename.startswith("Measure__1_1_11.txt"):
        os.rename(dir+filename , dir+"Channel_9.txt")
    if filename.startswith("Measure__1_1_12.txt"):
        os.rename(dir+filename , dir+"Channel_10.txt")
    if filename.startswith("Measure__1_1_9.txt"):
        os.rename(dir+filename , dir+"Channel_11.txt")
    if filename.startswith("Measure__1_1_10.txt"):
        os.rename(dir+filename , dir+"Channel_12.txt")
    if filename.startswith("Measure__1_1_15.txt"):
        os.rename(dir+filename , dir+"Channel_13.txt")
    if filename.startswith("Measure__1_1_16.txt"):
        os.rename(dir+filename , dir+"Channel_14.txt")
    if filename.startswith("Measure__1_1_13.txt"):
        os.rename(dir+filename , dir+"Channel_15.txt")
    if filename.startswith("Measure__1_1_14.txt"):
        os.rename(dir+filename , dir+"Channel_16.txt")
    if filename.startswith("Measure__1_1_19.txt"):
        os.rename(dir+filename , dir+"Channel_17.txt")
    if filename.startswith("Measure__1_1_20.txt"):
        os.rename(dir+filename , dir+"Channel_18.txt")
    if filename.startswith("Measure__1_1_17.txt"):
        os.rename(dir+filename , dir+"Channel_19.txt")
    if filename.startswith("Measure__1_1_18.txt"):
        os.rename(dir+filename , dir+"Channel_20.txt")
    if filename.startswith("Measure__1_1_23.txt"):
        os.rename(dir+filename , dir+"Channel_21.txt")
    if filename.startswith("Measure__1_1_24.txt"):
        os.rename(dir+filename , dir+"Channel_22.txt")
    if filename.startswith("Measure__1_1_21.txt"):
        os.rename(dir+filename , dir+"Channel_23.txt")
    if filename.startswith("Measure__1_1_22.txt"):
        os.rename(dir+filename , dir+"Channel_24.txt")
    if filename.startswith("Measure__1_1_27.txt"):
        os.rename(dir+filename , dir+"Channel_25.txt")
    if filename.startswith("Measure__1_1_28.txt"):
        os.rename(dir+filename , dir+"Channel_26.txt")
    if filename.startswith("Measure__1_1_25.txt"):
        os.rename(dir+filename , dir+"Channel_27.txt")
    if filename.startswith("Measure__1_1_26.txt"):
        os.rename(dir+filename , dir+"Channel_28.txt")
    if filename.startswith("Measure__1_1_31.txt"):
        os.rename(dir+filename , dir+"Channel_29.txt")
    if filename.startswith("Measure__1_1_32.txt"):
        os.rename(dir+filename , dir+"Channel_30.txt")
    if filename.startswith("Measure__1_1_29.txt"):
        os.rename(dir+filename , dir+"Channel_31.txt")
    if filename.startswith("Measure__1_1_30.txt"):
        os.rename(dir+filename , dir+"Channel_32.txt")
    if filename.startswith("Measure__1_1_35.txt"):
        os.rename(dir+filename , dir+"Channel_33.txt")
    if filename.startswith("Measure__1_1_36.txt"):
        os.rename(dir+filename , dir+"Channel_34.txt")
    if filename.startswith("Measure__1_1_33.txt"):
        os.rename(dir+filename , dir+"Channel_35.txt")
    if filename.startswith("Measure__1_1_34.txt"):
        os.rename(dir+filename , dir+"Channel_36.txt")
    if filename.startswith("Measure__1_1_39.txt"):
        os.rename(dir+filename , dir+"Channel_37.txt")
    if filename.startswith("Measure__1_1_40.txt"):
        os.rename(dir+filename , dir+"Channel_38.txt")
    if filename.startswith("Measure__1_1_37.txt"):
        os.rename(dir+filename , dir+"Channel_39.txt")
    if filename.startswith("Measure__1_1_38.txt"):
        os.rename(dir+filename , dir+"Channel_40.txt")
    if filename.startswith("Measure__1_1_43.txt"):
        os.rename(dir+filename , dir+"Channel_41.txt")
    if filename.startswith("Measure__1_1_44.txt"):
        os.rename(dir+filename , dir+"Channel_42.txt")
    if filename.startswith("Measure__1_1_41.txt"):
        os.rename(dir+filename , dir+"Channel_43.txt")
    if filename.startswith("Measure__1_1_42.txt"):
        os.rename(dir+filename , dir+"Channel_44.txt")
    if filename.startswith("Measure__1_1_47.txt"):
        os.rename(dir+filename , dir+"Channel_45.txt")
    if filename.startswith("Measure__1_1_48.txt"):
        os.rename(dir+filename , dir+"Channel_46.txt")
    if filename.startswith("Measure__1_1_45.txt"):
        os.rename(dir+filename , dir+"Channel_47.txt")
    if filename.startswith("Measure__1_1_46.txt"):
        os.rename(dir+filename , dir+"Channel_48.txt")
    if filename.startswith("Measure__1_1_51.txt"):
        os.rename(dir+filename , dir+"Channel_49.txt")
    if filename.startswith("Measure__1_1_52.txt"):
        os.rename(dir+filename , dir+"Channel_50.txt")
    if filename.startswith("Measure__1_1_49.txt"):
        os.rename(dir+filename , dir+"Channel_51.txt")
    if filename.startswith("Measure__1_1_50.txt"):
        os.rename(dir+filename , dir+"Channel_52.txt")
    if filename.startswith("Measure__1_1_55.txt"):
        os.rename(dir+filename , dir+"Channel_53.txt")
    if filename.startswith("Measure__1_1_56.txt"):
        os.rename(dir+filename , dir+"Channel_54.txt")
    if filename.startswith("Measure__1_1_53.txt"):
        os.rename(dir+filename , dir+"Channel_55.txt")
    if filename.startswith("Measure__1_1_54.txt"):
        os.rename(dir+filename , dir+"Channel_56.txt")
    if filename.startswith("Measure__1_1_59.txt"):
        os.rename(dir+filename , dir+"Channel_57.txt")
    if filename.startswith("Measure__1_1_60.txt"):
        os.rename(dir+filename , dir+"Channel_58.txt")
    if filename.startswith("Measure__1_1_57.txt"):
        os.rename(dir+filename , dir+"Channel_59.txt")
    if filename.startswith("Measure__1_1_58.txt"):
        os.rename(dir+filename , dir+"Channel_60.txt")
    if filename.startswith("Measure__1_1_63.txt"):
        os.rename(dir+filename , dir+"Channel_61.txt")
    if filename.startswith("Measure__1_1_64.txt"):
        os.rename(dir+filename , dir+"Channel_62.txt")
    if filename.startswith("Measure__1_1_61.txt"):
        os.rename(dir+filename , dir+"Channel_63.txt")
    if filename.startswith("Measure__1_1_62.txt"):
        os.rename(dir+filename , dir+"Channel_64.txt")
    if filename.startswith("Measure__1_1_67.txt"):
        os.rename(dir+filename , dir+"Channel_65.txt")
    if filename.startswith("Measure__1_1_68.txt"):
        os.rename(dir+filename , dir+"Channel_66.txt")
    if filename.startswith("Measure__1_1_65.txt"):
        os.rename(dir+filename , dir+"Channel_67.txt")
    if filename.startswith("Measure__1_1_66.txt"):
        os.rename(dir+filename , dir+"Channel_68.txt")
    if filename.startswith("Measure__1_1_71.txt"):
        os.rename(dir+filename , dir+"Channel_69.txt")
    if filename.startswith("Measure__1_1_72.txt"):
        os.rename(dir+filename , dir+"Channel_70.txt")
    if filename.startswith("Measure__1_1_69.txt"):
        os.rename(dir+filename , dir+"Channel_71.txt")
    if filename.startswith("Measure__1_1_70.txt"):
        os.rename(dir+filename , dir+"Channel_72.txt")
    if filename.startswith("Measure__1_1_75.txt"):
        os.rename(dir+filename , dir+"Channel_73.txt")
    if filename.startswith("Measure__1_1_76.txt"):
        os.rename(dir+filename , dir+"Channel_74.txt")
    if filename.startswith("Measure__1_1_73.txt"):
        os.rename(dir+filename , dir+"Channel_75.txt")
    if filename.startswith("Measure__1_1_74.txt"):
        os.rename(dir+filename , dir+"Channel_76.txt")
    if filename.startswith("Measure__1_1_79.txt"):
        os.rename(dir+filename , dir+"Channel_77.txt")
    if filename.startswith("Measure__1_1_80.txt"):
        os.rename(dir+filename , dir+"Channel_78.txt")
    if filename.startswith("Measure__1_1_77.txt"):
        os.rename(dir+filename , dir+"Channel_79.txt")
    if filename.startswith("Measure__1_1_78.txt"):
        os.rename(dir+filename , dir+"Channel_80.txt")
    if filename.startswith("Measure__1_1_83.txt"):
        os.rename(dir+filename , dir+"Channel_81.txt")
    if filename.startswith("Measure__1_1_84.txt"):
        os.rename(dir+filename , dir+"Channel_82.txt")
    if filename.startswith("Measure__1_1_81.txt"):
        os.rename(dir+filename , dir+"Channel_83.txt")
    if filename.startswith("Measure__1_1_82.txt"):
        os.rename(dir+filename , dir+"Channel_84.txt")
    if filename.startswith("Measure__1_1_87.txt"):
        os.rename(dir+filename , dir+"Channel_85.txt")
    if filename.startswith("Measure__1_1_88.txt"):
        os.rename(dir+filename , dir+"Channel_86.txt")
    if filename.startswith("Measure__1_1_85.txt"):
        os.rename(dir+filename , dir+"Channel_87.txt")
    if filename.startswith("Measure__1_1_86.txt"):
        os.rename(dir+filename , dir+"Channel_88.txt")
    if filename.startswith("Measure__1_1_91.txt"):
        os.rename(dir+filename , dir+"Channel_89.txt")
    if filename.startswith("Measure__1_1_92.txt"):
        os.rename(dir+filename , dir+"Channel_90.txt")
    if filename.startswith("Measure__1_1_89.txt"):
        os.rename(dir+filename , dir+"Channel_91.txt")
    if filename.startswith("Measure__1_1_90.txt"):
        os.rename(dir+filename , dir+"Channel_92.txt")
    if filename.startswith("Measure__1_1_95.txt"):
        os.rename(dir+filename , dir+"Channel_93.txt")
    if filename.startswith("Measure__1_1_96.txt"):
        os.rename(dir+filename , dir+"Channel_94.txt")
    if filename.startswith("Measure__1_1_93.txt"):
        os.rename(dir+filename , dir+"Channel_95.txt")
    if filename.startswith("Measure__1_1_94.txt"):
        os.rename(dir+filename , dir+"Channel_96.txt")
    if filename.startswith("Measure__1_1_99.txt"):
        os.rename(dir+filename , dir+"Channel_97.txt")
    if filename.startswith("Measure__1_1_100.txt"):
        os.rename(dir+filename , dir+"Channel_98.txt")
    if filename.startswith("Measure__1_1_97.txt"):
        os.rename(dir+filename , dir+"Channel_99.txt")
    if filename.startswith("Measure__1_1_98.txt"):
        os.rename(dir+filename , dir+"Channel_100.txt")
    if filename.startswith("Measure__1_1_103.txt"):
        os.rename(dir+filename , dir+"Channel_101.txt")
    if filename.startswith("Measure__1_1_104.txt"):
        os.rename(dir+filename , dir+"Channel_102.txt")
    if filename.startswith("Measure__1_1_101.txt"):
        os.rename(dir+filename , dir+"Channel_103.txt")
    if filename.startswith("Measure__1_1_102.txt"):
        os.rename(dir+filename , dir+"Channel_104.txt")
    if filename.startswith("Measure__1_1_107.txt"):
        os.rename(dir+filename , dir+"Channel_105.txt")
    if filename.startswith("Measure__1_1_108.txt"):
        os.rename(dir+filename , dir+"Channel_106.txt")
    if filename.startswith("Measure__1_1_105.txt"):
        os.rename(dir+filename , dir+"Channel_107.txt")
    if filename.startswith("Measure__1_1_106.txt"):
        os.rename(dir+filename , dir+"Channel_108.txt")
    if filename.startswith("Measure__1_1_111.txt"):
        os.rename(dir+filename , dir+"Channel_109.txt")
    if filename.startswith("Measure__1_1_112.txt"):
        os.rename(dir+filename , dir+"Channel_110.txt")
    if filename.startswith("Measure__1_1_109.txt"):
        os.rename(dir+filename , dir+"Channel_111.txt")
    if filename.startswith("Measure__1_1_110.txt"):
        os.rename(dir+filename , dir+"Channel_112.txt")
    if filename.startswith("Measure__1_1_115.txt"):
        os.rename(dir+filename , dir+"Channel_113.txt")
    if filename.startswith("Measure__1_1_116.txt"):
        os.rename(dir+filename , dir+"Channel_114.txt")
    if filename.startswith("Measure__1_1_113.txt"):
        os.rename(dir+filename , dir+"Channel_115.txt")
    if filename.startswith("Measure__1_1_114.txt"):
        os.rename(dir+filename , dir+"Channel_116.txt")
    if filename.startswith("Measure__1_1_119.txt"):
        os.rename(dir+filename , dir+"Channel_117.txt")
    if filename.startswith("Measure__1_1_120.txt"):
        os.rename(dir+filename , dir+"Channel_118.txt")
    if filename.startswith("Measure__1_1_117.txt"):
        os.rename(dir+filename , dir+"Channel_119.txt")
    if filename.startswith("Measure__1_1_118.txt"):
        os.rename(dir+filename , dir+"Channel_120.txt")
    if filename.startswith("Measure__1_1_123.txt"):
        os.rename(dir+filename , dir+"Channel_121.txt")
    if filename.startswith("Measure__1_1_124.txt"):
        os.rename(dir+filename , dir+"Channel_122.txt")
    if filename.startswith("Measure__1_1_131.txt"):
        os.rename(dir+filename , dir+"Channel_123.txt")
    if filename.startswith("Measure__1_1_141.txt"):
        os.rename(dir+filename , dir+"Channel_124.txt")
    if filename.startswith("Measure__1_1_137.txt"):
        os.rename(dir+filename , dir+"Channel_125.txt")
    if filename.startswith("Measure__1_1_128.txt"):
        os.rename(dir+filename , dir+"Channel_126.txt")
    if filename.startswith("Measure__1_1_125.txt"):
        os.rename(dir+filename , dir+"Channel_127.txt")
    if filename.startswith("Measure__1_1_136.txt"):
        os.rename(dir+filename , dir+"Channel_128.txt")

print " Ordering is finished, channels were reordered successfully "
