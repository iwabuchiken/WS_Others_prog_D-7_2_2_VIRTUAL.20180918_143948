#!C:\WORKS_2\Programs\Python\Python_3.5.1\python.exe
from enum import Enum

from Admin_Projects.definitions import ROOT_DIR
from Admin_Projects.definitions import DPATH_ROOT_CURR

TypeOf_Data_OpenClose   = "OpenClose"

'''###################
    Used in :
        libfx : def get_HighLowDiffs(aryOf_BarDatas, id_Start, id_End)
###################'''
class BarData(Enum):
    
    LABEL_OC        = "OC"
    LABEL_HL        = "HL"
    LABEL_RSI = "RSI"
    LABEL_MFI = "MFI"
    
    LABEL_BB_MAIN = "BB_Main"
    LABEL_BB_1S = "BB_1S"
    LABEL_BB_2S = "BB_2S"
    LABEL_BB_M1S = "BB_M1S"
    LABEL_BB_M2S = "BB_M2S"
    
    ROUND_BB    = 4
    ROUND_RSI   = 4
    ROUND_MFI   = 4
    
#     HighLowDiff_ID_Start    = 1
#     HighLowDiff_ID_End      = 5
#    HighLowDiff_ID_Start    = 195
#    HighLowDiff_ID_End      = 202
#    HighLowDiff_ID_Start    = 219	# 2017.12.18 13:00
#    HighLowDiff_ID_End      = 226	# 2017.12.16 06:00
    HighLowDiff_ID_Start    = 243	# 2017.12.15 13:00
    HighLowDiff_ID_End      = 250	# 2017.12.15 06:00

class FPath(Enum):
    
    fname_In_CSV = "44_1.14_file-io.EURUSD.Period-H1.Days-1900.Bars-45600.20180511_180935.csv"
    
    dpath_In_CSV = DPATH_ROOT_CURR + "\\data\\csv"
    
    fpath_Out_HighLowDiff = "outputs"

    ### file : output
    
    dpath_Data_Miscs = DPATH_ROOT_CURR + "/data/miscs"
    
    '''###################
        gen peak data        
    ###################'''
    fname_Gen_PeakData_Dflt = "49_20_file-io.USDJPY.Period-H1.Days-1200.Bars-28800.20180428_073251.csv"

    '''###################
        general        
    ###################'''
    dpath_LogFile = "C:\\WORKS_2\\WS\\WS_Others\\prog\\D-7\\2_2\\VIRTUAL\\Admin_Projects\\curr\\data\\log"
    
    fname_LogFile = "tester_BUSL.log"
    
    '''###################
        BUSL_3
    ###################'''
