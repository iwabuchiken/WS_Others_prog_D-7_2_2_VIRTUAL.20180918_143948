'''###################
            
    C:\WORKS_2\WS\WS_Others\prog\D-7\2_2\VIRTUAL\Admin_Projects\curr\data\miscs
    
<Start server>
r w && r d2
    
###################'''
from sympy.solvers.tests.test_constantsimp import C1

'''###################
    import : django        
###################'''
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django import template
#ref https://stackoverflow.com/questions/29304845/how-to-disable-cache-in-django-view
from django.views.decorators.cache import never_cache

'''###################
    import : original files        
###################'''
import sys
sys.path.append('.')
sys.path.append('..')
# sys.path.append('C:/WORKS_2/WS/WS_Others/free/fx/82_')
# 
# sys.path.append('C:/WORKS_2/WS/WS_Others/free/VX7GLZ_science-research/31_Materials')
sys.path.append('C:/WORKS_2/WS/WS_Others/prog/D-7/2_2/VIRTUAL/Admin_Projects/mm')

from mm.libs_mm import cons_mm, cons_fx, libs, libfx
# from mm.libs_mm import libs
# from mm.libs_mm import libfx



from Admin_Projects.definitions import ROOT_DIR
from Admin_Projects.definitions import DPATH_ROOT_CURR

'''###################
    import : built-in modules        
###################'''
import os
#ref https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory
from os import listdir
from os.path import isfile, join, splitext
# from os.path import splitext

from sympy.physics.units.dimensions import action
from pip._vendor.requests.api import request
from macpath import defpath
from pathlib import Path

import subprocess, copy, time, glob, re, datetime
#from C:\WORKS_2\WS\WS_Others\free\VX7GLZ_science-research\31_Materials\1_\1_1.3.py
import xml.etree.ElementTree as ET

# import datetime
# import copy
# import time

# import glob

# import re




'''######################################
    funcs        
######################################'''
def write_Log(str_Line):

    dpath = cons_fx.FPath.dpath_Data_Miscs.value
        
    fname = "detect_peaks.log"
    
    fpath = "%s/%s" % (dpath, fname)
    
    fout = open(fpath, "a")
    
    fout.write("\n")
    #                     fout.write("sumOf_Diff < (sum_Max / 2)" % (libs.get_TimeLabel_Now()))
    
#     msg = "[%s:%d] (%02d) %s : sumOf_Diff < (sum_Max / 2) : sumOf_Diff = %03f sum_Max = %03f" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#             , idx, item.dateTime_Local, sumOf_Diff, sum_Max
#             )
    fout.write(str_Line)
    
    fout.write("\n")
    
    fout.close()

#/ def write_Log(str_Line):

def get_CurrencyData_FileName(request):
    
#     pass
    
    print("[%s:%d] get_CurrencyData_FileName()" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        
        ), file=sys.stderr)

    '''###################
        file list        
    ###################'''
    
    
    '''###################
        return        
    ###################'''
    fname = "49_20_file-io.USDJPY.Period-H1.Days-1200.Bars-28800.20180428_073251.csv"
    
    return fname

#/ def get_CurrencyData_FileName(request):

def exec_correlations(request):
    
    '''###################
        time        
    ###################'''
    time_Start = time.time()
    
    '''###################
        time        
    ###################'''
    time_Elapsed = time.time() - time_Start
    
    message = "done (time : %02.3f sec)" % (time_Elapsed)

    dic = {"msg" : message}
    
#     print()
#     print("[%s:%d] rendering..." % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#         
#         ), file=sys.stderr)
    
    return render(request, 'curr/exec_correlations.html', dic)
    
#/def exec_correlations(request):
    
def correlations(request):
    
    dic = {}
    
    return render(request, 'curr/correlations.html', dic)
    
#/def correlations(request):
    
def exec_updown_patterns(request):
    
    '''###################
        time        
    ###################'''
    time_Start = time.time()
    
    '''###################
        param : body volume : up        
    ###################'''
    threshHold_Up = request.GET.get('body_volume_up', False)
    
    if threshHold_Up == False : #if threshHold_Up == False

        threshHold_Up = 0.1
        
    else:
        
        threshHold_Up = float(threshHold_Up)
        
    #/if threshHold_Up == False
    
    '''######################################
        updown
    ######################################'''
    '''###################
        get : list of bardatas        
    ###################'''
    lo_BarDatas = libfx.get_Listof_BarDatas()
    
    # validate
    alert = ""
    
    if lo_BarDatas == None : #if lo_BarDatas == None

        print()
        print("[%s:%d] lo_BarDatas => None" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            ), file=sys.stderr)
        
        # set : message
        alert = "ERROR : Get BarData ==> returned None"
        
    #/if lo_BarDatas == None

    '''###################
        pattern match  
              
    ###################'''
    lo_Updowns = [1,1,1]
    
#     threshHold_Up = 0.1
    threshHold_Down = 0.1
#     threshHold_Up = 0.2
#     threshHold_Down = 0.2
    
    lo_Matched = libfx.pattern_Match__Body_Updown(
                lo_BarDatas, lo_Updowns, threshHold_Up, threshHold_Down)
    
    '''###################
        report        
    ###################'''
    if len(lo_Matched) > 0 : #if len(lo_Matched) > 0
    
        match_1 = lo_Matched[0]
        
        ### display
        for i in range(len(match_1)):
    
            print()
            print("[%s:%d] match_1[%d].dateTime_Local => %s" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                , i, match_1[i].dateTime_Local
                ), file=sys.stderr)
            
        #/for i in range(len(match_1)):

        
#         print()
#         print("[%s:%d] match_1 => %s" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#             , match_1
#             ), file=sys.stderr)
        
    #/if len(lo_Matched) > 0
    
    '''###################
        time        
    ###################'''
    time_Elapsed = time.time() - time_Start
    
    '''###################
        message        
    ###################'''
    lenOf_Matched = len(lo_Matched)
    
    message = "done (time : %02.3f sec) (matched : %d)" \
                % (time_Elapsed, lenOf_Matched)
#                 % (time_Elapsed, len(lo_Matched))

    print()
    print("[%s:%d] message => %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , message
            ), file=sys.stderr)
    
    dic = {"msg" : message, "alert" : alert}
#     dic = {"msg" : message}
    
    '''###################
        save history
    ###################'''
    dpath_Out = DPATH_ROOT_CURR + "/" + "data/log"
    
    fname_Out = "pattern_match_history.log"
    
    fpath_Out_Full = dpath_Out + "/" + fname_Out
    
    fout = open(fpath_Out_Full, "a")
    
    ### timestamp
    fout.write("[%s : pattern match] ======================" \
            % libs.get_TimeLabel_Now(string_type = libs.TimeLabel.STRING_TYPE_BASIC.value))
#                 % libs.get_TimeLabel_Now(string_type = "basic"))
#     fout.write("updown pattern : %s" % str_Updown)
    fout.write("\n")
    
    ### file name
    fout.write("file : %s" % cons_fx.FPath.fname_In_CSV.value)
#     fout.write("updown pattern : %s" % str_Updown)
    fout.write("\n")
    
    ### updown pattern
    fout.write("updown pattern : %s" % ",".join([str(x) for x in lo_Updowns]))
#     fout.write("updown pattern : %s" % ",".join(lo_Updowns))
#     fout.write("updown pattern : %s" % str_Updown)
    fout.write("\n")
    
    ### threshHold_Up, Down
    fout.write("threshHold_Up = %.3f / threshHold_Down = %.3f" \
                    % (threshHold_Up, threshHold_Down))
    fout.write("\n")
    
    ### num of matched
    fout.write("num of matched : %d" % lenOf_Matched)
#     fout.write("num of matched : %d" % len(lenOf_Matched))
    fout.write("\n")
    
    ### matched data
    if lenOf_Matched > 0 : #if lenOf_Matched > 0
            
        for matched in lo_Matched:
#         for item in lo_Matched:
            
            for item in matched:
            
                fout.write("[%s:%d] datetime : %s / diff = %.3f" % \
                    (os.path.basename(libs.thisfile()), libs.linenum()
                    , item.dateTime_Local, (item.price_Close - item.price_Open)
                    )
                )
                 
                fout.write("\n")
                
                
            #/for item in matched:

            ### separator line
            fout.write("\n")
            
#             fout.write("[%s:%d] datetime : %s / diff = %.3f" % \
#                 (os.path.basename(libs.thisfile()), libs.linenum()
#                 , item.dateTime_Local, (item.price_Close - item.price_Open)
#                 )
#             )
#             
#             fout.write("\n")
            
        #/for item in lo_Matched:
        
    #/if lenOf_Matched > 0
    
    ### separation line
    fout.write("\n")
    fout.write("\n")
            
    ### close file
    fout.close()
    
    '''###################
        render        
    ###################'''
    return render(request, 'curr/exec_updown_patterns.html', dic)
    
#/def exec_updown_patterns(request):

def updown_patterns(request):

    dic = {}
#     dic = {'action' : action, "message" : message}
    
    '''###################
        get : referer        
    ###################'''
    referer_MM = "http://127.0.0.1:8000/curr/"
    
    referer_Current = request.META.get('HTTP_REFERER')


    '''###################
        render        
    ###################'''
    if referer_Current == referer_MM : #if referer_Current == referer_MM
    
        print()
        print("[%s:%d] referer_Current == referer_MM (current = %s / referer = %s" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                ,referer_Current, referer_MM
                ), file=sys.stderr)
    
        return render(request, 'curr/updown_patterns.html', dic)
#         return render(request, 'mm/numbering.html', dic)
        
    else : #if referer_Current == referer_MM

        print()
        print("[%s:%d] referer_Current <> referer_MM (current = %s / referer = %s" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                ,referer_Current, referer_MM
                ), file=sys.stderr)

        return render(request, 'curr/updown_patterns_full.html', dic)

def gen_peak_data(request):
    
#     #test
#     print("[%s:%d] sleeping..." % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#         
#         ), file=sys.stderr)
#     
#     time.sleep(2);

    '''###################
        vars        
    ###################'''
    dic = {}

    
    '''###################
        get : param : pair name        
    ###################'''
    nameOf_CurrencyPair = request.GET.get('currency_pair', False)
    
    # default
    if nameOf_CurrencyPair == False : #if nameOf_CurrencyPair == False
    
        nameOf_CurrencyPair = "USDJPY"
        
    #/if nameOf_CurrencyPair == False
    
    print("[%s:%d] nameOf_CurrencyPair => %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , nameOf_CurrencyPair
            ), file=sys.stderr)
    
    # set name
    dic['currency_pair'] = nameOf_CurrencyPair
    
    '''###################
        get : file path        
    ###################'''
    dpath_CSV = cons_fx.FPath.dpath_In_CSV.value
    
    print("[%s:%d] dpath_CSV => %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , dpath_CSV
            ), file=sys.stderr)
    
    fpath_Glob = "%s\\*.csv" % (dpath_CSV)
#     fpath_Glob = "%s\\*(*).csv" % (dpath_CSV)
#     fpath_Glob = "%s\\*.png" % (dpath_Full)

    #ref glob https://stackoverflow.com/questions/14798220/how-can-i-search-sub-folders-using-glob-glob-module-in-python answered Feb 10 '13 at 13:31    
    lo_Files = glob.glob(fpath_Glob)

    lo_Files.sort()

    print("[%s:%d] len(lo_Files) => %d" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , len(lo_Files)
            ), file=sys.stderr)
    
    # set list
    dic['lo_Files'] = [os.path.basename(x) for x in lo_Files]
#     dic['lo_Files'] = lo_Files
    
    '''###################
        main dir
    ###################'''
    dic['MAIN_DIR'] = dpath_CSV
    
    '''###################
        get : referer        
    ###################'''
#     referer_MM = "http://127.0.0.1:8000/curr/"
    referer_MM = "http://127.0.0.1:8000/curr/basics/"
    
    referer_Current = request.META.get('HTTP_REFERER')


    '''###################
        render        
    ###################'''
    '''###################
        time        
    ###################'''
#     dic = {}
    
    
#     time_Elapsed = time.time() - time_Start
    
#     message = "done (time : %02.3f sec)" % (time_Elapsed)

#     dic["msg"] = "rendering... (%s)(time : %02.3f sec)" \
#                     % (libs.get_TimeLabel_Now(), time_Elapsed)
    dic["msg"] = "rendering... (%s)" % libs.get_TimeLabel_Now()
    
    if referer_Current == referer_MM : #if referer_Current == referer_MM
    
        print()
        print("[%s:%d] referer_Current == referer_MM (current = %s / referer = %s" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                ,referer_Current, referer_MM
                ), file=sys.stderr)
    
        return render(request, 'curr/gen_peak_data.html', dic)
#         return render(request, 'mm/numbering.html', dic)
        
    else : #if referer_Current == referer_MM

        print()
        print("[%s:%d] referer_Current <> referer_MM (current = %s / referer = %s" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                ,referer_Current, referer_MM
                ), file=sys.stderr)

        return render(request, 'curr/gen_peak_data_full.html', dic)
#/ def gen_peak_data(request):

def exec_Gen_PeakData(request):

    '''###################
        exec
    ###################'''
    fname = request.GET.get('fname', False)
    
    # validate
    if fname == False : fname = cons_fx.FPath.fname_Gen_PeakData_Dflt.value
    
    '''###################
        exec
    ###################'''
    dic = {}
    
    dpath = cons_fx.FPath.dpath_In_CSV.value
    
#     fname = get_CurrencyData_FileName(request)
    
#     fname = cons_fx.FPath.fname_In_CSV.value
#     fname = "49_20_file-io.USDJPY.Period-H1.Days-1200.Bars-28800.20180428_073251.csv"
#     fname = cons_fx.FPath.fname_In_CSV.value
    
    header_Length   = 2
    
    skip_Header     = False

    #debug
#     lo_BarDatas = None
    lo_BarDatas = libfx.get_Listof_BarDatas_2(
                        dpath, fname, header_Length, skip_Header)
    
#     #test
#     lo_BarDatas = None
    
    # validate
    if lo_BarDatas == None : #if lo_BarDatas == None
    
        print()
        print("[%s:%d] lo_BarDatas => None" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                
                ), file=sys.stderr)

    
        msg = "lo_BarDatas => None"
        dic = {"msg" : msg}
    
        return render(request, 'curr/error.html', dic)
#         return render(request, 'curr/error.html', msg)

    else : #if lo_BarDatas == None
    
        print()
        print("[%s:%d] lo_BarDatas => %d" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                , len(lo_BarDatas)
                ), file=sys.stderr)
    
    # get peak data
    result = basics_Ops_1__DetectPieaks__V2(request, lo_BarDatas, dpath, fname)
