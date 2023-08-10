# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"100232.0","system":"med"},{"code":"100615.0","system":"med"},{"code":"101668.0","system":"med"},{"code":"101805.0","system":"med"},{"code":"101907.0","system":"med"},{"code":"102158.0","system":"med"},{"code":"102715.0","system":"med"},{"code":"102949.0","system":"med"},{"code":"103900.0","system":"med"},{"code":"104128.0","system":"med"},{"code":"104139.0","system":"med"},{"code":"104913.0","system":"med"},{"code":"105072.0","system":"med"},{"code":"106131.0","system":"med"},{"code":"106194.0","system":"med"},{"code":"106569.0","system":"med"},{"code":"106654.0","system":"med"},{"code":"10698.0","system":"med"},{"code":"107878.0","system":"med"},{"code":"107916.0","system":"med"},{"code":"108054.0","system":"med"},{"code":"108389.0","system":"med"},{"code":"108667.0","system":"med"},{"code":"110192.0","system":"med"},{"code":"11991.0","system":"med"},{"code":"15036.0","system":"med"},{"code":"15182.0","system":"med"},{"code":"15644.0","system":"med"},{"code":"15684.0","system":"med"},{"code":"15907.0","system":"med"},{"code":"15991.0","system":"med"},{"code":"16105.0","system":"med"},{"code":"16298.0","system":"med"},{"code":"17841.0","system":"med"},{"code":"18231.0","system":"med"},{"code":"18613.0","system":"med"},{"code":"19321.0","system":"med"},{"code":"20160.0","system":"med"},{"code":"21330.0","system":"med"},{"code":"22290.0","system":"med"},{"code":"22441.0","system":"med"},{"code":"23389.0","system":"med"},{"code":"24048.0","system":"med"},{"code":"24235.0","system":"med"},{"code":"24456.0","system":"med"},{"code":"26165.0","system":"med"},{"code":"26652.0","system":"med"},{"code":"26813.0","system":"med"},{"code":"27483.0","system":"med"},{"code":"27617.0","system":"med"},{"code":"27715.0","system":"med"},{"code":"27853.0","system":"med"},{"code":"28003.0","system":"med"},{"code":"28069.0","system":"med"},{"code":"28148.0","system":"med"},{"code":"29160.0","system":"med"},{"code":"30165.0","system":"med"},{"code":"30542.0","system":"med"},{"code":"31324.0","system":"med"},{"code":"31393.0","system":"med"},{"code":"31573.0","system":"med"},{"code":"318.0","system":"med"},{"code":"319.0","system":"med"},{"code":"32174.0","system":"med"},{"code":"33871.0","system":"med"},{"code":"34742.0","system":"med"},{"code":"34926.0","system":"med"},{"code":"36736.0","system":"med"},{"code":"37328.0","system":"med"},{"code":"37805.0","system":"med"},{"code":"3845.0","system":"med"},{"code":"39388.0","system":"med"},{"code":"39413.0","system":"med"},{"code":"39531.0","system":"med"},{"code":"39590.0","system":"med"},{"code":"40014.0","system":"med"},{"code":"40437.0","system":"med"},{"code":"4218.0","system":"med"},{"code":"42856.0","system":"med"},{"code":"43111.0","system":"med"},{"code":"43390.0","system":"med"},{"code":"43392.0","system":"med"},{"code":"43475.0","system":"med"},{"code":"43479.0","system":"med"},{"code":"43761.0","system":"med"},{"code":"44108.0","system":"med"},{"code":"44267.0","system":"med"},{"code":"44805.0","system":"med"},{"code":"45071.0","system":"med"},{"code":"4554.0","system":"med"},{"code":"45667.0","system":"med"},{"code":"45922.0","system":"med"},{"code":"46613.0","system":"med"},{"code":"47204.0","system":"med"},{"code":"47668.0","system":"med"},{"code":"47767.0","system":"med"},{"code":"47862.0","system":"med"},{"code":"47899.0","system":"med"},{"code":"48517.0","system":"med"},{"code":"4870.0","system":"med"},{"code":"48743.0","system":"med"},{"code":"49463.0","system":"med"},{"code":"49525.0","system":"med"},{"code":"50222.0","system":"med"},{"code":"50289.0","system":"med"},{"code":"50290.0","system":"med"},{"code":"50292.0","system":"med"},{"code":"50579.0","system":"med"},{"code":"50681.0","system":"med"},{"code":"50777.0","system":"med"},{"code":"50898.0","system":"med"},{"code":"51718.0","system":"med"},{"code":"51878.0","system":"med"},{"code":"51965.0","system":"med"},{"code":"52570.0","system":"med"},{"code":"53910.0","system":"med"},{"code":"53989.0","system":"med"},{"code":"54083.0","system":"med"},{"code":"54103.0","system":"med"},{"code":"54186.0","system":"med"},{"code":"54222.0","system":"med"},{"code":"54411.0","system":"med"},{"code":"54613.0","system":"med"},{"code":"54636.0","system":"med"},{"code":"54956.0","system":"med"},{"code":"54965.0","system":"med"},{"code":"55246.0","system":"med"},{"code":"55374.0","system":"med"},{"code":"56718.0","system":"med"},{"code":"57471.0","system":"med"},{"code":"57482.0","system":"med"},{"code":"57544.0","system":"med"},{"code":"58061.0","system":"med"},{"code":"58836.0","system":"med"},{"code":"58871.0","system":"med"},{"code":"59041.0","system":"med"},{"code":"59152.0","system":"med"},{"code":"59362.0","system":"med"},{"code":"59381.0","system":"med"},{"code":"59382.0","system":"med"},{"code":"59388.0","system":"med"},{"code":"60035.0","system":"med"},{"code":"60247.0","system":"med"},{"code":"60312.0","system":"med"},{"code":"60772.0","system":"med"},{"code":"60775.0","system":"med"},{"code":"61064.0","system":"med"},{"code":"61390.0","system":"med"},{"code":"61555.0","system":"med"},{"code":"61716.0","system":"med"},{"code":"62182.0","system":"med"},{"code":"62348.0","system":"med"},{"code":"62556.0","system":"med"},{"code":"62761.0","system":"med"},{"code":"63104.0","system":"med"},{"code":"63331.0","system":"med"},{"code":"63430.0","system":"med"},{"code":"63460.0","system":"med"},{"code":"63568.0","system":"med"},{"code":"63657.0","system":"med"},{"code":"63695.0","system":"med"},{"code":"63988.0","system":"med"},{"code":"63995.0","system":"med"},{"code":"64106.0","system":"med"},{"code":"64345.0","system":"med"},{"code":"64516.0","system":"med"},{"code":"64817.0","system":"med"},{"code":"65159.0","system":"med"},{"code":"65215.0","system":"med"},{"code":"65233.0","system":"med"},{"code":"65357.0","system":"med"},{"code":"65460.0","system":"med"},{"code":"65466.0","system":"med"},{"code":"65605.0","system":"med"},{"code":"65642.0","system":"med"},{"code":"66088.0","system":"med"},{"code":"66166.0","system":"med"},{"code":"66488.0","system":"med"},{"code":"66750.0","system":"med"},{"code":"67107.0","system":"med"},{"code":"67324.0","system":"med"},{"code":"6806.0","system":"med"},{"code":"68161.0","system":"med"},{"code":"69497.0","system":"med"},{"code":"69821.0","system":"med"},{"code":"70463.0","system":"med"},{"code":"70824.0","system":"med"},{"code":"71204.0","system":"med"},{"code":"71584.0","system":"med"},{"code":"71946.0","system":"med"},{"code":"72127.0","system":"med"},{"code":"72174.0","system":"med"},{"code":"72224.0","system":"med"},{"code":"72522.0","system":"med"},{"code":"73537.0","system":"med"},{"code":"73718.0","system":"med"},{"code":"73988.0","system":"med"},{"code":"73992.0","system":"med"},{"code":"86046.0","system":"med"},{"code":"86996.0","system":"med"},{"code":"89258.0","system":"med"},{"code":"89657.0","system":"med"},{"code":"90290.0","system":"med"},{"code":"90546.0","system":"med"},{"code":"91457.0","system":"med"},{"code":"91586.0","system":"med"},{"code":"91896.0","system":"med"},{"code":"9237.0","system":"med"},{"code":"92720.0","system":"med"},{"code":"93665.0","system":"med"},{"code":"93762.0","system":"med"},{"code":"93778.0","system":"med"},{"code":"94220.0","system":"med"},{"code":"94272.0","system":"med"},{"code":"94415.0","system":"med"},{"code":"94975.0","system":"med"},{"code":"95630.0","system":"med"},{"code":"95644.0","system":"med"},{"code":"95671.0","system":"med"},{"code":"96971.0","system":"med"},{"code":"97332.0","system":"med"},{"code":"98104.0","system":"med"},{"code":"98322.0","system":"med"},{"code":"98361.0","system":"med"},{"code":"98408.0","system":"med"},{"code":"98537.0","system":"med"},{"code":"98813.0","system":"med"},{"code":"98911.0","system":"med"},{"code":"99572.0","system":"med"},{"code":"99896.0","system":"med"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('primary-malignancy_other-organs-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["other---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["other---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["other---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
