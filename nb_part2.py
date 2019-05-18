import pandas as pd

dataset = pd.read_csv('TrainsetTugas1ML.csv')
datatest = pd.read_csv('TestsetTugas1ML.csv')

train = dataset.values.tolist()
testing = datatest.values.tolist()

i = 0
j = 0
besar = 0 #label total >50K
kurang = 0 #label total <=50K
young = 0
young_2 = 0
adult = 0
adult_2 = 0
old = 0
old_2 = 0
private = 0
private_2 = 0
local_gov = 0
local_gov_2 = 0
self = 0
self_2 = 0
some_college = 0
some_college_2 = 0
bachelors = 0
bachelors_2 = 0
hs_grad = 0
hs_grad_2 = 0
married_civ = 0
married_civ_2 = 0
never_married = 0
never_married_2 = 0
divorced = 0
divorced_2 = 0
craft_repair = 0
craft_repair_2 = 0
exec_managerial = 0
exec_managerial_2 = 0
prof_specialty = 0
prof_specialty_2 = 0
not_in_family = 0
not_in_family_2 = 0
husband = 0
husband_2 = 0
own_child = 0
own_child_2 = 0
normal = 0
normal_2 = 0
many= 0
many_2 = 0
low = 0
low_2 = 0
young_testing_lebih = 0
young_testing_kurang = 0
old_testing_lebih = 0
old_testing_kurang = 0
private_testing_lebih = 0
private_testing_kurang = 0
local_testing_lebih = 0
local_testing_kurang = 0
self_testing_lebih = 0
self_testing_kurang = 0
some_testing_lebih = 0
some_testing_kurang = 0
bachelors_testing_lebih = 0
bachelors_testing_kurang = 0
hs_grad_testing_lebih = 0
hs_grad_testing_kurang = 0
married_civ_lebih =0
married_civ_kurang = 0
never_married_lebih = 0
never_married_kurang =0
divorced_testing_lebih = 0
divorced_testing_kurang = 0
craft_repair_lebih = 0
craft_repair_kurang = 0
exec_managerial_lebih = 0
exec_managerial_kurang = 0
prof_specialty_lebih = 0
prof_specialty_kurang = 0
not_testing_lebih = 0
not_testing_kurang = 0
husband_testing_lebih = 0
husband_testing_kurang = 0
own_testing_lebih = 0
own_testing_kurang = 0
normal_testing_lebih = 0
normal_testing_kurang = 0
many_testing_lebih = 0
many_testing_kurang = 0
low_testing_lebih = 0
low_testing_kurang = 0



while i < len(train):
    # langkah 1 hitung total record pada class/ label
    if train[i][8] == '>50K':
        besar += 1
    elif train[i][8] == '<=50K':
        kurang += 1
    i += 1
    # langkah 2 dst hitung atribut dengan >50k || <=50k
for i in range(0,len(train)):
    for j in range(0,8):
            if train[i][j] == 'young':
                if train[i][8] == '>50K':
                    young += 1
                elif train[i][j] == '<=50K':
                    young_2 += 1
            elif train[i][j] == 'adult':
                if train[i][8] == '>50K':
                    adult += 1
                elif train[i][8] == '<=50K':
                    adult_2 += 1
            elif train[i][j] == 'old':
                if train[i][8] == '>50K':
                    old += 1
                elif train[i][8] == '<=50K':
                    old_2 += 1
            elif train[i][j] == 'Private':
                if train[i][8] == '>50K':
                    private += 1
                elif train[i][8] == '<=50K':
                    private_2 += 1
            elif train[i][j] == 'Local-gov':
                if train[i][8] == '>50K':
                    local_gov += 1
                elif train[i][8] == '<=50K':
                    local_gov_2 += 1
            elif train[i][j] == 'Self-emp-not-inc':
                if train[i][8] == '>50K':
                    self += 1
                elif train[i][8] == '<=50K':
                    self_2 += 1
            elif train[i][j] == 'Some-college':
                if train[i][8] == '>50K':
                    some_college += 1
                elif train[i][8] == '<=50K':
                    some_college_2 += 1
            elif train[i][j] == 'Bachelors':
                if train[i][8] == '>50K':
                    bachelors += 1
                elif train[i][8] == '<=50K':
                    bachelors_2 += 1
            elif train[i][j] == 'HS-grad':
                if train[i][8] == '>50K':
                    hs_grad += 1
                elif train[i][8] == '<=50K':
                    hs_grad_2 += 1
            elif train[i][j] == 'Married-civ-spouse':
                if train[i][8] == '>50K':
                    married_civ += 1
                elif train[i][8] == '<=50K':
                    married_civ_2 += 1
            elif train[i][j] == 'Never-married':
                if train[i][8] == '>50K':
                    never_married += 1
                elif train[i][8] == '<=50K':
                    never_married_2 += 1
            elif train[i][j] == 'Divorced':
                if train[i][8] == '>50K':
                    divorced += 1
                elif train[i][8] == '<=50K':
                    divorced_2 += 1
            elif train[i][j] == 'Craft-repair':
                if train[i][8] == '>50K':
                    craft_repair += 1
                elif train[i][8] == '<=50K':
                    craft_repair_2 += 1
            elif train[i][j] == 'Exec-managerial':
                if train[i][8] == '>50K':
                    exec_managerial += 1
                elif train[i][8] == '<=50K':
                    exec_managerial_2 += 1
            elif train[i][j] == 'Prof-specialty':
                if train[i][8] == '>50K':
                    prof_specialty += 1
                elif train[i][8] == '<=50K':
                    prof_specialty_2 += 1
            elif train[i][j] == 'Not-in-family':
                if train[i][8] == '>50K':
                    not_in_family += 1
                elif train[i][8] == '<=50K':
                    not_in_family_2 += 1
            elif train[i][j] == 'Husband':
                if train[i][8] == '>50K':
                    husband += 1
                elif train[i][8] == '<=50K':
                    husband_2 += 1
            elif train[i][j] == 'Own-child':
                if train[i][8] == '>50K':
                    own_child += 1
                elif train[i][8] == '<=50K':
                    own_child_2 += 1
            elif train[i][j] == 'normal':
                if train[i][8] == '>50K':
                    normal += 1
                elif train[i][8] == '<=50K':
                    normal_2 += 1
            elif train[i][j] == 'many':
                if train[i][8] == '>50K':
                    many += 1
                elif train[i][8] == '<=50K':
                    many_2 += 1
            elif train[i][j] == 'low':
                if train[i][8] == '>50K':
                    low += 1
                elif train[i][8] == '<=50K':
                    low_2 += 1


