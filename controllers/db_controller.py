from controllers import excel_controller
from time import sleep

def get_records():
    records = excel_controller.get_records("db.xlsx")
    return {"records": records}

def get_record(index):
    records = excel_controller.get_records("db.xlsx")
    return records[int(index)]

def add_record(name):
    sheet = excel_controller.get_sheet("db.xlsx")
    excel_controller.add_record(sheet, "db.xlsx", [name, 0,0,0,0])
    sleep(0.2)
    
def update_record(index, field, value):
    if field != "naam": value = int(value)
    sheet = excel_controller.get_sheet("db.xlsx")
    
    record = excel_controller.get_record(index)
    record[field] = value
    new_record = excel_controller.record_to_list(record)
    
    excel_controller.update_record(sheet, "db.xlsx", index + 1, new_record)