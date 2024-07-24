# -*- coding: utf-8 -*-
"""Pandas_task.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/10SJW4c3qUmT9-CxH4h1ft3nE1LkCVO5t
"""

# Task 0.
import pandas as pd
data = pd.read_csv("/content/adult.data.csv")
data.head()

# Task 1. Посчитайте, сколько мужчин и женщин (признак sex) представлено в этом датасете.

data.value_counts(subset = "sex")

# Task 2. Каков средний возраст мужчин (признак age) по всему датасету?

y = data[['age','sex']].query('sex == "Male"')
mean = y[['age']].mean()
print(mean)

# Task 3. Какова доля граждан Соединенных Штатов (признак native-country)?

filtered_data = data[data['native-country'] == 'United-States']
total_people = len(data)  # Total number of people in the original DataFrame
us_people = len(filtered_data)  # Number of people from the United States
us_percentage = int((us_people / total_people) * 100)
print(us_percentage,"%")

# Task 4-5. Рассчитайте среднее значение и
# среднеквадратичное отклонение возраста тех,
# кто получает более 50K в год (признак salary)
# и тех, кто получает менее 50K в год

age_salary = data[["age", "salary"]]

more_than_50 = age_salary.query('salary == ">50K"')
print("The average age of people making more than 50K is:", more_than_50["age"].mean())
print()
print("The standard deviation of their age is:", more_than_50["age"].std())
print()
less_than_50 = age_salary.query('salary == "<=50K"')
print("The average age of people making less than 50K is:",less_than_50["age"].mean())
print()
print("The standard deviation of their age is:",less_than_50["age"].std())

# Task 6. Правда ли, что люди, которые получают больше 50k,
# имеют минимум высшее образование? (признак education –
# Bachelors, Prof-school, Assoc-acdm, Assoc-voc, Masters или Doctorate)

education_salary = data[["education", "salary"]]

more_than_50_2 = education_salary.query('salary == ">50K"')
more_than_50_2.value_counts(normalize=True)*100

# Everything about Bachelors
have_bachelors = len(education_salary.query('education == "Bachelors"'))
Bachelors_and_more_than_50K = len(more_than_50_2.query('education == "Bachelors"'))
print("There are",have_bachelors, "people with Bachelors,", Bachelors_and_more_than_50K,\
      "people with Bachelors earn more than 50K, which is",int(100*(Bachelors_and_more_than_50K/\
                                                                    have_bachelors)),"%")

print()

# Everything about Prof-school
have_prof_school = len(education_salary.query('education == "Prof-school"'))
Profschool_and_more_than_50K = len(more_than_50_2.query('education == "Prof-school"'))
print("There are",have_prof_school, "people with Prof-school,", Profschool_and_more_than_50K,\
      "people with Prof-school earn more than 50K, which is",int(100*(Profschool_and_more_than_50K/\
                                                                      have_prof_school)),"%")

print()

# Everything about Assoc-acdm

have_assocacdm = len(education_salary.query('education == "Assoc-acdm"'))
Assocacdm_and_more_than_50K = len(more_than_50_2.query('education == "Assoc-acdm"'))
print("There are",have_assocacdm, "people with Assoc-acdm,", Assocacdm_and_more_than_50K,\
      "people with Assoc-acdm earn more than 50K, which is",int(100*(Assocacdm_and_more_than_50K/\
                                                                     have_assocacdm)),"%")

print()

# Everything about Assoc-voc

have_assocvoc = len(education_salary.query('education == "Assoc-voc"'))
Assocvoc_and_more_than_50K = len(more_than_50_2.query('education == "Assoc-voc"'))
print("There are",have_assocvoc, "people with Assoc-voc,", Assocvoc_and_more_than_50K,\
      "people with Assoc-voc earn more than 50K, which is",int(100*(Assocvoc_and_more_than_50K/\
                                                                    have_assocvoc)),"%")
print()

# Everything about Masters

have_masters = len(education_salary.query('education == "Masters"'))
Masters_and_more_than_50K = len(more_than_50_2.query('education == "Masters"'))
print("There are",have_masters, "people with Masters,", Masters_and_more_than_50K,\
      "people with Masters earn more than 50K, which is",int(100*(Masters_and_more_than_50K/\
                                                                  have_masters)),"%")

print()

# Everything about Doctorate

have_doctorate = len(education_salary.query('education == "Doctorate"'))
Doctorate_and_more_than_50K = len(more_than_50_2.query('education == "Doctorate"'))
print("There are",have_doctorate, "people with Doctorate,", Doctorate_and_more_than_50K,\
      "people with Doctorate earn more than 50K, which is",int(100*(Doctorate_and_more_than_50K/\
                                                                    have_doctorate)),"%")

