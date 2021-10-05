# Agile-CS555-Team-4
def dif_line(ve_line):
    stripped = ve_line.strip('\n') 
    return stripped.split(" ")

def correct_tags (dif_lines):
    imp_zero_tags = ["INDI",  "FAM",  "HEAD", "TRLR", "NOTE"]
    imp_one_tags = ["NAME", "SEX", "BIRT", "DEAT", "FAMC", "FAMS", "MARR", "HUSB", "WIFE", "CHIL", "DIV"]
    imp_two_tags = ["DATE"]

    level = dif_lines.pop(0)
    tag = dif_lines.pop(0)
    args = " ".join(dif_lines)

    if (args in imp_zero_tags or args in imp_one_tags or args in imp_two_tags):
        temp = tag
        tag = args
        args = temp

    if (level == "0"):
        if tag in imp_zero_tags:
            valid = "Y"
        else:
            valid = "N"
    elif (level == "1"):
        if tag in imp_one_tags:
            valid = "Y"
        else: 
            valid = "N"
    elif (level == "2"):
        if tag in imp_two_tags:
            valid = "Y"
        else:
            valid = "N"
    else: 
        valid = "N"

    return "<-- " + level + "|" + tag + "|" + valid + "|" + args 
            




if __name__ == "__main__":
   file = open('gedcome file.ged')
    
ve_lines = file.readlines()

for ve_line in ve_lines:
        print ("--> " + ve_line)
        print(correct_tags(dif_line(ve_line)))

file.close
