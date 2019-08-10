import re
import random
from name_object import Name
from epithet_object import Epithet


class Hero:
    quality_pool = None
    main_quality = None
    name = None
    father = None
    father_name = ""
    grammatical_gender = ""

    def __init__(self, name, father):
        self.name = name
        self.father = father
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