#     result = basics_Ops_1__DetectPieaks(request, lo_BarDatas, dpath, fname)
    
    #debug
    print()
    print("[%s:%d] result => %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , result
            ), file=sys.stderr)
    
    '''###################
        get : referer        
    ###################'''
    referer_MM = "http://127.0.0.1:8000/curr/gen_peak_data/"
#     referer_MM = "http://127.0.0.1:8000/curr/"
    
    referer_Current = request.META.get('HTTP_REFERER')


    '''###################
        render        
    ###################'''
    dic = {}
#     dic["msg"] = "rendering... (%s)(time : %02.3f sec)" \
    dic["msg"] = "rendering... (%s)" \
                    % (libs.get_TimeLabel_Now())
#                     % (libs.get_TimeLabel_Now(), time_Elapsed)
#     dic["msg"] = "rendering... (%s)(time : %02.3f sec)" % libs.get_TimeLabel_Now()
    
    if referer_Current == referer_MM : #if referer_Current == referer_MM
    
        print()
        print("[%s:%d] referer_Current == referer_MM (current = %s / referer = %s" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                ,referer_Current, referer_MM
                ), file=sys.stderr)
    
        return render(request, 'curr/exec_Gen_PeakData.html', dic)
#         return render(request, 'mm/numbering.html', dic)
        
    else : #if referer_Current == referer_MM

        print()
        print("[%s:%d] referer_Current <> referer_MM (current = %s / referer = %s" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                ,referer_Current, referer_MM
                ), file=sys.stderr)

        return render(request, 'curr/exec_Gen_PeakData.html', dic)


#/ def exec_Gen_PeakData():

def basics_Ops(request, lo_BarDatas):
    
    '''###################
        ops        
    ###################'''
    lo_Data = []
    
    cntOf_Item = 0
    
    sumOf_Diff_OC = 0
    
    for item in lo_BarDatas:

        if item.diff_OC >= 0 : #if item.diff_OC >= 0

            val = 1
        
        else : #if item.diff_OC >= 0
        
            val = -1
        
        #/if item.diff_OC >= 0
        
        # append data
        sumOf_Diff_OC += item.diff_OC
        
        lo_Data.append([cntOf_Item, val, item.diff_OC, item.dateTime_Local, sumOf_Diff_OC])
#         lo_Data.append(val)
        
        # count
        cntOf_Item += 1
        
    #/for item in lo_BarDatas:
    
    print()
    print("[%s:%d] lo_Data => " % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                
                ), file=sys.stderr)
    
    for item in lo_Data[:20]:
            
        print(item)
        
    #/for item in lo_Data[:20]:

#     print(lo_Data[:20])
    
    '''###################
        write data        
    ###################'''
    dpath = cons_fx.FPath.dpath_Data_Miscs.value
    
    fname = "lo_BarDatas.20180502_113828.txt"
    
    fpath = "%s/%s" % (dpath, fname)
    
    fout = open(fpath, "w")
    
    for item in lo_Data:
    
        str_Line = ""
        
        for elem in item:
            
            str_Line += "%s," % elem
        
        fout.write(str_Line)
        
        fout.write("\n")
        
    #/for elem in item:
    
    fout.close()
        
    #/for item in lo_Data:
    
    print()
    print("[%s:%d] lo_Data => written" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                
                ), file=sys.stderr)

    
#/ def basics_Ops(request, lo_BarDatas):

def basics_Ops_1__DetectPieaks__V2(request, lo_BarDatas, dpath_Data, fname_Data):
# def basics_Ops_1__DetectPieaks(request, lo_BarDatas):
    
    '''###################
        vars        
    ###################'''
    idx         = 0
    idx_Start   = 0
    sumOf_Diff  = 0.0
    sum_Max     = 0.0
    f_New       = True
    
    lo_Max      = []
    
    idxOf_SumMax = -1
    
    '''###################
        file : finish        
    ###################'''
    dpath = cons_fx.FPath.dpath_Data_Miscs.value
        
    fname = "detect_peaks.log"
    
    fpath = "%s/%s" % (dpath, fname)
    
    fout = open(fpath, "a")
    
    fout.write("\n")
    fout.write("[%s]======================" % (libs.get_TimeLabel_Now()))
    fout.write("\n")
    
    fout.close()

    '''###################
        flows        
    ###################'''
    lo_BarDatas_Tmp = copy.deepcopy(lo_BarDatas)
    
    lo_BarDatas_Tmp.reverse()
    
    for item in lo_BarDatas_Tmp :
    
#         #debug
#         if idx > 50 : break
    
#         # reset idx_Start
#         if f_New == True : idx_Start = idx
        
        '''###################
            j : 1
        ###################'''
        diff_OC = item.diff_OC
        
        if diff_OC < 0 : #if item.diff_OC < 0
    
            '''###################
                j : 4
            ###################'''
            if f_New == True : #if f_New == True
                
                # next index in the loop f1
                #count
                idx += 1
                
                # next index
                continue
            
            else : #if f_New == True
            
                # sum of dill
                sumOf_Diff += diff_OC
#                 sumOf_Diff -= diff_OC
            
                '''###################
                    j : 5
                ###################'''
                if sumOf_Diff < (sum_Max / 2) : #if sumOf_Diff < (sum_Max / 2)

                    '''###################
                        file : finish        
                    ###################'''
                    dpath = cons_fx.FPath.dpath_Data_Miscs.value
                        
#                     fname = "detect_peaks.log"
#                     
#                     fpath = "%s/%s" % (dpath, fname)
#                     
#                     fout = open(fpath, "a")
#                     
#                     fout.write("\n")
#                     fout.write("sumOf_Diff < (sum_Max / 2)" % (libs.get_TimeLabel_Now()))
                    
#                     msg = "[%s:%d] (%02d) %s : sumOf_Diff < (sum_Max / 2) : sumOf_Diff = %03f sum_Max = %03f" % \
#                             (os.path.basename(libs.thisfile()), libs.linenum()
#                             , idx, item.dateTime_Local, sumOf_Diff, sum_Max
#                             )
#                     fout.write(msg)
# 
#                     fout.write("\n")
                    
#                     fout.close()

                    '''###################
                        ops : sumOf_Diff ---> went under
                    ###################'''
                    # reset flag    ### j : 5 / y : 1
                    f_New = True
                    
#                     # report
#                     msg = "[%s:%d] (%02d) %s : f_New => back to %s" % \
#                             (os.path.basename(libs.thisfile()), libs.linenum()
#                             , idx, item.dateTime_Local, f_New
#                             )
# 
#                     write_Log(msg)
                    
                    '''###################
                        append data        
                    ###################'''
                    # register : sum_Max, idx    ### j : 5 / y : 2
                    data = \
                            (round(sum_Max, 3)
                            , int(idx_Start)
                            , int(idxOf_SumMax)
                            , int(idx)
                            
                            # datetime ---> Local
                            , lo_BarDatas_Tmp[idx_Start].dateTime_Local
                            , lo_BarDatas_Tmp[idxOf_SumMax].dateTime_Local
                            , item.dateTime_Local
                            
                            # datetime ---> default
                            , lo_BarDatas_Tmp[idx_Start].dateTime
                            , lo_BarDatas_Tmp[idxOf_SumMax].dateTime
                            , item.dateTime
#                             , item.dateTime_Local

                            # price_Close
                            , lo_BarDatas_Tmp[idx_Start].price_Close
                            , lo_BarDatas_Tmp[idxOf_SumMax].price_Close
                            , item.price_Close
                            
                            # BB prices : idxOf_SumMax
                            , lo_BarDatas_Tmp[idxOf_SumMax].bb_2S
                            , lo_BarDatas_Tmp[idxOf_SumMax].bb_1S
                            , lo_BarDatas_Tmp[idxOf_SumMax].bb_Main
                            , lo_BarDatas_Tmp[idxOf_SumMax].bb_M1S
                            , lo_BarDatas_Tmp[idxOf_SumMax].bb_M2S
                            
                            )
                    
                    lo_Max.append(data)
                    
                    ### j : 5 / y : 3
                    # reset : sum_Max
                    sum_Max = 0.0
                    
                    # reset : sumOf_Diff
                    sumOf_Diff = 0.0
                    
                    # next index in the loop f1
                    #count
                    idx += 1
                    
                    # next index
                    continue
                
                else : #if sumOf_Diff < (sum_Max / 2)
                
                    # next index in the loop f1
                    #count
                    idx += 1
                    
                    # next index
                    continue
                
                #/if sumOf_Diff < (sum_Max / 2) ### j : 5
                
            #/if f_New == True ### j : 3
        
        else : #if item.diff_OC < 0 ### j : 1
        
            # f_New ---> on
            if f_New == True : 
                
                # set flag
                f_New = False
                
                # set : idx_Start
                idx_Start = idx
                
                # report
                dpath = cons_fx.FPath.dpath_Data_Miscs.value
                
                fname = "detect_peaks.log"
                
                fpath = "%s/%s" % (dpath, fname)
                
                fout = open(fpath, "a")
                
#                 msg = "[%s:%d] (%02d) %s : f_New ==> turned to False" % \
#                         (os.path.basename(libs.thisfile()), libs.linenum()
#                         , idx, item.dateTime_Local
#                         )
#                 fout.write(msg)
#                 
#                 fout.write("\n")
            
            # sum of diff
            sumOf_Diff += diff_OC
            
            '''###################
                j : 2        
            ###################'''
            if sumOf_Diff > sum_Max : #if sumOf_Diff> sum_Max
                
                # update sum_Max
                sum_Max = sumOf_Diff
                
                # update index
                idxOf_SumMax = idx
            
                # next index in the loop f1
                #count
                idx += 1
                
                # next index
                continue

            else : #if sumOf_Diff> sum_Max
            
                # next index in the loop f1
                #count
                idx += 1
                
                # next index
                continue
            
            #/if sumOf_Diff> sum_Max
        
        #/if item.diff_OC < 0 ### j : 1
        
        '''###################
            j : 3
            next item
        ###################'''
        # counter
        idx += 1
        
        # next index in the loop f1
        continue
        
    #/for item in lo_BarDatas:

    '''###################
        write : lo_Max
    ###################'''
    # report
    dpath = cons_fx.FPath.dpath_Data_Miscs.value
    
    fname = "detect_peaks.sum_Max.%s.log" % libs.get_TimeLabel_Now()
    
    fpath = "%s/%s" % (dpath, fname)
    
    fout = open(fpath, "w")
    
    # header : meta data
    msg = "source = %s (%s)" % \
            (fname_Data, dpath_Data)
    
    # column names
            # data = \
            #         (round(sum_Max, 3)
            #         , int(idx_Start)
            #         , int(idxOf_SumMax)
            #         , int(idx)
            #         
            #         # datetime ---> Local
            #         , lo_BarDatas_Tmp[idx_Start].dateTime_Local
            #         , lo_BarDatas_Tmp[idxOf_SumMax].dateTime_Local
            #         , item.dateTime_Local
            #         
            #         # datetime ---> default
            #         , lo_BarDatas_Tmp[idx_Start].dateTime
            #         , lo_BarDatas_Tmp[idxOf_SumMax].dateTime
            #         , item.dateTime
            # #                             , item.dateTime_Local
            # # price_Close
            # , lo_BarDatas_Tmp[idx_Start].price_Close
            # , lo_BarDatas_Tmp[idxOf_SumMax].price_Close
            # , item.price_Close

            # # BB prices : idxOf_SumMax
            # , lo_BarDatas_Tmp[idxOf_SumMax].bb_2S
            # , lo_BarDatas_Tmp[idxOf_SumMax].bb_1S
            # , lo_BarDatas_Tmp[idxOf_SumMax].bb_Main
            # , lo_BarDatas_Tmp[idxOf_SumMax].bb_M1S
            # , lo_BarDatas_Tmp[idxOf_SumMax].bb_M2S
            
            #         )

    fout.write(msg)
    
    fout.write("\n")
    
    msg = "Max\tidx_Start\tidxOf_SumMax\tidx(when ended)" \
            + "\tdateTime_Local(started)\tdateTime_Local(max)\tdateTime_Local(ended)" \
            + "\tdateTime(started)\tdateTime(max)\tdateTime(ended)" \
            + "\tprice_Close(started)\tprice_Close(max)\tprice_Close(ended)" \
            + "\tBB_2S(max)\tBB_1S(max)\tBB_Main(max)\tBB_M1S(max)\tBB_M2S(max)"
            
    fout.write(msg)
    fout.write("\n")
    
    # write
    for item in lo_Max:
        
#         msg = "%03f\t%02d\t%02d\t%02d\t%s" % \
        msg = "%03f\t%02d\t%02d\t%02d\t%s\t%s\t%s\t%s\t%s\t%s\t%.03f\t%.03f\t%.03f\t%.03f\t%.03f\t%.03f\t%.03f\t%.03f" % \
                (item[0], int(item[1]), int(item[2]), item[3], item[4],
                 
                 # dateTime
                 item[5], item[6], item[7], item[8], item[9]
                 
                 # price_Close
                 , float(item[10]), float(item[11]), float(item[12])
                 
                 # BB
                 , float(item[13]), float(item[14]), float(item[15]), 
                    float(item[16]), float(item[17])
                 )
                
        fout.write(msg)
        fout.write("\n")
        
    #/for item in lo_Max:

    
    fout.write("\n")
    
    fout.close()

    '''###################
        file : finish        
    ###################'''
    msg = "\n\n"
    
    write_Log(msg)
    
#     dpath = cons_fx.FPath.dpath_Data_Miscs.value
#         
#     fname = "detect_peaks.log"
#     
#     fpath = "%s/%s" % (dpath, fname)
#     
#     fout = open(fpath, "a")
#     
#     fout.write("\n\n")
#     
#     fout.close()

    
#/ def basics_Ops_1__DetectPieaks__V2(request, lo_BarDatas, dpath_Data, fname_Data)
    


def basics_Ops_1__DetectPieaks(request, lo_BarDatas, dpath_Data, fname_Data):
# def basics_Ops_1__DetectPieaks(request, lo_BarDatas):
    
    '''###################
        vars        
    ###################'''
    idx         = 0
    idx_Start   = 0
    sumOf_Diff  = 0.0
    sum_Max     = 0.0
    f_New       = True
    
    lo_Max      = []
    
    idxOf_SumMax = -1
    
    '''###################
        file : finish        
    ###################'''
    dpath = cons_fx.FPath.dpath_Data_Miscs.value
        
    fname = "detect_peaks.log"
    
    fpath = "%s/%s" % (dpath, fname)
    
    fout = open(fpath, "a")
    
    fout.write("\n")
    fout.write("[%s]======================" % (libs.get_TimeLabel_Now()))
    fout.write("\n")
    
    fout.close()

    '''###################
        flows        
    ###################'''
    lo_BarDatas_Tmp = copy.deepcopy(lo_BarDatas)
    
    lo_BarDatas_Tmp.reverse()
    
    for item in lo_BarDatas_Tmp :
