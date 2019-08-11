import random
import re
from name_object import Name
from verb_object import Verb, get_form
from hero_object import Hero

hex_structure = "^--^--^--^--^--^-"


male_names = [Name("Тамерлан", 3, "male"),
              Name("Владислав", 3, "male"),
              Name("Юрий", 1, "male"),
              Name("Владимир", 2, "male"),
              Name("Никита", 2, "male"),
              Name("Илья", 2, "male"),
              Name("Николай", 3, "male")]

female_names = [Name("Камисса", 2, "female"),
                Name("Ольга", 1, "female"),
                Name("Катерина", 3, "female"),
                Name("Полина", 2, "female"),
                Name("Анна", 1, "female"),
                Name("Александра", 3, "female"),
                Name("Мария", 2, "female")]

fathers = [Name("Руслан", 2, "male"),
           Name("Игорь", 1, "male"),
           Name("Алексей", 3, "male"),
           Name("Дмитрий", 1, "male"),
           Name("Олег", 2, "male"),
           Name("Егор", 2, "male"),
           Name("Евгений", 2, "male")]


def generate_hero():
    return Hero(random.choice(male_names), random.choice(fathers))


def put_stress(*args):
    result = ""
    for arg in args:
        pattern = re.compile("[аеёиоуыэюя]", re.I)
        i = 0
        for match in re.finditer(pattern, arg.text):
            if i == arg.stress_position - 1:
                result.append(arg.text[:match.span()[0]] + "^" + arg.text[match.span()[0]:])
            i += 1


def hexameter_checker(text):
    p = re.findall(r"(\^[аеёиоуэюыя]|[аеёиоуэюыя])", text, re.I)
    text_structure = ""
    for x in p:
        if re.match(r"\^.", x):
            text_structure += "^"
        else:
            text_structure += "-"
    return hex_structure == text_structure


texts = ["Гр^озно взглян^ув на нег^о, возраз^ил [Hero:N-E,n]",
         "М^олча ты ст^ой, [Hero:N,n], моем^у повин^уясь сов^ету",
         "Т^ак [Hero:N,n] размышл^ял, и ем^у показ^алося л^учше",
         "В^ызвать [Hero:N,a]. Наш^ёл он гер^оя, в друж^инах посл^едних",
         "Пр^адзно сто^ящего: гн^ев он всегд^ашний пит^ал на [Hero:N,p]",
         "Ст^ав перед н^им, [Hero:N,n] устремл^яет крыл^атые р^ечи:",
         "[Hero:N-E,n] - тро^ян повел^итель, и ^если о бл^ижних",
         "Т^ы сострад^аешь, теб^е заступ^иться за бл^ижнего д^олжно",
         "Сл^едуй за мн^ой, защит^им [Hero:P,a]; теб^я он, почт^енный,",
         "Б^удучи з^ятем, восп^итывал в с^обственном д^оме."]


def find_and_compare(text):
    p = re.findall(r"(\^[аеёиоуэюыя]|[аеёиоуэюыя]|\[.*\])", text, re.I)
    text_structure = ""
    for x in p:
        if re.match(r"\[.*\]", x):
            text_structure += "(.*)"
        elif re.match(r"\^.", x):
            text_structure += r"\^"
        else:
            text_structure += "-"
    return re.findall(text_structure, hex_structure)[0]


def parse_text(text):
    p = re.findall(r"\[.*\]", text, re.I)
    results = None
    if len(p) > 0:
        for x in p:
            while not results:
                new_hero = generate_hero()
                text_type, style = x[1:-1].split(':')
                base, case = style.split(',')
                structure = find_and_compare(text)
                results = new_hero.get_possible_combinations(base, case, structure)
            result = random.choice(results)
            print(text.replace(p[0], result).replace("^", ""))
    else:
        print(text.replace("^", ""))


def debug_verbs(verbs_array, tense, persons, single_or_plural, gender):
    for y in verbs_array:
        for x in persons:
            for z in gender:
                print(get_form(y, tense, x, z, single_or_plural).text + " "
                      + get_form(y, tense, x, z, single_or_plural).rhytmic_structure)


