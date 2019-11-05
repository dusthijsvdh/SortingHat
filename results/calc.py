import excel_parser.parser as exp
from random import choice

def calculate(index):
    rec = exp.get_record(exp.get_records("db.xlsx"), int(index))
    an = rec["punten_an"]
    ad = rec["punten_ad"]
    re = rec["punten_re"]
    on = rec["punten_on"]
    mc = rec["punten_mc"]
    ia = rec["bool_ia"]

    low = range(0, 25)
    mid = range(25, 50)
    high = range(50, 100)

    result = ""

    if re in high and on in high:
        if ia:
            result = "Iat"
        else:
            result = "Se"
    elif ad in high:
        result = "Bdam"
    elif on in low:
        result = "Fict"
    else:
        result = choice(["Iat_rng", "Se_rng", "Fict_rng", "Bdam_rng"])
    return result