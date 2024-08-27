# import libraries 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


#Reading Data
try:
    HeartDiseaseData = pd.read_csv('heart_2020_cleaned.csv')
    print(f'Data shape is: {HeartDiseaseData.shape}')
except BaseException as err:
    print("Error message is:", err)
    
# Information from The Data    

print('head of data:\n{0}\ndtypes:\n{1}\ninfo:{2}\nsum of nulls:\n{3}'
          .format(HeartDiseaseData.head(), HeartDiseaseData.dtypes,
                  HeartDiseaseData.info(), HeartDiseaseData.isnull().sum()))




# Create DataFrame and drop rows with at least one Nan value
    # used dropna to delete rows that contains nulls
HeartDiseaseDataf = pd.DataFrame(HeartDiseaseData).dropna()
# check again the size of data:
print('new DataFrame shape is: {}'.format(HeartDiseaseDataf.shape))  

for column in HeartDiseaseDataf:
    # get the unique values for every column
    uniq_val = np.unique(HeartDiseaseDataf[column])
    # count the unique values for every column
    np_val = len(uniq_val)
    if np_val < 15:
        print('The number of values for feature {} : {} -- :{}'.format(column, np_val, uniq_val))
    else:
        print('The number of values for feature {} : {}'.format(column, np_val))
        
        
        

# NADP is: NumberOfAlcoholHeartDiseasePersons
# NADP_not is: NumberOfNotAlcoholHeartDiseasePersons
def AlcoholDrinking():

  NADP = 0
  NADP_not = 0
  for Disease, Alcohol in zip(HeartDiseaseDataf['HeartDisease'], HeartDiseaseDataf['AlcoholDrinking']):
      #     print(Disease, Alcohol)/
      if Disease == Alcohol == 'Yes':
          NADP += 1
      elif Disease == Alcohol == 'No':
          NADP_not += 1
  NADPPeracentage = round(NADP/HeartDiseaseData.shape[0], 6)*100
  print("Alcohol Drinkers percentage that have Heart Disease to the data: {} %".format(NADPPeracentage))

  print('Number of Alcohol Drinkers that has Heart Disease', NADP)

  print("Number of Alcohol Drinkers that hasn't Heart Disease", NADP_not)
AlcoholDrinking()



# smoking is: NumberOfsmokingHeartDiseasePersons
# not_smoking is: NumberOfnotsmokingHeartDiseasePersons
smoking = 0
not_smoking = 0
for Disease, smoke in zip(HeartDiseaseDataf['HeartDisease'], HeartDiseaseDataf['Smoking']):
    if Disease == smoke == 'Yes':
        smoking += 1
    elif Disease == smoke == 'No':
        not_smoking += 1

print('Number of smoking Drinkers that has Heart Disease', smoking)
print('Number of Alcohol Drinkers that has Heart Disease', not_smoking)



def smoking():
    # smoking is: NumberOfsmokingHeartDiseasePersons
    # not_smoking is: NumberOfnotsmokingHeartDiseasePersons
    smoking = 0
    not_smoking = 0
    for Disease, smoke in zip(HeartDiseaseDataf['HeartDisease'], HeartDiseaseDataf['Smoking']):
        #print(Disease, Alcohol)/
        if Disease == smoke == 'Yes':
            smoking += 1
        elif Disease == smoke == 'No':
            not_smoking += 1

    print('Number of smoking Drinkers that has Heart Disease', smoking)
    print('Number of Alcohol Drinkers that has Heart Disease', not_smoking)

smoking()




male = 0
female = 0
for gender in HeartDiseaseDataf['Sex']:
    if gender == 'Male':
        male += 1
    elif gender == 'Female':
        female += 1

print('Number of male in the DataSet', male)
print('Number of female in the DataSet', female)


def gender():
    male = 0
    female = 0
    for Disease, gender in zip(HeartDiseaseDataf['HeartDisease'], HeartDiseaseDataf['Sex']):
        if Disease == 'Yes' and gender == 'Male':
            male += 1
        elif Disease == 'No' and gender == 'Female':
            female += 1

    print('Number of male that has Heart Disease', male)
    print('__________________________________')

    print('Number of female that has Heart Disease', female)
    print('__________________________________')

gender()



     
# check the count of heart desease for every AgeCategory:
ageGroupsCount = {}

