# -*- coding: utf-8 -*-
'''
file : C:\WORKS_2\WS\WS_Others\prog\D-7\2_2\VIRTUAL\Admin_Projects\others\VX7GLZ\28_physics\1_\_16\1_16.py
orig : -
at : 2018/02/17 13:57:51

pushd C:\WORKS_2\WS\WS_Others\prog\D-7\2_2\VIRTUAL\Admin_Projects\others\VX7GLZ\28_physics\1_\_16\
python 1_16.py

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
sys.path.append('C:\\WORKS_2\\WS\\WS_Others\\prog\\D-7\\2_2\\VIRTUAL\\Admin_Projects')
# sys.path.append('C:\\WORKS_2\\WS\\WS_Others\\prog\\D-7\\2_2\\VIRTUAL\\Admin_Projects\\mm')
# sys.path.append('C:/WORKS_2/WS/WS_Others/prog/D-7/2_2/VIRTUAL/Admin_Projects/mm')

# #debug
# for item in sys.path :
#     
#     print(item)

from mm.libs_mm import cons_mm, cons_fx, libs, libfx
# from mm.libs_mm import libs
# from mm.libs_mm import libfx

# from Admin_Projects.definitions import ROOT_DIR
# from Admin_Projects.definitions import DPATH_ROOT_CURR

'''###################
    import : built-in modules        
###################'''
import getopt, inspect, struct, random
import xml.etree.ElementTree as ET, math as math, matplotlib.pyplot as plt \
        , numpy as np
from shutil import copyfile
from scipy.stats.stats import pearsonr

###############################################
def test_3():
    
    '''###################
        vars        
    ###################'''
    tlabel = libs.get_TimeLabel_Now()
    
    '''###################
        dir        
    ###################'''
    dpath_Out = "C:\\WORKS_2\\WS\\WS_Others\\prog" \
                + "\\D-7\\2_2\\VIRTUAL\\Admin_Projects" \
                + "\\others\\VX7GLZ\\28_physics\\1_\\_16" \
                + "\\images\\\images_%s" % (tlabel)
    
    ### make dir
    #ref https://www.tutorialspoint.com/python/os_mkdir.htm
    os.makedirs(dpath_Out)
    
    print()
    print("[%s:%d] dpath_Out => %s" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , dpath_Out
        ), file=sys.stderr)
    
    #from : C:\WORKS_2\WS\WS_Others\JVEMV6\34\libs\labs.py
    
#     for a in np.arange(1,2):
#     for a in np.arange(1,10, 0.5):
#     for a in np.arange(1,2, 0.1):
#     for a in np.arange(1, 5, 0.1):
    
    maxnum = 30
    
#     tick = np.pi / 60
    tick = np.pi / 30
    
#     for a in np.arange(0, np.pi * 4, tick):
    for a in np.arange(0, np.pi * 2, tick):
#     for a in np.arange(0, maxnum, tick):
#     for a in np.arange(0, 10, 0.1):

#         a = 1
        
#         s1 = [np.sin(x + a) for x in np.arange(-np.pi, np.pi, np.pi / 360)]
        s1 = [np.sin(x) for x in np.arange(-np.pi, np.pi, np.pi / 360)]
#         s1 = [np.sin(x * a) for x in np.arange(-np.pi, np.pi, np.pi / 360)]
        s2 = [np.cos(x * a) for x in np.arange(-np.pi, np.pi, np.pi / 360)]
#         s2 = [np.cos(x) for x in np.arange(-np.pi, np.pi, np.pi / 360)]
#         s2 = [np.cos(x + a) for x in np.arange(-np.pi, np.pi, np.pi / 360)]
        
#         s3 = [np.sin(x + a) for x in np.arange(-np.pi, np.pi, np.pi / 360)]
#         s4 = [np.cos(x) for x in np.arange(-np.pi, np.pi, np.pi / 360)]
        
#         s2 = [np.sin(x) for x in np.arange(-np.pi, np.pi, np.pi / 360)]
#         s2 = [np.sin(x + a) for x in np.arange(-np.pi, np.pi, np.pi / 360)]
    
        '''###################
            file path        
        ###################'''
#         dpath_Out = "C:\\WORKS_2\\WS\\WS_Others\\prog\\D-7\\2_2\\VIRTUAL\\Admin_Projects\\others\\VX7GLZ\\28_physics\\1_\\_16"
        ### fpath full
        fpath_Full = "%s\\tmp.%s.a=%.3f.png" % (dpath_Out, libs.get_TimeLabel_Now(), a)
#         fpath_Full = "%s\\tmp.%s.a=%.1f.png" % (dpath_Out, libs.get_TimeLabel_Now(), a)
#         fpath_Full = "%s\\tmp.%s.a=%.1f.png" % (dpath_Out, libs.get_TimeLabel_Now(), a)
        
        '''###################
            gca        
        ###################'''
        fig = plt.figure()
        ax = fig.gca()
        ax.set_xticks(np.arange(-1, 1, 0.1))
        ax.set_yticks(np.arange(-1, 1, 0.1))

        
        
        '''###################
            plot
        ###################'''    
        plt.plot(s1, s2)
