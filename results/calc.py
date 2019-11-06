import excel_parser.parser as exp
import json

def calculate(index):
    rec = exp.get_record(exp.get_records("db.xlsx"), int(index))
    
    specs = {
        "se": {"max": 0, "cur": rec["punten_se"], "procent": 0},
        "fict": {"max": 0, "cur": rec["punten_fict"], "procent": 0},
        "bdam": {"max": 0, "cur": rec["punten_bdam"], "procent": 0},
        "iat": {"max": 0, "cur": rec["punten_iat"], "procent": 0}
    }
    
    with open("./routes/vragen.json") as f:
        vragenDict = json.load(f)
        
    for antwoorden in vragenDict["antwoorden"]:
        for antwoord in antwoorden:
            specs[antwoord[2]]["max"] += antwoord[1]
            specs[antwoord[2]]["procent"] = (specs[antwoord[2]]["cur"] / specs[antwoord[2]]["max"]) * 100
    
    return "testing"