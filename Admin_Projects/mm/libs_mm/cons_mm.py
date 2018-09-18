#!C:\WORKS_2\Programs\Python\Python_3.5.1\python.exe
from enum import Enum

class ImOp(Enum):
    
    lo_Commands = [
        
        [0, "Numbering"],
        [1, "De-numbering"],
        [2, "Build history"],
        
#         [1, "Numbering"],
#         [2, "De-numbering"],

    
    ]
    
    
#/class ImOp(Enum):

class CURROp(Enum):
    
    lo_Commands = [
        
        [0, "Updown patterns"],
        [1, "Correlations"],
    
    ]
    
    
#/class ImOp(Enum):

class FPath(Enum):
    
    '''###################
        @USED
                
    ###################'''
    DPATH_MM_PROJECTS   = "C:\WORKS_2\WS\FM_2_20171104_225946\Projects"
    
class Numbering(Enum):
    
    ID_BT_EXEC_NUMBERING_0 = "bt_Exec_Numbering_0"
    
    
class ExecNumbering(Enum):

    DICKEY_MSG      = "msg"
    DICKEY_DPATH      = "dpath"
    DICKEY_FNAME      = "fname"


class RetVal(Enum):
    
    RET_OK      = "OK"
    
#/class RetVal(Enum):

class MM(Enum):
    
    MM_NUMBERING_OMIT_NODES = [
        
        'arrowlink' ,
        'attribute' ,
        'attribute_layout' ,
        'cloud' ,
        'icon' ,
        'font' ,
        'linktarget'
        
    ]
    
    MM_NUMBERING_OMIT_LABELS = [
        
        "NEXT",
        "DROP",
        "ENOUGH",
        
        "HISTORY",
        
        "ADMIN",
        
        "Z",    #=> used in : Music.mm : "1-1-1) accompany" ---> patterns
        
    ]
        
#/ class MM(Enum):
    
    
    
# C:\\WORKS_2\\WS\\FM_2_20171104_225946\\Projects