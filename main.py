##Python Portfolio Project
import csv

#Lists for individual columns
ages = []
sex = []
bmis = []
children = []
smoker = []
regions = []
charges = []

with open('insurance.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        ages.append(row["age"])
        sex.append(row["sex"])
        bmis.append(row["bmi"])
        children.append(row["children"])
        smoker.append(row["smoker"])
        regions.append(row["region"])
        charges.append(row["charges"])

#Master List
main_list = [ages, sex, bmis, children, smoker, regions, charges]

## Verify if all the lists are of same length
""" print("Sex:", len(sex))
print("Bmi:", len(bmis))
print("children:", len(children))
print("smoker:", len(smoker))
print("region:", len(regions))
print("charges:", len(charges)) """


#Insurance Cost calculator
#insurance_cost=250∗age−128∗sex+370∗bmi+425∗num_of_children+24000∗smoker−12500
def calc_insurance_cost(age, sex, bmi, children, smoker):
    insurance_cost = int(250*age) - int(128*sex) + (370*float(bmi)) + (425*children) \
        + (24000*smoker) - 12500
    return insurance_cost

## Avg Insurance Cost
total_cost = 0.0
for charge in charges:
    total_cost += float(charge)
total_avg_cost = total_cost/len(charges)
print(f"The average insurance cost of the dataset is ${round(total_avg_cost,2)}")

## Average BMI
total_bmi = 0.0
for bmi_ind in bmis:
    total_bmi += float(bmi_ind)
total_avg_bmi = total_bmi/len(bmis)
print(f"The average BMI of the dataset is {round(total_avg_bmi,2)}")

## Average Age
total_age = 0.0
for age_ind in ages:
    total_age += float(age_ind)
total_avg_age = total_age/len(ages)
print(f"The average Age of the dataset is {round(total_avg_age,2)} years old")

##Relation between smoker and non-smoker w.r.t to Insurance Cost for one person
element = smoker.index('yes')
new_insurance_cost = calc_insurance_cost(int(ages[element]), sex[element]=='Male',\
                                          bmis[element], int(children[element]), 0)
#print(f"The change in insurance cost if you do not smoke, for one person is \
# ${round(new_insurance_cost - float(charges[element]),2)}")

## Relation between smoker and non-smoker for all smokers involved
element = 'yes'
new_insurance_cost_list = []
change_in_dollars = []
change_perc = []
avg_change_in_dollars = 0
avg_change_in_perc = 0
j= 0
indices_smoker = [i for i, val in enumerate(smoker) if val == element]
for index in indices_smoker:
    new_insurance_cost_list.append(calc_insurance_cost(int(ages[index]), \
                                                       sex[index]=='Male',bmis[index],\
                                                       int(children[index]), 0))
    change_in_dollars.append(float(charges[index]) - new_insurance_cost_list[j])
    change_perc.append((change_in_dollars[j]/float(charges[index]))*100)
    j += 1
avg_change_in_dollars = sum(change_in_dollars)/len(change_in_dollars)
avg_change_in_perc = sum(change_perc)/len(change_perc)
print(f"Average change in cost if people stopped smoking is ${round(avg_change_in_dollars,2)}")
print(f"Average change in cost % if stopped smoking is {round(avg_change_in_perc, 2)}%")



## Relation between Region and Insurance Cost
region_insurance_cost = {}
def calc_insurance_total_region(region_chk):
    insurance_total_region = 0
    indices_region = [i for i, val in enumerate(regions) if val == region_chk]
    for index in indices_region:
            insurance_total_region += float(charges[index])
    print(f"The number of perople from {region_chk} are {len(indices_region)}")
    return insurance_total_region/len(indices_region)

for region in list(set(regions)):
    region_insurance_cost[region] = calc_insurance_total_region(region)

for key, value in region_insurance_cost.items():
    if value == max(region_insurance_cost.values()):
        print(f"The maximum average insurance cost is seen in {key} region \
with a value of ${round(value,2)}")

#Average cost of insurance based on no_of_children
children_avg_insurance_cost = {}
def avg_cost_insurance_children(no_of_children):
    total_insurance_cost_children = 0
    indices_children = [i for i, val in enumerate(children) if val == no_of_children]
    for index in indices_children:
        total_insurance_cost_children += float(charges[index])
    return total_insurance_cost_children/len(indices_children)
list1 = list(set(children))
list1.sort()
for num in list1:
    children_avg_insurance_cost[num] = avg_cost_insurance_children(num)
    print(f"The average insurance cost with {num} children is {round(children_avg_insurance_cost[num],2)}")

#Average cost of insurance based on BMI
bmi_avg_insurance_cost = {}
def avg_cost_insurance_bmi(bmi_ind):
    total_insurance_cost_bmi = 0
    indices_bmi = [i for i, val in enumerate(bmis) if val == bmi_ind]
    for index in indices_bmi:
        total_insurance_cost_bmi += float(charges[index])
    return total_insurance_cost_bmi/len(indices_bmi)
list1 = list(set(bmis))
list1.sort()
for num in list1:
    bmi_avg_insurance_cost[num] = avg_cost_insurance_bmi(num)

for key, value in bmi_avg_insurance_cost.items():
    if value == max(bmi_avg_insurance_cost.values()):
        print(f"The maximum average insurance cost is seen in {key} BMI \
with a value of ${round(value,2)}")
        

##Average cost of insurance based on Age
age_avg_insurance_cost = {}
def avg_cost_insurance_age(age_ind):
    total_insurance_cost_age = 0
    indices_age = [i for i, val in enumerate(ages) if val == age_ind]
    for index in indices_age:
        total_insurance_cost_age += float(charges[index])
    return total_insurance_cost_age/len(indices_age)
list1 = list(set(ages))
list1.sort()
for num in list1:
    age_avg_insurance_cost[num] = avg_cost_insurance_age(num)

for key, value in age_avg_insurance_cost.items():
    if value == max(age_avg_insurance_cost.values()):
        print(f"The maximum average insurance cost is seen in {key} years old \
with a value of ${round(value,2)}")
        
##Average cost of insurance based on Sex
sex_avg_insurance_cost = {}
def avg_cost_insurance_sex(sex_ind):
    total_insurance_cost_sex = 0
    indices_sex = [i for i, val in enumerate(sex) if val == sex_ind]
    for index in indices_sex:
        total_insurance_cost_sex += float(charges[index])
    return total_insurance_cost_sex/len(indices_sex)
list1 = list(set(sex))
list1.sort()
for num in list1:
    sex_avg_insurance_cost[num] = avg_cost_insurance_sex(num)

for key, value in sex_avg_insurance_cost.items():
    if value == max(sex_avg_insurance_cost.values()):
        print(f"The maximum average insurance cost is seen in {key} type \
with a value of ${round(value,2)}")