#     for item in lo_BarDatas:
    
#         #debug
#         if idx > 50 : break
    
#         # reset idx_Start
#         if f_New == True : idx_Start = idx
        
        '''###################
            j : 1
        ###################'''
        diff_OC = item.diff_OC
        
        if diff_OC < 0 : #if item.diff_OC < 0
#             #report
# #             msg = "[%s:%d] (%02d) %s : diff_OC < 0 : %03f" % \
#             msg = "[%s:%d] (%02d) %s : diff_OC < 0 : %03f (f_New = %s)" % \
#                             (os.path.basename(libs.thisfile()), libs.linenum()
#                             , idx, item.dateTime_Local, diff_OC, f_New
#                             )
#                              
#             write_Log(msg)
    
            '''###################
                j : 4
            ###################'''
            if f_New == True : #if f_New == True
                
                # next index in the loop f1
                #count
                idx += 1
                
                # next index
                continue
            
            else : #if f_New == True
            
                # sum of dill
                sumOf_Diff += diff_OC
#                 sumOf_Diff -= diff_OC
            
                '''###################
                    j : 5
                ###################'''
                if sumOf_Diff < (sum_Max / 2) : #if sumOf_Diff < (sum_Max / 2)

                    '''###################
                        file : finish        
                    ###################'''
                    dpath = cons_fx.FPath.dpath_Data_Miscs.value
                        
                    fname = "detect_peaks.log"
                    
                    fpath = "%s/%s" % (dpath, fname)
                    
                    fout = open(fpath, "a")
                    
                    fout.write("\n")
#                     fout.write("sumOf_Diff < (sum_Max / 2)" % (libs.get_TimeLabel_Now()))
                    
                    msg = "[%s:%d] (%02d) %s : sumOf_Diff < (sum_Max / 2) : sumOf_Diff = %03f sum_Max = %03f" % \
                            (os.path.basename(libs.thisfile()), libs.linenum()
                            , idx, item.dateTime_Local, sumOf_Diff, sum_Max
                            )
                    fout.write(msg)

                    fout.write("\n")
                    
                    fout.close()

                    '''###################
                        ops : sumOf_Diff ---> went under
                    ###################'''
                    # reset flag    ### j : 5 / y : 1
                    f_New = True
                    
                    # report
                    msg = "[%s:%d] (%02d) %s : f_New => back to %s" % \
                            (os.path.basename(libs.thisfile()), libs.linenum()
                            , idx, item.dateTime_Local, f_New
                            )

                    write_Log(msg)
                    
                    '''###################
                        append data        
                    ###################'''
                    # register : sum_Max, idx    ### j : 5 / y : 2
                    data = (round(sum_Max, 3)
                            , int(idx_Start)
                            , int(idxOf_SumMax)
                            , int(idx)
                            , item.dateTime_Local
                            
                            )
#                     data = (round(sum_Max, 3)
#                             , int(idx_Start)
#                             , round(idxOf_SumMax, 3)
#                             , item.dateTime_Local
#                             
#                             )
#                     data = (round(sum_Max, 3), round(idxOf_SumMax, 3))
                    
                    
                    lo_Max.append(data)
#                     lo_Max.append((round(sum_Max, 3), round(idxOf_SumMax, 3)))
#                     lo_Max.append((sum_Max, idxOf_SumMax))
                    
                    ### j : 5 / y : 3
                    # reset : sum_Max
                    sum_Max = 0.0
                    
                    # reset : sumOf_Diff
                    sumOf_Diff = 0.0
                    
                    # next index in the loop f1
                    #count
                    idx += 1
                    
                    # next index
                    continue
                
                else : #if sumOf_Diff < (sum_Max / 2)
                
                    # next index in the loop f1
                    #count
                    idx += 1
                    
                    # next index
                    continue
#                     pass
                
                #/if sumOf_Diff < (sum_Max / 2) ### j : 5
                
                
            
            #/if f_New == True ### j : 3
    
    
        
        else : #if item.diff_OC < 0 ### j : 1
        
#             #report
# #             msg = "[%s:%d] (%02d) %s : diff_OC >= 0 : %03f" % \
#             msg = "[%s:%d] (%02d) %s : diff_OC >= 0 : %03f (f_New = %s)" % \
#                             (os.path.basename(libs.thisfile()), libs.linenum()
#                             , idx, item.dateTime_Local, diff_OC, f_New
#                             )
#                             
#             write_Log(msg)

            # f_New ---> on
            if f_New == True : 
                
                # set flag
                f_New = False
                
                # set : idx_Start
                idx_Start = idx
                
                # report
                dpath = cons_fx.FPath.dpath_Data_Miscs.value
                
                fname = "detect_peaks.log"
                
                fpath = "%s/%s" % (dpath, fname)
                
                fout = open(fpath, "a")
                
                msg = "[%s:%d] (%02d) %s : f_New ==> turned to False" % \
                        (os.path.basename(libs.thisfile()), libs.linenum()
                        , idx, item.dateTime_Local
                        )
                fout.write(msg)
                
                fout.write("\n")
            
            # sum of diff
            sumOf_Diff += diff_OC
            
            '''###################
                j : 2        
            ###################'''
            if sumOf_Diff > sum_Max : #if sumOf_Diff> sum_Max
                
                # update sum_Max
                sum_Max = sumOf_Diff
                
                # update index
                idxOf_SumMax = idx
            
                # next index in the loop f1
                #count
                idx += 1
                
                # next index
                continue

            else : #if sumOf_Diff> sum_Max
            
                # next index in the loop f1
                #count
                idx += 1
                
                # next index
                continue
#                 pass
            
            #/if sumOf_Diff> sum_Max
            
            
        
        #/if item.diff_OC < 0 ### j : 1
        
#         '''###################
#             report        
#         ###################'''
#         dpath = cons_fx.FPath.dpath_Data_Miscs.value
#         
#         fname = "detect_peaks.log"
#         
#         fpath = "%s/%s" % (dpath, fname)
#         
#         fout = open(fpath, "a")
#         
#         msg = "[%s:%d] (%02d) %s / diff_OC = %03f / sumOf_Diff = %03f / sum_Max = %03f" % \
#                 (os.path.basename(libs.thisfile()), libs.linenum()
#                 , idx, item.dateTime_Local, diff_OC, sumOf_Diff, sum_Max
#                 )
#         fout.write(msg)
#         
#         fout.write("\n")
#             
#         #/for elem in item:
#         
#         fout.close()

#         print()
#         print("[%s:%d] (%02d) %s / sumOf_Diff = %03f / sum_Max = %03f" % \
#                 (os.path.basename(libs.thisfile()), libs.linenum()
#                 , idx, item.dateTime_Local, sumOf_Diff, sum_Max
#                 ), file=sys.stderr)
        
        '''###################
            j : 3
            next item
        ###################'''
        # counter
        idx += 1
        
        # next index in the loop f1
        continue
        
    #/for item in lo_BarDatas:

    '''###################
        report : sum_Max
    ###################'''
#     print()
#     print("[%s:%d] lo_Max ==>" % \
#                     (os.path.basename(libs.thisfile()), libs.linenum()
#                     
#                     ), file=sys.stderr)
#     
#     print(lo_Max)
#     msg = "[%s:%d] lo_Max ==>" % \
#                         (os.path.basename(libs.thisfile()), libs.linenum()
#                         
#                         )
#                         
#     write_Log(msg)
#     write_Log(lo_Max)
    
    '''###################
        write : lo_Max
    ###################'''
    # report
    dpath = cons_fx.FPath.dpath_Data_Miscs.value
    
    fname = "detect_peaks.sum_Max.%s.log" % libs.get_TimeLabel_Now()
    
    fpath = "%s/%s" % (dpath, fname)
    
    fout = open(fpath, "w")
#     fout = open(fpath, "a")
    
    # header : meta data
    msg = "source = %s (%s)" % \
            (fname_Data, dpath_Data)
#             (fname_Data, dpath_Data)
            
    fout.write(msg)
    
    fout.write("\n")
    
    # header : columns
    #     data = (round(sum_Max, 3)
    #                 , int(idx_Start)
    #                 , round(idxOf_SumMax, 3)
    #                 , item.dateTime_Local
    msg = "Max\tidx_Start\tidxOf_SumMax\tidx(when ended)\tdateTime_Local(max)"
#     msg = "Max,idx_Start,idxOf_SumMax,idx(when ended),dateTime_Local(max)"
#     msg = "Max,idx_Start,idxOf_SumMax,dateTime_Local"
            
    fout.write(msg)
    fout.write("\n")
    
    # write
    for item in lo_Max:
        
            # data = (round(sum_Max, 3), round(idxOf_SumMax, 3))
            # data = (round(sum_Max, 3)
            #         , int(idx_Start)
            #         , int(idxOf_SumMax)
            #         , int(idx)
            #         , item.dateTime_Local
            
#         msg = "%03f,%02d,%02d,%02d,%s" % \
        msg = "%03f\t%02d\t%02d\t%02d\t%s" % \
                (item[0], int(item[1]), int(item[2]), item[3], item[4])
#                 (item[0], item[1])
                
        fout.write(msg)
        fout.write("\n")
        
    #/for item in lo_Max:

    
    fout.write("\n")
    
    fout.close()

    '''###################
        file : finish        
    ###################'''
    msg = "\n\n"
    
    write_Log(msg)
    
#     dpath = cons_fx.FPath.dpath_Data_Miscs.value
#         
#     fname = "detect_peaks.log"
#     
#     fpath = "%s/%s" % (dpath, fname)
#     
#     fout = open(fpath, "a")
#     
#     fout.write("\n\n")
#     
#     fout.close()

    
#/ def basics_Ops_1__DetectPieaks(request, lo_BarDatas):
    
def basics(request):
    
    # time
    time_Start = time.time()
    
#     '''###################
#         time        
#     ###################'''
#     time_Elapsed = time.time() - time_Start
#     
#     message = "done (time : %02.3f sec)" % (time_Elapsed)

    
    dic = {}
#     dic = {'action' : action, "message" : message}
    
    '''###################
        params
    ###################'''
    
    '''###################
        ops
    ###################'''
    dpath = cons_fx.FPath.dpath_In_CSV.value
    
    fname = get_CurrencyData_FileName(request)
    
#     fname = cons_fx.FPath.fname_In_CSV.value
#     fname = "49_20_file-io.USDJPY.Period-H1.Days-1200.Bars-28800.20180428_073251.csv"
#     fname = cons_fx.FPath.fname_In_CSV.value
    
    header_Length   = 2
     
    skip_Header     = False

    #debug
#     lo_BarDatas = None
    lo_BarDatas = libfx.get_Listof_BarDatas_2(
                        dpath, fname, header_Length, skip_Header)
    
#     #test
#     lo_BarDatas = None
    
    # validate
    if lo_BarDatas == None : #if lo_BarDatas == None
    
        print()
        print("[%s:%d] lo_BarDatas => None" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                
                ), file=sys.stderr)

    
        msg = "lo_BarDatas => None"
        dic = {"msg" : msg}
    
        return render(request, 'curr/error.html', dic)
#         return render(request, 'curr/error.html', msg)

    else : #if lo_BarDatas == None
    
        print()
        print("[%s:%d] lo_BarDatas => %d" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                , len(lo_BarDatas)
                ), file=sys.stderr)
    
    #/if lo_BarDatas == None
#     result = basics_Ops_1__DetectPieaks(request, lo_BarDatas, dpath, fname)

    '''###################
        list of commands
    ###################'''
    lo_Commands = [
        
        ["gen_peak_data", "generate peak data"],
        
        ["gen_bottom_data", "generate bottom data"],
    ]
    
    
    # set var
    dic["lo_Commands"] = lo_Commands
    

    '''###################
        get : referer        
    ###################'''
    referer_MM = "http://127.0.0.1:8000/curr/"
    
    referer_Current = request.META.get('HTTP_REFERER')


    '''###################
        render        
    ###################'''
    '''###################
        time        
    ###################'''
    time_Elapsed = time.time() - time_Start
    
#     message = "done (time : %02.3f sec)" % (time_Elapsed)

    dic["msg"] = "rendering... (%s)(time : %02.3f sec)" \
                    % (libs.get_TimeLabel_Now(), time_Elapsed)
#     dic["msg"] = "rendering... (%s)(time : %02.3f sec)" % libs.get_TimeLabel_Now()
    
    if referer_Current == referer_MM : #if referer_Current == referer_MM
    
        print()
        print("[%s:%d] referer_Current == referer_MM (current = %s / referer = %s" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                ,referer_Current, referer_MM
                ), file=sys.stderr)
    
        return render(request, 'curr/basics.html', dic)
#         return render(request, 'mm/numbering.html', dic)
        
    else : #if referer_Current == referer_MM

        print()
        print("[%s:%d] referer_Current <> referer_MM (current = %s / referer = %s" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                ,referer_Current, referer_MM
                ), file=sys.stderr)

        return render(request, 'curr/basics_full.html', dic)

#     return render(request, 'curr/updown_patterns.html', dic)

    
#/def basics(request):
    
    
def index(request):


    action = "action"
    message = "message"
    
    lo_Commands = cons_mm.CURROp.lo_Commands.value
#     lo_Commands = cons_mm.ImOp.lo_Commands.value
    
    #debug
    print()
    print(lo_Commands)
    
    dic = {'action' : action, "message" : message, "lo_Commands" : lo_Commands}
    
    return render(request, 'curr/index.html', dic)
#     return render(request, 'mm/index.html', dic)

    
#     return HttpResponse("Hello Django")

def testers(request):


    action = "action"
    message = "message"
    
    lo_Commands = cons_fx.Tester.lo_Commands.value
#     lo_Commands = cons_mm.ImOp.lo_Commands.value
    
    #debug
    print()
    print(lo_Commands)
    
    dic = {'action' : action, "message" : message, "lo_Commands" : lo_Commands}
    
    return render(request, 'curr/testers.html', dic)
#     return render(request, 'mm/index.html', dic)

    
#     return HttpResponse("Hello Django")

def tester_BuyUps_SellLows__BUSL_2__1_Exec(request, lo_BarDatas, time_Start, time_End):
    
    '''###################
        BarData : by datetime
    ###################'''