print()

education_plus_50k = len(more_than_50_2.query('education == "Doctorate" or education\
 == "Masters" or education == "Assoc-voc" or education == "Assoc-acdm" or education ==\
  "Prof-school" or education == "Bachelors"'))

highly_educated = have_bachelors + have_prof_school + have_assocacdm + have_assocvoc + have_masters + have_doctorate

print("There are", len(data), "people in the data-set.",highly_educated,"people \
(",int(100*(highly_educated/len(data))),"%) have a higher education. And only",education_plus_50k,\
      "people (",int(100*(education_plus_50k/highly_educated)),"%) with higher education earn more than 50k.")

# Нет нужды включать в задание. Тут я просто проверяла.
education_salary = data[["education", "salary"]]
education_salary.value_counts("education", normalize=True)*100

# Task 7. Выведите статистику возраста для каждой расы
# (признак race) и каждого пола. Используйте groupby и describe.
# Найдите таким образом максимальный возраст мужчин расы Asian-Pac-Islander.

data["age"].describe()

# Группировка дата-сета с помощью метода groupby по признаку sex
gk = data.groupby('sex')

# Применение метода describe на сгруппированом дата-сете.
gk["age"].describe()

# Группировка дата-сета с помощью метода groupby по признаку race
gz = data.groupby('race')

# Применение метода describe на сгруппированом дата-сете.
gzg = gz[["age"]].describe()
gzg
print(f"The maximum age of the {gzg.iloc[1,7]}")

# ОСТОРОЖНО - ЗДЕСЬ УКАЗАНА РАЗБИВКА БЕЗ ПОЛА. ТО ЕСТЬ, И ЖЕНЩИНЫ, И МУЖЧИНЫ.

# Группировка дата-сета с помощью метода groupby по признаку race
gr = data.groupby('race')

# Применение метода describe на сгруппированом дата-сете.
gr[["age"]].describe()

# Группировка дата-сета с помощью метода groupby по признаку race
gz = data.query('sex == "Male"').groupby('race')

# Применение метода describe на сгруппированом дата-сете.
rc = gz[["age"]].describe()

rc

# А ВОТ ТУТ УЖЕ ЧИСТО ВЫПОЛНЕНО - ИМЕННО МУЖЧИНЫ РАЗБИТЫ ПО РАСАМ

print("The maximum age of a man of the Asian-Pac-Islander race is",int(rc.iloc[1,7]))

# Task 8. Среди кого больше доля зарабатывающих много (>50K):
# среди женатых или холостых мужчин (признак marital-status)?
# Женатыми считаем тех, у кого marital-status начинается с Married
# (Married-civ-spouse, Married-spouse-absent или Married-AF-spouse), остальных считаем холостыми.

# Переименовываем колонку для удобства

data = data.rename(columns={"marital-status": "marital_status"})

# Ограничиваем сет данных до семейного положения, дохода и пола

men = data[["marital_status", "salary","sex"]].query('sex == "Male"')
print("There are",len(marital_status),"men in this data-set.")

# Ограничиваем дата-сет до тех, кто зарабатывает больше 50K
more_than_50k = men.query('salary == ">50K"')
print("There are",len(more_than_50k),"men that earn more than 50k in this data-set.")

#Узнаём количество женатых мужчин
married_men = men.query('marital_status == "Married-civ-spouse" or marital_status =="Married-spouse-absent" or marital_status == "Married-AF-spouse"')

# Узнаём количество женатых мужчин, зарабатывающих больше 50K
married_men_more_than_50 = married_men.query('salary == ">50K"')


# Узнаём количество неженатых мужчин
not_married_men = men.query('marital_status=="Divorced" or \
marital_status=="Never-married" or marital_status=="Separated" or \
marital_status=="Widowed"')

# Узнаём количество неженатых мужчин, зарабатывающих больше 50K
not_married_men_more_than_50 = not_married_men.query('salary == ">50K"')

print("Количество женатых мужчин:",len(married_men))
print("Количество неженатых мужчин:",len(not_married_men))
print()

print("Количество женатых мужчин, зарабатывающих больше 50K:",len(married_men_more_than_50))
print("Количество неженатых мужчин, зарабатывающих больше 50K:",len(not_married_men_more_than_50))

print()
print("Доля женатых мужчин, зарабатывающих больше 50K:",len(married_men_more_than_50),"/",\
      len(married_men),"=",int(100*(len(married_men_more_than_50)/len(married_men))),"%")
