# def strcounter(s):
#     for sym in set(s):
#         counter = 0
#         for sub_sym in s:
#             if sub_sym == sym:
#                 counter += 1
#         print(sym, counter)
# strcounter('abacda')



def palindrom():
    a = input('Введите слово: ')
    if a == a[::-1]: #это проверка первого и 
        print('True')
    else:
        print('False') 
palindrom()  

