import random
import re

hex_structure = "^--^--^--^--^--^-"


class Word:
    grammatical_gender = "male"
    syllables_count = 1
    stress_position = 1

    def __init__(self, text, stress_position):
        self.text = text
        self.syllables_count = len(re.findall("[аеёиоуыэюя]", self.text))
        self.stress_position = stress_position


class WordStructure:

    def __init__(self, text, rhytmic_structure):
        self.text = text
        self.rhytmic_structure = rhytmic_structure


class Name(Word):

    def __init__(self, text, stress_position, grammatical_gender):
        super().__init__(text, stress_position)
        self.text = text
        self.syllables_count = len(re.findall("[аеёиоуыэюя]", text, re.I))
        self.stress_position = stress_position
        self.grammatical_gender = grammatical_gender
        self.base = text[:-1]

    def get_case(self, case):
        if case == "n":
            return self.nominative_case()
        elif case == "g":
            return self.genitive_case()
        elif case == "d":
            return self.dative_case()
        elif case == "a":
            return self.accusative_case()
        elif case == "i":
            return self.instrumental_case()
        elif case == "p":
            return self.prepositional_case()

    def nominative_case(self):
        return WordStructure(self.text, get_rhytmic_structure(self))

    def genitive_case(self):
        last_letter = self.text[len(self.text) - 1]
        if self.grammatical_gender == "male":
            if re.match("[бвгджзклмнпрстфхцчшщ]", last_letter):
                return WordStructure(self.text + "а", get_rhytmic_structure(self) + "-")
            elif last_letter == "й":
                return WordStructure(self.base + "я", get_rhytmic_structure(self) + "-")
            elif last_letter == "а":
                return WordStructure(self.base + "ы", get_rhytmic_structure(self))
            elif last_letter == "я":
                return WordStructure(self.base + "и", get_rhytmic_structure(self))
        elif self.grammatical_gender == "female":
            if last_letter == "а":
                return WordStructure(self.base + "ы", get_rhytmic_structure(self))
            elif last_letter == "я":
                return WordStructure(self.base + "и", get_rhytmic_structure(self))
            elif last_letter == "ь":
                return WordStructure(self.base + "и", get_rhytmic_structure(self) + "-")
            else:
                return WordStructure(self.text, get_rhytmic_structure(self))

    def dative_case(self):
        last_letter = self.text[len(self.text) - 1]
        if self.grammatical_gender == "male":
            if re.match("[бвгджзклмнпрстфхцчшщ]", last_letter):
                return WordStructure(self.text + "у", get_rhytmic_structure(self) + "-")
            elif last_letter == "й":
                return WordStructure(self.base + "ю", get_rhytmic_structure(self) + "-")
            elif last_letter == "а":
                return WordStructure(self.base + "е", get_rhytmic_structure(self))
            elif last_letter == "я":
                return WordStructure(self.base + "е", get_rhytmic_structure(self))
        elif self.grammatical_gender == "female":
            if last_letter == "а":
                return WordStructure(self.base + "е", get_rhytmic_structure(self))
            elif last_letter == "я":
                return WordStructure(self.base + "е", get_rhytmic_structure(self))
            elif last_letter == "ь":
                return WordStructure(self.base + "и", get_rhytmic_structure(self) + "-")
            else:
                return WordStructure(self.text, get_rhytmic_structure(self))

    def accusative_case(self):
        last_letter = self.text[len(self.text) - 1]
        if self.grammatical_gender == "male":
            if re.match("[бвгджзклмнпрстфхцчшщ]", last_letter):
                return WordStructure(self.text + "а", get_rhytmic_structure(self) + "-")
            elif last_letter == "й":
                return WordStructure(self.base + "я", get_rhytmic_structure(self) + "-")
            elif last_letter == "а":
                return WordStructure(self.base + "у", get_rhytmic_structure(self))
            elif last_letter == "я":
                return WordStructure(self.base + "ю", get_rhytmic_structure(self))
        elif self.grammatical_gender == "female":
            if last_letter == "а":
                return WordStructure(self.base + "у", get_rhytmic_structure(self))
            elif last_letter == "я":
                return WordStructure(self.base + "ю", get_rhytmic_structure(self))
            else:
                return WordStructure(self.text, get_rhytmic_structure(self))

    def instrumental_case(self):
        last_letter = self.text[len(self.text) - 1]
        if self.grammatical_gender == "male":
            if re.match("[бвгджзклмнпрстфхцчшщ]", last_letter):
                return WordStructure(self.text + "ом", get_rhytmic_structure(self) + "-")
            elif last_letter == "й":
                return WordStructure(self.base + "ем", get_rhytmic_structure(self) + "-")
            elif last_letter == "а":
                return WordStructure(self.base + "ой", get_rhytmic_structure(self))
            elif last_letter == "я":
                return WordStructure(self.base + "ёй", get_rhytmic_structure(self))
        elif self.grammatical_gender == "female":
            if last_letter == "а":
                return WordStructure(self.base + "ой", get_rhytmic_structure(self))
            elif last_letter == "я":
                return WordStructure(self.base + "ей", get_rhytmic_structure(self))
            elif last_letter == "ь":
                return WordStructure(self.base + "ью", get_rhytmic_structure(self) + "-")
            else:
                return WordStructure(self.text, get_rhytmic_structure(self))

    def prepositional_case(self):
        last_letter = self.text[len(self.text) - 1]
        if self.grammatical_gender == "male":
            if re.match("[бвгджзклмнпрстфхцчшщ]", last_letter):
                return WordStructure(self.text + "а", get_rhytmic_structure(self) + "-")
            elif last_letter == "й":
                return WordStructure(self.base + "я", get_rhytmic_structure(self) + "-")
            elif last_letter == "а":
                return WordStructure(self.base + "у", get_rhytmic_structure(self))
            elif last_letter == "я":
                return WordStructure(self.base + "ю", get_rhytmic_structure(self))
        elif self.grammatical_gender == "female":
            if last_letter == "а":
                return WordStructure(self.base + "у", get_rhytmic_structure(self))
            elif last_letter == "я":
                return WordStructure(self.base + "ю", get_rhytmic_structure(self))
            else:
                return WordStructure(self.text, get_rhytmic_structure(self))

    def rhytmic_structure(self):
        structure = ""
        for x in range(self.syllables_count):
            if x + 1 == self.stress_position:
                structure += "^"
            else:
                structure += "-"
        return structure


