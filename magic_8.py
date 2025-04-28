import random
import random as rn
question = ['Бесспорно', 'Мне кажется - да', 'Пока неясно, попробуй снова',
           'Даже не думай', 'Предрешено', 'Вероятнее всего', 'Спроси позже',
           'Мой ответ - нет', 'Никаких сомнений', 'Хорошие перспективы',
           'Лучше не рассказывать', 'По моим данным - нет', 'Определённо да',
           'Знаки говорят - да', 'Сейчас нельзя предсказать', 'Перспективы не очень хорошие',
           'Можешь быть уверен в этом', 'Да', 'Сконцентрируйся и спроси опять', 'Весьма сомнительно'
            ]
print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
name_user = input('Как тебя зову?\n')
print(f'Привет, {name_user}!')

#Функция возврата ответа от шара
def question_for(name, question_list):
    s_quest = str(input(f'{name}, что ты хочешь спросить?\n'))
    return print(random.choice(question_list))

#Функция проверки на продолжение
def user_next():
    flag = False
    while True:
        print('Хочешь задать ещё один вопрос?')
        answer = str(input())
        if answer == 'Да':
            flag = True
            break
        elif answer == 'Нет':
            break
        else:
            print('Я не понял твой ответ, нужно сказать Да или Нет')
            continue
    return flag

while True:
    question_for(name_user, question)
    if user_next():
        continue
    else:
        print('Возвращайся, если возникнут вопросы!')
        break