# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"C23","system":"icd10"},{"code":"C26.1","system":"icd10"},{"code":"C30.0","system":"icd10"},{"code":"C31","system":"icd10"},{"code":"C32","system":"icd10"},{"code":"C37","system":"icd10"},{"code":"C48","system":"icd10"},{"code":"C51","system":"icd10"},{"code":"C52","system":"icd10"},{"code":"C58","system":"icd10"},{"code":"C60","system":"icd10"},{"code":"C69","system":"icd10"},{"code":"C80","system":"icd10"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('primary-malignancy_other-organs-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["primary-malignancy_other-organs-neoplasm---secondary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["primary-malignancy_other-organs-neoplasm---secondary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["primary-malignancy_other-organs-neoplasm---secondary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
