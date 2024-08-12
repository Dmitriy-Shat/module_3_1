calls = 0
def count_calls():
    global calls
    calls += 1
    return(calls)


def string_info(string = ''):
    lenth = len(string)
    print('string_info:', (lenth, string.upper(), string.lower()))
    count_calls()


string_info('Привет мир!')


def is_contains(line_ = '', list_ = []):
    list_1 = []
    print('is_contains:', (line_, list_))
    for index in list_[0::1]: # Перевод списка List_ в нижний регистр
        index = index.lower()
        list_1.append(index)  # и сохраняем его в списке list_1.
    line_ = line_.lower()     # перевод строки в нижний регистр.
    print(line_ in list_1)    # поиск строки в списке.
    count_calls()


is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])
print(calls)