for Disease, age in zip(HeartDiseaseDataf['HeartDisease'], HeartDiseaseDataf['AgeCategory']):
    if Disease == 'Yes':
        ageGroupsCount[age] = ageGroupsCount.get(age, 0) + 1

print('count of heart desease for every AgeCategory:', sorted(ageGroupsCount.items()))




#list comprehensive examples
list = [i for i in HeartDiseaseDataf['PhysicalHealth'] if i % 2 == 0]
print(list)
print(len(list))

list = [i for i in HeartDiseaseDataf['PhysicalHealth'] if i % 2 != 0]
print(list)
print (len(list))

list = [i for i in HeartDiseaseDataf['SleepTime'] if i >= 10]
print(list)
print (len(list))




class HeartDisease: 
  def __init__(self):#initial value for all number of Kidney Disease people and skin cancer people as (count =0)
    self.Kidney_Disease = 0
    self.not_Kidney_Disease = 0
    self.skin_cancer = 0
    self.not_skin_cancer = 0
  
  def KidneyDisease(self):#function to calc number of people have heard disease and kidney disease or  Unsatisfactory people
        for HeartDisease, KidneyDisease in zip(HeartDiseaseDataf['HeartDisease'], HeartDiseaseDataf['KidneyDisease']):
            if HeartDisease == KidneyDisease == 'Yes':#if person have heart disease and kidney disease increment the count of Kidney_Disease
                self.Kidney_Disease += 1
            elif HeartDisease == KidneyDisease == 'No':#if Unsatisfactory people increment the count of not_Kidney_Disease
                self.not_Kidney_Disease += 1
        print('Number of people have HeartDisease and KidneyDisease : ', self.Kidney_Disease)  
        print('Number of people have not HeartDisease and KidneyDisease : ', self.not_Kidney_Disease) 

  def SkinCancer(self):#function to calc number of people have heard disease and Skin cancer or  Unsatisfactory people
        for HeartDisease, SkinCancer in zip(HeartDiseaseDataf['HeartDisease'], HeartDiseaseDataf['SkinCancer']):
            if HeartDisease == SkinCancer == 'Yes':#if person have heart disease and SkinCancer increment the count of skin_cancer
                self.skin_cancer += 1
            elif HeartDisease == SkinCancer == 'No':#if Unsatisfactory people increment the count of not_skin_cancer
                self.not_skin_cancer += 1

        print('Number of people have HeartDisease and Skin Cancer : ', self.skin_cancer)  
        print('Number of people have not  HeartDisease and Skin Cancer : ', self.not_skin_cancer)     
      
heart=HeartDisease()  



heart.KidneyDisease()



heart.SkinCancer()



#list to count number of people have Asthma
L1 = []
L2 = []
for i in HeartDiseaseDataf['Asthma']:
        if i == 'Yes':
            L1.append(i)
        elif i == 'No':
            L2.append(i)
print("Number of people have Asthma = ",len(L1))
print("Number of people not have Asthma =", len(L2))





# plots

def drawPlots():
    plt.style.use('Solarize_Light2')
    plt.figure(figsize=(12, 10))
    plt.title('Heart disease patients vs. non-heart disease patients in dataset')
    sns.countplot(x='HeartDisease', data=HeartDiseaseDataf)
    plt.show()

    plt.figure(figsize=(12, 10))
    plt.title('Smoking persons vs. non-Smoking persons dataset')
    sns.countplot(x='Smoking', data=HeartDiseaseDataf)
    plt.show()

    plt.figure(figsize=(12, 10))
    plt.title('Alcohol Drinking persons vs. non-AlcoholDrinking persons dataset')
    sns.countplot(x='AlcoholDrinking', data=HeartDiseaseDataf)
    plt.show()

    plt.figure(figsize=(12, 10))
    plt.title('Male vs. Female persons dataset')
    sns.countplot(x='Sex', data=HeartDiseaseDataf)
    plt.show()

    plt.figure(figsize=(12, 10))
    plt.title('Race color fo persons in dataset')
    sns.countplot(x='Race', data=HeartDiseaseDataf)
    plt.show()

    plt.figure(figsize=(12, 10))
    plt.title('General Health fo persons in dataset')
    sns.countplot(x='GenHealth', data=HeartDiseaseDataf)
    plt.show()

        
    plt.figure(figsize=(12, 10))
    plt.title('Infection of individuals in the sample with diabetes')
    sns.countplot(x='Diabetic', data=HeartDiseaseDataf)
    plt.show()
drawPlots()