import random
import re
from name_object import Name
from verb_object import Verb
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


def debug_verbs(verbs_array, tense, persons, single_or_plural):
    for y in verbs_array:
        string1 = ""
        for x in persons:
            print(y.get_form(tense, x, "male", single_or_plural).text + " "
                  + y.get_form(tense, x, "male", single_or_plural).rhytmic_structure)


verbs = [Verb("воспевать", 3, False),
         Verb("делать", 1, False),
         Verb("низвергать", 3, False),
         Verb("распростирать", 4, False),
         Verb("воздвигать", 3, False),
         Verb("пылать", 2, False),
         Verb("приходить", 3, False),
         Verb("умолять", 3, False),
         Verb("искупать", 3, False),
         Verb("приносить", 3, False),
         Verb("помогать", 3, False),
         Verb("искать", 2, False),
         Verb("разрушать", 3, False),
         Verb("возвращать", 3, False),
         Verb("принимать", 3, False),
         Verb("разить", 2, False),
         Verb("оказывать", 2, False)]

# debug_verbs(verbs)

print("\nПервое спряжение:")
verbs = [Verb("желать", 2, True),
         Verb("рисовать", 3, True),
         Verb("доставать", 3, True),
         Verb("писать", 2, True),
         Verb("подсказывать", 2, True),
         Verb("белеть", 2, True),
         Verb("читать", 2, True),
         Verb("брить", 1, True),
         Verb("паять", 2, True),
         Verb("краснеть", 2, True),
         Verb("открывать", 3, True),
         Verb("таять", 1, True),
         Verb("сеять", 1, True),
         Verb("танцевать", 3, True),
         Verb("петь", 1, True),
         Verb("сидеть", 2, True),
         Verb("копать", 2, True),
         Verb("летать", 2, True),
         Verb("мешать", 2, True),
         Verb("рыть", 1, True),
         Verb("печатать", 2, True),
         Verb("копировать", 2, True),
         Verb("срывать", 2, True),
         Verb("колоть", 2, True),
         Verb("стелить", 2, True)]

# debug_verbs(verbs)

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

# debug_verbs(verbs)

print("\nИзолированные глаголы:")
verbs = [Verb("хотеть", 2, False),
         Verb("бежать", 2, False),
         Verb("чтить", 1, False),
         Verb("надоедать", 3, False),
         Verb("есть", 1, False),
         Verb("ехать", 1, False),
         Verb("идти", 2, False)]

# debug_verbs(verbs)

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
         Verb("рисоваться", 3, True),
         Verb("писаться", 2, True),
         Verb("читаться", 2, True),
         Verb("бриться", 1, True),
         Verb("мешаться", 2, True),
         Verb("пилиться", 2, False),
         Verb("терпеться", 2, False),
         Verb("вертеться", 2, False),
         Verb("тратиться", 1, False)]

debug_verbs(verbs, "present", [1], False)
