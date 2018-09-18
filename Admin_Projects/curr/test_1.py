# -*- coding: utf-8 -*-
'''
file : C:\WORKS_2\WS\WS_Others\prog\D-7\2_2\VIRTUAL\Admin_Projects\curr\test_1.py
orig : C:\WORKS_2\WS\WS_Others\prog\D-7\2_2\1_1.py
at : 2018/02/17 09:13:55

pushd C:\WORKS_2\WS\WS_Others\prog\D-7\2_2\VIRTUAL\Admin_Projects\curr
python test_1.py



    Regex
print "[%s:%d] result => %s" % (libs.thisfile(), libs.linenum(), result_HighLowDiffs)
^ +(print )(".+" %.+\(.+\).*)$
^( +)(print )(".+" %.+\(.+\).*)$
$1$2($3)

print "[%s:%d] result => %s" % \
        (libs.thisfile(), libs.linenum(), result_HighLowDiffs)
^( +)(print )(".+" %) \\\r\n(.+)$
$1$2($3)$4$5
$1$2($3 \\\r\n$4)

print ("[%s:%d] all done" % (libs.thisfile(), libs.linenum()))
^( +)(print )(.+)(libs.+file\(\))(.+)
$1$2$3os.path.basename($4)$5
'''


import sys, os

'''###################
    import : original files        
###################'''
sys.path.append('.')
sys.path.append('..')
# sys.path.append('C:/WORKS_2/WS/WS_Others/free/fx/82_')
# 
# sys.path.append('C:/WORKS_2/WS/WS_Others/free/VX7GLZ_science-research/31_Materials')
# sys.path.append('C:/WORKS_2/WS/WS_Others/prog/D-7/2_2/VIRTUAL/Admin_Projects/mm')

from mm.libs_mm import cons_mm, cons_fx, libs, libfx
# from mm.libs_mm import libs
# from mm.libs_mm import libfx

from Admin_Projects.definitions import ROOT_DIR
from Admin_Projects.definitions import DPATH_ROOT_CURR

'''###################
    import : built-in modules        
###################'''
import getopt, inspect, math as math, struct, random
import xml.etree.ElementTree as ET
from shutil import copyfile
from scipy.stats.stats import pearsonr

###############################################
def test_1():
    
    '''###################
        vars
    ###################'''
    a1 = bin(random.randint(1, 100))[2:]
    a2 = bin(random.randint(1, 100))[2:]
    a3 = bin(random.randint(1, 100))[2:]
    
    ### length
    len1 = len(a1)
    len2 = len(a2)
    len3 = len(a3)
    
    s1 = ''.join(["0"]*(8 - len1)) + a1
    s2 = ''.join(["0"]*(8 - len2)) + a2
    s3 = ''.join(["0"]*(8 - len3)) + a3
    
    lo_1_tmp = list(s1)
    lo_2_tmp = list(s2)
    lo_3_tmp = list(s3)
    
    lo_1 = [int(x) for x in lo_1_tmp]
    lo_2 = [int(x) for x in lo_2_tmp]
    lo_3 = [int(x) for x in lo_3_tmp]
    
    '''###################
        pearson        
    ###################'''
    pr_1_2 = pearsonr(lo_1, lo_2)
    pr_1_3 = pearsonr(lo_1, lo_3)
    
    print()
    print("[%s:%d]\ns1 = %s (%s)\ns2 = %s (%s)\ns3 = %s (%s)" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , s1, lo_1, s2, lo_2, s3, lo_3
            ), file=sys.stderr)
#     print("[%s:%d] lo_1 = %s / lo_2 = %s" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#             , lo_1, lo_2
#             ), file=sys.stderr)
    print("[%s:%d] pr_1_2 => %.6f / pr_1_3[0] => %.6f" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , pr_1_2[0], pr_1_3[0]
            ), file=sys.stderr)

#/def test_1():

def exec_prog(): # from : 
    
    '''###################
        ops        
    ###################'''
    test_1()
    
    '''###################
        Report        
    ###################'''
    print ("[%s:%d] exec_prog => done" % (os.path.basename(libs.thisfile()), libs.linenum()))
 
#/def exec_prog(): # from : 20180116_103908





'''
<usage>
'''
if __name__ == "__main__" :

    '''###################
        validate : help option        
    ###################'''

    '''###################
        get options        
    ###################'''

    '''###################
        evecute        
    ###################'''
    exec_prog()

    print()
    
    print ("[%s:%d] all done" % (os.path.basename(os.path.basename(libs.thisfile())), libs.linenum()))


'''

lo_1 = ['0', '0', '0', '1', '0', '1', '1', '1']
lo_2 = ['0', '1', '0', '1', '0', '1', '1', '0']


'''