import random
def random_zpvd():
    zap =  ['Я Господь, Бог твой; да не будет у тебя других богов пред лицем Моим',
           'Не произноси имени Господа, Бога твоего напрасно',
           'Почитай отца твоего и мать твою, чтобы продлились дни твои на земле',
           'Не убивай', 'Не прелюбодействуй', 'Не кради', 'Не произноси ложного свидетельства на ближнего твоего']
    return zap[random.randint(0, len(zap))]

print(random_zpvd())

def get_word(number):
    word = ""
    if number == 1: word = 'Камень'
    elif number == 2: word = 'Ножницы'
    elif number == 3: word = 'Бумага'
    elif number == 4: word = 'Ящерица'
    else: word = 'Спок'
    return word

def game(word):
    result1 = ''
    result2 = ''
    comp_number = random.randint(1, 5)
    comp_word = get_word(comp_number)
    result1 = 'Пользователь: ' + word + ', Компьютер: ' + comp_word
    if word == 'Камень' and comp_word == 'Ножницы':
        result2 = 'Победил пользователь, так как камень ломает ножницы'
    elif word == 'Ножницы' and comp_word == 'Бумага':
        result2 = 'Победил пользователь, так как ножницы режут бумагу'
    elif word == 'Бумага' and comp_word == 'Камень':
        result2 = 'Победил пользователь, так как бумага заворачивает камень'
    elif word == 'Ящерица' and comp_word == 'Спок':
        result2 = 'Победил пользователь, так как ящерица отравляет спока'
    elif word == 'Спок' and comp_word == 'Ножницы':
        result2 = 'Победил пользователь, так как спок разбивает ножницы'
    elif word == 'Камень' and comp_word == 'Ящерица':
        result2 = 'Победил пользователь, так как камень давит ящерицу'
    elif word == 'Ножницы' and comp_word == 'Ящерица':
        result2 = 'Победил пользователь, так как ножницы обезглавливают ящерицу'
    elif word == 'Ящерица' and comp_word == 'Бумага':
        result2 = 'Победил пользователь, так как ящерица ест бумагу'
    elif word == 'Спок' and comp_word == 'Камень':
        result2 = 'Победил пользователь, так как спок испаряет камень'
    elif word == 'Бумага' and comp_word == 'Спок':
        result2 = 'Победил пользователь, так как бумага опровергает спока'

    elif word == 'Ножницы' and comp_word == 'Камень':
        result2 = 'Победил компьютер, так как камень ломает ножницы'
    elif word == 'Бумага' and comp_word == 'Ножницы':
        result2 = 'Победил компьютер, так как ножницы режут бумагу'
    elif word == 'Камень' and comp_word == 'Бумага':
        result2 = 'Победил компьютер, так как бумага заворачивает камень'
    elif word == 'Спок' and comp_word == 'Ящерица':
        result2 = 'Победил компьютер, так как ящерица отравляет спока'
    elif word == 'Ножницы' and comp_word == 'Спок':
        result2 = 'Победил компьютер, так как спок разбивает ножницы'
    elif word == 'Камень' and comp_word == 'Ящерица':
        result2 = 'Победил компьютер, так как камень давит ящерицу'
    elif word == 'Ящерица' and comp_word == 'Ножницы':
        result2 = 'Победил компьютер, так как ножницы обезглавливают ящерицу'
    elif word == 'Бумага' and comp_word == 'Ящерица':
        result2 = 'Победил компьютер, так как ящерица ест бумагу'
    elif word == 'Камень' and comp_word == 'Спок':
        result2 = 'Победил компьютер, так как спок испаряет камень'
    elif word == 'Спок' and comp_word == 'Бумага':
        result2 = 'Победил компьютер, так как бумага опровергает спока'

    elif word == comp_word:
        result2 = 'Ничья'

    return str(result1) + '\n' + str(result2)

user = ['Камень', 'Ножницы', 'Бумага', 'Ящерица', 'Спок']
print(game(user[random.randint(0, len(user))]))

