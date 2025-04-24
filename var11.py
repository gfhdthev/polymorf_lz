#Gfhdthev
#Основной файл для лабораторной работы номер 4


#импорт библиотек
import pandas as pd


#создаем основной класс
class Bank:
    def __init__(self): #инициализация
        self.file = pd.read_csv('var11.csv')

    def __pos__(self): #доопределения унарного +
        self.df = self.file.drop_duplicates() #удаляем дубликаты строк
        first_count = self.file.shape[0] #считаем кол-ыо дубликатов
        second_count = self.df.shape[0]
        dropped = first_count - second_count
        print(f'В файле удалено {dropped} дубликатов')

    def oper(self): #разделение датафрейма на 2 разных

        self.df1 = self.df[self.df['Время оплаты'] >= '09:00:00']    # строки, удовлетворяющие условию
        self.df1 = self.df1[self.df1['Время оплаты'] <= '23:00:00']    # строки, удовлетворяющие условию
        self.df1.to_csv('first.csv')
    

        self.df2 = self.df[self.df['Время оплаты'] < '09:00:00']    # строки, не удовлетворяющие условию
        self.df3 = self.df[self.df['Время оплаты'] > '23:00:00']    # строки, не удовлетворяющие условию
        self.result = pd.concat([self.df2, self.df3], axis=0)
        self.result.to_csv('second.csv')

    def __del__(self):
        print('Датафрейм удален')