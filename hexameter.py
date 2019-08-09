import random
import re
from name_object import Name
from epithet_object import Epithet
from verb_object import Verb

hex_structure = "^--^--^--^--^--^-"


class Hero:
    quality_pool = None
    main_quality = None
    name = None
    father = None
    father_name = ""
    grammatical_gender = ""

    def __init__(self):
        self.name = random.choice(names)
        self.father = random.choice(fathers)
        self.grammatical_gender = self.name.grammatical_gender
        self.father_name = self.father.text
        self.quality_pool = random.choice(epithet_pool).copy()
        self.main_quality = self.quality_pool.pop(random.randrange(len(self.quality_pool)))

    def get_patronym(self):
        last_two_letters = self.father_name[len(self.father_name) - 2:]
        last_letter = self.father_name[len(self.father_name) - 1]
        if re.match("ей|ий|ес|ья|ид", last_two_letters):
            if self.name.grammatical_gender == "male":
                patronym = self.father_name[:-2] + "ид"
            else:
                patronym = self.father_name[:-2] + "ида"
        elif last_two_letters == "он":
            patronym = self.father_name[:-2] + "ос"
        elif last_letter == "ь":
            if self.name.grammatical_gender == "male":
                patronym = self.father_name[:-1] + "ид"
            else:
                patronym = self.father_name[:-1] + "ида"
        else:
            if self.name.grammatical_gender == "male":
                patronym = self.father_name + "ид"
            else:
                patronym = self.father_name + "ида"
        return Name(patronym, self.name.stress_position, self.grammatical_gender)

    def get_possible_combinations(self, style, case, structure):
        possible_combinations = []
        if style == "N-E" or style == "NE" or style == "EN":
            noun = self.name.get_case(case)
            epithets = [self.main_quality.get_case(case, self.grammatical_gender)]
            for epithet in self.quality_pool:
                epithets.append(epithet.get_case(case, self.grammatical_gender))
            for epithet in epithets:
                if style != "NE" and epithet.rhytmic_structure + noun.rhytmic_structure == structure:
                    possible_combinations.append(epithet.text + " " + noun.text)
                if style != "EN" and noun.rhytmic_structure + epithet.rhytmic_structure == structure:
                    possible_combinations.append(noun.text + " " + epithet.text)
        if style == "P":
            noun = self.get_patronym().get_case(case)
            if noun.rhytmic_structure == structure:
                possible_combinations.append(noun.text)
        if style == "N":
            noun = self.name.get_case(case)
            if noun.rhytmic_structure == structure:
                possible_combinations.append(noun.text)
        return possible_combinations


courageous_epithets = [Epithet("храбрый", 1),
                       Epithet("храбрейший", 2),
                       Epithet("бесстрашный", 2),
                       Epithet("непокорный", 3),
                       Epithet("пламенный", 1),
                       Epithet("доблестный", 1)]
warmonger_epithets = [Epithet("кровавый", 2),
                      Epithet("воинственный", 2),
                      Epithet("стрелолюбивый", 5),
                      Epithet("мечегрозящий", 4),
                      Epithet("сокрушительный", 3)]
beautiful_epithets = [Epithet("благородный", 3),
                      Epithet("прекрасный", 2),
                      Epithet("светлоносный", 3),
                      Epithet("сверкающий", 2),
                      Epithet("лепокудрый", 3)]
godly_epithets = [Epithet("божественный", 2),
                  Epithet("славоносный", 3),
                  Epithet("милосердный", 3),
                  Epithet("преисполненный", 3),
                  Epithet("бессмертный", 2)]

epithet_pool = [courageous_epithets, warmonger_epithets, beautiful_epithets, godly_epithets]

names = [Name("Тамерлан", 3, "male"),
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


def describe(name):
    quality = ""
    if name.quality == "courageous":
        quality = random.choice(courageous_epithets)
    elif name.quality == "warmonger":
        quality = random.choice(warmonger_epithets)
    elif name.quality == "beautiful":
        quality = random.choice(beautiful_epithets)
    elif name.quality == "godly":
        quality = random.choice(godly_epithets)
    rhytmic_tone = ""
    for x in range(name.syllables_count):
        if x + 1 == name.stress_position:
            rhytmic_tone += "^"
        else:
            rhytmic_tone += "-"
    for x in range(quality.syllables_count):
        if x + 1 == quality.stress_position:
            rhytmic_tone += "^"
        else:
            rhytmic_tone += "-"
    print(name.text + " " + quality.text + "\nРитмический рисунок: " + rhytmic_tone)


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
                new_hero = Hero()
                text_type, style = x[1:-1].split(':')
                base, case = style.split(',')
                structure = find_and_compare(text)
                results = new_hero.get_possible_combinations(base, case, structure)
            result = random.choice(results)
            print(text.replace(p[0], result).replace("^", ""))
    else:
        print(text.replace("^", ""))


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

for y in verbs:
    print(y.get_form("present", 1, "male").text
          + " " + y.get_form("present", 2, "male").text
          + " " + y.get_form("present", 3, "male").text
          + " " + y.get_form("present", 1, "plural").text
          + " " + y.get_form("present", 2, "plural").text
          + " " + y.get_form("present", 3, "plural").text + " " + y.get_form("present", 3, "plural").rhytmic_structure)

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
for y in verbs:
    print(y.get_form("present", 1, "male").text
          + " " + y.get_form("present", 2, "male").text
          + " " + y.get_form("present", 3, "male").text
          + " " + y.get_form("present", 1, "plural").text
          + " " + y.get_form("present", 2, "plural").text
          + " " + y.get_form("present", 3, "plural").text + " " + y.get_form("present", 3, "plural").rhytmic_structure)

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
for y in verbs:
    print(y.get_form("present", 1, "male").text
          + " " + y.get_form("present", 2, "male").text
          + " " + y.get_form("present", 3, "male").text
          + " " + y.get_form("present", 1, "plural").text
          + " " + y.get_form("present", 2, "plural").text
          + " " + y.get_form("present", 3, "plural").text + " " + y.get_form("present", 3, "plural").rhytmic_structure)

print("\nИзолированные глаголы:")
verbs = [Verb("хотеть", 2, False),
         Verb("бежать", 2, False),
         Verb("чтить", 1, False),
         Verb("надоедать", 3, False),
         Verb("есть", 1, False),
         Verb("ехать", 1, False),
         Verb("идти", 2, False)]
for y in verbs:
    print(y.get_form("present", 1, "male").text
          + " " + y.get_form("present", 2, "male").text
          + " " + y.get_form("present", 3, "male").text
          + " " + y.get_form("present", 1, "plural").text
          + " " + y.get_form("present", 2, "plural").text
          + " " + y.get_form("present", 3, "plural").text + " " + y.get_form("present", 3, "plural").rhytmic_structure)