#     time_Start = "2018.05.09"
#     time_End = "2018.05.10"
#     time_Start = "2018.07.07 06:30"
#     time_End = "2018.07.07 07:00"
#     time_Start = "2018.07.07 06:00"
#     time_End = "2018.07.07 06:30"
#     time_End = "2018.05.11"
    
    msg = "\ntime_Start = %s, time_End = %s" %\
            (time_Start, time_End)
    
    # message : time period
    time_Period = (time_Start, time_End)
#     time_Period = msg
    
    msg_Log = "[%s / %s:%d] %s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , msg)
    
    libs.write_Log(msg_Log
                , cons_fx.FPath.dpath_LogFile.value
                , cons_fx.FPath.fname_LogFile.value
                , 1)

    
    flag_Period_Open = False
    
    lo_BarDatas__By_Datetime = \
                libfx.get_LO_BarData___By_Datetime(
                        lo_BarDatas
                        , time_Start
                        , time_End
                        , flag_Period_Open)
    
    if lo_BarDatas__By_Datetime == False : #if not lo_BarDatas__By_Datetime == False

        print()
        print("[%s:%d] lo_BarDatas__By_Datetime => False" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
        
    
    else : #if not lo_BarDatas__By_Datetime == False
    
        pass
#         print()
#         print("[%s:%d] len(lo_BarDatas__By_Datetime) => %d" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#             , len(lo_BarDatas__By_Datetime)
#             ), file=sys.stderr)
#         print("lo_BarDatas__By_Datetime[0] =>")
#         print(lo_BarDatas__By_Datetime[0].dateTime_Local)
    
    #/if not lo_BarDatas__By_Datetime == False
    
    '''###################
        exec : BUSL_2
    ###################'''
    # sort
    orderOf_Sort = 2 #=> old --> new
#     orderOf_Sort = 1 #=> new --> old
    
    lo_BarDatas__By_Datetime = \
            libfx.sort_LO_BarData__By_Datetime(lo_BarDatas__By_Datetime, orderOf_Sort)
    
    # execute
    (cntOf_Both2Bars_Up, lenOf_LO_BarData, lo_BarData__2Bar_Up) = \
                    libfx.BUSL_2(lo_BarDatas__By_Datetime)
#     (cntOf_Both2Bars_Up, lenOf_LO_BarData) = libfx.BUSL_2(lo_BarDatas__By_Datetime)
#     result = libfx.BUSL_2(lo_BarDatas__By_Datetime)
    
#     print()
#     print("[%s:%d] result of BUSL_2 =>" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#             
#             ), file=sys.stderr)
#     
#     print((cntOf_Both2Bars_Up, lenOf_LO_BarData))    
# #     print(result)    
    
    '''###################
        return        
    ###################'''
    
    return time_Period, cntOf_Both2Bars_Up, lenOf_LO_BarData, lo_BarData__2Bar_Up
#     return time_Period, cntOf_Both2Bars_Up, lenOf_LO_BarData
#/ def tester_BuyUps_SellLows__BUSL_2__1_Exec(request):
    
def __tester_BuyUps_SellLows__BUSL_3__2Ups(request):
    
    '''###################
        vars
    ###################'''
    dic = {}
    
    '''###################
        prep : file path
    ###################'''
    dpath = "C:\\WORKS_2\\WS\\WS_Others\\prog\\D-7\\2_2\\VIRTUAL\\Admin_Projects\\curr\\data\\csv_raw"
#     fname = "44_3.2_15_file-io.EURJPY.Period-H1.Days-5000.Bars-120000.20180903_135341.SHRINK-200.csv"
    fname = "44_3.2_5_file-io.USDJPY.Period-M5.Days-26000.Bars-26000.20180721_160222.SHRINK-100.csv"

    # validate
    fpath_Full = os.path.join(dpath, fname)
    
    if not os.path.isfile(fpath_Full) : #if not os.path.isfile(fpath_Full)
    
        print("[%s:%d] csv file --> NOT exist : %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , fpath_Full
            ), file=sys.stderr)
        
        # return
        '''###################
            message
        ###################'''
        dic['message'] = "CSV NOT EXIST : %s" % fpath_Full
        
        '''###################
            pages
        ###################'''
        render_Page = 'curr/busl_2.html'
        render_Page_full = 'curr/busl_2_full.html'
        
        '''###################
            return        
        ###################'''
        return render_Page, render_Page_full, dic
        
    #/if not os.path.isfile(fpath_Full)
    
    

    '''###################
        get : list of BarDatas
    ###################'''
    header_Length   = 2
    skip_Header     = False
    
    lo_BarDatas, lo_CSVs = libfx.get_Listof_BarDatas_2(
                        dpath, fname, header_Length, skip_Header)
    
    print()
    print("[%s:%d] len(lo_BarDatas) => %d" % \
                        (os.path.basename(libs.thisfile()), libs.linenum()
                        , len(lo_BarDatas)
                        ), file=sys.stderr)
    
    '''###################
        op : BUSL_3
    ###################'''
    libfx.BUSL_3(lo_BarDatas)
    
#     '''###################
#         time        
#     ###################'''
#     time_Exec_Elapsed = time.time() - time_Exec_Start
    
#     message = "done (time : %02.3f sec)" % (time_Elapsed)
    
#     '''###################
#         messages
#     ###################'''
# #     dic['message'] = "done (%s)" % libs.get_TimeLabel_Now()
#     dic['message'] = "BUSL_3 ==> done (%s)(elapsed = %02.3f sec)" % \
#                     (libs.get_TimeLabel_Now(), time_Exec_Elapsed)
    
    '''###################
        pages
    ###################'''
    render_Page = 'curr/busl_2.html'
    render_Page_full = 'curr/busl_2_full.html'
    
    '''###################
        return        
    ###################'''
    return render_Page, render_Page_full, dic
    
#/ def __tester_BuyUps_SellLows__BUSL_3__2Ups(request):

def __tester_BuyUps_SellLows__BUSL_3__3Ups(request):
    
    '''###################
        vars
    ###################'''
    dic = {}
    
    '''###################
        get : list of BarDatas
    ###################'''
    dpath = "C:\\WORKS_2\\WS\\WS_Others\\prog\\D-7\\2_2\\VIRTUAL\\Admin_Projects\\curr\\data\\csv_raw"
    fname = "44_3.2_5_file-io.USDJPY.Period-M5.Days-26000.Bars-26000.20180721_160222.SHRINK-100.csv"
    
    header_Length   = 2
    skip_Header     = False
    
    lo_BarDatas, lo_CSVs = libfx.get_Listof_BarDatas_2(
                        dpath, fname, header_Length, skip_Header)
    
    print()
    print("[%s:%d] len(lo_BarDatas) => %d" % \
                        (os.path.basename(libs.thisfile()), libs.linenum()
                        , len(lo_BarDatas)
                        ), file=sys.stderr)
    
    '''###################
        op : BUSL_3
    ###################'''
    libfx.BUSL_3(lo_BarDatas)
    
    '''###################
        pages
    ###################'''
    render_Page = 'curr/busl_2.html'
    render_Page_full = 'curr/busl_2_full.html'
    
    '''###################
        return        
    ###################'''
    return render_Page, render_Page_full, dic

#/ def __tester_BuyUps_SellLows__BUSL_3__3Ups(request):

def __tester_BuyUps_SellLows__BUSL_3__NextUp(request):
    
    '''###################
        vars
    ###################'''
    dic = {}
    
    '''###################
        get : list of BarDatas
    ###################'''
    fname = cons_fx.FPath.BUSL_3_FNAME_PEAK_LIST.value
    dpath = cons_fx.FPath.BUSL_3_DPATH_PEAK_LIST.value
#     dpath = "C:\\WORKS_2\\WS\\WS_Others\\prog\\D-7\\2_2\\VIRTUAL\\Admin_Projects\\curr\\data\\csv_raw"
#     fname = "44_3.2_5_file-io.USDJPY.Period-M5.Days-26000.Bars-26000.20180721_160221.SHRINK-1000.csv"
#     fname = "44_3.2_5_file-io.USDJPY.Period-M5.Days-26000.Bars-26000.20180721_160221.SHRINK-1000.csv"
#     fname = "44_3.2_5_file-io.USDJPY.Period-M5.Days-26000.Bars-26000.20180721_160222.SHRINK-100.csv"
    
    header_Length   = 2
    skip_Header     = False
    
    lo_BarDatas, lo_CSVs = libfx.get_Listof_BarDatas_2(
                        dpath, fname, header_Length, skip_Header)
    
    print()
    print("[%s:%d] len(lo_BarDatas) => %d" % \
                        (os.path.basename(libs.thisfile()), libs.linenum()
                        , len(lo_BarDatas)
                        ), file=sys.stderr)
    
    '''###################
        op : BUSL_3
    ###################'''
    libfx.BUSL_3__NextUp(lo_BarDatas)
    
    '''###################
        pages
    ###################'''
    render_Page = 'curr/busl_2.html'
    render_Page_full = 'curr/busl_2_full.html'
    
    '''###################
        return        
    ###################'''
    return render_Page, render_Page_full, dic

#/ def __tester_BuyUps_SellLows__BUSL_3__NextUp(request):

def __tester_BuyUps_SellLows__BUSL_3__Expert__Over_BB_1S(request):
    
    '''###################
        vars
    ###################'''
    dic = {}
    
    '''###################
        get : list of BarDatas
    ###################'''
    fname = cons_fx.FPath.BUSL_3_FNAME_PEAK_LIST.value
    dpath = cons_fx.FPath.BUSL_3_DPATH_PEAK_LIST.value
    
    header_Length   = 2
    skip_Header     = False
    
    lo_BarDatas, lo_CSVs = libfx.get_Listof_BarDatas_2(
                        dpath, fname, header_Length, skip_Header)
    
    print()
    print("[%s:%d] len(lo_BarDatas) => %d" % \
                        (os.path.basename(libs.thisfile()), libs.linenum()
                        , len(lo_BarDatas)
                        ), file=sys.stderr)
    
    '''###################
        op : BUSL_3
    ###################'''
    libfx.BUSL_3__Expert__Over_BB_1S(lo_BarDatas, fname)
#     libfx.BUSL_3__Expert__Over_BB_1S(lo_BarDatas)
    
    '''###################
        pages
    ###################'''
    render_Page = 'curr/busl_2.html'
    render_Page_full = 'curr/busl_2_full.html'
    
    '''###################
        return        
    ###################'''
    return render_Page, render_Page_full, dic

#/ def __tester_BuyUps_SellLows__BUSL_3__Expert__Over_BB_1S(request):

def __tester_BuyUps_SellLows__BUSL_3__Utils_1_UpsDowns_In_BB_Ranges(request):
    
    '''###################
        vars
    ###################'''
    dic = {}
    
    '''###################
        prep
    ###################'''
    fname = cons_fx.FPath.BUSL_3_FNAME_PEAK_LIST.value
    dpath = cons_fx.FPath.BUSL_3_DPATH_PEAK_LIST.value
    
    # validate
    fpath_Full = os.path.join(dpath, fname)
    
    if not os.path.isfile(fpath_Full) : #if not os.path.isfile(fpath_Full)
    
        print("[%s:%d] csv file --> NOT exist : %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , fpath_Full
            ), file=sys.stderr)
        
        # return
        '''###################
            message
        ###################'''
        dic['message'] = "CSV NOT EXIST : %s" % fpath_Full
        
        '''###################
            pages
        ###################'''
        render_Page = 'curr/busl_2.html'
        render_Page_full = 'curr/busl_2_full.html'
        
        '''###################
            return        
        ###################'''
        return render_Page, render_Page_full, dic
    
    
    '''###################
        get : list of BarDatas
    ###################'''
    header_Length   = 2
    skip_Header     = False
    
    lo_BarDatas, lo_CSVs = libfx.get_Listof_BarDatas_2(
                        dpath, fname, header_Length, skip_Header)
    
    print()
    print("[%s:%d] len(lo_BarDatas) => %d" % \
                        (os.path.basename(libs.thisfile()), libs.linenum()
                        , len(lo_BarDatas)
                        ), file=sys.stderr)
    
    '''###################
        op : BUSL_3
    ###################'''
    libfx.BUSL_3__Util__1_UpsDowns_In_BB_Ranges(lo_BarDatas, fname)
#     libfx.BUSL_3__Expert__Over_BB_1S(lo_BarDatas, fname)
#     libfx.BUSL_3__Expert__Over_BB_1S(lo_BarDatas)
    
    '''###################
        pages
    ###################'''
    render_Page = 'curr/busl_2.html'
    render_Page_full = 'curr/busl_2_full.html'
    
    '''###################
        return        
    ###################'''
    return render_Page, render_Page_full, dic

#/ __tester_BuyUps_SellLows__BUSL_3__Utils_1_UpsDowns_In_BB_Ranges(request)

def __tester_BuyUps_SellLows__BUSL_3__Res_1__DetectPatterns__UpDownPattern(request):
    
    '''###################
        vars
    ###################'''
    dic = {}
    
    '''###################
        prep
    ###################'''
    fname = cons_fx.FPath.BUSL_3_FNAME_PEAK_LIST.value
    dpath = cons_fx.FPath.BUSL_3_DPATH_PEAK_LIST.value
    
    # validate
    fpath_Full = os.path.join(dpath, fname)
    
    if not os.path.isfile(fpath_Full) : #if not os.path.isfile(fpath_Full)
    
        print("[%s:%d] csv file --> NOT exist : %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , fpath_Full
            ), file=sys.stderr)
        
        # return
        '''###################
            message
        ###################'''
        dic['message'] = "CSV NOT EXIST : %s" % fpath_Full
        
        '''###################
            pages
        ###################'''
        render_Page = 'curr/busl_2.html'
        render_Page_full = 'curr/busl_2_full.html'
        
        '''###################
            return        
        ###################'''
        return render_Page, render_Page_full, dic
    
    
    '''###################
        get : list of BarDatas
    ###################'''
    header_Length   = 2
    skip_Header     = False
    
    lo_BarDatas, lo_CSVs = libfx.get_Listof_BarDatas_2(
                        dpath, fname, header_Length, skip_Header)
    
    print()
    print("[%s:%d] len(lo_BarDatas) => %d" % \
                        (os.path.basename(libs.thisfile()), libs.linenum()
                        , len(lo_BarDatas)
                        ), file=sys.stderr)
    
    '''###################
        op : BUSL_3
    ###################'''
    libfx.BUSL_3__Res_1__DetectPatterns__UpDownPattern(lo_BarDatas, fname)