class Epithet(Word):
    soft_stem = False
    mixed_type = False
    base = ""

    def __init__(self, text, stress_position):
        super().__init__(text, stress_position)
        self.text = text
        self.syllables_count = len(re.findall("[аеёиоуыэюя]", text, re.I))
        self.stress_position = stress_position
        if re.search("[нчщ]ий$", text):
            self.soft_stem = True
        if re.search("[гкх].й$", text) or (re.search("ш.й$", text) and self.syllables_count == self.stress_position):
            self.mixed_type = True
        self.base = text[:-2]

    def get_case(self, case, gender_or_plural):
        if case == "n":
            return self.nominative_case(gender_or_plural)
        elif case == "g":
            return self.genitive_case(gender_or_plural)
        elif case == "d":
            return self.dative_case(gender_or_plural)
        elif case == "a":
            return self.accusative_case(gender_or_plural)
        elif case == "i":
            return self.instrumental_case(gender_or_plural)
        elif case == "p":
            return self.prepositional_case(gender_or_plural)

    def nominative_case(self, gender_or_plural):
        if gender_or_plural == "plural":
            return WordStructure(self.base + ("ие" if (self.soft_stem or self.mixed_type) else "ые"),
                                 get_rhytmic_structure(self) + "-")
        elif gender_or_plural == "female":
            return WordStructure(self.base + ("яя" if self.soft_stem else "ая"),
                                 get_rhytmic_structure(self) + "-")
        elif gender_or_plural == "neutral":
            return WordStructure(self.base + ("ее" if self.soft_stem else "ое"),
                                 get_rhytmic_structure(self) + "-")
        else:
            return WordStructure(self.text, get_rhytmic_structure(self))

    def genitive_case(self, gender_or_plural):
        if gender_or_plural == "plural":
            return WordStructure(self.base + ("их" if (self.soft_stem or self.mixed_type) else "ых"),
                                 get_rhytmic_structure(self))
        elif gender_or_plural == "female":
            return WordStructure(self.base + ("ей" if self.soft_stem else "ой"),
                                 get_rhytmic_structure(self))
        else:
            return WordStructure(self.base + ("его" if self.soft_stem else "ого"),
                                 get_rhytmic_structure(self) + "-")

    def dative_case(self, gender_or_plural):
        if gender_or_plural == "plural":
            return WordStructure(self.base + ("им" if (self.soft_stem or self.mixed_type) else "ым"),
                                 get_rhytmic_structure(self))
        elif gender_or_plural == "female":
            return WordStructure(self.base + "ей" if self.soft_stem else "ой",
                                 get_rhytmic_structure(self))
        else:
            return WordStructure(self.base + ("ему" if self.soft_stem else "ому"),
                                 get_rhytmic_structure(self) + "-")

    def accusative_case(self, gender_or_plural):
        if gender_or_plural == "plural":
            return WordStructure(self.base + ("ие" if (self.soft_stem or self.mixed_type) else "ые"),
                                 get_rhytmic_structure(self) + "-")
        elif gender_or_plural == "female":
            return WordStructure(self.base + ("юю" if self.soft_stem else "ую"),
                                 get_rhytmic_structure(self) + "-")
        elif gender_or_plural == "neutral":
            return WordStructure(self.base + ("ее" if self.soft_stem else "ое"),
                                 get_rhytmic_structure(self) + "-")
        else:
            return WordStructure(self.text, get_rhytmic_structure(self))

    def instrumental_case(self, gender_or_plural):
        if gender_or_plural == "plural":
            return WordStructure(self.base + ("ими" if (self.soft_stem or self.mixed_type) else "ыми"),
                                 get_rhytmic_structure(self) + "-")
        elif gender_or_plural == "female":
            return WordStructure(self.base + ("ей" if self.soft_stem else "ой"),
                                 get_rhytmic_structure(self))
        else:
            return WordStructure(self.base + ("им" if (self.soft_stem or self.mixed_type) else "ым"),
                                 get_rhytmic_structure(self))

    def prepositional_case(self, gender_or_plural):
        if gender_or_plural == "plural":
            return WordStructure(self.base + ("их" if (self.soft_stem or self.mixed_type) else "ых"),
                                 get_rhytmic_structure(self))
        elif gender_or_plural == "female":
            return WordStructure(self.base + ("ей" if self.soft_stem else "ой"),
                                 get_rhytmic_structure(self))
        else:
            return WordStructure(self.base + ("ем" if self.soft_stem else "ом"),
                                 get_rhytmic_structure(self))


