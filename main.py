s1 = "Spam"
s2 = "eggs"

name = "Aigerim"
last_name = "Omuralieva"
middle_name = "Omuralieva"
full_name = name + ' ' + last_name
full_name_1 = name + ' ' + ((last_name + ' ') * 2)
i1 = 1222222

s = 'Python'
s3 = 'everYThing You cAn imAgine is rEaL'
s4 = 'foo goo moo'
s5 = '123abc'
s6 = ' ' ' '
s7 = 'hello, my friend'
s8 = ['my', 'name', 'is', 'Mark' ]
s9 = 'www.python.ru'
s10 = 'py'


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(len(name))
    print(full_name, last_name * 1)
    print(len(str(i1)))
    print(type(full_name_1))
    print(type(i1))

    print(s.find('th'))              #  возвращает наименьший индекс в строке
    print(s.rfind('yth'))            #  работает как "find", только справа налево
    print(s.index('hon'))            #  работает как "find", но выдает ошибку, если заданной подстроки нету
    print(s.rindex('hon'))           #  ищет в строке заданную подстроку справа налево
    print(s.replace('h', 't'))       #  заменяет что-то на другое
    print(s7.split())                # делит строку на список из подстрок
    print(s3.capitalize())           #  преобразует первую букву в заглавную, остальные в строчные
    print(s3.lower())                #  преобразует все буквы в строчные
    print(s3.upper())                #  преобразует все буквы в заглавные
    print(s3.swapcase())             #  преобразует заглавные буквы в строчные, а строчные в заглавные
    print(s3.title())                #  преобразует первые буквы всех слов в заглавные
    print((s4.count('oo')))          #  подсчитывает  количество заданных подстрок в строке
    print(s3.endswith('aL'))         #  определяет заканчивается ли строка заданной подстрокой
    print(s3.startswith('ever'))     #  определяет начинается ли строка с заданной подстроки
    print(s5.isalnum())              #  определяет состоит ли строка из букв и цифр
    print(s5.isalpha())              #  определяет состоит ли строка только из букв
    print(s5.isdigit())              #  определяет состоит ли строка только из цифр
    print(s5.isidentifier())         #  определяет является ли строка допустимым идентификатором Python
    print(s3.islower())              #  определяет являются ли буквы строчными
    print(s6.isspace())              #  определяет состоит ли строка только из пробельных символов
    print(s3.istitle())              #  определяет начинаются ли слова строки с заглавных букв
    print(s3.isupper())              #  определяет являются ли все буквы в строке заглавными
    print(' '.join(s8))              #  объединяет список в строку
    print(s9.partition('.'))         #  делит строку на основе заданного разделителя
    print(s9.rpartition('.'))        #  делит строку на основе заданного разделителя с конца
    print(s10.center(10))            #  отцентризовывает
    print(('a\tb\tc').expandtabs(8)) #  заменяет табуляции на пробелы
    print((' foo').lstrip())         #  обрезает пробелы в начале строки
    print(('foo ').rstrip())         #  обрезает пробелы в конце строки
    print((' foo ').strip())         #  обрезает пробелы в начале и в конце строки
    print(('42').zfill(5))           #  дополняет строку слева нулями для достижения заданной в скобках длины
    print(('42').ljust(8, '-'))      #  выравнивает по правому краю (можно использовать fillchar)
    print(('42').rjust(8, '-'))      #  выравнивает по левому краю (можно использовать fillchar)
    print(('Hi, {}!').format('mom')) #  подставляет заданное нами значение