#     libfx.BUSL_3__Util__1_UpsDowns_In_BB_Ranges(lo_BarDatas, fname)
    
    '''###################
        pages
    ###################'''
    render_Page = 'curr/busl_2.html'
    render_Page_full = 'curr/busl_2_full.html'
    
    '''###################
        return        
    ###################'''
    return render_Page, render_Page_full, dic

#/ __tester_BuyUps_SellLows__BUSL_3__Res_1__DetectPatterns__UpDownPattern(request)

def tester_BuyUps_SellLows__BUSL_3(request):
    
    '''###################
        time        
    ###################'''
    time_Exec_Start = time.time()

#     '''###################
#         vars
#     ###################'''
#     dic = {}
    
    '''######################################
        params
    ###################'''
    param_Cmd = request.GET.get(
                    cons_fx.ParamConstants.PARAM_BUSL3_KEY__ACTION.value
                    , False)
    
    print()
    print("[%s:%d] param_Cmd => %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , param_Cmd
            ), file=sys.stderr)
    
    '''###################
        param : default
    ###################'''
    if param_Cmd == cons_fx.ParamConstants.PARAM_BUSL3_CMD_2UPS.value : #if param_Cmd == cons_fx.ParamConstants.PARAM_BUSL3_CMD_2UPS.value
    
        render_Page, render_Page_full, dic = \
                    __tester_BuyUps_SellLows__BUSL_3__2Ups(request)
    
    elif param_Cmd == cons_fx.ParamConstants.PARAM_BUSL3_CMD_3UPS.value : #if param_Cmd == cons_fx.ParamConstants.PARAM_BUSL3_CMD_2UPS.value
    
        render_Page, render_Page_full, dic = \
                    __tester_BuyUps_SellLows__BUSL_3__3Ups(request)

        #debug
#         dic['message'] = " (param is '%s')" % param_Cmd
        dic['message'] = " (param for 'action' is '%s')" % param_Cmd
#         dic['message'] = " (param for 'action' is '%s' ==> use default)" % param_Cmd
    
    #PARAM_BUSL3_CMD_NEXTUP = "next_up"
    elif param_Cmd == cons_fx.ParamConstants.PARAM_BUSL3_CMD_NEXTUP.value : #if param_Cmd == cons_fx.ParamConstants.PARAM_BUSL3_CMD_2UPS.value
        
        render_Page, render_Page_full, dic = \
                    __tester_BuyUps_SellLows__BUSL_3__NextUp(request)

        #debug
        dic['message'] = " (param for 'action' is '%s')" % param_Cmd
    
    #PARAM_BUSL3_CMD_EXPERT_1_OVER_BB_1S = "expert_busl3___1_over_bb_1s"
    elif param_Cmd == cons_fx.ParamConstants.PARAM_BUSL3_CMD_EXPERT_1_OVER_BB_1S.value : #if param_Cmd == cons_fx.ParamConstants.PARAM_BUSL3_CMD_2UPS.value
        
        render_Page, render_Page_full, dic = \
                    __tester_BuyUps_SellLows__BUSL_3__Expert__Over_BB_1S(request)

        #debug
        dic['message'] = " (param for 'action' is '%s')" % param_Cmd
    
    elif param_Cmd == cons_fx.ParamConstants.PARAM_BUSL3_CMD_UTIL__1_UPSDOWNS_IN_BB_RANGES.value : #if param_Cmd == cons_fx.ParamConstants.PARAM_BUSL3_CMD_2UPS.value
        
        print("[%s:%d] elif : PARAM_BUSL3_CMD_UTIL__1_UPSDOWNS_IN_BB_RANGES --> starting..." % \
                        (os.path.basename(libs.thisfile()), libs.linenum()
                        
                        ), file=sys.stderr)
        
        render_Page, render_Page_full, dic = \
                    __tester_BuyUps_SellLows__BUSL_3__Utils_1_UpsDowns_In_BB_Ranges(request)

        print("[%s:%d] dic is now ..." % \
                        (os.path.basename(libs.thisfile()), libs.linenum()
                        
                        ), file=sys.stderr)
        print(dic)

        #debug
        if 'message' in dic : #if 'message' in dic
            
            dic['message'] += " (param for 'action' is '%s')" % param_Cmd
            
        else :
            
            dic['message'] = " (param for 'action' is '%s')" % param_Cmd

    elif param_Cmd == cons_fx.ParamConstants.PARAM_BUSL3_CMD_RES__1_DETECT_PATTERNS__UPSDOWNS.value : #if param_Cmd == cons_fx.ParamConstants.PARAM_BUSL3_CMD_2UPS.value
        '''###################
            detect patterns : up down patterns
        ###################'''
        render_Page, render_Page_full, dic = \
                    __tester_BuyUps_SellLows__BUSL_3__Res_1__DetectPatterns__UpDownPattern(request)
#                     __tester_BuyUps_SellLows__BUSL_3__Utils_1_UpsDowns_In_BB_Ranges(request)
                    
    else : #if param_Cmd == cons_fx.ParamConstants.PARAM_BUSL3_CMD_2UPS.value
    
        render_Page, render_Page_full, dic = \
                    __tester_BuyUps_SellLows__BUSL_3__2Ups(request)
        
        print()
        print("[%s:%d] dic =>" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
        print(dic)

        #debug
#         dic['message'] = " (param is '%s')" % param_Cmd
        dic['message'] = " (param for 'action' is '%s' ==> use default)" % param_Cmd
# #         dic['message'] = dic['message'] + " (param is '%s')" % param_Cmd
# #         dic['message'] += " (param is '%s')" % param_Cmd
    
    #/if param_Cmd == cons_fx.ParamConstants.PARAM_BUSL3_CMD_2UPS.value
    
    
#     render_Page, render_Page_full, dic = __tester_BuyUps_SellLows__BUSL_3__2Ups(request)
    
    '''###################
        time        
    ###################'''
    time_Exec_Elapsed = time.time() - time_Exec_Start
    
    # build : message
    if 'message' in dic : #if 'message' in dic
                
        dic['message'] += "BUSL_3 ==> done (%s)(elapsed = %02.3f sec)" % \
                        (libs.get_TimeLabel_Now(), time_Exec_Elapsed)
                    
    else : #if 'message' in dic
    
        dic['message'] = "BUSL_3 ==> done (%s)(elapsed = %02.3f sec)" % \
                        (libs.get_TimeLabel_Now(), time_Exec_Elapsed)
        
    
    #/if 'message' in dic
                
                
#     dic['message'] = "BUSL_3 ==> done (%s)(elapsed = %02.3f sec)" % \
#                     (libs.get_TimeLabel_Now(), time_Exec_Elapsed)

    '''###################
        return        
    ###################'''
    return render_Page, render_Page_full, dic

#/ def tester_BuyUps_SellLows__BUSL_3(request):
    
def tester_BuyUps_SellLows__BUSL_2(request):

    '''###################
        time : start
    ###################'''
    time_Exec_Start = time.time()
    
    '''###################
        vars
    ###################'''
    dic = {}
    
    '''###################
        opening
    ###################'''
    print()
    print("[%s:%d] param ==> BUSL_2" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
    
    msg = "param ==> BUSL_2 ======================="
                
#     msg_Log = "[%s / %s:%d] %s" % \
    msg_Log = "\n[%s / %s:%d] %s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , msg)
    
    libs.write_Log(msg_Log
                , cons_fx.FPath.dpath_LogFile.value
                , cons_fx.FPath.fname_LogFile.value
                , 1)

    '''######################################
        ops
    ######################################'''
#     dpath = "C:\\WORKS_2\\WS\\WS_Others\\prog\\D-7\\2_2\\VIRTUAL\\Admin_Projects\\curr\\data\\csv"
#     fname = "44_1.14_file-io.AUDJPY.Period-H1.Days-1900.Bars-45600.20180511_181322.csv"
    dpath = "C:\\WORKS_2\\WS\\WS_Others\\prog\\D-7\\2_2\\VIRTUAL\\Admin_Projects\\curr\\data\\csv_raw"
    fname = "44_3.2_file-io.USDJPY.Period-M1.Days-1500.Bars-90000.20180708_165621.SHIRINKED_0707-0706.csv"
#     fname = "44_3.2_file-io.USDJPY.Period-M1.Days-1500.Bars-90000.20180708_165621.SHIRINKED-361.csv"
#     fname = "44_3.2_file-io.USDJPY.Period-M1.Days-1500.Bars-90000.20180708_165622.SHRINKED.csv"
    
    header_Length   = 2
    skip_Header     = False
    
    lo_BarDatas, lo_CSVs = libfx.get_Listof_BarDatas_2(
                        dpath, fname, header_Length, skip_Header)
    
    print()
    print("[%s:%d] len(lo_BarDatas) => %d" % \
                        (os.path.basename(libs.thisfile()), libs.linenum()
                        , len(lo_BarDatas)
                        ), file=sys.stderr)
    
    '''###################
        execute        
    ###################'''
    # params
    base_Date = "2018.07.06"
    hour_Start = 1
    hour_End = 6

    lo_PairOf_Time_StartEnd = \
            libfx.get_LO_PairOf_Time_StartEnd__V1(base_Date, hour_Start, hour_End)
#     lo_PairOf_Time_StartEnd = libfx.get_LO_PairOf_Time_StartEnd("2018.07.07")

    print()
    print("[%s:%d] lo_PairOf_Time_StartEnd =>" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        
        ), file=sys.stderr)
    print(lo_PairOf_Time_StartEnd)

    # iteration
    lo_MetaData = []
    
    for pairOf_Times in lo_PairOf_Time_StartEnd:
        
        time_Start = pairOf_Times[0]
        time_End = pairOf_Times[1]
        
#         time_Period, cntOf_Both2Bars_Up, lenOf_LO_BarData = tester_BuyUps_SellLows__BUSL_2__1_Exec( \
        time_Period, cntOf_Both2Bars_Up, lenOf_LO_BarData, lo_BarData__2Bar_Up \
                = tester_BuyUps_SellLows__BUSL_2__1_Exec( \
                        request, lo_BarDatas, time_Start, time_End)
        
        # add to list
        lo_MetaData.append(( \
                time_Period
                , cntOf_Both2Bars_Up
                , lenOf_LO_BarData
                , lo_BarData__2Bar_Up
                ))
#         lo_MetaData.append((time_Period, cntOf_Both2Bars_Up, lenOf_LO_BarData))
        
    #/for pairOf_Times in lo_PairOf_Time_StartEnd:

    #debug
    print()
    print("[%s:%d] lo_MetaData =>" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
    print(lo_MetaData)
    
    '''###################
        write to file : meta data
    ###################'''
    msg = "[%s:%d] lo_MetaData" %\
            (os.path.basename(libs.thisfile()), libs.linenum())
    
    msg_Log = "[%s / %s:%d] %s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , msg)
    
    libs.write_Log(msg_Log
                , cons_fx.FPath.dpath_LogFile.value
                , cons_fx.FPath.fname_LogFile.value
                , 1)
    
    for item in lo_MetaData:
    
        msg_Log = "%s\t%s\t%d\t%d" % \
                (
                        item[0][0], item[0][1], item[1], item[2]
                )
        
        libs.write_Log(msg_Log
                    , cons_fx.FPath.dpath_LogFile.value
                    , cons_fx.FPath.fname_LogFile.value
                    , 1)
    
    # separator

    msg_Log = ""
    
    libs.write_Log(msg_Log
                , cons_fx.FPath.dpath_LogFile.value
                , cons_fx.FPath.fname_LogFile.value
                , 1)
        
    #/for item in lo_MetaData:

    '''###################
        write to file : BB-related
    ###################'''
    msg = "[%s:%d] lo_MetaData" %\
            (os.path.basename(libs.thisfile()), libs.linenum())
    
    msg_Log = "[%s / %s:%d] %s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , msg)
    
    libs.write_Log(msg_Log
                , cons_fx.FPath.dpath_LogFile.value
                , cons_fx.FPath.fname_LogFile.value
                , 1)
    
    for item in lo_MetaData:
        
        # list
        lo_2Bar_Up = item[3]
        
        #debug
        print()
        print("[%s:%d] lo_2Bar_Up =>" % \
                    (os.path.basename(libs.thisfile()), libs.linenum()
                    
                    ), file=sys.stderr)
        print(lo_2Bar_Up)
        print()
        
        # each list
        # e_1.dateTime_Local, e_1.price_Close, e_1.bb_Main
        for item2 in lo_2Bar_Up:
    
            msg_Log = "%s\t%3.3f\t%3.3f" % \
                    (
                            item2[0], item2[1], item2[2]
                    )
             
            libs.write_Log(msg_Log
                        , cons_fx.FPath.dpath_LogFile.value
                        , cons_fx.FPath.fname_LogFile.value
                        , 1)
            
            
        #/for item2 in lo_2Bar_Up:
        
        # line separator
        msg_Log = ""
         
        libs.write_Log(msg_Log
                    , cons_fx.FPath.dpath_LogFile.value
                    , cons_fx.FPath.fname_LogFile.value
                    , 1)

    
#     #debug
#     print()
#     print("[%s:%d] lo_BarData__2Bar_Up =>" % \
#                 (os.path.basename(libs.thisfile()), libs.linenum()
#                 
#                 ), file=sys.stderr)
#     print(lo_BarData__2Bar_Up)
#     print()
    
#     tester_BuyUps_SellLows__BUSL_2__1_Exec(request, lo_BarDatas, lo_PairOf_Time_StartEnd)
# #     tester_BuyUps_SellLows__BUSL_2__1_Exec(request, lo_BarDatas)

    '''###################
        time        
    ###################'''
    time_Exec_Elapsed = time.time() - time_Exec_Start
    
#     message = "done (time : %02.3f sec)" % (time_Elapsed)
    
    '''###################
        messages
    ###################'''
#     dic['message'] = "done (%s)" % libs.get_TimeLabel_Now()
    dic['message'] = "done (%s)(elapsed = %02.3f sec)" % \
                    (libs.get_TimeLabel_Now(), time_Exec_Elapsed)
    
    '''###################
        pages
    ###################'''
    render_Page = 'curr/busl_2.html'
    render_Page_full = 'curr/busl_2_full.html'
    
    '''###################
        return        
    ###################'''
    return render_Page, render_Page_full, dic
    
    
#/ def tester_BuyUps_SellLows__BUSL_2(request):
    
def tester_BuyUps_SellLows(request):
    
    '''###################
        log
    ###################'''
    msg = "\n\nstarting : tester_BuyUps_SellLows ======================="
#     msg = "\nstarting : tester_BuyUps_SellLows ======================="
                
    msg_Log = "[%s / %s:%d] %s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , msg)
    
    libs.write_Log(msg_Log
                , cons_fx.FPath.dpath_LogFile.value
                , cons_fx.FPath.fname_LogFile.value
                , 1)
    
    '''###################
        vars
    ###################'''
    dic = {}
    
    '''###################
        params
    ###################'''
    param_Cmd = request.GET.get('command', False)
#     param_Cmd = request.GET.get('command', False)
    
    if not param_Cmd == False and param_Cmd == "BUSL_2" : #if not param_Cmd == False and param_Cmd == 

        '''###################
            vars : render pages
        ###################'''
        render_Page, render_Page_full, dic = tester_BuyUps_SellLows__BUSL_2(request)
        
    elif not param_Cmd == False and param_Cmd == "BUSL_3" : #if not param_Cmd == False and param_Cmd == 

        '''###################
            vars : render pages
        ###################'''
        render_Page, render_Page_full, dic = tester_BuyUps_SellLows__BUSL_3(request)
        
    else : #if not param_Cmd == False and param_Cmd == 
    
        '''###################
            vars : render pages
        ###################'''
        render_Page = 'curr/tester_BuyUps_SellLows.html'
        render_Page_full = 'curr/tester_BuyUps_SellLows_full.html'
        
        '''###################
            get : files list
        ###################'''
        dpath_Images = "C:\\WORKS_2\\WS\\WS_Others\\prog\\D-7\\2_2\\VIRTUAL\\Admin_Projects" \
                    + "\\curr\\data\\csv"
        
        fpath_Glob = "%s\\*.csv" % (dpath_Images)
    
        #ref glob https://stackoverflow.com/questions/14798220/how-can-i-search-sub-folders-using-glob-glob-module-in-python answered Feb 10 '13 at 13:31    
        lo_Files = glob.glob(fpath_Glob)
    
        lo_Files.sort()
        
        print()
        print("[%s:%d] len(lo_Files) => %d" % \
                    (os.path.basename(libs.thisfile()), libs.linenum()
                    , len(lo_Files)
                    ), file=sys.stderr)
    
        # set list
        dic['lo_Files'] = [os.path.basename(x) for x in lo_Files]
        
        # set : dpath
        dic['dpath_Images'] = dpath_Images
    
    
    
        dic['action'] = "action"
        dic["message"] = "message"
    #     action = "action"
    #     message = "message"
        
        lo_Commands = cons_fx.Tester.lo_Commands.value
    #     lo_Commands = cons_mm.ImOp.lo_Commands.value
        
        #debug
        print()
        print(lo_Commands)
        
    
    #/if not param_Cmd == False and param_Cmd == 

    '''###################
        list of parameters for table
    ###################'''
    dic["list_of_params"] = cons_fx.Tester.lo_Actions__BUSL.value
#     dic["list_of_params"] = [
#         
#             [
#                 "1"
#                 ,"get stats for BB"
#                 , cons_fx.ParamConstants.PARAM_BUSL3_CMD_UTIL__1_UPSDOWNS_IN_BB_RANGES.value
#                 , "20180915_124138"
#             ],
#         
#             [
#                 "2-1"
#                 ,"res : pattern detection"
#                 , cons_fx.ParamConstants.PARAM_BUSL3_CMD_RES__1_DETECT_PATTERNS__UPSDOWNS.value
#                 , "20180915_125135"
#             ],
#         
#         
#         ]
        
    '''###################
        render        
    ###################'''
    '''###################
        get : referer        
    ###################'''
    referer_MM = "http://localhost:8000/curr/testers/"
#     referer_MM = "http://127.0.0.1:8000/curr/"
    
    referer_Current = request.META.get('HTTP_REFERER')

    
    dic["msg"] = "rendering... (%s)" \
                    % (libs.get_TimeLabel_Now())

    if referer_Current == referer_MM : #if referer_Current == referer_MM
    
        print()
        print("[%s:%d] referer_Current == referer_MM (current = %s / referer = %s" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                ,referer_Current, referer_MM
                ), file=sys.stderr)
    
        return render(request, render_Page, dic)
        
    else : #if referer_Current == referer_MM

        print()
        print("[%s:%d] referer_Current <> referer_MM (current = %s / referer = %s" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                ,referer_Current, referer_MM
                ), file=sys.stderr)

        return render(request, render_Page_full, dic)
    
    pass