print("Доля неженатых мужчин, зарабатывающих больше 50K:",len(not_married_men_more_than_50),"/",len(not_married_men),\
      "=",int(100*(len(not_married_men_more_than_50)/len(not_married_men))),"%")
print("Таким образом, доля женатых  мужчин, зарабатывающих более 50K, в",44/8,"раз больше, чем доля неженатых мужчин, зарабатывающих более 50K.")

# Task 9. Какое максимальное число часов человек работает
# в неделю (признак hours-per-week)? Сколько людей работают
# такое количество часов и каков среди них процент зарабатывающих много?

# Переименовываем колонку ради удобства
data = data.rename(columns={"hours-per-week": "hours_per_week"})

# Ищем максимальное значение по колонке
max_value = data['hours_per_week'].max()
print(f"The maximum value in the column is: {max_value}")

# Проверяем  максимальное значение по столбику с помощью метода describe()
data["hours_per_week"].describe()

# Находим всех людей, которые работают 99 часов в неделю
people_who_work_99_hours = data.query('hours_per_week == 99')
len(people_who_work_99_hours)
print(f"There are {len(people_who_work_99_hours)}","people who work 99 hours a week.")

# Просто для справки и удобства
data.value_counts(subset = "hours_per_week")

people_who_work_99_hours_and_earn_more_than_50K = people_who_work_99_hours.query('salary == ">50K"')
len(people_who_work_99_hours_and_earn_more_than_50K)
print(f"Only {len(people_who_work_99_hours_and_earn_more_than_50K)} \
people earn more than 50K out of all {len(people_who_work_99_hours)} \
working 99 hours a week, which is",int(100*(len(people_who_work_99_hours_and_earn_more_than_50K)\
                                            /len(people_who_work_99_hours))),"%.")

# Task 10. Посчитайте среднее время работы (hours-per-week)
  # зарабатывающих мало и много (salary) для каждой страны (native-country).

data.groupby(['native-country', 'salary'])['hours_per_week'].mean().reset_index()

# Task 11. Сгруппируйте людей по возрастным группам young, adult, retiree, где:
# young соответствует 16-35 лет
# adult - 35-70 лет
# retiree - 70-100 лет

# Прописываем функцию
def f(row):
 if row['age'] >= 70:
  val = 'retiree'
 elif row['age'] >= 35:
  val = 'adult'
 else :
  val = 'young'
 return val

# Применяем полученную функцию
data['AgeGroup'] = data.apply (f, axis=1)

# Смотрим результат
data

# Task 12-13. Определите количество зарабатывающих >50K в каждой
# из возрастных групп (колонка AgeGroup), а также выведите название
# возрастной группы, в которой чаще зарабатывают больше 50К (>50K).

plus = data.query('salary == ">50K"')

# Всё по категории retirees
retirees = len(data.query('AgeGroup == "retiree"'))
retirees_50 = len(plus.query('AgeGroup == "retiree"'))

# Всё по категории adults
adults = len(data.query('AgeGroup == "adult"'))
adults_50 = len(plus.query('AgeGroup == "adult"'))

# Всё по категории young
young = len(data.query('AgeGroup == "young"'))
young_50 = len(plus.query('AgeGroup == "young"'))


print(f"There are {young} young people in the data-set. {young_50} earn more than 50k, which is {int(100*(young_50/young))} %.")
print()

print(f"There are {adults} adults in the data-set. {adults_50} earn more than 50k, which is {int(100*(adults_50/adults))} %.")
print()

print(f"There are {retirees} retirees in the data-set. {retirees_50} earn more than 50k, which is {int(100*(retirees_50/retirees))} %.")
print()

print("'Adults' category is leading in earning more than 50k, both absolutely and relatively.")

# Task 14. Сгруппируйте людей по типу занятости (колонка occupation)
# и определите количество людей в каждой группе. После чего напишите
# функцию фильтрации filter_func, которая будет возвращать только те группы,
# в которых средний возраст (колонка age) не больше 40 и в которых все
# работники отрабатывают более 5 часов в неделю (колонка hours-per-week).

data = data.rename(columns={"hours-per-week": "hours_per_week"})

occupation_counts = data.groupby('occupation').size().reset_index(name='counts')

# Define the filter function
def filter_func(group):
    average_age = group['age'].mean()
    all_work_more_than_5_hours = (group['hours_per_week'] > 5).all()
    return average_age <= 40 and all_work_more_than_5_hours

# Apply the filter function to the groups
filtered_groups = data.groupby('occupation').filter(filter_func)

# Display the result
filtered_groups