from django import template

import sys

sys.path.append('C:/WORKS_2/WS/WS_Others/prog/D-7/2_2/VIRTUAL/Admin_Projects/mm')
from mm.libs_mm import cons_mm, cons_fx, libs, libfx


register = template.Library()

@register.simple_tag
# def print(param):
def p(param):
# def show(param):
    
    param = param + " done"
    
#     return "yes : " % (param)
#     return "yes : " % param
    return param


#ref https://stackoverflow.com/questions/4731572/django-counter-in-loop-to-index-list
@register.filter
def access_index(sequence, position):
    return sequence[position]

# @register.simple_tag

# @register.tag
@register.simple_tag
def get_CurrencyPair_Name(param):
    
    # split the file name
    tokens = param.split(".")
    
    '''###################
        vars        
    ###################'''
    target = ""
    
    '''###################
        search        
    ###################'''
    pair_Names = cons_fx.PairName.pair_Names.value
# #     pair_Names = [
#         
#         "USDJPY",
#         "EURJPY",
#         "USDJPY",
#         
#     ]
    
    for item in tokens:

        # search
        if item in pair_Names : #if item in pair_Names
    
            target = item
            
            break
            
        #/if item in pair_Names
        
    #/for item in tokens:

    
    return target
#     return tokens[0]
#     return "yes : %s" % param