#     BUSL_3_FNAME_PEAK_LIST = "44_3.2_5_file-io.USDJPY.Period-M5.Days-26000.Bars-26000.20180721_160221.SHRINK-2000.csv"
#     BUSL_3_FNAME_PEAK_LIST = "44_3.2_5_file-io.USDJPY.Period-M5.Days-26000.Bars-26000.20180721_160221.csv"
#     BUSL_3_FNAME_PEAK_LIST = "44_3.2_11_file-io.USDJPY.Period-H1.Days-6000.Bars-144000.20180813_113150.csv"
#     BUSL_3_FNAME_PEAK_LIST = "44_3.2_11_file-io.EURJPY.Period-H1.Days-5000.Bars-120000.20180813_115015.csv"
#     BUSL_3_FNAME_PEAK_LIST = "44_3.2_11_file-io.EURJPY.Period-M5.Days-25000.Bars-25000.20180813_120112.csv"
#     BUSL_3_FNAME_PEAK_LIST = "44_3.2_5_file-io.USDJPY.Period-M5.Days-26000.Bars-26000.20180721_160222.SHRINK-100.csv"
#     BUSL_3_FNAME_PEAK_LIST = "44_3.2_11_file-io.USDJPY.Period-H1.Days-6000.Bars-144000.20180813_113150.SHRINK-100.csv"
#     BUSL_3_FNAME_PEAK_LIST = "44_3.2_11_file-io.EURJPY.Period-M5.Days-25000.Bars-25000.20180813_120112.SHRINK-100.csv"
#     BUSL_3_FNAME_PEAK_LIST = "44_3.2_11_file-io.EURJPY.Period-M5.Days-25000.Bars-25000.20180813_120112.SHRINK-1000.csv"
#     BUSL_3_FNAME_PEAK_LIST = "44_3.2_11_file-io.EURJPY.Period-H1.Days-5000.Bars-120000.20180813_115015.SHRINK-100.csv"
#     BUSL_3_FNAME_PEAK_LIST = "44_3.2_11_file-io.EURJPY.Period-H1.Days-5000.Bars-120000.20180813_115015.SHRINK-1000.csv"
#     BUSL_3_FNAME_PEAK_LIST = \
#             "44_3.2_11_file-io.EURJPY.Period-H1.Days-5000.Bars-120000.20180813_115015" \
#             + ".SHRINK-100.csv"
    BUSL_3_FNAME_PEAK_LIST = \
            "44_3.2_15_file-io.EURJPY.Period-H1.Days-5000.Bars-120000.20180903_135341" \
            + ".2018-07.csv"
#             + ".2018-08.csv"
#     BUSL_3_FNAME_PEAK_LIST = \
#             "44_3.2_15_file-io.EURJPY.Period-H1.Days-5000.Bars-120000.20180903_135341" \
#             + ".SHRINK-200.csv"
#     BUSL_3_FNAME_PEAK_LIST = "44_3.2_15_file-io.EURJPY.Period-H1.Days-5000.Bars-120000.20180903_135341.SHRINK-100.csv"
#     BUSL_3_FNAME_PEAK_LIST = "44_3.2_15_file-io.EURJPY.Period-H1.Days-5000.Bars-120000.20180903_135341.2018-08.csv"
#     BUSL_3_FNAME_PEAK_LIST = "44_3.2_15_file-io.EURJPY.Period-H1.Days-5000.Bars-120000.20180903_135341.2018-07.csv"
#     BUSL_3_FNAME_PEAK_LIST = "44_3.2_15_file-io.EURJPY.Period-H1.Days-5000.Bars-120000.20180903_135341.2018-06.csv"
    BUSL_3_DPATH_PEAK_LIST = "C:\\WORKS_2\\WS\\WS_Others\\prog\\D-7\\2_2\\VIRTUAL\\Admin_Projects\\curr\\data\\csv_raw"
    
class Label_ColNames(Enum):
    
    PAIR    = 'PAIR'
    PERIOD  = 'PERIOD'
    DAYS    = 'DAYS'
    SHIFT   = 'SHIFT'
    

class PatternMatch(Enum) :
    
    '''###################
        get_AryOf_BarDatas_PatternMatched__RSI__V2
    ###################'''
    PATTERNMATCH_NUMOFSEQUENCE_RSI = 3  # USED IN : get_AryOf_BarDatas_PatternMatched__RSI
    
    RANGE_FLAT_RSI          = 1.0  # USED IN : get_AryOf_BarDatas_PatternMatched__RSI
    
    FLAG_UPDOWN_UP          = 1  # USED IN : get_AryOf_BarDatas_PatternMatched__RSI
    
    FLAG_UPDOWN_DOWN        = 0  # USED IN : get_AryOf_BarDatas_PatternMatched__RSI
    
    '''###################
        get_AryOf_BarDatas_PatternMatched__Body_UpDown()
    ###################'''
    VOLUMEOF_BODY       = 0.05   # JPY
