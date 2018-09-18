#!C:\WORKS_2\Programs\Python\Python_3.5.1\python.exe
from enum import Enum

class ImOp(Enum):
    
    OP_0_1 = "0-1"      # 0-1) start xampp, filezilla, open folder, open files.bat
    OP_1 = "1"          # 1) change_file_names.bat
    OP_1_2 = "1-2"      # 1-2) Delete_in-db-existing-files.bat
    OP_1_3 = "1-3"      # 1-3) Delete temporary-purpose files
    
    OP_2_0 = "2-0"      # 2-0) edit_memos.9-0.bat
    OP_4 = "4"          # 4) edit_memos.8.open-csv-file.bat - ショートカット
    OP_5 = "5"          # 5) edit_memos.3.insert-to-db.bat - ショートカット
    
    OP_7 = "7"      # 7) edit_memos.12.delete-image-files.bat - ショートカット
    OP_8 = "8"      # 8) edit_memos.4.delete-photos.bat - ショートカット
    OP_9 = "9"      # 9) edit_memos.13.validate-admin-value.bat - ショートカット
    OP_9_1 = "9-1"      
    
    OP_10 = "10"
    OP_10_1 = "10-1"

    OP_11 = "11"
    OP_11_0 = "11-0"
    OP_11_1 = "11-1"

    OP_12 = "12"
    OP_13 = "13"

    OP_14 = "14"

    OP_15 = "15"
    OP_16 = "16"

    lo_Commands = [
        
        [OP_0_1, "0-1) start xampp, filezilla, open folder, open files.bat", "start apps"],
        [OP_1, "1) change_file_names.bat", "change_file_names"],
        [OP_1_2, "1-2) Delete_in-db-existing-files.bat", "Delete_in-db-existing-files"],
        [OP_1_3, "", "*Delete temporary-purpose files*"],

        [OP_2_0, "2-0) edit_memos.9-0.bat", "start editing"],
        [OP_4, "4) edit_memos.8.open-csv-file.bat - ショートカット", "open csv file"],
        [OP_5, "edit_memos.3.insert-to-db.bat", "insert to db"],
               
        [OP_7, "edit_memos.12.delete-image-files.bat", "delete image files"],
        [OP_8, "edit_memos.4.delete-photos.bat", "delete db entries"],
        [OP_9, "edit_memos.13.validate-admin-value.bat", "validate admin value"],
#         [OP_9, "9) edit_memos.13.validate-admin-value.bat - ショートカット"],
#         [OP_0_1, "0-1) start xampp, filezilla, open folder, open files.bat"],
#         [OP_1, "1) change_file_names.bat"],
#         [OP_1_2, "1-2) Delete_in-db-existing-files.bat"],
# 
#         [OP_2_0, "2-0) edit_memos.9-0.bat"],
#         [OP_4, "4) edit_memos.8.open-csv-file.bat - ショートカット"],
#         [OP_5, "edit_memos.3.insert-to-db.bat"],
# #         [OP_5, "5) edit_memos.3.insert-to-db.bat - ショートカット"],
#                
#         [OP_7, "edit_memos.12.delete-image-files.bat"],
# #         [OP_7, "7) edit_memos.12.delete-image-files.bat - ショートカット"],
#         [OP_8, "edit_memos.4.delete-photos.bat"],
# #         [OP_8, "8) edit_memos.4.delete-photos.bat - ショートカット"],
#                
#         [OP_9, "edit_memos.13.validate-admin-value.bat"],
# #         [OP_9, "9) edit_memos.13.validate-admin-value.bat - ショートカット"],

        [OP_9_1, "9-1) upload db file.txt", "***"],
        [OP_16, "9-2) upload db file", "upload db file"],    # C:\WORKS_2\WS\WS_Cake_IFM11\commands
        [OP_10, "edit_memos.14.add-data-to-remote.bat", "data ==> to remote"],

        [OP_10_1, "10-1) edit_memos.14.add-data-to-remote.history.txt", "data ==> to file"],
        [OP_11, "edit_memos.15.validate-update.bat", "validate updates"],
        [OP_11_0, "11-0) update date.txt", "update data ==> to file"],

        [OP_11_1, "11-1) open update page.bat", "open update page"],    # C:\WORKS_2\WS\WS_Cake_IFM11\commands
        [OP_12, "edit_memos.5.copy-image-files.bat", "copy image files"],    # 
        [OP_13, "13) image_move-uploaded-files.bat", "move uploaded images"],    # C:\WORKS_2\WS\WS_Cake_IFM11\commands
    
        [OP_14, "14) upload image files", "upload image files"],    # C:\WORKS_2\WS\WS_Cake_IFM11\commands
        [OP_15, "15) close-apps.bat", "close apps"],    # C:\WORKS_2\WS\WS_Cake_IFM11\commands
        
#         [OP_9_1, "9-1) upload db file.txt", "upload db file"],
#         
#         [OP_16, "9-2) upload db file"],    # C:\WORKS_2\WS\WS_Cake_IFM11\commands
#     
# 
#         [OP_10, "edit_memos.14.add-data-to-remote.bat"],
#         [OP_10_1, "10-1) edit_memos.14.add-data-to-remote.history.txt"],
#                    
#         [OP_11, "edit_memos.15.validate-update.bat"],
#         [OP_11_0, "11-0) update date.txt"],
#         [OP_11_1, "11-1) open update page.bat"],    # C:\WORKS_2\WS\WS_Cake_IFM11\commands
#                    
#         [OP_12, "edit_memos.5.copy-image-files.bat"],    # 
#         
#         [OP_13, "13) image_move-uploaded-files.bat"],    # C:\WORKS_2\WS\WS_Cake_IFM11\commands
#     
#         [OP_14, "14) upload image files"],    # C:\WORKS_2\WS\WS_Cake_IFM11\commands
#     
#         [OP_15, "15) close-apps.bat"],    # C:\WORKS_2\WS\WS_Cake_IFM11\commands
#         
    ]
    
#/class ImOp(Enum):

class FPath(Enum):
    
    '''###################
        @USED
        viwes :: _im_actions__Ops_4()
                _im_actions__Ops_5(action)
                
    ###################'''
    DPATH_CMD_LIB_OTHERS = "C:\\WORKS_2\\WS\\Eclipse_Luna\\Cake_IFM11\\lib\\others"
    
    DPATH_CMD_LIB_WS_CAKE_IFM11 = "C:\\WORKS_2\\WS\\WS_Cake_IFM11\\commands"
    
    FPATH_LOG_FILE = "C:\\WORKS_2\\WS\\WS_Cake_IFM11\\commands\\12-2) upload image files.log"
    
    #ref capitalize, upper case http://vim.wikia.com/wiki/Changing_case_with_regular_expressions
    DPATH_DB_FILES__LOCAL = "C:\\WORKS_2\\WS\\Eclipse_Luna\\Cake_IFM11\\app\\Lib\\data"
    
    '''###################
        paths : remote        
    ###################'''
    DIR_TARGET_REMOTE__UPLOAD_DB_FILE = "/cake_apps/Cake_IFM11/app/Lib/data"
    
    '''###################
        names        
    ###################'''
    FNAME_DB = "ifm11_backup_20160110_080900.bk"
    
    