class Verb(Word):
    perfective = False

    def __init__(self, text, stress_position, perfective):
        super().__init__(text, stress_position)
        self.text = text
        self.stress_position = stress_position
        self.syllables_count = len(re.findall("[аеёиоуыэюя]", text, re.I))
        self.perfective = perfective
        self.conjugation = self.get_conjugation()

    def get_conjugation(self):
        if re.search(".*(есть)|(дать)|(быть)$", self.text, re.I):
            return 3
        for x in ["хотеть", "бежать", "чтить", "ехать", "идти"]:
            if x == self.text:
                return 3
        for x in ["брить", "стелить"]:
            if re.search(x + "$", self.text, re.I):
                return 1
        for x in ["смотреть", "видеть", "ненавидеть", "зависеть", "терпеть",
                  "обидеть", "вертеть", "слышать", "держать", "гнать", "дышать"]:
            if re.search(x + "$", self.text, re.I):
                return 2
        if re.search("ить$", self.text, re.I):
            return 2
        return 1

    def get_type(self):
        if re.search(".*[аяе]ть$", self.text, re.I):
            if re.search(".*[ое]вать$", self.text, re.I):
                return 2
            elif re.search(".*авать$", self.text, re.I):
                return 13
            elif re.search(".*ереть$", self.text, re.I):
                return 9
            if re.search(".*[аяе]ть$", self.text, re.I):
                return 1
            elif re.search(".*[аяе]ть$", self.text, re.I):
                return 5
            elif re.search(".*[ая]ть$", self.text, re.I):
                return 6
            elif re.search(".*[ая]ть", self.text, re.I):
                return 14
        elif re.search(".*[ыуи]ть$", self.text, re.I):
            if re.search(".*нуть$", self.text, re.I):
                return 3
            elif re.search(".*ить$", self.text, re.I):
                return 4
            elif re.search(".*ить$", self.text, re.I):
                return 11
            elif re.search(".*[ыуи]ть$", self.text, re.I):
                return 12
        elif re.search(".*[зс]т[ьи]$", self.text, re.I):
            return 7
        elif re.search(".*чь$", self.text, re.I):
            return 8
        elif re.search(".*о[лр]оть$", self.text, re.I):
            return 10
        elif re.search(".*ть", self.text, re.I):
            if re.search(".*ть", self.text, re.I):
                return 15
            elif re.search(".*ть", self.text, re.I):
                return 16

    def get_form(self, tense, person, gender_or_plural):
        if tense == "present":
            if gender_or_plural != "plural":
                if person == 1:
                    if self.conjugation == 1:
                        if re.search(".*еть$", self.text, re.I):
                            if re.search(".*деть$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "жу", get_rhytmic_structure(self))
                            elif re.search(".*теть$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "чу", get_rhytmic_structure(self))
                            elif re.search(".*петь$", self.text, re.I):
                                return WordStructure(self.text[:-3] + "ою", get_rhytmic_structure(self)[:-2] + "-^")
                            else:
                                return WordStructure(self.text[:-2] + "ю", get_rhytmic_structure(self) + "-")
                        elif re.search(".*ать$", self.text, re.I):
                            if re.search(".*сать$", self.text, re.I) and self.stress_position == self.syllables_count:
                                return WordStructure(self.text[:-4] + "шу", get_rhytmic_structure(self))
                            elif re.search(".*певать$", self.text, re.I):
                                return WordStructure(self.text[:-2] + "ю", get_rhytmic_structure(self) + "-")
                            elif re.search(".*[ое]вать$", self.text, re.I):
                                if self.stress_position == self.syllables_count:
                                    return WordStructure(self.text[:-5] + "ую", get_rhytmic_structure(self)[:-2] + "^-")
                                else:
                                    return WordStructure(self.text[:-5] + "ую", get_rhytmic_structure(self))
                            elif re.search(".*авать$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "ю", get_rhytmic_structure(self))
                            elif re.search(".*скать$", self.text, re.I):
                                return WordStructure(self.text[:-5] + "щу", get_rhytmic_structure(self))
                            else:
                                return WordStructure(self.text[:-2] + "ю", get_rhytmic_structure(self) + "-")
                        elif re.search(".*ить", self.text, re.I):
                            if re.search(".*рить$", self.text, re.I):
                                return WordStructure(self.text[:-3] + "ею", get_rhytmic_structure(self) + "-")
                            else:
                                return WordStructure(self.text[:-3] + "ю", get_rhytmic_structure(self))
                        elif re.search(".*ять$", self.text, re.I):
                            if re.search(".*[ал]ять", self.text, re.I) and self.stress_position == self.syllables_count:
                                return WordStructure(self.text[:-2] + "ю", get_rhytmic_structure(self) + "-")
                            else:
                                return WordStructure(self.text[:-3] + "ю", get_rhytmic_structure(self))
                        elif re.search(".*оть$", self.text, re.I):
                            return WordStructure(self.text[:-3] + "ю", get_rhytmic_structure(self))
                        elif re.search(".*ыть$", self.text, re.I):
                            return WordStructure(self.text[:-3] + "ою", get_rhytmic_structure(self) + "-")
                    elif self.conjugation == 2:
                        if re.search(".*ить$", self.text, re.I):
                            if re.search(".*зить$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "жу", get_rhytmic_structure(self))
                            elif re.search(".*дить$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "жу", get_rhytmic_structure(self))
                            elif re.search(".*тить$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "чу", get_rhytmic_structure(self))
                            elif re.search(".*сить$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "шу", get_rhytmic_structure(self))
                            else:
                                return WordStructure(self.text[:-3] + "ю", get_rhytmic_structure(self)[:-1] + "^")
                        elif re.search(".*еть$", self.text, re.I):
                            if re.search(".*теть$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "чу", get_rhytmic_structure(self))
                            elif re.search(".*деть$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "жу", get_rhytmic_structure(self))
                            elif re.search(".*петь$", self.text, re.I):
                                return WordStructure(self.text[:-3] + "лю", get_rhytmic_structure(self))
                            elif re.search(".*сеть$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "шу", get_rhytmic_structure(self))
                            else:
                                return WordStructure(self.text[:-3] + "ю", get_rhytmic_structure(self))
                        elif re.search(".*ать$", self.text, re.I):
                            if re.search(".*[жш]ать$", self.text, re.I):
                                return WordStructure(self.text[:-3] + "у", get_rhytmic_structure(self))
                            elif re.search(".*гнать$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "оню", get_rhytmic_structure(self)[:-1] + "-^")
                            else:
                                return WordStructure(self.text[:-3] + "ю", get_rhytmic_structure(self))
                    else:
                        if re.search(".*есть$", self.text, re.I):
                            if self.text == "есть":
                                return WordStructure("ем", "^")
                            else:
                                return WordStructure(self.text[:-3] + "даю", "-^")
                        elif re.search(".*дать$", self.text, re.I):
                            return WordStructure(self.text[:-2] + "ю", get_rhytmic_structure(self))
                        elif re.search(".+быть$", self.text, re.I):
                            return WordStructure(self.text[:-2] + "ваю", get_rhytmic_structure(self))
                        elif self.text == "хотеть":
                            return WordStructure("хочу", "-^")
                        elif self.text == "бежать":
                            return WordStructure("бегу", "-^")
                        elif self.text == "чтить":
                            return WordStructure("чту", "^")
                        elif self.text == "ехать":
                            return WordStructure("еду", "^-")
                        elif self.text == "идти":
                            return WordStructure("иду", "-^")
                        elif self.text == "быть":
                            return WordStructure("есть", "^")

                elif person == 2:
                    if self.conjugation == 1:
                        if re.search(".*еть$", self.text, re.I):
                            if re.search(".*деть$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "дишь", get_rhytmic_structure(self))
                            elif re.search(".*теть$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "тишь", get_rhytmic_structure(self))
                            elif re.search(".*петь$", self.text, re.I):
                                return WordStructure(self.text[:-3] + "оёшь", get_rhytmic_structure(self)[:-1] + "-^")
                            else:
                                return WordStructure(self.text[:-2] + "ешь", get_rhytmic_structure(self) + "-")
                        elif re.search(".*ать$", self.text, re.I):
                            if re.search(".*сать$", self.text, re.I) and self.stress_position == self.syllables_count:
                                return WordStructure(self.text[:-4] + "шешь", get_rhytmic_structure(self)[:-2] + "^-")
                            elif re.search(".*певать$", self.text, re.I):
                                return WordStructure(self.text[:-2] + "ешь", get_rhytmic_structure(self) + "-")
                            elif re.search(".*[ое]вать$", self.text, re.I):
                                if self.stress_position == self.syllables_count:
                                    return WordStructure(self.text[:-5] + "уешь", get_rhytmic_structure(self)[:-2]
                                                         + "^-")
                                else:
                                    return WordStructure(self.text[:-5] + "уешь", get_rhytmic_structure(self))
                            elif re.search(".*авать$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "ёшь", get_rhytmic_structure(self))
                            elif re.search(".*скать$", self.text, re.I):
                                return WordStructure(self.text[:-5] + "щешь", get_rhytmic_structure(self)[:-2] + "^-")
                            else:
                                return WordStructure(self.text[:-2] + "ешь", get_rhytmic_structure(self) + "-")
                        elif re.search(".*ить", self.text, re.I):
                            if re.search(".*рить$", self.text, re.I):
                                return WordStructure(self.text[:-3] + "еешь", get_rhytmic_structure(self) + "-")
                            else:
                                return WordStructure(self.text[:-3] + "ешь", get_rhytmic_structure(self)[:-2] + "^-")
                        elif re.search(".*ять$", self.text, re.I):
                            if re.search(".*[ал]ять", self.text, re.I) and self.stress_position == self.syllables_count:
                                return WordStructure(self.text[:-2] + "ешь", get_rhytmic_structure(self) + "-")
                            else:
                                return WordStructure(self.text[:-3] + "ешь", get_rhytmic_structure(self))
                        elif re.search(".*оть$", self.text, re.I):
                            return WordStructure(self.text[:-3] + "ешь", get_rhytmic_structure(self)[:-2] + "^-")
                        elif re.search(".*ыть$", self.text, re.I):
                            return WordStructure(self.text[:-3] + "оешь", get_rhytmic_structure(self) + "-")
                    elif self.conjugation == 2:
                        if re.search(".*ить$", self.text, re.I):
                            if re.search(".*зить$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "зишь", get_rhytmic_structure(self)[:-2] + "^-")
                            if re.search(".*дить$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "дишь", get_rhytmic_structure(self)[:-2] + "^-")
                            elif re.search(".*тить$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "тишь", get_rhytmic_structure(self)[:-2] + "^-")
                            elif re.search(".*сить$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "сишь", get_rhytmic_structure(self)[:-2] + "^-")
                            else:
                                return WordStructure(self.text[:-3] + "ишь", get_rhytmic_structure(self)[:-2]
                                                     + "^-")
                        elif re.search(".*еть$", self.text, re.I):
                            if re.search(".*теть$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "тишь", get_rhytmic_structure(self)[:-2] + "^-")
                            elif re.search(".*деть$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "дишь", get_rhytmic_structure(self)[:-2] + "^-")
                            elif re.search(".*петь$", self.text, re.I):
                                return WordStructure(self.text[:-3] + "ишь", get_rhytmic_structure(self)[:-2] + "^-")
                            elif re.search(".*сеть$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "сишь", get_rhytmic_structure(self)[:-2] + "^-")
                            else:
                                return WordStructure(self.text[:-3] + "ишь", get_rhytmic_structure(self)[:-2] + "^-")
                        elif re.search(".*ать$", self.text, re.I):
                            if re.search(".*[жш]ать$", self.text, re.I):
                                return WordStructure(self.text[:-3] + "ишь", get_rhytmic_structure(self)[:-2] + "^-")
                            elif re.search(".*гнать$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "онишь", get_rhytmic_structure(self) + "-")
                            else:
                                return WordStructure(self.text[:-3] + "ишь", get_rhytmic_structure(self))
                    else:
                        if re.search(".*есть$", self.text, re.I):
                            if self.text == "есть":
                                return WordStructure("ешь", "^")
                            else:
                                return WordStructure(self.text[:-3] + "даешь", get_rhytmic_structure(self))
                        elif re.search(".*дать$", self.text, re.I):
                            return WordStructure(self.text[:-2] + "ешь", get_rhytmic_structure(self))
                        elif re.search(".+быть$", self.text, re.I):
                            return WordStructure(self.text[:-2] + "ваешь", get_rhytmic_structure(self))
                        elif self.text == "хотеть":
                            return WordStructure("хочешь", "^-")
                        elif self.text == "бежать":
                            return WordStructure("бежишь", "-^")
                        elif self.text == "чтить":
                            return WordStructure("чтишь", "^")
                        elif self.text == "ехать":
                            return WordStructure("едешь", "^-")
                        elif self.text == "идти":
                            return WordStructure("идёшь", "-^")
                        elif self.text == "быть":
                            return WordStructure("есть", "^")

                elif person == 3:
                    if self.conjugation == 1:
                        if re.search(".*еть$", self.text, re.I):
                            if re.search(".*деть$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "дит", get_rhytmic_structure(self))
                            elif re.search(".*теть$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "тит", get_rhytmic_structure(self))
                            elif re.search(".*петь$", self.text, re.I):
                                return WordStructure(self.text[:-3] + "оёт", get_rhytmic_structure(self)[:-1] + "-^")
                            else:
                                return WordStructure(self.text[:-2] + "ет", get_rhytmic_structure(self) + "-")
                        elif re.search(".*ать$", self.text, re.I):
                            if re.search(".*сать$", self.text, re.I):
                                if self.stress_position == self.syllables_count:
                                    return WordStructure(self.text[:-4] + "шет", get_rhytmic_structure(self)[:-2]
                                                         + "^-")
                                else:
                                    return WordStructure(self.text[:-4] + "шет", get_rhytmic_structure(self))
                            elif re.search(".*певать$", self.text, re.I):
                                return WordStructure(self.text[:-2] + "ет", get_rhytmic_structure(self) + "-")
                            elif re.search(".*[ое]вать$", self.text, re.I):
                                if self.stress_position == self.syllables_count:
                                    return WordStructure(self.text[:-5] + "ует", get_rhytmic_structure(self)[:-2]
                                                         + "^-")
                                else:
                                    return WordStructure(self.text[:-5] + "ует", get_rhytmic_structure(self))
                            elif re.search(".*авать$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "ёт", get_rhytmic_structure(self))
                            elif re.search(".*скать$", self.text, re.I):
                                return WordStructure(self.text[:-5] + "щет", get_rhytmic_structure(self)[:-2] + "^-")
                            else:
                                return WordStructure(self.text[:-2] + "ет", get_rhytmic_structure(self) + "-")
                        elif re.search(".*ить", self.text, re.I):
                            if re.search(".*рить$", self.text, re.I):
                                return WordStructure(self.text[:-3] + "еет", get_rhytmic_structure(self) + "-")
                            else:
                                return WordStructure(self.text[:-3] + "ет", get_rhytmic_structure(self)[:-2] + "^-")
                        elif re.search(".*ять$", self.text, re.I):
                            if re.search(".*[ал]ять", self.text, re.I) and self.stress_position == self.syllables_count:
                                return WordStructure(self.text[:-2] + "ет", get_rhytmic_structure(self) + "-")
                            else:
                                return WordStructure(self.text[:-3] + "ет", get_rhytmic_structure(self))
                        elif re.search(".*оть$", self.text, re.I):
                            return WordStructure(self.text[:-3] + "ет", get_rhytmic_structure(self)[:-2] + "^-")
                        elif re.search(".*ыть$", self.text, re.I):
                            return WordStructure(self.text[:-3] + "оет", get_rhytmic_structure(self) + "-")
                    elif self.conjugation == 2:
                        if re.search(".*ить$", self.text, re.I):
                            if re.search(".*зить$", self.text, re.I):
                                if self.text == "возить":
                                    return WordStructure(self.text[:-4] + "зит", get_rhytmic_structure(self)[:-2]
                                                         + "^-")
                                else:
                                    return WordStructure(self.text[:-4] + "зит", get_rhytmic_structure(self))
                            if re.search(".*дить$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "дит", get_rhytmic_structure(self)[:-2] + "^-")
                            elif re.search(".*тить$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "тит", get_rhytmic_structure(self)[:-2] + "^-")
                            elif re.search(".*сить$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "сит", get_rhytmic_structure(self)[:-2] + "^-")
                            else:
                                return WordStructure(self.text[:-3] + "ит", get_rhytmic_structure(self)[:-2] + "^-")
                        elif re.search(".*еть$", self.text, re.I):
                            if re.search(".*теть$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "тит", get_rhytmic_structure(self)[:-2] + "^-")
                            elif re.search(".*деть$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "дит", get_rhytmic_structure(self)[:-2] + "^-")
                            elif re.search(".*петь$", self.text, re.I):
                                return WordStructure(self.text[:-3] + "ит", get_rhytmic_structure(self)[:-2] + "^-")
                            elif re.search(".*сеть$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "сит", get_rhytmic_structure(self)[:-2] + "^-")
                            else:
                                return WordStructure(self.text[:-3] + "ит", get_rhytmic_structure(self)[:-2] + "^-")
                        elif re.search(".*ать$", self.text, re.I):
                            if re.search(".*[жш]ать$", self.text, re.I):
                                return WordStructure(self.text[:-3] + "ит", get_rhytmic_structure(self)[:-2] + "^-")
                            elif re.search(".*гнать$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "онит", get_rhytmic_structure(self) + "-")
                            else:
                                return WordStructure(self.text[:-3] + "ит", get_rhytmic_structure(self))
                    else:
                        if re.search(".*есть$", self.text, re.I):
                            if self.text == "есть":
                                return WordStructure("ест", "^")
                            else:
                                return WordStructure(self.text[:-3] + "дает", get_rhytmic_structure(self))
                        elif re.search(".*дать$", self.text, re.I):
                            return WordStructure(self.text[:-2] + "ет", get_rhytmic_structure(self))
                        elif re.search(".+быть$", self.text, re.I):
                            return WordStructure(self.text[:-2] + "вает", get_rhytmic_structure(self))
                        elif self.text == "хотеть":
                            return WordStructure("хочет", "^-")
                        elif self.text == "бежать":
                            return WordStructure("бежит", "-^")
                        elif self.text == "чтить":
                            return WordStructure("чтит", "^")
                        elif self.text == "ехать":
                            return WordStructure("едет", "^-")
                        elif self.text == "идти":
                            return WordStructure("идёт", "-^")
                        elif self.text == "быть":
                            return WordStructure("есть", "^")
            else:
                if person == 1:
                    if self.conjugation == 1:
                        if re.search(".*еть$", self.text, re.I):
                            if re.search(".*деть$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "дим", get_rhytmic_structure(self))
                            elif re.search(".*теть$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "тим", get_rhytmic_structure(self))
                            elif re.search(".*петь$", self.text, re.I):
                                return WordStructure(self.text[:-3] + "оём", get_rhytmic_structure(self)[:-1] + "-^")
                            else:
                                return WordStructure(self.text[:-2] + "ем", get_rhytmic_structure(self) + "-")
                        elif re.search(".*ать$", self.text, re.I):
                            if re.search(".*сать$", self.text, re.I) and self.stress_position == self.syllables_count:
                                return WordStructure(self.text[:-4] + "шем", get_rhytmic_structure(self)[:-2] + "^-")
                            elif re.search(".*певать$", self.text, re.I):
                                return WordStructure(self.text[:-2] + "ем", get_rhytmic_structure(self) + "-")
                            elif re.search(".*[ое]вать$", self.text, re.I):
                                if self.stress_position == self.syllables_count:
                                    return WordStructure(self.text[:-5] + "уем",
                                                         get_rhytmic_structure(self)[:-2] + "^-")
                                else:
                                    return WordStructure(self.text[:-5] + "уем", get_rhytmic_structure(self))
                            elif re.search(".*авать$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "ём", get_rhytmic_structure(self))
                            elif re.search(".*скать$", self.text, re.I):
                                return WordStructure(self.text[:-5] + "щем", get_rhytmic_structure(self)[:-2] + "^-")
                            else:
                                return WordStructure(self.text[:-2] + "ем", get_rhytmic_structure(self) + "-")
                        elif re.search(".*ить", self.text, re.I):
                            if re.search(".*рить$", self.text, re.I):
                                return WordStructure(self.text[:-3] + "еем", get_rhytmic_structure(self) + "-")
                            else:
                                return WordStructure(self.text[:-3] + "ем", get_rhytmic_structure(self)[:-2] + "^-")
                        elif re.search(".*ять$", self.text, re.I):
                            if re.search(".*[ал]ять", self.text, re.I) and self.stress_position == self.syllables_count:
                                return WordStructure(self.text[:-2] + "ем", get_rhytmic_structure(self) + "-")
                            else:
                                return WordStructure(self.text[:-3] + "ем", get_rhytmic_structure(self))
                        elif re.search(".*оть$", self.text, re.I):
                            return WordStructure(self.text[:-3] + "ем", get_rhytmic_structure(self)[:-2] + "^-")
                        elif re.search(".*ыть$", self.text, re.I):
                            return WordStructure(self.text[:-3] + "оем", get_rhytmic_structure(self) + "-")
                    elif self.conjugation == 2:
                        if re.search(".*ить$", self.text, re.I):
                            if re.search(".*озить$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "зим", get_rhytmic_structure(self)[:-2] + "^-")
                            elif re.search(".*зить$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "зим", get_rhytmic_structure(self))
                            elif re.search(".*дить$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "дим", get_rhytmic_structure(self)[:-2] + "^-")
                            elif re.search(".*тить$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "тим", get_rhytmic_structure(self)[:-2] + "^-")
                            elif re.search(".*сить$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "сим", get_rhytmic_structure(self)[:-2] + "^-")
                            else:
                                return WordStructure(self.text[:-3] + "им", get_rhytmic_structure(self)[:-2] + "^-")
                        elif re.search(".*еть$", self.text, re.I):
                            if re.search(".*теть$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "тим", get_rhytmic_structure(self)[:-2] + "^-")
                            elif re.search(".*деть$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "дим", get_rhytmic_structure(self)[:-2] + "^-")
                            elif re.search(".*петь$", self.text, re.I):
                                return WordStructure(self.text[:-3] + "им", get_rhytmic_structure(self)[:-2] + "^-")
                            elif re.search(".*сеть$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "сим", get_rhytmic_structure(self)[:-2] + "^-")
                            else:
                                return WordStructure(self.text[:-3] + "им", get_rhytmic_structure(self)[:-2] + "^-")
                        elif re.search(".*ать$", self.text, re.I):
                            if re.search(".*[жш]ать$", self.text, re.I):
                                if re.search(".*ижать$", self.text, re.I):
                                    return WordStructure(self.text[:-3] + "аем", get_rhytmic_structure(self) + "-")
                                else:
                                    return WordStructure(self.text[:-3] + "им", get_rhytmic_structure(self)[:-2] + "^-")
                            elif re.search(".*гнать$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "оним", get_rhytmic_structure(self) + "-")
                            else:
                                return WordStructure(self.text[:-3] + "им", get_rhytmic_structure(self) + "-")
                    else:
                        if re.search(".*есть$", self.text, re.I):
                            if self.text == "есть":
                                return WordStructure("едим", "-^")
                            else:
                                return WordStructure(self.text[:-3] + "даем", get_rhytmic_structure(self))
                        elif re.search(".*дать$", self.text, re.I):
                            return WordStructure(self.text[:-2] + "ем", get_rhytmic_structure(self) + "-")
                        elif re.search(".+быть$", self.text, re.I):
                            return WordStructure(self.text[:-2] + "ваем", get_rhytmic_structure(self))
                        elif self.text == "хотеть":
                            return WordStructure("хотим", "-^")
                        elif self.text == "бежать":
                            return WordStructure("бежим", "-^")
                        elif self.text == "чтить":
                            return WordStructure("чтим", "^")
                        elif self.text == "ехать":
                            return WordStructure("едем", "^-")
                        elif self.text == "идти":
                            return WordStructure("идём", "-^")
                        elif self.text == "быть":
                            return WordStructure("есть", "^")

                elif person == 2:
                    if self.conjugation == 1:
                        if re.search(".*еть$", self.text, re.I):
                            if re.search(".*деть$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "дите", get_rhytmic_structure(self) + "-")
                            elif re.search(".*теть$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "тите", get_rhytmic_structure(self) + "-")
                            elif re.search(".*петь$", self.text, re.I):
                                return WordStructure(self.text[:-3] + "оёте", get_rhytmic_structure(self)[:-1] + "-^-")
                            else:
                                return WordStructure(self.text[:-2] + "ете", get_rhytmic_structure(self) + "--")
                        elif re.search(".*ать$", self.text, re.I):
                            if re.search(".*сать$", self.text, re.I) and self.stress_position == self.syllables_count:
                                return WordStructure(self.text[:-4] + "шете", get_rhytmic_structure(self)[:-2]
                                                     + "^--")
                            elif re.search(".*певать$", self.text, re.I):
                                return WordStructure(self.text[:-2] + "ете", get_rhytmic_structure(self) + "--")
                            elif re.search(".*[ое]вать$", self.text, re.I):
                                if self.stress_position == self.syllables_count:
                                    return WordStructure(self.text[:-5] + "уете", get_rhytmic_structure(self)[:-2]
                                                         + "^--")
                                else:
                                    return WordStructure(self.text[:-5] + "уете", get_rhytmic_structure(self) + "-")
                            elif re.search(".*авать$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "ётe", get_rhytmic_structure(self) + "-")
                            elif re.search(".*скать$", self.text, re.I):
                                return WordStructure(self.text[:-5] + "щете", get_rhytmic_structure(self)[:-2] + "^--")
                            else:
                                return WordStructure(self.text[:-2] + "ете", get_rhytmic_structure(self) + "--")
                        elif re.search(".*ить", self.text, re.I):
                            if re.search(".*рить$", self.text, re.I):
                                return WordStructure(self.text[:-3] + "еете", get_rhytmic_structure(self) + "--")
                            else:
                                return WordStructure(self.text[:-3] + "ете", get_rhytmic_structure(self)[:-2] + "^--")
                        elif re.search(".*ять$", self.text, re.I):
                            if re.search(".*[ал]ять", self.text, re.I) and self.stress_position == self.syllables_count:
                                return WordStructure(self.text[:-2] + "ете", get_rhytmic_structure(self) + "--")
                            else:
                                return WordStructure(self.text[:-3] + "ете", get_rhytmic_structure(self) + "-")
                        elif re.search(".*оть$", self.text, re.I):
                            return WordStructure(self.text[:-3] + "ете", get_rhytmic_structure(self)[:-2] + "^--")
                        elif re.search(".*ыть$", self.text, re.I):
                            return WordStructure(self.text[:-3] + "оете", get_rhytmic_structure(self) + "--")
                    elif self.conjugation == 2:
                        if re.search(".*ить$", self.text, re.I):
                            if re.search(".*озить$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "зите", get_rhytmic_structure(self)[:-2] + "^--")
                            if re.search(".*зить$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "зите", get_rhytmic_structure(self)[:-2] + "-^-")
                            elif re.search(".*дить$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "дите", get_rhytmic_structure(self)[:-2] + "^--")
                            elif re.search(".*тить$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "тите", get_rhytmic_structure(self)[:-2] + "^--")
                            elif re.search(".*сить$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "сите", get_rhytmic_structure(self)[:-2] + "^--")
                            else:
                                return WordStructure(self.text[:-3] + "ите", get_rhytmic_structure(self)[:-2] + "^--")
                        elif re.search(".*еть$", self.text, re.I):
                            if re.search(".*теть$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "тите", get_rhytmic_structure(self)[:-2] + "^--")
                            elif re.search(".*деть$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "дите", get_rhytmic_structure(self)[:-2] + "^--")
                            elif re.search(".*петь$", self.text, re.I):
                                return WordStructure(self.text[:-3] + "ите", get_rhytmic_structure(self)[:-2] + "^--")
                            elif re.search(".*сеть$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "сите", get_rhytmic_structure(self)[:-2] + "^--")
                            else:
                                return WordStructure(self.text[:-3] + "ите", get_rhytmic_structure(self)[:-2] + "^--")
                        elif re.search(".*ать$", self.text, re.I):
                            if re.search(".*[жш]ать$", self.text, re.I):
                                return WordStructure(self.text[:-3] + "ите", get_rhytmic_structure(self)[:-2] + "^--")
                            elif re.search(".*гнать$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "оните", get_rhytmic_structure(self) + "--")
                            else:
                                return WordStructure(self.text[:-3] + "ите", get_rhytmic_structure(self)[:-2] + "^--")
                    else:
                        if re.search(".*есть$", self.text, re.I):
                            if self.text == "есть":
                                return WordStructure("едите", "-^-")
                            else:
                                return WordStructure(self.text[:-3] + "даете", "^--")
                        elif re.search(".*дать$", self.text, re.I):
                            return WordStructure(self.text[:-2] + "ете", get_rhytmic_structure(self)[:-2] + "^--")
                        elif re.search(".+быть$", self.text, re.I):
                            return WordStructure(self.text[:-2] + "ваете", get_rhytmic_structure(self)[:-2] + "^-")
                        elif self.text == "хотеть":
                            return WordStructure("хотите", "-^-")
                        elif self.text == "бежать":
                            return WordStructure("бежите", "-^-")
                        elif self.text == "чтить":
                            return WordStructure("чтите", "^-")
                        elif self.text == "ехать":
                            return WordStructure("едете", "^--")
                        elif self.text == "идти":
                            return WordStructure("идёте", "-^-")
                        elif self.text == "быть":
                            return WordStructure("есть", "^")

                elif person == 3:
                    if self.conjugation == 1:
                        if re.search(".*еть$", self.text, re.I):
                            if re.search(".*деть$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "дят", get_rhytmic_structure(self))
                            elif re.search(".*теть$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "тят", get_rhytmic_structure(self)[:-2] + "^-")
                            elif re.search(".*петь$", self.text, re.I):
                                return WordStructure(self.text[:-3] + "оют", get_rhytmic_structure(self)[:-1] + "-^")
                            else:
                                return WordStructure(self.text[:-2] + "ют", get_rhytmic_structure(self) + "-")
                        elif re.search(".*ать$", self.text, re.I):
                            if re.search(".*сать$", self.text, re.I) and self.stress_position == self.syllables_count:
                                return WordStructure(self.text[:-4] + "шут", get_rhytmic_structure(self)[:-2] + "^-")
                            elif re.search(".*певать$", self.text, re.I):
                                return WordStructure(self.text[:-2] + "ют", get_rhytmic_structure(self) + "-")
                            elif re.search(".*[ое]вать$", self.text, re.I):
                                if self.syllables_count == self.stress_position:
                                    return WordStructure(self.text[:-5] + "уют", get_rhytmic_structure(self)[:-2]
                                                         + "^-")
                                else:
                                    return WordStructure(self.text[:-5] + "уют", get_rhytmic_structure(self))
                            elif re.search(".*авать$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "ют", get_rhytmic_structure(self))
                            elif re.search(".*скать$", self.text, re.I):
                                return WordStructure(self.text[:-5] + "щут", get_rhytmic_structure(self)[:-2] + "^-")
                            else:
                                return WordStructure(self.text[:-2] + "ют", get_rhytmic_structure(self) + "-")
                        elif re.search(".*ить", self.text, re.I):
                            if re.search(".*рить$", self.text, re.I):
                                return WordStructure(self.text[:-3] + "еют", get_rhytmic_structure(self) + "-")
                            else:
                                return WordStructure(self.text[:-3] + "ют", get_rhytmic_structure(self)[:-2] + "^-")
                        elif re.search(".*ять$", self.text, re.I):
                            if re.search(".*[ал]ять", self.text, re.I) and self.stress_position == self.syllables_count:
                                return WordStructure(self.text[:-2] + "ют", get_rhytmic_structure(self) + "-")
                            else:
                                return WordStructure(self.text[:-3] + "ют", get_rhytmic_structure(self))
                        elif re.search(".*оть$", self.text, re.I):
                            return WordStructure(self.text[:-3] + "ят", get_rhytmic_structure(self)[:-2] + "^-")
                        elif re.search(".*ыть$", self.text, re.I):
                            return WordStructure(self.text[:-3] + "оют", get_rhytmic_structure(self) + "-")
                    elif self.conjugation == 2:
                        if re.search(".*ить$", self.text, re.I):
                            if re.search(".*азить$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "зят", get_rhytmic_structure(self)[:-2] + "-^")
                            if re.search(".*зить$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "зят", get_rhytmic_structure(self)[:-2] + "^-")
                            if re.search(".*дить$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "дят", get_rhytmic_structure(self)[:-2] + "^-")
                            elif re.search(".*тить$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "тят", get_rhytmic_structure(self)[:-2] + "^-")
                            elif re.search(".*сить$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "сят", get_rhytmic_structure(self)[:-2] + "^-")
                            else:
                                return WordStructure(self.text[:-3] + "ят", get_rhytmic_structure(self)[:-2] + "^-")
                        elif re.search(".*еть$", self.text, re.I):
                            if re.search(".*теть$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "тят", get_rhytmic_structure(self)[:-2] + "^-")
                            elif re.search(".*деть$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "дят", get_rhytmic_structure(self)[:-2] + "^-")
                            elif re.search(".*петь$", self.text, re.I):
                                return WordStructure(self.text[:-3] + "ят", get_rhytmic_structure(self)[:-2] + "^-")
                            elif re.search(".*сеть$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "сят", get_rhytmic_structure(self)[:-2] + "^-")
                            else:
                                return WordStructure(self.text[:-3] + "ят", get_rhytmic_structure(self)[:-2] + "^-")
                        elif re.search(".*ать$", self.text, re.I):
                            if re.search(".*[жш]ать$", self.text, re.I):
                                return WordStructure(self.text[:-3] + "ат", get_rhytmic_structure(self)[:-2] + "^-")
                            elif re.search(".*гнать$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "онят", get_rhytmic_structure(self) + "-")
                            else:
                                return WordStructure(self.text[:-3] + "ят", get_rhytmic_structure(self))
                    else:
                        if re.search(".*есть$", self.text, re.I):
                            if self.text == "есть":
                                return WordStructure("едят", "-^")
                            else:
                                return WordStructure(self.text[:-3] + "дают", get_rhytmic_structure(self))
                        elif re.search(".*дать$", self.text, re.I):
                            return WordStructure(self.text[:-2] + "ют", get_rhytmic_structure(self))
                        elif re.search(".+быть$", self.text, re.I):
                            return WordStructure(self.text[:-2] + "вают", get_rhytmic_structure(self))
                        elif self.text == "хотеть":
                            return WordStructure("хотят", "-^")
                        elif self.text == "бежать":
                            return WordStructure("бегут", "-^")
                        elif self.text == "чтить":
                            return WordStructure("чтят", "^")
                        elif self.text == "ехать":
                            return WordStructure("едут", "^-")
                        elif self.text == "идти":
                            return WordStructure("идут", "-^")
                        elif self.text == "быть":
                            return WordStructure("есть", "^")


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


def get_rhytmic_structure(word):
    rhytmic_structure = ""
    for x in range(word.syllables_count):
        if x == word.stress_position - 1:
            rhytmic_structure += "^"
        else:
            rhytmic_structure += "-"
    return rhytmic_structure


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