#     VOLUMEOF_BODY       = 0.1   # JPY
#     VOLUMEOF_BODY       = 0.15   # JPY
#     VOLUMEOF_BODY       = 0.20   # JPY
#     VOLUMEOF_BODY       = 0.25   # JPY
#     VOLUMEOF_BODY       = 0.30   # JPY
#     VOLUMEOF_BODY       = 0.35   # JPY
#     VOLUMEOF_BODY       = 0.40   # JPY
#     VOLUMEOF_BODY       = 0.45   # JPY
#     VOLUMEOF_BODY       = 0.5   # JPY
    
    UPDOWN_PATTERN      = [1,1,1,0]
    
class PairName(Enum) :
    
    pair_Names = [
        
        "USDJPY",
        "EURJPY",
        "AUDJPY",
        "GBPJPY",
        
        "EURUSD",
        
    ]

class ParamConstants(Enum):
    
    '''###################
        http://127.0.0.1:8000/curr/tester_BuyUps_SellLows/?command=BUSL_3&busl3_action=        
        key : busl3_action
    ###################'''
    # key
    PARAM_BUSL3_KEY__ACTION = "busl3_action"
    
    # values
    PARAM_BUSL3_CMD_2UPS = "busl3_command_2ups"
    PARAM_BUSL3_CMD_3UPS = "busl3_command_3ups"
#     PARAM_BUSL3_CMD_2UPS = "2ups"
    '''###################
        next_up        
    ###################'''
    PARAM_BUSL3_CMD_NEXTUP = "next_up"
    PARAM_BUSL3_CMD_NEXTUP_ABOVE_BB_MAIN = "next_up_above_bb_main"
    
    '''######################################
        expert : busl3
    ######################################'''
    '''###################
        expert : busl3 : 1 : over BB.1S
    ###################'''
    PARAM_BUSL3_CMD_EXPERT_1_OVER_BB_1S = "expert_busl3___1_over_bb_1s"
    '''###################
        expert : busl3 : 2 : up-up, down-down
    ###################'''
    PARAM_BUSL3_CMD_EXPERT_2_UPUPS_DOWNDOWNS = "expert_busl3___2_upups_downdowns"
    
    '''###################
        utils : busl3 : 1 : UpsDowns_in_BB_Ranges
    ###################'''
    PARAM_BUSL3_CMD_UTIL__1_UPSDOWNS_IN_BB_RANGES = \
                    "util_get_stats__1_upsdowns_in_bb_ranges"
    
    '''######################################
        utils : busl3 : 2 : research
    ######################################'''
    '''###################
        utils : busl3 : 2 : research / 1 : up-down pattern
    ###################'''
    PARAM_BUSL3_CMD_RES__1_DETECT_PATTERNS__UPSDOWNS = \
                    "busl3_res__1_detect_patterns__updowns"
    
    
    
class Tester(Enum):
    
    lo_Commands = [
        
        ["buy_Ups_Sell_Lows", "Buy ups, sell lows"],
        
#         [1, "Numbering"],
#         [2, "De-numbering"],

    
    ]

    # http://127.0.0.1:8000/curr/tester_BuyUps_SellLows/?command=BUSL_3&
    lo_Actions__BUSL__IDs = [
            
            "1"         # num of up bars and down bars in each of BB areas
            , "2-1"     # up-down pattern of 5 bars : log at detect_pattern.Updowns.XXX.log
            
        ]
    
    lo_Actions__BUSL = [
        
            [
                lo_Actions__BUSL__IDs[0]
                ,"get stats for BB"
                , ParamConstants.PARAM_BUSL3_CMD_UTIL__1_UPSDOWNS_IN_BB_RANGES.value
                , "num of up bars and down bars in each of BB areas"
                , "20180915_124138"
            ],
        
            [
                lo_Actions__BUSL__IDs[1]
                ,"res : pattern detection"
                , ParamConstants.PARAM_BUSL3_CMD_RES__1_DETECT_PATTERNS__UPSDOWNS.value
                , "up-down pattern of 5 bars : log at detect_pattern.Updowns.XXX.log"
                , "20180915_125135"
            ],
        
        
        ]