print("\nПервое спряжение:")
verbs = [Verb("желать", 2, False),
         Verb("рисовать", 3, False),
         Verb("доставать", 3, False),
         Verb("писать", 2, False),
         Verb("подсказывать", 2, False),
         Verb("белеть", 2, False),
         Verb("читать", 2, False),
         Verb("брить", 1, False),
         Verb("паять", 2, False),
         Verb("краснеть", 2, False),
         Verb("открывать", 3, False),
         Verb("таять", 1, False),
         Verb("сеять", 1, False),
         Verb("танцевать", 3, False),
         Verb("петь", 1, False),
         Verb("сидеть", 2, False),
         Verb("копать", 2, False),
         Verb("летать", 2, False),
         Verb("мешать", 2, False),
         Verb("рыть", 1, False),
         Verb("печатать", 2, False),
         Verb("копировать", 2, False),
         Verb("срывать", 2, False),
         Verb("колоть", 2, False),
         Verb("стелить", 2, False)]

# debug_verbs(verbs, "future", [1], True, "male")

print("\nВторое спряжение:")
verbs = [Verb("возить", 2, False),
         Verb("пилить", 3, False),
         Verb("тратить", 1, False),
         Verb("смотреть", 2, False),
         Verb("видеть", 1, False),
         Verb("терпеть", 2, False),
         Verb("ненавидеть", 3, False),
         Verb("обижать", 3, False),
         Verb("зависеть", 2, False),
         Verb("вертеть", 2, False),
         Verb("гнать", 1, False),
         Verb("держать", 2, False),
         Verb("слышать", 1, False),
         Verb("дышать", 2, False)]

# debug_verbs(verbs, "future", [1], True, "male")

print("\nИзолированные глаголы:")
verbs = [Verb("хотеть", 2, False),
         Verb("бежать", 2, False),
         Verb("чтить", 1, False),
         Verb("надоедать", 3, False),
         Verb("есть", 1, False),
         Verb("ехать", 1, False),
         Verb("идти", 2, False)]

# debug_verbs(verbs, "future", [1], True, "male")

print("\nВозвратные глаголы:")
verbs = [Verb("раскаляться", 3, False),
         Verb("смеяться", 2, False),
         Verb("сомневаться", 3, False),
         Verb("низвергаться", 3, False),
         Verb("сподвигаться", 3, False),
         Verb("возвращаться", 3, False),
         Verb("открываться", 3, False),
         Verb("обижаться", 3, False),
         Verb("делаться", 1, False),
         Verb("воздвигаться", 3, False),
         Verb("искупаться", 3, False),
         Verb("разрушаться", 3, False),
         Verb("приниматься", 3, False),
         Verb("рисоваться", 3, False),
         Verb("писаться", 2, False),
         Verb("читаться", 2, False),
         Verb("бриться", 1, False),
         Verb("мешаться", 2, False),
         Verb("пилиться", 2, False),
         Verb("терпеться", 2, False),
         Verb("вертеться", 2, False),
         Verb("тратиться", 1, False)]

# debug_verbs(verbs, "future", [1], True, "male")

verbs = [Verb("воспеть", 2, True),
         Verb("сделать", 1, True),
         Verb("низвергнуть", 2, True),
         Verb("распростереть", 4, True),
         Verb("воздвигнуть", 2, True),
         Verb("воспылать", 3, True),
         Verb("придти", 2, True),
         Verb("искупить", 3, True),
         Verb("принести", 3, True),
         Verb("помочь", 2, True),
         Verb("найти", 2, True),
         Verb("разрушить", 2, True),
         Verb("вернуть", 2, True),
         Verb("принять", 2, True),
         Verb("поразить", 3, True),
         Verb("оказать", 3, True),
         Verb("увлечься", 2, True)]

debug_verbs(verbs, "future", [3], True, ["male"])