def tester_BuyUps_SellLows__V2(request):
    
    '''###################
        vars
    ###################'''
    dic = {}
    
    render_Page = 'curr/plain_research_result.html'
    
    '''###################
        get param
    ###################'''
    param = request.GET.get('param', False)
    
    '''###################
        validate : no param?
    ###################'''
    if param == False : #if param == False
    
        dic['message'] = "no param"
        
        '''###################
            render        
        ###################'''
        return render(request, render_Page, dic)
        
    #/if param == False
    
    
    '''###################
        message
    ###################'''
    dic['message'] = "param is ===> '%s'" % param
    
    '''###################
        dispatch
    ###################'''
    if param == (cons_fx.Tester.lo_Actions__BUSL__IDs.value)[0] : #if param == cons_fx.Tester.lo_Actions__BUSL__IDs[0].value
#     if param == cons_fx.Tester.lo_Actions__BUSL__IDs[0].value : #if param == cons_fx.Tester.lo_Actions__BUSL__IDs[0].value
        
        dic['message'] += "(num of up bars and down bars in each of BB areas)"
        
    elif param == (cons_fx.Tester.lo_Actions__BUSL__IDs.value)[1] : #if param == cons_fx.Tester.lo_Actions__BUSL__IDs[0].value : #if param == cons_fx.Tester.lo_Actions__BUSL__IDs[0].value
#     elif param == cons_fx.Tester.lo_Actions__BUSL__IDs[1].value : #if param == cons_fx.Tester.lo_Actions__BUSL__IDs[0].value : #if param == cons_fx.Tester.lo_Actions__BUSL__IDs[0].value
        
        dic['message'] += "up-down pattern of 5 bars : log at detect_pattern.Updowns.XXX.log"
        
    else : #if param == cons_fx.Tester.lo_Actions__BUSL__IDs[0].value
    
        dic['message'] += "(UNKNOWN PARAM)"
    
    #/if param == cons_fx.Tester.lo_Actions__BUSL__IDs[0].value
        
        
    
    '''###################
        render
    ###################'''
    return render(request, render_Page, dic)
    
#/ def  tester_BuyUps_SellLows__V2(request):
    
def agt_BUSL_v_1_0(dpath, fname):
    
#     #debug
#     return

    '''###################
        get : bar data
    ###################'''
    # params
    header_Length   = 2
    skip_Header     = False

    #debug
#     lo_BarDatas = None
#     lo_BarDatas = libfx.get_Listof_BarDatas_2(
    lo_BarDatas, lo_CSVs = libfx.get_Listof_BarDatas_2(
                        dpath, fname, header_Length, skip_Header)
#                         dpath_image, fname, header_Length, skip_Header)

#     print()
#     print("[%s:%d] len(lo_BarDatas) => %d" % \
#                 (os.path.basename(libs.thisfile()), libs.linenum()
#                 , len(lo_BarDatas)
#                 ), file=sys.stderr)
    
#     print()
# #     print("[%s:%d] len(lo_CSVs[:header_Length]) => %d" % \
#     print("[%s:%d] lo_CSVs[:header_Length] =>" % \
#                 (os.path.basename(libs.thisfile()), libs.linenum()
#                 ), file=sys.stderr)
#     
#     print(lo_CSVs)
    
            #     [views.py:1748] lo_CSVs[:header_Length] =>
            # [['Pair=AUDJPY', 'Period=H1', 'Days=1900', 'Shift=1', 'Bars=45600', 'Time=201805
            # 11_181322'], ['no', 'Open', 'High', 'Low', 'Close', 'RSI', 'MFI', 'BB.2s', 'BB.1
            # s', 'BB.main', 'BB.-1s', 'BB.-2s', 'Diff', 'High/Low', 'datetime']]
            
    msg = "lo_CSVs ==>"
    
    msg_Log = "[%s / %s:%d] %s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , msg)
    
    msg_Log += "\n"
    
    lenOf_LO_CSVs = len(lo_CSVs)
    
    for i in range(lenOf_LO_CSVs):
                        
#             msg_Log += lo_Profit_Loss[i]
#             msg_Log += ",".join(lo_Profit_Loss[i])
        msg_Log += "\t".join([str(x) for x in lo_CSVs[i]])
        msg_Log += "\n"
        
    #/for i in range(len(lo_Profit_Loss)):

    libs.write_Log(
                msg_Log
                , cons_fx.FPath.dpath_LogFile.value
                , cons_fx.FPath.fname_LogFile.value
                , 2)
    
#     #test
#     lo_BarDatas = None
    
    # validate
    if lo_BarDatas == None : #if lo_BarDatas == None
    
        print()
        print("[%s:%d] lo_BarDatas => None" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                
                ), file=sys.stderr)

    
        msg = "lo_BarDatas => None"
        dic = {"msg" : msg}
    
        return render(request, 'curr/error.html', dic)
#         return render(request, 'curr/error.html', msg)

    else : #if lo_BarDatas == None
    
        print()
        print("[%s:%d] lo_BarDatas => %d" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                , len(lo_BarDatas)
                ), file=sys.stderr)
    
        '''###################
            buy, sell
        ###################'''
        # reverse
        lo_BarDatas.reverse()
        
        entry_0 = lo_BarDatas[0]
        
#         print()
#         print("[%s:%d] entry_0 =>" % \
#                     (os.path.basename(libs.thisfile()), libs.linenum()
#                      
#                     ), file=sys.stderr)
#          
#         print(entry_0)
#         print(entry_0.dateTime_Local)
        
        '''###################
            iteration        
        ###################'''
        lenOf_Lo_BarData = len(lo_BarDatas)
        
        # price of the position
        priceOf_Position = -1
        
        # flag
        flg_In = False
        
        # counter
        cntOf_Iteration = 0
        
        #debug
        dbg_MaxCount = 20
#             dbg_MaxCount = 10
        
        # profit_loss
        lo_Profit_Loss = []
        
        for i in range(1, lenOf_Lo_BarData):
            
            # bars
            e_0 = lo_BarDatas[i - 1]
            e_1 = lo_BarDatas[i]
            
            # price : close
            pc_0 = e_0.price_Close
            pc_1 = e_1.price_Close
            
            # compare prices
            res = (pc_0 < pc_1)
            
            #debug
#             print()
#             print("[%s:%d] comparing : e_0.dateTime_Local = %s, e_1.dateTime_Local = %s (count = %d)" % \
#                 (os.path.basename(libs.thisfile()), libs.linenum()
#                 , e_0.dateTime_Local, e_1.dateTime_Local, cntOf_Iteration
#                 ), file=sys.stderr)

            msg = "comparing : e_0.dateTime_Local = %s, e_1.dateTime_Local = %s (count = %d)" %\
                    (e_0.dateTime_Local, e_1.dateTime_Local, cntOf_Iteration)
            
            msg_Log = "[%s / %s:%d] %s" % \
                    (
                    libs.get_TimeLabel_Now()
                    , os.path.basename(libs.thisfile()), libs.linenum()
                    , msg)
            
            libs.write_Log(
                        msg_Log
                        , cons_fx.FPath.dpath_LogFile.value
                        , cons_fx.FPath.fname_LogFile.value
                        , 1)

            
            '''###################
                judge : j1 : price is up        
            ###################'''
            # judge
            # res == True ---> price is up
            if res == True : #if res == True

                # judge
                '''###################
                    j2 : flag is up ?        
                ###################'''
                # flag is True ---> pc_0 is of up from pc_-1
                if flg_In == True : #if flg_In == True

                    # update : price of the position
                    priceOf_Position = e_1.price_Close
                    
                    print()
                    print("[%s:%d] priceOf_Position : updated => %.03f" % \
                        (os.path.basename(libs.thisfile()), libs.linenum()
                        , priceOf_Position
                        ), file=sys.stderr)
                    
                    # counter
                    cntOf_Iteration += 1
                    
                    #debug
                    if cntOf_Iteration > dbg_MaxCount :     #if cntOf_Iteration > dbg_MaxCount
                
                        print()
                        print("[%s:%d] break the for loop" % \
                            (os.path.basename(libs.thisfile()), libs.linenum()
                            
                            ), file=sys.stderr)
                        
                        break

                    # next iteration
                    continue
                    
                else :  ### j2.N

                    print()
                    print("[%s:%d] flg_In => %s" % \
                        (os.path.basename(libs.thisfile()), libs.linenum()
                        , flg_In
                        ), file=sys.stderr)
                    
                    # flag : up
                    flg_In = True
#                         flg_in = True
                    
                    print()
                    print("[%s:%d] flg_In is now => %s" % \
                        (os.path.basename(libs.thisfile()), libs.linenum()
                        , flg_In
                        ), file=sys.stderr)
                    
                    # set the price of the position
                    priceOf_Position = e_1.price_Close
                    
                    #debug
#                     print()
# #                         print("[%s:%d] position opened => %.03f" % \
# #                     print("[%s:%d] position opened => %.03f (count = %d)" % \
#                     print("[%s:%d] position opened => %.03f (count = %d / datetime_Local = %s)" % \
#                         (os.path.basename(libs.thisfile()), libs.linenum()
#                         , priceOf_Position, cntOf_Iteration, e_1.dateTime_Local
#                         ), file=sys.stderr)

                    msg = "position opened => %.03f (count = %d / datetime_Local = %s" %\
                            (priceOf_Position, cntOf_Iteration, e_1.dateTime_Local)
                    
                    msg_Log = "[%s / %s:%d] %s" % \
                            (
                            libs.get_TimeLabel_Now()
                            , os.path.basename(libs.thisfile()), libs.linenum()
                            , msg)
                    
                    libs.write_Log(msg_Log
                                , cons_fx.FPath.dpath_LogFile.value
                                , cons_fx.FPath.fname_LogFile.value
                                , 1)

                                        
                    # counter
                    cntOf_Iteration += 1
                    
                    #debug
                    if cntOf_Iteration > dbg_MaxCount :     #if cntOf_Iteration > dbg_MaxCount
                
                        print()
                        print("[%s:%d] break the for loop" % \
                            (os.path.basename(libs.thisfile()), libs.linenum()
                            
                            ), file=sys.stderr)
                        
                        break

                    # next iteration
                    continue
                    
                #/if flg_In == True    ### j2
                
            else : #/if res == True    ### j1.N

