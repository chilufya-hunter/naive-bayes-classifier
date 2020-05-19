#В этом примере я буду использовать набор данных (который я собрал) с тремя столбцами: 
#(настроение), (количество сна),(пойти или не пойти). 
#Первые два-это особенности (настроение, часы сна) , а второй-ярлык " пойти"
#сварлтвый(grumpy),активный(enegetic),невеселый(sad)
mood=['grumpy','grumpy','energetic','sad','sad','sad','energetic','grumpy','grumpy',  
'sad','grumpy','energetic','energetic','sad']
hours=['three','three','three','five','eight','eight','eight','five','eight','five','five','five','three','five']

go=['No','No','Yes','Yes','Yes','No','Yes','No','Yes','Yes','Yes','Yes','Yes','No']


# Во-первых, вам нужно преобразовать эти строковые метки в числа. например: "сварлтвый", "активный", "невеселый"
#  как 0, 1, 2. Это называется кодированием меток. Scikit-learn предоставляет библиотеку LabelEncoder
#   для кодирования меток со значением от 0 до одного меньше числа дискретных классов
from sklearn import preprocessing
#creating labelEncoder
le = preprocessing.LabelEncoder()
# Преобразование строковых меток в числа.
mood_encoded=le.fit_transform(mood)
print (mood_encoded)

# Аналогично, вы также можете кодировать столбцы <<часы сна>> и <<пойти>>.
hours_encoded=le.fit_transform(hours)
label=le.fit_transform(go)
print (hours)
print (go)


#Теперь объедините обе функции (настроение и количество часов) в одну переменную (список кортежей).
features=[(2, 1), (2, 1), (0, 1), (1, 2), (1, 0), (1, 0), (0, 0), (2, 2), (2, 0), (1, 2), (2, 2), (0, 2), (0, 1), (1, 2)]
print (features) 


#Import Гауссовой модели упрощенного алгоритма Байеса
from sklearn.naive_bayes import GaussianNB

#Создание Гауссова классификатора
model = GaussianNB()

# Тренируйте модель с помощью обучающих наборов
model.fit(features,label)

#Прогнозируемый Выход
predicted= model.predict([[0,2]]) # 0:невеселый,sad, 2:пять часов сна 5
print ('predicted :' , predicted)