prob_lebih = besar / (besar + kurang)
prob_kurang = kurang / (besar + kurang)

for i in range(0,len(testing)):
    for j in range(0,8):
        if testing[i][j] == 'young':
            young_testing_lebih = young / besar
            young_testing_kurang = young_2 / kurang
        elif testing[i][j] == 'adult':
            young_testing_lebih = adult / besar
            young_testing_kurang = adult_2 / kurang
        elif testing[i][j] == 'old':
            young_testing_lebih = old / besar
            young_testing_kurang = old_2 / kurang
        elif testing[i][j] == 'Private':
            private_testing_lebih = private / besar
            private_testing_kurang = private_2 / kurang
        elif testing[i][j] == 'Local-gov':
            private_testing_lebih = local_gov / besar
            private_testing_kurang = local_gov_2 / kurang
        elif testing[i][j] == 'Self-emp-not-inc':
            private_testing_lebih = self / besar
            private_testing_kurang = self_2 / kurang
        elif testing[i][j] == 'Some-college':
            some_testing_lebih = some_college / besar
            some_testing_kurang = some_college_2 / kurang
        elif testing[i][j] == 'Bachelors':
            some_testing_lebih = bachelors / besar
            some_testing_kurang = bachelors_2 / kurang
        elif testing[i][j] == 'HS-grad':
            some_testing_lebih = hs_grad / besar
            some_testing_kurang = hs_grad_2 / kurang
        elif testing[i][j] == 'Married-civ-spouse':
            married_civ_lebih = married_civ / besar
            married_civ_kurang = married_civ_2 / kurang
        elif testing[i][j] == 'Never-married':
            married_civ_lebih = never_married / besar
            married_civ_kurang = never_married_2 / kurang
        elif testing[i][j] == 'Divorced':
            married_civ_lebih = divorced / besar
            married_civ_kurang = divorced_2 / kurang
        elif testing[i][j] == 'Craft-repair':
            craft_repair_lebih = craft_repair / besar
            craft_repair_kurang = craft_repair_2 / kurang
        elif testing[i][j] == 'Exec-managerial':
            craft_repair_lebih = exec_managerial / besar
            craft_repair_kurang = exec_managerial_2 / kurang
        elif testing[i][j] == 'Prof-specialty':
            craft_repair_lebih = prof_specialty / besar
            craft_repair_kurang = prof_specialty_2 / kurang
        elif testing[i][j] == 'Not-in-family':
            craft_repair_lebih = not_in_family / besar
            craft_repair_kurang = not_in_family_2 / kurang
        elif testing[i][j] == 'Husband':
            husband_testing_lebih = husband / besar
            husband_testing_kurang = husband_2 / kurang
        elif testing[i][j] == 'Own-child':
            husband_testing_lebih = own_child / besar
            husband_testing_kurang = own_child_2 / kurang
        elif testing[i][j] == 'normal':
            normal_testing_lebih = normal / besar
            normal_testing_kurang = normal_2 / kurang
        elif testing[i][j] == 'many':
            normal_testing_lebih = many / besar
            normal_testing_kurang = many_2 / kurang
        elif testing[i][j] == 'low':
            normal_testing_lebih = low / besar
            normal_testing_kurang = low_2 / kurang

    pro = (prob_lebih * young_testing_lebih  * private_testing_lebih * some_testing_lebih  * married_civ_lebih  * craft_repair_lebih  * husband_testing_lebih * normal_testing_lebih)
    kurs = (prob_kurang * young_testing_kurang * private_testing_kurang * some_testing_kurang * married_civ_kurang * craft_repair_kurang * husband_testing_kurang * normal_testing_kurang)

    if pro > kurs:
        print('>50K')
    else:
        print('<=50K')