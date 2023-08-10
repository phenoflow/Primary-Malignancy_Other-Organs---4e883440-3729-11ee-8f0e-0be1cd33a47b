# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"101465.0","system":"med"},{"code":"101778.0","system":"med"},{"code":"102688.0","system":"med"},{"code":"103353.0","system":"med"},{"code":"104324.0","system":"med"},{"code":"105025.0","system":"med"},{"code":"1056.0","system":"med"},{"code":"107126.0","system":"med"},{"code":"107638.0","system":"med"},{"code":"108037.0","system":"med"},{"code":"109342.0","system":"med"},{"code":"10995.0","system":"med"},{"code":"11009.0","system":"med"},{"code":"11035.0","system":"med"},{"code":"12490.0","system":"med"},{"code":"13559.0","system":"med"},{"code":"15976.0","system":"med"},{"code":"16280.0","system":"med"},{"code":"17559.0","system":"med"},{"code":"18270.0","system":"med"},{"code":"19141.0","system":"med"},{"code":"19144.0","system":"med"},{"code":"20166.0","system":"med"},{"code":"23861.0","system":"med"},{"code":"26034.0","system":"med"},{"code":"26454.0","system":"med"},{"code":"27449.0","system":"med"},{"code":"28272.0","system":"med"},{"code":"29283.0","system":"med"},{"code":"29462.0","system":"med"},{"code":"30646.0","system":"med"},{"code":"31399.0","system":"med"},{"code":"32240.0","system":"med"},{"code":"35186.0","system":"med"},{"code":"37618.0","system":"med"},{"code":"38736.0","system":"med"},{"code":"38978.0","system":"med"},{"code":"39027.0","system":"med"},{"code":"40608.0","system":"med"},{"code":"41931.0","system":"med"},{"code":"42218.0","system":"med"},{"code":"42569.0","system":"med"},{"code":"43450.0","system":"med"},{"code":"44356.0","system":"med"},{"code":"44884.0","system":"med"},{"code":"45260.0","system":"med"},{"code":"45262.0","system":"med"},{"code":"45267.0","system":"med"},{"code":"4555.0","system":"med"},{"code":"45766.0","system":"med"},{"code":"46153.0","system":"med"},{"code":"47286.0","system":"med"},{"code":"47810.0","system":"med"},{"code":"49292.0","system":"med"},{"code":"49301.0","system":"med"},{"code":"49828.0","system":"med"},{"code":"51255.0","system":"med"},{"code":"51818.0","system":"med"},{"code":"52029.0","system":"med"},{"code":"52316.0","system":"med"},{"code":"54267.0","system":"med"},{"code":"55098.0","system":"med"},{"code":"55101.0","system":"med"},{"code":"55588.0","system":"med"},{"code":"56490.0","system":"med"},{"code":"56918.0","system":"med"},{"code":"57191.0","system":"med"},{"code":"57756.0","system":"med"},{"code":"57854.0","system":"med"},{"code":"58903.0","system":"med"},{"code":"58962.0","system":"med"},{"code":"59286.0","system":"med"},{"code":"60052.0","system":"med"},{"code":"60918.0","system":"med"},{"code":"62814.0","system":"med"},{"code":"63224.0","system":"med"},{"code":"64195.0","system":"med"},{"code":"64309.0","system":"med"},{"code":"64427.0","system":"med"},{"code":"64497.0","system":"med"},{"code":"64567.0","system":"med"},{"code":"64568.0","system":"med"},{"code":"64810.0","system":"med"},{"code":"65106.0","system":"med"},{"code":"65434.0","system":"med"},{"code":"65458.0","system":"med"},{"code":"65793.0","system":"med"},{"code":"66646.0","system":"med"},{"code":"67217.0","system":"med"},{"code":"67949.0","system":"med"},{"code":"68236.0","system":"med"},{"code":"68332.0","system":"med"},{"code":"68787.0","system":"med"},{"code":"68824.0","system":"med"},{"code":"70716.0","system":"med"},{"code":"71609.0","system":"med"},{"code":"71672.0","system":"med"},{"code":"72500.0","system":"med"},{"code":"73510.0","system":"med"},{"code":"8693.0","system":"med"},{"code":"86997.0","system":"med"},{"code":"87113.0","system":"med"},{"code":"88144.0","system":"med"},{"code":"8918.0","system":"med"},{"code":"89916.0","system":"med"},{"code":"90659.0","system":"med"},{"code":"92329.0","system":"med"},{"code":"93384.0","system":"med"},{"code":"94355.0","system":"med"},{"code":"94776.0","system":"med"},{"code":"94935.0","system":"med"},{"code":"95421.0","system":"med"},{"code":"95792.0","system":"med"},{"code":"96226.0","system":"med"},{"code":"97547.0","system":"med"},{"code":"97996.0","system":"med"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('primary-malignancy_other-organs-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["possible-primary-malignancy_other-organs---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["possible-primary-malignancy_other-organs---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["possible-primary-malignancy_other-organs---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