#         plt.plot(s3, s4)
        
        ### ratio
        #ref https://matplotlib.org/examples/pylab_examples/equal_aspect_ratio.html
        #ref https://stackoverflow.com/questions/7965743/how-can-i-set-the-aspect-ratio-in-matplotlib
#         plt.axes().set_aspect('equal', 'datalim')
        plt.axes().set_aspect('equal')
#         plt.axes().set_aspect(2)
#         plt.set_aspect(2)
        
        #ref https://stackoverflow.com/questions/8209568/how-do-i-draw-a-grid-onto-a-plot-in-python answered Nov 21 '11 at 11:00
        
#         fig = plt.figure()
#         ax = fig.gca()
#         ax.set_xticks(np.arange(-1, 1, 0.1))
#         ax.set_yticks(np.arange(-1, 1, 0.1))
        
        plt.grid(b=None, which='major', axis='both')
        
        plt.xlabel("sin(x)")
#         plt.xlabel("sin(x + %.3f)" % a)
        plt.ylabel("cos(x * %.3f)" % a)
#         plt.ylabel("cos(x + %.3f)" % a)
#         plt.ylabel("cos(x)")
        
        plt.title("a = %.3f" % a)
        
#         plt.show()
        plt.savefig(fpath_Full)
        
        
        ### close
        plt.close(fig)
        
#         print()
#         print("[%s:%d] file saved => %s" % \
#                 (os.path.basename(libs.thisfile()), libs.linenum()
#                 , fpath_Full
#                 ), file=sys.stderr)
    #/for a in np.arange(1,3):


    
#     plt.close(fig)
#     plt.close(fig)
    
#     plt.show()
    
#/def test_2():

def test_2():
    
    #from : C:\WORKS_2\WS\WS_Others\JVEMV6\34\libs\labs.py
    a = 1
    
    s1 = [np.sin(x) for x in np.arange(-np.pi, np.pi, np.pi / 360)]
    s2 = [np.sin(x + a) for x in np.arange(-np.pi, np.pi, np.pi / 360)]

    '''###################
        file path        
    ###################'''
    dpath_Out = "C:\\WORKS_2\\WS\\WS_Others\\prog\\D-7\\2_2\\VIRTUAL\\Admin_Projects\\others\\VX7GLZ\\28_physics\\1_\\_16"
    ### fpath full
    fpath_Full = "%s\\tmp.%s.a=%.1f.png" % (dpath_Out, libs.get_TimeLabel_Now(), a)
    
    '''###################
        plot
    ###################'''    
    plt.plot(s1, s2)
    
    plt.savefig(fpath_Full)

    print()
    print("[%s:%d] file saved => %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , fpath_Full
            ), file=sys.stderr)
    
#     plt.close(fig)
#     plt.close(fig)
    
#     plt.show()
    
#/def test_2():


def test_1():
    
    '''###################
        vars        
    ###################'''
    dpath_Out = "C:\\WORKS_2\\WS\\WS_Others\\free\\VX7GLZ_science-research\\28_Physics\\1_\\_15"
    
    #ref https://stackoverflow.com/questions/9622163/save-plot-to-image-file-instead-of-displaying-it-using-matplotlib answered Apr 28 '15 at 22:35
    fig, ax = plt.subplots( nrows=1, ncols=1 )
    
    x = np.arange(-100, 100, 0.1)
#     x = np.arange(0, 100, 0.1)
    
    a = np.arange(-2, 2, 0.5)
    
#     b = 2; d = 2
#     a = 2; b = 2; d = 2
    a = -2.0; b = 2; d = 2
#     a = 2.0; b = 2; d = 2
    
    y = [i**3 + a * i**2 + b * i + d for i in x]
#     
    ax.plot(x,y)
#     
    ax.show()

#     ### fpath full
    fpath_Full = "%s\\tmp.%s.a=%.1f.png" % (dpath_Out, libs.get_TimeLabel_Now(), a)
#     fpath_Full = "%s\\tmp.%s.png" % (dpath_Out, libs.get_TimeLabel_Now())
#     
#     fig.savefig(fpath_Full)
    
#     time_Label = libs.get_TimeLabel_Now()
    
#     for num in a:
#         
#         y = [i**3 + a * i**2 + b * i + d for i in x]
#         
#         ax.plot(x,y)
#         
#         ### fpath full
#         fpath_Full = "%s\\tmp.%s.a=%s.png" % (dpath_Out, time_Label, str(num))
#         
#         fig.savefig(fpath_Full)

# #     fig.savefig('tmp.20180217_134221.png')
#         
#         ### reset fig
#         fig, ax = plt.subplots( nrows=1, ncols=1 )

    print()
    print("[%s:%d] file saved => %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , fpath_Full
            ), file=sys.stderr)
    
    plt.close(fig)

#/def test_1():

def exec_prog(): # from : 
    
    '''###################
        ops        
    ###################'''
    test_3()
#     test_2()
#     test_1()
    
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



