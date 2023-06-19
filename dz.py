def palindrom():
    a = input('Введите слово: ')
    if a == a[::-1]: #это проверка сходства исходного слова и перевернутого
        print('True')
    else:
        print('False') 
palindrom()  

