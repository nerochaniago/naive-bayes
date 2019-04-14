import csv
with open('TrainsetTugas1ML.csv','r') as csv_file :
    csv_reader = csv.reader(csv_file)
    hitung_line = 0
    age = []
    for row in csv_reader:
        if hitung_line == 0:
            hitung_line = hitung_line + 1
        else:
            age.append(row)

with open('TestsetTugas1ML.csv','r') as csv_file :
    csv_reader = csv.reader(csv_file)
    hitung_line = 0
    profesi = []
    for row in csv_reader:
        if hitung_line == 0:
             hitung_line = hitung_line + 1
        else:
             profesi.append(row)


hasil = []



def Kondisi(age,profesi):
    husband = 0
    hus = 0
    many = 0
    man = 0
    normal = 0
    nor = 0
    low = 0
    low_2 = 0
    no = 0
    ns = 0
    own = 0
    owc = 0
    prof = 0
    ps = 0
    ex = 0
    ev = 0
    craft = 0
    cr = 0
    never = 0
    nv = 0
    divo = 0
    divv = 0
    married = 0
    mrd = 0
    hs = 0
    grad = 0
    bc = 0
    bcs = 0
    some = 0
    col = 0
    local = 0
    gov = 0
    self = 0
    emp = 0
    private = 0
    private_2 = 0
    ya = 0
    yaa = 0
    ncc = 0
    sinff = 0
    a = 0
    adult = 0
    old = 0
    o = 0
    for i in range(0, len(age)):
            if age[i][8] == '>50K':
                ya = ya + 1
            elif age[i][8] == '<=50K':
                yaa = yaa + 1
    for i in range(0, len(age)):
            if age[i][1] == 'young':
                if age[i][8] == '>50K':
                    ncc = ncc + 1
                elif age[i][8] == '<=50K':
                    sinff = sinff + 1
            elif age[i][1] == 'adult':
                if age[i][8] == '>50K':
                    a = a + 1
                elif age[i][8] == '<=50K':
                    adult = adult + 1
            elif age[i][1] == 'old':
                if age[i][8] == '>50K':
                    old = old + 1
                elif age[i][8] == '<=50K':
                    o = o + 1
    prob = (ncc / ya)
    prob_0 = (sinff / yaa)
    prob_1 = (a / ya)
    prob_2 = (adult / yaa)
    prob_3 = (old / ya)
    prob_4 = (o / yaa)
    for i in range(0, len(age)):
        if age[i][2] == 'Private':
            if age[i][8] == '>50K':
                private = private + 1
            elif age[i][8] == '<=50K':
                private_2 = private_2 + 1
        elif age[i][2] == 'Local-gov':
            if age[i][8] == '>50K':
                local = local + 1
            elif age[i][8] == '<=50K':
                gov = gov + 1
        elif age[i][2] == 'Self-emp-not-inc':
            if age[i][8] == '>50K':
                self = self + 1
            elif age[i][8] == '<=50K':
                emp = emp + 1
    prob_5 = (private / ya)
    prob_6 = (private_2 / yaa)
    prob_7 = (local / ya)
    prob_8 = (gov / yaa)
    prob_9 = (self / ya)
    prob_10 =(emp / yaa)
    for i in range(0, len(age)):
        if age[i][3] == 'Some-college':
            if age[i][8] == '>50K':
                some = some + 1
            elif age[i][8] == '<=50K':
                col = col + 1
        elif age[i][3] == 'Bachelors':
            if age[i][8] == '>50K':
                bc = bc + 1
            elif age[i][8] == '<=50K':
                bcs = bcs + 1
        elif age[i][3] == 'HS-grad':
            if age[i][8] == '>50K':
                hs = hs + 1
            elif age[i][8] == '<=50K':
                grad = grad + 1
    prob_11 = (some / ya)
    prob_12 = (col / yaa)
    prob_13 = (bc / ya)
    prob_14 = (bcs / yaa)
    prob_15 = (hs / ya)
    prob_16 = (grad / yaa)
    for i in range(0, len(age)):
        if age[i][4] == 'Married':
            if age[i][8] == '>50K':
                married = married + 1
            elif age[i][8] == '<=50K':
                mrd = mrd + 1
        elif age[i][4] == 'Divorced':
            if age[i][8] == '>50K':
                divo = divo + 1
            elif age[i][8] == '<=50K':
                divv = divv + 1
        elif age[i][4] == 'Never-married':
            if age[i][8] == '>50K':
                never = never + 1
            elif age[i][8] == '<=50K':
                nv = nv + 1
    prob_17 = (married / ya)
    prob_18 = (mrd / yaa)
    prob_19 = (divo / ya)
    prob_20 = (divv / yaa)
    prob_21 = (never / ya)
    prob_22 = (nv / yaa)
    for i in range(0, len(age)):
        if age[i][5] == 'Craft-repair':
            if age[i][8] == '>50K':
                craft = craft + 1
            elif age[i][8] == '<=50K':
                cr = cr + 1
        elif age[i][5] == 'Exec_managerial':
            if age[i][8] == '>50K':
                ex = ex + 1
            elif age[i][8] == '<=50K':
                ev = ev + 1
        elif age[i][5] == 'Prof-speciality':
            if age[i][8] == '>50K':
                prof = prof + 1
            elif age[i][8] == '<=50K':
                ps = ps + 1
    prob_23 = (craft / ya)
    prob_24 = (cr / yaa)
    prob_25 = (ex / ya)
    prob_26 = (ev / yaa)
    prob_27 = (prof / ya)
    prob_28 = (ps / yaa)
    for i in range(0, len(age)):
        if age[i][6] == 'Own-child':
            if age[i][8] == '>50K':
                own = own + 1
            elif age[i][8] == '<=50K':
                owc = owc + 1
        elif age[i][6] == 'Not-in-family':
            if age[i][8] == '>50K':
                no = no + 1
            elif age[i][8] == '<=50K':
                ns = ns + 1
        elif age[i][6] == 'Husband':
            if age[i][8] == '>50K':
                hus = hus + 1
            elif age[i][8] == '<=50K':
                husband = husband + 1
    prob_29 = (own / ya)
    prob_30 = (owc / yaa)
    prob_31 = (no / ya)
    prob_32 = (ns / yaa)
    prob_33 = (hus / ya)
    prob_34 = (husband / yaa)
    for i in range(0, len(age)):
        if age[i][7] == 'low':
            if age[i][8] == '>50K':
                low = low + 1
            elif age[i][8] == '<=50K':
                low_2 = low_2 + 1
        elif age[i][7] == 'normal':
            if age[i][8] == '>50K':
                normal = normal + 1
            elif age[i][8] == '<=50K':
                nor = nor + 1
        elif age[i][7] == 'many':
            if age[i][8] == '>50K':
                many = many + 1
            elif age[i][8] == '<=50K':
                man = man + 1
    prob_35 = (low / ya)
    prob_36 = (low_2 / yaa)
    prob_37 = (normal / ya)
    prob_38 = (nor / yaa)
    prob_39 = (many / ya)
    prob_40 = (man / yaa)
    for i in range(0, len(profesi)):
        if profesi[i][1] == 'young':
            nc = (prob * 1)
            sinf = (prob_0 * 1)
        elif profesi[i][1] == 'adult':
            nc = (prob_1 * 1)
            sinf = (prob_2 * 1)
        elif profesi[i][1] == 'old':
            nc = (prob_3 * 1)
            sinf = (prob_4 * 1)
        if profesi[i][2] == 'Private':
            nc = (prob_5 * nc)
            sinf = (prob_6 * sinf)
        elif profesi[i][2] == 'Local-gov':
            nc = (prob_7 * nc)
            sinf = (prob_8 * sinf)
        elif profesi[i][2] == 'Self-emp-not-inc':
            nc = (prob_9 * nc)
            sinf = (prob_10 * sinf)
        if profesi[i][3] == 'Some-college':
            nc = (prob_11 * nc)
            sinf = (prob_12 * sinf)
        elif profesi[i][3] == 'Bachelors':
            nc = (prob_13 * nc)
            sinf = (prob_14 * sinf)
        elif profesi[i][3] == 'HS-grad':
            nc = (prob_15 * nc)
            sinf = (prob_16 * sinf)
        if profesi[i][4] == 'Married':
            nc = (prob_17 * nc)
            sinf = (prob_18 * sinf)
        elif profesi[i][4] == 'Divorced':
            nc = (prob_19 * nc)
            sinf = (prob_20 * sinf)
        elif profesi[i][4] == 'Never-married':
            nc = (prob_21 * nc)
            sinf = (prob_22 * sinf)
        if profesi[i][5] == 'Craft-repair':
            nc = (prob_23 * nc)
            sinf = (prob_24 * sinf)
        elif profesi[i][5] == 'Exec-managerial':
            nc = (prob_25 * nc)
            sinf = (prob_26 * sinf)
        elif profesi[i][5] == 'Prof-speciality':
            nc = (prob_27 * nc)
            sinf = (prob_28 * sinf)
        if profesi[i][6] == 'Own-child':
            nc = (prob_29 * nc)
            sinf = (prob_30 * sinf)
        elif profesi[i][6] == 'Not-in-family':
            nc = (prob_31 * nc)
            sinf = (prob_32 * sinf)
        elif profesi[i][6] == 'Husband':
            nc = (prob_33 * nc)
            sinf = (prob_34 * sinf)
        if profesi[i][7] == 'low':
            nc = (prob_35 * nc)
            sinf = (prob_36 * sinf)
        elif profesi[i][7] == 'normal':
            nc = (prob_37 * nc)
            sinf = (prob_38 * sinf)
        elif profesi[i][7] == 'many':
            nc = (prob_39 * nc)
            sinf = (prob_40 * sinf)

        if (nc > sinf):
            hasil.append('>50K')
        else:
            hasil.append('<=50K')

def Main():
    Kondisi(age,profesi)
    print(hasil)
    print('hasilnya bisa dilihat pada output file csv oleh program ini')

    with open('TebakanTugas1ML.csv', 'w', newline='') as write:
        writeup = csv.writer(write)
        for i in range(0, len(profesi)):
            writeup.writerow({hasil[i]})

if __name__ == '__main__':
    Main()