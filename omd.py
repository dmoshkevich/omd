def inevitable_death(message):
    print(message)
    return 0


def step4_square(umbrella):
    print('ф - Подойти к фонтану х - Подойти к храму')
    if umbrella:
        a_dict = dict(
            ф='Вы полюбовались фонтаном, вернулись домой и через несколько лет умерли от рака молочной железы',
            х='Вас заметили служители и посчитали утку с зонтом дурным знаком. Вы были казнены через сожжение и стали '
              'ужином для большой дружной семьи')
    else:
        a_dict = dict(
            ф='Вы полюбовались фонтаном, простудились и умерли он депрессии',
            х='Вас заметили служители, приняли к себе. Через 5 лет вас избрали новым папой римским, но вследствии '
              'заговора занять пост вам так и не удалось. Вы были сожжены, шёл белый дым')
    option = ''
    while option not in a_dict:
        print('Выберите: {}/{}'.format(*a_dict))
        option = input()
    return inevitable_death(a_dict[option])


def step4_bystreet(umbrella):
    print('Вам преградили путь бандиты о - Отдать деньги д - Драться')
    a_dict = dict(о='Вы отдали деньги, простудились и умерли от рака молочной железы',
                  д='Вы не победили в бою и стали ужином для большой дружной семьи')
    if umbrella:
        a_dict['д'] = 'Вы навешали бандитам зонтом, но затем подскользнулись и сломали шею'
    option = ''
    while option not in a_dict:
        print('Выберите: {}/{}'.format(*a_dict))
        option = input()
    return inevitable_death(a_dict[option])


def step3_town(umbrella):
    print('п - Пойти на площадь р - Пойти в переулок')
    a_dict = {'п': step4_square, 'р': step4_bystreet}
    option = ''
    while option not in a_dict:
        print('Выберите: {}/{}'.format(*a_dict))
        option = input()
    return a_dict[option](umbrella)


def step3_nature(umbrella):
    print('х - Пойти на холм п - Пойти в поле')
    a_dict = dict(х='Поздравляю, вас убила молния', п='Поздравляю, вы утонули в болоте. Это было не поле')
    if not umbrella:
        a_dict['х'] = 'Поздравляю, вы подскользнулись и сломали нос - не смогли принять свою новую внешность и ' \
                      'покончили с собой '
    option = ''
    while option not in a_dict:
        print('Выберите: {}/{}'.format(*a_dict))
        option = input()
    return inevitable_death(a_dict[option])


def step2(umbrella):
    print('г - Пойти в город? п - Пойти на природу')
    a_dict = {'г': step3_town, 'п': step3_nature}
    option = ''
    while option not in a_dict:
        print('Выберите: {}/{}'.format(*a_dict))
        option = input()
    return a_dict[option](umbrella)


def step1():
    print('Вы утка-маляр и решили погулять. '
          'Возьмете	зонтик?	☂')
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()
    return step2(options[option])


if __name__ == '__main__':
    step1()
