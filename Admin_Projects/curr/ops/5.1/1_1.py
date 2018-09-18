# -*- coding: utf-8 -*-
'''
file : C:\WORKS_2\WS\WS_Others\prog\D-7\2_2\VIRTUAL\Admin_Projects\curr\ops\5.1\1_1.py
orig : C:\WORKS_2\WS\WS_Others.Art\JVEMV6\46_art\VIRTUAL\Admin_Projects\ip\data\ops\1_1.py
at : 2018/09/14 06:37:44

pushd C:\WORKS_2\WS\WS_Others\prog\D-7\2_2\VIRTUAL\Admin_Projects\curr\ops\5.1
python 1_1.py

'''
###############################################
import sys
from _datetime import datetime
from numpy import append

'''###################
    import : original files        
###################'''
sys.path.append('.')
sys.path.append('..')

sys.path.append('C:/WORKS_2/WS/WS_Others/prog/D-7/2_2/VIRTUAL/Admin_Projects')
# sys.path.append('C:/WORKS_2/WS/WS_Others/prog/D-7/2_2/VIRTUAL/Admin_Projects/mm')

from mm.libs_mm import cons_mm, cons_fx, libs, libfx

'''###################
    import : built-in modules        
###################'''
import os

###############################################
def show_Message() :
    
    msg = '''
    <Options>
    -v	Volume down the amplitude --> 1.0 * v / 1000
    -f	Base frequency ---> e.g. 262 for the A tone
    -p	Phase of the sine curves ---> sin(2 * np.pi * f0 * n * phase / fs)'''
    
    print (msg)

def test_1():

    '''###################
        file path
    ###################'''
    dpath_Log_Fx = "C:\\Users\\iwabuchiken\\AppData\\Roaming\\MetaQuotes\\Terminal\\56FC49B0C953127FDE33461B90444E81\\MQL4\\Files\\Logs"
    fname_Log_Fx = "dev.20180914_063011.log"
#     fname_Log_Fx = "dev.20180913_084909.log"
#     fname_Log_Fx = "dev.20180913_084909.SHRIK-500.log"
    
    fpath_Log_Fx = os.path.join(dpath_Log_Fx, fname_Log_Fx)
    
    dpath_Log = "C:\\WORKS_2\\WS\\WS_Others\\prog\\D-7\\2_2\\VIRTUAL\\Admin_Projects\\curr\\ops\\5.1"
    fname_Log = "log_CountTicks.%s.log" % libs.get_TimeLabel_Now()
    
    fpath_Log = os.path.join(dpath_Log, fname_Log)
    
    '''###################
        file : open
    ###################'''
    f_Log_FX = open(fpath_Log_Fx, "r")
    
    
    '''###################
        read file content
    ###################'''
    data = f_Log_FX.readlines()
    
    print("[%s:%d] len(data) = %d" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , len(data)
            ), file=sys.stderr)
    
    '''###################
        extract target tokesn from each line
    ###################'''
#     ['[2018.09.13', '08:49:18', '/', 'fnc_CountTick.mq4:289]cntOf_Ticks', '=', '1', '/', 'cntOf_Ticks_In_The_Bar', '=', '1', '(2018.09.13', '08:49:18)']
        # >>> len(b)
        # 12
    lenOf_Data = len(data)
    
    aryOf_Hit_Data = []
    
    for i in range(1, lenOf_Data - 1):
        
        item = data[i]
        item2 = data[i - 1]
        
        # split
        tokens = item.split(" ")
        tokens2 = item2.split(" ")
        
        # tokens
        cntOf_Ticks = tokens[5]
        cntOf_Ticks_In_The_Bar = tokens[9]
        dateTime_Local = (" ".join([tokens[10], tokens[11]])).strip()
        dateTime_Local2 = (" ".join([tokens2[10], tokens2[11]])).strip()
#         dateTime_Local = " ".join([tokens[10], tokens[11]])
#         dateTime_Local = tokens[10]
        
        # judge
        if cntOf_Ticks_In_The_Bar == "1" : #if cntOf_Ticks_In_The_Bar == "1"

            # append
#             aryOf_Hit_Data.append([cntOf_Ticks, cntOf_Ticks_In_The_Bar, dateTime_Local])
            
            #debug
#             msg = "[%s:%d] dateTime_Local = %s / prev count = %s" % \
#             msg = "dateTime_Local = %s / prev count = %s" % \
            msg = "dateTime_Local\t%s\tprev count\t%s" % \
                (
                     dateTime_Local2, tokens2[9]
#                      dateTime_Local, tokens2[9]
                )
                
#             print(msg, file=sys.stderr)
            
            # append
            aryOf_Hit_Data.append(msg)
            
        #/if cntOf_Ticks_In_The_Bar == "1"

    #/for item in data:
    
    '''###################
        last item
    ###################'''
    #debug
    item = data[-1]
    tokens = item.split(" ")
    dateTime_Local = (" ".join([tokens[10], tokens[11]])).strip()
    
#     msg = "dateTime_Local = %s / prev count = %s" % \
    msg = "dateTime_Local\t%s\tprev count\t%s" % \
                (
                    dateTime_Local, tokens[9]
#                     dateTime_Local, tokens[9]
                )
    
    # append
    aryOf_Hit_Data.append(msg)
    
#     print(msg, file=sys.stderr)            
    
    '''###################
        file : close
    ###################'''
    f_Log_FX.close()

    '''###################
        report
    ###################'''
    # file : open
    f_Log = open(fpath_Log, "a")
    
    #debug
    msg = "[%s:%d] len(aryOf_Hit_Data) = %d" % \
                    (os.path.basename(libs.thisfile()), libs.linenum()
                    , len(aryOf_Hit_Data)
                    )
    
    print(msg, file=sys.stderr)
    
    # write file
    # file path
#     msg = "[%s / %s:%d] file = %s\n" % \
    msg = "[%s / %s:%d]\nfile = %s\ndir = %s" % \
                    (
                    libs.get_TimeLabel_Now()
                    , os.path.basename(libs.thisfile()), libs.linenum()
                    , fname_Log_Fx, dpath_Log_Fx
#                     , fpath_Log_Fx
                    )
    
    f_Log.write(msg)
    
    # len of hit data
    msg = "[%s / %s:%d] len(aryOf_Hit_Data) = %d\n" % \
                    (
                    libs.get_TimeLabel_Now()
                    , os.path.basename(libs.thisfile()), libs.linenum()
                    , len(aryOf_Hit_Data)
                    )
    
    f_Log.write(msg)
    
    for item in aryOf_Hit_Data:
    
#         print(item)
        
        # write file
        f_Log.write(item)
        f_Log.write("\n")
        
    #/for item in aryOf_Hit_Data:

    # separation line
    f_Log.write("\n")
    
    # file : close
    f_Log.close()
    
    '''###################
        message
    ###################'''
    print()
    print("[%s:%d] test_1 =======================" % \
                    (os.path.basename(libs.thisfile()), libs.linenum()

                    ), file=sys.stderr)
#/ def test_1():

def exec_prog():
    
    '''###################
        ops        
    ###################'''
#     test_8__Matplotlib__Bar_Chart()
    test_1()
    
    print("[%s:%d] exec_prog() => done" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
    
#def exec_prog()

'''
<usage>
test_1.py [-fXXX]  #=> frequency
test_1.py -f402
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
    
    print("[%s:%d] done" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
#     print "[%s:%d] done" % (thisfile(), linenum())
