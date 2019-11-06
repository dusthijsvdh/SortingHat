import excel_parser.parser as exp
from random import choice

def calculate(index):
    rec = exp.get_record(exp.get_records("db.xlsx"), int(index))
    
    se = rec["punten_se"]
    fict = rec["punten_fict"]
    bdam = rec["punten_bdam"]
    iat = rec["punten_bdam"]
    
    res = [se, fict, bdam, iat]
    res.sort()
    specs = ["se", "fict", "bdam", "iat"]
    uitslag = ""
    
    for spec in specs:
        if rec["punten_" + spec] == res[-1]:
            uitslag = spec
    return uitslag