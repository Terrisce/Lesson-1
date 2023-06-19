def palindrom():
    a = input('Введите слово: ')
    if a == a[::-1]: #это проверка первого и 
        print('True')
    else:
        print('False') 
palindrom()  