#                 print()
#                 print("[%s:%d] res ==> not True (price is down)" % \
#                     (os.path.basename(libs.thisfile()), libs.linenum()
#                     
#                     ), file=sys.stderr)

                msg = "res ==> not True (price is down)"
                
                msg_Log = "[%s / %s:%d] %s" % \
                        (
                        libs.get_TimeLabel_Now()
                        , os.path.basename(libs.thisfile())
                        , libs.linenum()
                        , msg)
                
                libs.write_Log( \
                            msg_Log
                            , cons_fx.FPath.dpath_LogFile.value
                            , cons_fx.FPath.fname_LogFile.value
                            , 1)

                
                '''###################
                    j3 : flag is up ?
                ###################'''
                if flg_In == True : #if flg_In == True
# 
#                     print()
#                     print("[%s:%d] flg_In ==> True (prev is up, now down)" % \
#                         (os.path.basename(libs.thisfile()), libs.linenum()
#                         
#                         ), file=sys.stderr)

                    msg = "flg_In ==> True (prev is up, now down)"
                    
                    msg_Log = "[%s / %s:%d] %s" % \
                            (
                            libs.get_TimeLabel_Now()
                            , os.path.basename(libs.thisfile()), libs.linenum()
                            , msg)
                    
                    libs.write_Log(msg_Log
                                , cons_fx.FPath.dpath_LogFile.value
                                , cons_fx.FPath.fname_LogFile.value
                                , 1)

                    # sell
                    
                    # calculate : profit/loss
                    profit_loss = priceOf_Position - pc_1
                    
                    print()
                    print("[%s:%d] position => closed" % \
                        (os.path.basename(libs.thisfile()), libs.linenum()
                        ), file=sys.stderr)
                    print("[%s:%d] profit_loss => %.03f" % \
                    (os.path.basename(libs.thisfile()), libs.linenum()
                    , profit_loss
                    ), file=sys.stderr)
                    
                    # append profit_loss
                    lo_Profit_Loss.append(
                            [
                                i
                                 , profit_loss
                                 , e_1.dateTime_Local
                                 , e_1.dateTime
                                 , e_1.price_Close
                             ]
                            )
                    
                    
                    # flag : down
                    flg_In = False
                    
                    # reset : price of the positin
                    priceOf_Position = 0
                    
                    # counter
                    cntOf_Iteration += 1
                    
                    #debug
                    if cntOf_Iteration > dbg_MaxCount :     #if cntOf_Iteration > dbg_MaxCount
                
                        print()
                        print("[%s:%d] break the for loop" % \
                            (os.path.basename(libs.thisfile()), libs.linenum()
                            
                            ), file=sys.stderr)
                        
                        break
                    
                    # next iteration
                    continue
                
                else : #if flg_In == True    ### j3.N
                
                    # counter
                    cntOf_Iteration += 1
                    
                    #debug
                    if cntOf_Iteration > dbg_MaxCount :     #if cntOf_Iteration > dbg_MaxCount
                
                        print()
                        print("[%s:%d] break the for loop" % \
                            (os.path.basename(libs.thisfile()), libs.linenum()
                            
                            ), file=sys.stderr)
                        
                        break
                
                    # next
                    continue
                
                #/if flg_In == True    ### j3



#                     pass
            
            #/if res == True    ### j1


            
            
            # counter
            cntOf_Iteration += 1
            
            #debug
            if cntOf_Iteration > dbg_MaxCount :     #if cntOf_Iteration > dbg_MaxCount
        
                print()
                print("[%s:%d] break the for loop" % \
                    (os.path.basename(libs.thisfile()), libs.linenum()
                    
                    ), file=sys.stderr)
                
                break
            
            #/if cntOf_Iteration > dbg_MaxCount
        
        
        
        #/for i in range(lenOf_Lo_BarData - 1:

        #report
#         print()
#         print("[%s:%d] lo_Profit_Loss ==>" % \
#                 (os.path.basename(libs.thisfile()), libs.linenum()
#                 
#                 ), file=sys.stderr)
        
        msg = "lo_Profit_Loss ==>"
        
        msg_Log = "[%s / %s:%d] %s" % \
                (
                libs.get_TimeLabel_Now()
                , os.path.basename(libs.thisfile()), libs.linenum()
                , msg)
        
        msg_Log += "\n"
        
        lenOf_LO_Profit_Loss = len(lo_Profit_Loss)
        
        for i in range(lenOf_LO_Profit_Loss):
                            
#             msg_Log += lo_Profit_Loss[i]
#             msg_Log += ",".join(lo_Profit_Loss[i])
            msg_Log += ",".join([str(x) for x in lo_Profit_Loss[i]])
            msg_Log += "\n"
            
        #/for i in range(len(lo_Profit_Loss)):

        libs.write_Log(
                    msg_Log
                    , cons_fx.FPath.dpath_LogFile.value
                    , cons_fx.FPath.fname_LogFile.value
                    , 2)


        
        for item in lo_Profit_Loss:
        
            print(item)
            
        #/for item in lo_Profit_Loss:

#             print(lo_Profit_Loss)
        
        lo_Tmp = [x[1] for x in lo_Profit_Loss]
        
        sumOf_Profit_Loss = sum(lo_Tmp)
        
        print("sum is => %.03f" % sumOf_Profit_Loss)
#             print("sum is => %.03f" % sum(lo_Profit_Loss))

#/ def agt_BUSL_v_1_0():

def __exec_Tester_BuyUps_SellLows__Basic(request) :
    
    '''###################
        vars
    ###################'''
    dic = {}

    
    '''###################
        time        
    ###################'''
    time_Start = time.time()
    
    '''###################
        tester
    ###################'''
    '''###################
        param : body volume : up        
    ###################'''
    fname = request.GET.get('fname', False)
    dpath_image = request.GET.get('dpath_image', False)

    msg = "__exec_Tester_BuyUps_SellLows__Basic(request) ================================"
    
    msg_Log = "[%s / %s:%d] %s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , msg)
    
#     dpath_Log = cons_fx.FPath.dpath_LogFile.value
#     
#     fname_Log = cons_fx.FPath.fname_LogFile.value

    libs.write_Log(
                msg_Log
                , cons_fx.FPath.dpath_LogFile.value
                , cons_fx.FPath.fname_LogFile.value
                , 1)
#                 , True)
    
#     print()
#     print("[%s:%d] dpath_image = '%s', fname = '%s'" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#             , dpath_image, fname
#             ), file=sys.stderr)

    msg_Log = "[%s / %s:%d] dpath_image = '%s', fname = '%s'" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , dpath_image, fname)

    libs.write_Log(
                msg_Log
                , cons_fx.FPath.dpath_LogFile.value
                , cons_fx.FPath.fname_LogFile.value
                , 1)
#                 , True)
    
    '''###################
        validate : params
    ###################'''
    if fname == False and dpath_image == False : #if fname == False and dpath_image == False
        
        '''###################
            time        
        ###################'''
        time_Elapsed = time.time() - time_Start
        
        '''###################
            vars        
        ###################'''
        dic['action'] = "action"
        dic["msg"] = "params ==> not valid ('%s', '%s')" \
                    % (dpath_image, fname)

        '''###################
            time        
        ###################'''
        time_Elapsed = time.time() - time_Start

    else :#/if fname == False and dpath_image == False
        
        '''###################
            vars        
        ###################'''
        dic['action'] = "action"
        dic["msg"] = "params ==> valid"
#         dic["msg"] = "params ==> valid ('%s', '%s')" \
#                     % (dpath_image, fname)
        
        '''###################
            processes        
        ###################'''
        print("[%s:%d] calling 'agt_BUSL_v_1_0' ..." % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                
                ), file=sys.stderr)
        
        agt_BUSL_v_1_0(dpath_image, fname)

        '''###################
            time        
        ###################'''
        time_Elapsed = time.time() - time_Start#/ def __exec_Tester_BuyUps_SellLows__Basic(request) :

    dic["msg"] += " (%s)(time : %02.3f sec)" \
                    % (libs.get_TimeLabel_Now(), time_Elapsed)

    '''###################
        paths
    ###################'''
    url_Path = 'curr/exec_Tester_BuyUps_SellLows.html'
    url_Path_Full = 'curr/exec_Tester_BuyUps_SellLows_full.html'
    
    
    '''###################
        return        
    ###################'''
    return url_Path_Full, url_Path, dic

def __exec_Tester_BUSL(request) :
    
    '''###################
        vars        
    ###################'''
    dpath_Peak_Files = "C:\\WORKS_2\\WS\\WS_Others\\prog\\D-7\\2_2\\VIRTUAL\\Admin_Projects\\curr\\data\\csv"
    
    fname_Peak_File = "44_1.14_file-io.AUDJPY.Period-H1.Days-1900.Bars-45600.20180511_181322.csv"
    
    fpath_Peak_File = os.path.join(dpath_Peak_Files, fname_Peak_File)
    
    dic = {}
    
    '''###################
        get : list of bar data
    ###################'''
    # params
    header_Length   = 2
    skip_Header     = False

    #debug
#     lo_BarDatas = libfx.get_Listof_BarDatas_2(
    lo_BarDatas, lo_Header_Lines = libfx.get_Listof_BarDatas_2(
                        dpath_Peak_Files, fname_Peak_File, header_Length, skip_Header)
#                         dpath_image, fname, header_Length, skip_Header)

    # validate
    if lo_BarDatas == None : #if lo_BarDatas == None
    
        print()
        print("[%s:%d] lo_BarDatas => None" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                
                ), file=sys.stderr)

    
        msg = "lo_BarDatas => None"
        dic = {"msg" : msg}
    
        return render(request, 'curr/error.html', dic)
    
    # length
    lenOf_LO_BarData = len(lo_BarDatas)
    
#     print()
#     print("[%s:%d] len(lo_BarDatas) => %d" % \
#                 (os.path.basename(libs.thisfile()), libs.linenum()
#                 , lenOf_LO_BarData
#                 ), file=sys.stderr)
#     
#     print()
#     print("[%s:%d] lo_Header_Lines =>" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#             
#             ), file=sys.stderr)
#     
#     print(lo_Header_Lines)
    
    '''######################################
        for-loop
    ######################################'''
    # prep : reverse
    lo_BarDatas.reverse()
    
    '''###################
        vars
    ###################'''
    cntOf_Price_Ups = 0
    
    '''###################
        log : header
    ###################'''
    # file
    dpath_Log = "C:\\WORKS_2\\WS\\WS_Others\\prog\\D-7\\2_2\\VIRTUAL\\Admin_Projects\\curr\\data\\log"
    fname_Log = "BUSL.log"
    fpath_Log = os.path.join(dpath_Log, fname_Log)
    
    fout = open(fpath_Log, "a")

    msg = "source : %s" % fname_Peak_File
    
    print()
    print("[%s:%d] %s" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , msg
        ), file=sys.stderr)

    fout.write("[%s / %s:%d] BUSL ===============================" % \
        (
        libs.get_TimeLabel_Now()
        , os.path.basename(libs.thisfile())
         , libs.linenum()
        )
    )
     
    fout.write("\n")
    
    fout.write("[%s:%d] %s" % \
        (
        os.path.basename(libs.thisfile())
         , libs.linenum()
         , msg
        )
    )
     
    fout.write("\n")
    
    # for-loop
    for i in range(1, lenOf_LO_BarData):
        
        '''###################
            proc 1 : get : bars
        ###################'''
        # bars
        e_0 = lo_BarDatas[i - 1]
        e_1 = lo_BarDatas[i]

        '''###################
            proc 2 : get : prices
        ###################'''
        # price : close
        pc_0 = e_0.price_Close
        pc_1 = e_1.price_Close
        
        '''###################
            proc 3 : get : diff
        ###################'''
        diffOf_Prices = pc_1 - pc_0
        
        '''###################
            j1 : diff --> up?
        ###################'''
        if diffOf_Prices > 0 : #if diffOf_Prices > 0
            
            '''###################
                count
            ###################'''
            cntOf_Price_Ups += 1
            
            '''###################
                log        
            ###################'''
            msg = "price up : %.03f (date : %s)" % (diffOf_Prices, e_1.dateTime_Local)
            
#             print()
#             print("[%s:%d] %s" % \
#                 (os.path.basename(libs.thisfile()), libs.linenum()
#                 , msg
#                 ), file=sys.stderr)

            fout.write("[%s / %s:%d] %s" % \
                (
                libs.get_TimeLabel_Now()
                , os.path.basename(libs.thisfile())
                 , libs.linenum()
                , msg
                )
            )
             
            fout.write("\n")
        
        else : #if diffOf_Prices > 0
        
            pass
        
        #/if diffOf_Prices > 0
    
    
        
        
        
        '''###################
            get : prices
        ###################'''
        
    #/for i in range(lenOf_LO_BarData):

    '''###################
        file : meta data
    ###################'''
    msg = "total price-up : %d" % (cntOf_Price_Ups)
    
    fout.write("[%s / %s:%d] stats ==>" % \
        (libs.get_TimeLabel_Now(), os.path.basename(libs.thisfile()), libs.linenum()
        )
    )
     
    fout.write("\n")
    
    msg = "price-up = %d / total = %d / up ratio = %.03f" %\
             (
                 cntOf_Price_Ups
                 , lenOf_LO_BarData
                 , cntOf_Price_Ups * 1.0 / lenOf_LO_BarData
              )
    
    fout.write("%s" % \
        (
        msg
        )
    )
     
    fout.write("\n")

    '''###################
        file : close
    ###################'''
    # separator line
    fout.write("\n")
    
    fout.close()

    
    '''###################
        paths        
    ###################'''
    url_Path_Full = "curr/exec_Tester_BUSL_full.html"
    url_Path = "curr/exec_Tester_BUSL.html"
      
    dic['msg'] = "exec_Tester_BUSL.html (lenOf_LO_BarData => %d)" % lenOf_LO_BarData
#     dic['msg'] = "exec_Tester_BUSL.html"
#     dic['msg'] = "exec_Tester_BUSL.html (param.commands = '%s')" % param_Cmd

    '''###################
        return        
    ###################'''
    return url_Path_Full, url_Path, dic

#/ def __exec_Tester_BUSL(request) :

def exec_Tester_BuyUps_SellLows(request):
    
    '''###################
        params
    ###################'''
    param_Cmd = request.GET.get('commands', False)
    
    param_Cmd__BUSL = "BUSL"
    
    # jusfwf
    if param_Cmd == False : #if param_Cmd == False
    
        # ops
        url_Path_Full, url_Path, dic = __exec_Tester_BuyUps_SellLows__Basic(request)
    
#             url_Path_Full = "ip/ops/ip_ops_full.html"
#         url_Path = "ip/ops/ip_ops.html"
#         
#         dic['msg'] = "ip_ops.html"

    elif param_Cmd == param_Cmd__BUSL : #if param_Cmd == False

        # ops
        url_Path_Full, url_Path, dic = __exec_Tester_BUSL(request)
        
#         dic = {}
#         
#         url_Path_Full = "curr/exec_Tester_BUSL_full.html"
#         url_Path = "curr/exec_Tester_BUSL.html"
#          
#         dic['msg'] = "exec_Tester_BUSL.html (param.commands = '%s')" % param_Cmd
        
    else : #if param_Cmd == False
        
        # ops
        # default ==> same as param_Cmd is False
        url_Path_Full, url_Path, dic = __exec_Tester_BuyUps_SellLows__Basic(request)
    
    #/if param_Cmd == False
    
    
    
    
#     '''###################
#         vars
#     ###################'''
#     dic = {}
# 
#     
#     '''###################
#         time        
#     ###################'''
#     time_Start = time.time()
#     
#     '''###################
#         tester
#     ###################'''
#     '''###################
#         param : body volume : up        
#     ###################'''
#     fname = request.GET.get('fname', False)
#     dpath_image = request.GET.get('dpath_image', False)
#     
#     print()
#     print("[%s:%d] dpath_image = '%s', fname = '%s'" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#             , dpath_image, fname
#             ), file=sys.stderr)
#     
#     '''###################
#         validate : params
#     ###################'''
#     if fname == False and dpath_image == False : #if fname == False and dpath_image == False
#         
#         '''###################
#             time        
#         ###################'''
#         time_Elapsed = time.time() - time_Start
#         
#         '''###################
#             vars        
#         ###################'''
#         dic['action'] = "action"
#         dic["msg"] = "params ==> not valid ('%s', '%s')" \
#                     % (dpath_image, fname)
# 
#         '''###################
#             time        
#         ###################'''
#         time_Elapsed = time.time() - time_Start
# 
#     else :#/if fname == False and dpath_image == False
#         
#         '''###################
#             vars        
#         ###################'''
#         dic['action'] = "action"
#         dic["msg"] = "params ==> valid"
# #         dic["msg"] = "params ==> valid ('%s', '%s')" \
# #                     % (dpath_image, fname)
#         
#         '''###################
#             processes        
#         ###################'''
#         print("[%s:%d] calling 'agt_BUSL_v_1_0' ..." % \
#                 (os.path.basename(libs.thisfile()), libs.linenum()
#                 
#                 ), file=sys.stderr)
#         
#         agt_BUSL_v_1_0(dpath_image, fname)
# #         agt_BUSL_v_1_0(dpath_image, fname)
#         
# #         '''###################
# #             get : bar data
# #         ###################'''
# #         # params
# #         header_Length   = 2
# #         skip_Header     = False
# #     
# #         #debug
# #     #     lo_BarDatas = None
# #         lo_BarDatas = libfx.get_Listof_BarDatas_2(
# #                             dpath_image, fname, header_Length, skip_Header)
# #         
# #     #     #test
# #     #     lo_BarDatas = None
# #         
# #         # validate
# #         if lo_BarDatas == None : #if lo_BarDatas == None
# #         
# #             print()
# #             print("[%s:%d] lo_BarDatas => None" % \
# #                     (os.path.basename(libs.thisfile()), libs.linenum()
# #                     
# #                     ), file=sys.stderr)
# #     
# #         
# #             msg = "lo_BarDatas => None"
# #             dic = {"msg" : msg}
# #         
# #             return render(request, 'curr/error.html', dic)
# #     #         return render(request, 'curr/error.html', msg)
# #     
# #         else : #if lo_BarDatas == None
# #         
# #             print()
# #             print("[%s:%d] lo_BarDatas => %d" % \
# #                     (os.path.basename(libs.thisfile()), libs.linenum()
# #                     , len(lo_BarDatas)
# #                     ), file=sys.stderr)
# #         
# #             '''###################
# #                 buy, sell
# #             ###################'''
# #             # reverse
# #             lo_BarDatas.reverse()
# #             
# #             entry_0 = lo_BarDatas[0]
# #             
# #             print()
# #             print("[%s:%d] entry_0 =>" % \
# #                         (os.path.basename(libs.thisfile()), libs.linenum()
# #                          
# #                         ), file=sys.stderr)
# #              
# #             print(entry_0)
# #             print(entry_0.dateTime_Local)
# #             
# #             '''###################
# #                 iteration        
# #             ###################'''
# #             lenOf_Lo_BarData = len(lo_BarDatas)
# #             
# #             # price of the position
# #             priceOf_Position = -1
# #             
# #             # flag
# #             flg_In = False
# #             
# #             # counter
# #             cntOf_Iteration = 0
# #             
# #             #debug
# #             dbg_MaxCount = 20
# # #             dbg_MaxCount = 10
# #             
# #             # profit_loss
# #             lo_Profit_Loss = []
# #             
# #             for i in range(1, lenOf_Lo_BarData):
# #                 
# #                 # bars
# #                 e_0 = lo_BarDatas[i - 1]
# #                 e_1 = lo_BarDatas[i]
# #                 
# #                 # price : close
# #                 pc_0 = e_0.price_Close
# #                 pc_1 = e_1.price_Close
# #                 
# #                 # compare prices
# #                 res = (pc_0 < pc_1)
# #                 
# #                 #debug
# #                 print()
# #                 print("[%s:%d] comparing : e_0.dateTime_Local = %s, e_1.dateTime_Local = %s (count = %d)" % \
# #                     (os.path.basename(libs.thisfile()), libs.linenum()
# #                     , e_0.dateTime_Local, e_1.dateTime_Local, cntOf_Iteration
# #                     ), file=sys.stderr)
# #                 
# #                 '''###################
# #                     judge : j1 : price is up        
# #                 ###################'''
# #                 # judge
# #                 # res == True ---> price is up
# #                 if res == True : #if res == True
# #     
# #                     # judge
# #                     '''###################
# #                         j2 : flag is up ?        
# #                     ###################'''
# #                     # flag is True ---> pc_0 is of up from pc_-1
# #                     if flg_In == True : #if flg_In == True
# #     
# #                         # update : price of the position
# #                         priceOf_Position = e_1.price_Close
# #                         
# #                         print()
# #                         print("[%s:%d] priceOf_Position : updated => %.03f" % \
# #                             (os.path.basename(libs.thisfile()), libs.linenum()
# #                             , priceOf_Position
# #                             ), file=sys.stderr)
# #                         
# #                         # counter
# #                         cntOf_Iteration += 1
# #                         
# #                         #debug
# #                         if cntOf_Iteration > dbg_MaxCount :     #if cntOf_Iteration > dbg_MaxCount
# #                     
# #                             print()
# #                             print("[%s:%d] break the for loop" % \
# #                                 (os.path.basename(libs.thisfile()), libs.linenum()
# #                                 
# #                                 ), file=sys.stderr)
# #                             
# #                             break
# # 
# #                         # next iteration
# #                         continue
# #                         
# #                     else :  ### j2.N
# # 
# #                         print()
# #                         print("[%s:%d] flg_In => %s" % \
# #                             (os.path.basename(libs.thisfile()), libs.linenum()
# #                             , flg_In
# #                             ), file=sys.stderr)
# #                         
# #                         # flag : up
# #                         flg_In = True
# # #                         flg_in = True
# #                         
# #                         print()
# #                         print("[%s:%d] flg_In is now => %s" % \
# #                             (os.path.basename(libs.thisfile()), libs.linenum()
# #                             , flg_In
# #                             ), file=sys.stderr)
# #                         
# #                         # set the price of the position
# #                         priceOf_Position = e_1.price_Close
# #                         
# #                         #debug
# #                         print()
# # #                         print("[%s:%d] position opened => %.03f" % \
# #                         print("[%s:%d] position opened => %.03f (count = %d)" % \
# #                             (os.path.basename(libs.thisfile()), libs.linenum()
# #                             , priceOf_Position, cntOf_Iteration
# #                             ), file=sys.stderr)
# #                         
# #                         # counter
# #                         cntOf_Iteration += 1
# #                         
# #                         #debug
# #                         if cntOf_Iteration > dbg_MaxCount :     #if cntOf_Iteration > dbg_MaxCount
# #                     
# #                             print()
# #                             print("[%s:%d] break the for loop" % \
# #                                 (os.path.basename(libs.thisfile()), libs.linenum()
# #                                 
# #                                 ), file=sys.stderr)
# #                             
# #                             break
# # 
# #                         # next iteration
# #                         continue
# #                         
# #                     #/if flg_In == True    ### j2
# #                     
# #                 else : #/if res == True    ### j1.N
# # 
# #                     print()
# #                     print("[%s:%d] res ==> not True (price is down)" % \
# #                         (os.path.basename(libs.thisfile()), libs.linenum()
# #                         
# #                         ), file=sys.stderr)
# #                     
# #                     '''###################
# #                         j3 : flag is up ?
# #                     ###################'''
# #                     if flg_In == True : #if flg_In == True
# # 
# #                         print()
# #                         print("[%s:%d] flg_In ==> True (prev is up, now down)" % \
# #                             (os.path.basename(libs.thisfile()), libs.linenum()
# #                             
# #                             ), file=sys.stderr)
# # 
# #                         # sell
# #                         
# #                         # calculate : profit/loss
# #                         profit_loss = priceOf_Position - pc_1
# #                         
# #                         print()
# #                         print("[%s:%d] position => closed" % \
# #                             (os.path.basename(libs.thisfile()), libs.linenum()
# #                             ), file=sys.stderr)
# #                         print("[%s:%d] profit_loss => %.03f" % \
# #                         (os.path.basename(libs.thisfile()), libs.linenum()
# #                         , profit_loss
# #                         ), file=sys.stderr)
# #                         
# #                         # append profit_loss
# #                         lo_Profit_Loss.append(
# #                                 [
# #                                     i
# #                                      , profit_loss
# #                                      , e_1.dateTime_Local
# #                                      , e_1.dateTime
# #                                      , e_1.price_Close
# #                                  ]
# #                                 )
# #                         
# #                         
# #                         # flag : down
# #                         flg_In = False
# #                         
# #                         # reset : price of the positin
# #                         priceOf_Position = 0
# #                         
# #                         # counter
# #                         cntOf_Iteration += 1
# #                         
# #                         #debug
# #                         if cntOf_Iteration > dbg_MaxCount :     #if cntOf_Iteration > dbg_MaxCount
# #                     
# #                             print()
# #                             print("[%s:%d] break the for loop" % \
# #                                 (os.path.basename(libs.thisfile()), libs.linenum()
# #                                 
# #                                 ), file=sys.stderr)
# #                             
# #                             break
# #                         
# #                         # next iteration
# #                         continue
# #                     
# #                     else : #if flg_In == True    ### j3.N
# #                     
# #                         # counter
# #                         cntOf_Iteration += 1
# #                         
# #                         #debug
# #                         if cntOf_Iteration > dbg_MaxCount :     #if cntOf_Iteration > dbg_MaxCount
# #                     
# #                             print()
# #                             print("[%s:%d] break the for loop" % \
# #                                 (os.path.basename(libs.thisfile()), libs.linenum()
# #                                 
# #                                 ), file=sys.stderr)
# #                             
# #                             break
# #                     
# #                         # next
# #                         continue
# #                     
# #                     #/if flg_In == True    ### j3
# # 
# # 
# # 
# # #                     pass
# #                 
# #                 #/if res == True    ### j1
# #     
# #     
# #                 
# #                 
# #                 # counter
# #                 cntOf_Iteration += 1
# #                 
# #                 #debug
# #                 if cntOf_Iteration > dbg_MaxCount :     #if cntOf_Iteration > dbg_MaxCount
# #             
# #                     print()
# #                     print("[%s:%d] break the for loop" % \
# #                         (os.path.basename(libs.thisfile()), libs.linenum()
# #                         
# #                         ), file=sys.stderr)
# #                     
# #                     break
# #                 
# #                 #/if cntOf_Iteration > dbg_MaxCount
# #             
# #             
# #             
# #             #/for i in range(lenOf_Lo_BarData - 1:
# # 
# #             #report
# #             print()
# #             print("[%s:%d] lo_Profit_Loss ==>" % \
# #                     (os.path.basename(libs.thisfile()), libs.linenum()
# #                     
# #                     ), file=sys.stderr)
# #             
# #             for item in lo_Profit_Loss:
# #             
# #                 print(item)
# #                 
# #             #/for item in lo_Profit_Loss:
# # 
# # #             print(lo_Profit_Loss)
# #             
# #             lo_Tmp = [x[1] for x in lo_Profit_Loss]
# #             
# #             sumOf_Profit_Loss = sum(lo_Tmp)
# #             
# #             print("sum is => %.03f" % sumOf_Profit_Loss)
# # #             print("sum is => %.03f" % sum(lo_Profit_Loss))
#             
#         '''###################
#             time        
#         ###################'''
#         time_Elapsed = time.time() - time_Start

    
    #/if fname == False and dpath_image == False
        
        
    
#     '''###################
#         time        
#     ###################'''
#     time_Elapsed = time.time() - time_Start
    
#     '''###################
#         vars
#     ###################'''
#     dic = {}
    

#     dic['action'] = "action"
#     dic["msg"] = "message"

    '''###################
        render        
    ###################'''
    '''###################
        get : referer        
    ###################'''
    referer_MM = "http://localhost:8000/curr/testers/"
#     referer_MM = "http://127.0.0.1:8000/curr/"
    
    referer_Current = request.META.get('HTTP_REFERER')
    
#     # set : message
# #     dic["msg"] = "rendering... (%s)(time : %02.3f sec)" \
#     dic["msg"] += " (%s)(time : %02.3f sec)" \
#                     % (libs.get_TimeLabel_Now(), time_Elapsed)
    
    if referer_Current == referer_MM : #if referer_Current == referer_MM
    
        print()
        print("[%s:%d] referer_Current == referer_MM (current = %s / referer = %s" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                ,referer_Current, referer_MM
                ), file=sys.stderr)
    
        return render(request, url_Path, dic)
#         return render(request, 'curr/exec_Tester_BuyUps_SellLows.html', dic)
#         return render(request, 'mm/numbering.html', dic)
        
    else : #if referer_Current == referer_MM

        print()
        print("[%s:%d] referer_Current <> referer_MM (current = %s / referer = %s" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                ,referer_Current, referer_MM
                ), file=sys.stderr)

        return render(request, url_Path_Full, dic)
#         return render(request, 'curr/exec_Tester_BuyUps_SellLows_full.html', dic)


    
#     return HttpResponse("Hello Django")


