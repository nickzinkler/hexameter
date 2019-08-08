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
            return 0
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

    def get_form(self, tense, person, gender_or_plural):
        if tense == "present":
            if gender_or_plural != "plural":
                if person == 1:
                    if self.conjugation == 1:
                        if re.search(".*еть$", self.text, re.I):
                            if re.search(".*деть$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "жу", "^--")
                            elif re.search(".*теть$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "чу", "^--")
                            elif re.search(".*петь$", self.text, re.I):
                                return WordStructure(self.text[:-3] + "ою", "^--")
                            else:
                                return WordStructure(self.text[:-2] + "ю", "^--")
                        elif re.search(".*ать$", self.text, re.I):
                            if re.search(".*сать$", self.text, re.I) and self.stress_position == self.syllables_count:
                                return WordStructure(self.text[:-4] + "шу", "^--")
                            elif re.search(".*певать$", self.text, re.I):
                                return WordStructure(self.text[:-2] + "ю", "^--")
                            elif re.search(".*[ое]вать$", self.text, re.I):
                                return WordStructure(self.text[:-5] + "ую", "^--")
                            elif re.search(".*авать$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "ю", "^--")
                            elif re.search(".*скать$", self.text, re.I):
                                return WordStructure(self.text[:-5] + "щу", "^--")
                            else:
                                return WordStructure(self.text[:-2] + "ю", "^--")
                        elif re.search(".*ить", self.text, re.I):
                            if re.search(".*рить$", self.text, re.I):
                                return WordStructure(self.text[:-3] + "ею", "^--")
                            else:
                                return WordStructure(self.text[:-3] + "ю", "^--")
                        elif re.search(".*ять$", self.text, re.I):
                            if re.search(".*[ал]ять", self.text, re.I) and self.stress_position == self.syllables_count:
                                return WordStructure(self.text[:-2] + "ю", "^--")
                            else:
                                return WordStructure(self.text[:-3] + "ю", "^--")
                        elif re.search(".*оть$", self.text, re.I):
                            return WordStructure(self.text[:-3] + "ю", "^--")
                        elif re.search(".*ыть$", self.text, re.I):
                            return WordStructure(self.text[:-3] + "ою", "^--")
                    elif self.conjugation == 2:
                        if re.search(".*ить$", self.text, re.I):
                            if re.search(".*зить$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "жу", "^--")
                            elif re.search(".*дить$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "жу", "^--")
                            elif re.search(".*тить$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "чу", "^--")
                            elif re.search(".*сить$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "шу", "^--")
                            else:
                                return WordStructure(self.text[:-3] + "ю", "^--")
                        elif re.search(".*еть$", self.text, re.I):
                            if re.search(".*теть$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "чу", "^--")
                            elif re.search(".*деть$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "жу", "^--")
                            elif re.search(".*петь$", self.text, re.I):
                                return WordStructure(self.text[:-3] + "лю", "^--")
                            elif re.search(".*сеть$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "шу", "^--")
                            else:
                                return WordStructure(self.text[:-3] + "ю", "^--")
                        elif re.search(".*ать$", self.text, re.I):
                            if re.search(".*[жш]ать$", self.text, re.I):
                                return WordStructure(self.text[:-3] + "у", "^--")
                            elif re.search(".*гнать$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "оню", "^--")
                            else:
                                return WordStructure(self.text[:-3] + "ю", "^--")
                    else:
                        if re.search(".*есть$", self.text, re.I):
                            return WordStructure(self.text[:-3] + "даю", "^--")
                        elif re.search(".*дать$", self.text, re.I):
                            return WordStructure(self.text[:-2] + "ю", "^--")
                        elif re.search(".+быть$", self.text, re.I):
                            return WordStructure(self.text[:-2] + "ваю", "^--")
                        elif self.text == "хотеть":
                            return WordStructure("хочу", "-^")
                        elif self.text == "бежать":
                            return WordStructure("бегу", "-^")
                        elif self.text == "чтить":
                            return WordStructure("чту", "^")
                        elif self.text == "есть":
                            return WordStructure("ем", "^")
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
                                return WordStructure(self.text[:-4] + "дишь", "^--")
                            elif re.search(".*теть$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "тишь", "^--")
                            elif re.search(".*петь$", self.text, re.I):
                                return WordStructure(self.text[:-3] + "оёшь", "^--")
                            else:
                                return WordStructure(self.text[:-2] + "ешь", "^--")
                        elif re.search(".*ать$", self.text, re.I):
                            if re.search(".*сать$", self.text, re.I) and self.stress_position == self.syllables_count:
                                return WordStructure(self.text[:-4] + "шешь", "^--")
                            elif re.search(".*певать$", self.text, re.I):
                                return WordStructure(self.text[:-2] + "ешь", "^--")
                            elif re.search(".*[ое]вать$", self.text, re.I):
                                return WordStructure(self.text[:-5] + "уешь", "^--")
                            elif re.search(".*авать$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "ёшь", "^--")
                            elif re.search(".*скать$", self.text, re.I):
                                return WordStructure(self.text[:-5] + "щешь", "^--")
                            else:
                                return WordStructure(self.text[:-2] + "ешь", "^--")
                        elif re.search(".*ить", self.text, re.I):
                            if re.search(".*рить$", self.text, re.I):
                                return WordStructure(self.text[:-3] + "еешь", "^--")
                            else:
                                return WordStructure(self.text[:-3] + "ешь", "^--")
                        elif re.search(".*ять$", self.text, re.I):
                            if re.search(".*[ал]ять", self.text, re.I) and self.stress_position == self.syllables_count:
                                return WordStructure(self.text[:-2] + "ешь", "^--")
                            else:
                                return WordStructure(self.text[:-3] + "ешь", "^--")
                        elif re.search(".*оть$", self.text, re.I):
                            return WordStructure(self.text[:-3] + "ешь", "^--")
                        elif re.search(".*ыть$", self.text, re.I):
                            return WordStructure(self.text[:-3] + "оешь", "^--")
                    elif self.conjugation == 2:
                        if re.search(".*ить$", self.text, re.I):
                            if re.search(".*зить$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "зишь", "^--")
                            if re.search(".*дить$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "дишь", "^--")
                            elif re.search(".*тить$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "тишь", "^--")
                            elif re.search(".*сить$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "сишь", "^--")
                            else:
                                return WordStructure(self.text[:-3] + "ишь", "^--")
                        elif re.search(".*еть$", self.text, re.I):
                            if re.search(".*теть$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "тишь", "^--")
                            elif re.search(".*деть$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "дишь", "^--")
                            elif re.search(".*петь$", self.text, re.I):
                                return WordStructure(self.text[:-3] + "ишь", "^--")
                            elif re.search(".*сеть$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "сишь", "^--")
                            else:
                                return WordStructure(self.text[:-3] + "ишь", "^--")
                        elif re.search(".*ать$", self.text, re.I):
                            if re.search(".*[жш]ать$", self.text, re.I):
                                return WordStructure(self.text[:-3] + "ишь", "^--")
                            elif re.search(".*гнать$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "онишь", "^--")
                            else:
                                return WordStructure(self.text[:-3] + "ишь", "^--")
                    else:
                        if re.search(".*есть$", self.text, re.I):
                            return WordStructure(self.text[:-3] + "даешь", "^--")
                        elif re.search(".*дать$", self.text, re.I):
                            return WordStructure(self.text[:-2] + "ёшь", "^--")
                        elif re.search(".+быть$", self.text, re.I):
                            return WordStructure(self.text[:-2] + "ваешь", "^--")
                        elif self.text == "хотеть":
                            return WordStructure("хочешь", "-^")
                        elif self.text == "бежать":
                            return WordStructure("бежишь", "-^")
                        elif self.text == "чтить":
                            return WordStructure("чтишь", "^")
                        elif self.text == "есть":
                            return WordStructure("ешь", "^")
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
                                return WordStructure(self.text[:-4] + "дит", "^--")
                            elif re.search(".*теть$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "тит", "^--")
                            elif re.search(".*петь$", self.text, re.I):
                                return WordStructure(self.text[:-3] + "оёт", "^--")
                            else:
                                return WordStructure(self.text[:-2] + "ет", "^--")
                        elif re.search(".*ать$", self.text, re.I):
                            if re.search(".*сать$", self.text, re.I) and self.stress_position == self.syllables_count:
                                return WordStructure(self.text[:-4] + "шет", "^--")
                            elif re.search(".*певать$", self.text, re.I):
                                return WordStructure(self.text[:-2] + "ет", "^--")
                            elif re.search(".*[ое]вать$", self.text, re.I):
                                return WordStructure(self.text[:-5] + "ует", "^--")
                            elif re.search(".*авать$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "ёт", "^--")
                            elif re.search(".*скать$", self.text, re.I):
                                return WordStructure(self.text[:-5] + "щет", "^--")
                            else:
                                return WordStructure(self.text[:-2] + "ет", "^--")
                        elif re.search(".*ить", self.text, re.I):
                            if re.search(".*рить$", self.text, re.I):
                                return WordStructure(self.text[:-3] + "еет", "^--")
                            else:
                                return WordStructure(self.text[:-3] + "ет", "^--")
                        elif re.search(".*ять$", self.text, re.I):
                            if re.search(".*[ал]ять", self.text, re.I) and self.stress_position == self.syllables_count:
                                return WordStructure(self.text[:-2] + "ет", "^--")
                            else:
                                return WordStructure(self.text[:-3] + "ет", "^--")
                        elif re.search(".*оть$", self.text, re.I):
                            return WordStructure(self.text[:-3] + "ет", "^--")
                        elif re.search(".*ыть$", self.text, re.I):
                            return WordStructure(self.text[:-3] + "оет", "^--")
                    elif self.conjugation == 2:
                        if re.search(".*ить$", self.text, re.I):
                            if re.search(".*зить$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "зит", "^--")
                            if re.search(".*дить$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "дит", "^--")
                            elif re.search(".*тить$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "тит", "^--")
                            elif re.search(".*сить$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "сит", "^--")
                            else:
                                return WordStructure(self.text[:-3] + "ит", "^--")
                        elif re.search(".*еть$", self.text, re.I):
                            if re.search(".*теть$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "тит", "^--")
                            elif re.search(".*деть$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "дит", "^--")
                            elif re.search(".*петь$", self.text, re.I):
                                return WordStructure(self.text[:-3] + "ит", "^--")
                            elif re.search(".*сеть$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "сит", "^--")
                            else:
                                return WordStructure(self.text[:-3] + "ит", "^--")
                        elif re.search(".*ать$", self.text, re.I):
                            if re.search(".*[жш]ать$", self.text, re.I):
                                return WordStructure(self.text[:-3] + "ит", "^--")
                            elif re.search(".*гнать$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "онит", "^--")
                            else:
                                return WordStructure(self.text[:-3] + "ит", "^--")
                    else:
                        if re.search(".*есть$", self.text, re.I):
                            return WordStructure(self.text[:-3] + "дает", "^--")
                        elif re.search(".*дать$", self.text, re.I):
                            return WordStructure(self.text[:-2] + "ёт", "^--")
                        elif re.search(".+быть$", self.text, re.I):
                            return WordStructure(self.text[:-2] + "вает", "^--")
                        elif self.text == "хотеть":
                            return WordStructure("хочет", "-^")
                        elif self.text == "бежать":
                            return WordStructure("бежит", "-^")
                        elif self.text == "чтить":
                            return WordStructure("чтит", "^")
                        elif self.text == "есть":
                            return WordStructure("ест", "^")
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
                                return WordStructure(self.text[:-4] + "дим", "^--")
                            elif re.search(".*теть$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "тим", "^--")
                            elif re.search(".*петь$", self.text, re.I):
                                return WordStructure(self.text[:-3] + "оём", "^--")
                            else:
                                return WordStructure(self.text[:-2] + "ем", "^--")
                        elif re.search(".*ать$", self.text, re.I):
                            if re.search(".*сать$", self.text, re.I) and self.stress_position == self.syllables_count:
                                return WordStructure(self.text[:-4] + "шем", "^--")
                            elif re.search(".*певать$", self.text, re.I):
                                return WordStructure(self.text[:-2] + "ем", "^--")
                            elif re.search(".*[ое]вать$", self.text, re.I):
                                return WordStructure(self.text[:-5] + "уем", "^--")
                            elif re.search(".*авать$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "ём", "^--")
                            elif re.search(".*скать$", self.text, re.I):
                                return WordStructure(self.text[:-5] + "щем", "^--")
                            else:
                                return WordStructure(self.text[:-2] + "ем", "^--")
                        elif re.search(".*ить", self.text, re.I):
                            if re.search(".*рить$", self.text, re.I):
                                return WordStructure(self.text[:-3] + "еем", "^--")
                            else:
                                return WordStructure(self.text[:-3] + "ем", "^--")
                        elif re.search(".*ять$", self.text, re.I):
                            if re.search(".*[ал]ять", self.text, re.I) and self.stress_position == self.syllables_count:
                                return WordStructure(self.text[:-2] + "ем", "^--")
                            else:
                                return WordStructure(self.text[:-3] + "ем", "^--")
                        elif re.search(".*оть$", self.text, re.I):
                            return WordStructure(self.text[:-3] + "ем", "^--")
                        elif re.search(".*ыть$", self.text, re.I):
                            return WordStructure(self.text[:-3] + "оем", "^--")
                    elif self.conjugation == 2:
                        if re.search(".*ить$", self.text, re.I):
                            if re.search(".*зить$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "зим", "^--")
                            if re.search(".*дить$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "дим", "^--")
                            elif re.search(".*тить$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "тим", "^--")
                            elif re.search(".*сить$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "сим", "^--")
                            else:
                                return WordStructure(self.text[:-3] + "им", "^--")
                        elif re.search(".*еть$", self.text, re.I):
                            if re.search(".*теть$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "тим", "^--")
                            elif re.search(".*деть$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "дим", "^--")
                            elif re.search(".*петь$", self.text, re.I):
                                return WordStructure(self.text[:-3] + "им", "^--")
                            elif re.search(".*сеть$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "сим", "^--")
                            else:
                                return WordStructure(self.text[:-3] + "им", "^--")
                        elif re.search(".*ать$", self.text, re.I):
                            if re.search(".*[жш]ать$", self.text, re.I):
                                return WordStructure(self.text[:-3] + "им", "^--")
                            elif re.search(".*гнать$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "оним", "^--")
                            else:
                                return WordStructure(self.text[:-3] + "им", "^--")
                    else:
                        if re.search(".*есть$", self.text, re.I):
                            return WordStructure(self.text[:-3] + "даем", "^--")
                        elif re.search(".*дать$", self.text, re.I):
                            return WordStructure(self.text[:-2] + "ём", "^--")
                        elif re.search(".+быть$", self.text, re.I):
                            return WordStructure(self.text[:-2] + "ваем", "^--")
                        elif self.text == "хотеть":
                            return WordStructure("хотим", "-^")
                        elif self.text == "бежать":
                            return WordStructure("бежим", "-^")
                        elif self.text == "чтить":
                            return WordStructure("чтим", "^")
                        elif self.text == "есть":
                            return WordStructure("едим", "^")
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
                                return WordStructure(self.text[:-4] + "дите", "^--")
                            elif re.search(".*теть$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "тите", "^--")
                            elif re.search(".*петь$", self.text, re.I):
                                return WordStructure(self.text[:-3] + "оёте", "^--")
                            else:
                                return WordStructure(self.text[:-2] + "ете", "^--")
                        elif re.search(".*ать$", self.text, re.I):
                            if re.search(".*сать$", self.text, re.I) and self.stress_position == self.syllables_count:
                                return WordStructure(self.text[:-4] + "шете", "^--")
                            elif re.search(".*певать$", self.text, re.I):
                                return WordStructure(self.text[:-2] + "ете", "^--")
                            elif re.search(".*[ое]вать$", self.text, re.I):
                                return WordStructure(self.text[:-5] + "уете", "^--")
                            elif re.search(".*авать$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "ёт", "^--")
                            elif re.search(".*скать$", self.text, re.I):
                                return WordStructure(self.text[:-5] + "щете", "^--")
                            else:
                                return WordStructure(self.text[:-2] + "ете", "^--")
                        elif re.search(".*ить", self.text, re.I):
                            if re.search(".*рить$", self.text, re.I):
                                return WordStructure(self.text[:-3] + "еете", "^--")
                            else:
                                return WordStructure(self.text[:-3] + "ете", "^--")
                        elif re.search(".*ять$", self.text, re.I):
                            if re.search(".*[ал]ять", self.text, re.I) and self.stress_position == self.syllables_count:
                                return WordStructure(self.text[:-2] + "ете", "^--")
                            else:
                                return WordStructure(self.text[:-3] + "ете", "^--")
                        elif re.search(".*оть$", self.text, re.I):
                            return WordStructure(self.text[:-3] + "ете", "^--")
                        elif re.search(".*ыть$", self.text, re.I):
                            return WordStructure(self.text[:-3] + "оете", "^--")
                    elif self.conjugation == 2:
                        if re.search(".*ить$", self.text, re.I):
                            if re.search(".*зить$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "зите", "^--")
                            if re.search(".*дить$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "дите", "^--")
                            elif re.search(".*тить$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "тите", "^--")
                            elif re.search(".*сить$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "сите", "^--")
                            else:
                                return WordStructure(self.text[:-3] + "ите", "^--")
                        elif re.search(".*еть$", self.text, re.I):
                            if re.search(".*теть$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "тите", "^--")
                            elif re.search(".*деть$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "дите", "^--")
                            elif re.search(".*петь$", self.text, re.I):
                                return WordStructure(self.text[:-3] + "ите", "^--")
                            elif re.search(".*сеть$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "сите", "^--")
                            else:
                                return WordStructure(self.text[:-3] + "ите", "^--")
                        elif re.search(".*ать$", self.text, re.I):
                            if re.search(".*[жш]ать$", self.text, re.I):
                                return WordStructure(self.text[:-3] + "ите", "^--")
                            elif re.search(".*гнать$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "оните", "^--")
                            else:
                                return WordStructure(self.text[:-3] + "ите", "^--")
                    else:
                        if re.search(".*есть$", self.text, re.I):
                            return WordStructure(self.text[:-3] + "даетн", "^--")
                        elif re.search(".*дать$", self.text, re.I):
                            return WordStructure(self.text[:-2] + "ётн", "^--")
                        elif re.search(".+быть$", self.text, re.I):
                            return WordStructure(self.text[:-2] + "ваетн", "^--")
                        elif self.text == "хотеть":
                            return WordStructure("хотите", "-^")
                        elif self.text == "бежать":
                            return WordStructure("бежите", "-^")
                        elif self.text == "чтить":
                            return WordStructure("чтите", "^")
                        elif self.text == "есть":
                            return WordStructure("едите", "^")
                        elif self.text == "ехать":
                            return WordStructure("едете", "^-")
                        elif self.text == "идти":
                            return WordStructure("идёте", "-^")
                        elif self.text == "быть":
                            return WordStructure("есть", "^")
                        
                elif person == 3:
                    if self.conjugation == 1:
                        if re.search(".*еть$", self.text, re.I):
                            if re.search(".*деть$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "дят", "^--")
                            elif re.search(".*теть$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "тят", "^--")
                            elif re.search(".*петь$", self.text, re.I):
                                return WordStructure(self.text[:-3] + "оют", "^--")
                            else:
                                return WordStructure(self.text[:-2] + "ят", "^--")
                        elif re.search(".*ать$", self.text, re.I):
                            if re.search(".*сать$", self.text, re.I) and self.stress_position == self.syllables_count:
                                return WordStructure(self.text[:-4] + "шут", "^--")
                            elif re.search(".*певать$", self.text, re.I):
                                return WordStructure(self.text[:-2] + "ют", "^--")
                            elif re.search(".*[ое]вать$", self.text, re.I):
                                return WordStructure(self.text[:-5] + "уют", "^--")
                            elif re.search(".*авать$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "ют", "^--")
                            elif re.search(".*скать$", self.text, re.I):
                                return WordStructure(self.text[:-5] + "щут", "^--")
                            else:
                                return WordStructure(self.text[:-2] + "ют", "^--")
                        elif re.search(".*ить", self.text, re.I):
                            if re.search(".*рить$", self.text, re.I):
                                return WordStructure(self.text[:-3] + "еют", "^--")
                            else:
                                return WordStructure(self.text[:-3] + "ют", "^--")
                        elif re.search(".*ять$", self.text, re.I):
                            if re.search(".*[ал]ять", self.text, re.I) and self.stress_position == self.syllables_count:
                                return WordStructure(self.text[:-2] + "ют", "^--")
                            else:
                                return WordStructure(self.text[:-3] + "ют", "^--")
                        elif re.search(".*оть$", self.text, re.I):
                            return WordStructure(self.text[:-3] + "ят", "^--")
                        elif re.search(".*ыть$", self.text, re.I):
                            return WordStructure(self.text[:-3] + "оют", "^--")
                    elif self.conjugation == 2:
                        if re.search(".*ить$", self.text, re.I):
                            if re.search(".*зить$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "зят", "^--")
                            if re.search(".*дить$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "дят", "^--")
                            elif re.search(".*тить$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "тят", "^--")
                            elif re.search(".*сить$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "сят", "^--")
                            else:
                                return WordStructure(self.text[:-3] + "ят", "^--")
                        elif re.search(".*еть$", self.text, re.I):
                            if re.search(".*теть$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "тят", "^--")
                            elif re.search(".*деть$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "дят", "^--")
                            elif re.search(".*петь$", self.text, re.I):
                                return WordStructure(self.text[:-3] + "ят", "^--")
                            elif re.search(".*сеть$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "сят", "^--")
                            else:
                                return WordStructure(self.text[:-3] + "ят", "^--")
                        elif re.search(".*ать$", self.text, re.I):
                            if re.search(".*[жш]ать$", self.text, re.I):
                                return WordStructure(self.text[:-3] + "ят", "^--")
                            elif re.search(".*гнать$", self.text, re.I):
                                return WordStructure(self.text[:-4] + "онят", "^--")
                            else:
                                return WordStructure(self.text[:-3] + "ят", "^--")
                    else:
                        if re.search(".*есть$", self.text, re.I):
                            return WordStructure(self.text[:-3] + "дают", "^--")
                        elif re.search(".*дать$", self.text, re.I):
                            return WordStructure(self.text[:-2] + "ят", "^--")
                        elif re.search(".+быть$", self.text, re.I):
                            return WordStructure(self.text[:-2] + "вают", "^--")
                        elif self.text == "хотеть":
                            return WordStructure("хотят", "-^")
                        elif self.text == "бежать":
                            return WordStructure("бегут", "-^")
                        elif self.text == "чтить":
                            return WordStructure("чтят", "^")
                        elif self.text == "есть":
                            return WordStructure("едяь", "^")
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
         Name("Николай", 3, "male"),
         Name("Камисса", 2, "female"),
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


text1mod = "Гр^озно взглян^ув на нег^о, возраз^ил [Hero:N-E,n]"
text2mod = "М^олча ты ст^ой, [Hero:N,n], моем^у повин^уясь сов^ету"
text3mod = "Т^ак [Hero:N,n] размышл^ял, и ем^у показ^алося л^учше"
text4mod = "В^ызвать [Hero:N,a]. Наш^ёл он гер^оя, в друж^инах посл^едних"
text5mod = "Пр^адзно сто^ящего: гн^ев он всегд^ашний пит^ал на [Hero:N,p]"
text6mod = "Ст^ав перед н^им, [Hero:N,n] устремл^яет крыл^атые р^ечи:"
text7mod = "[Hero:N-E,n] - тро^ян повел^итель, и ^если о бл^ижних"
text8mod = "Т^ы сострад^аешь, теб^е заступ^иться за бл^ижнего д^олжно"
text9mod = "Сл^едуй за мн^ой, защит^им [Hero:P,a]; теб^я он, почт^енный,"
text10mod = "Б^удучи з^ятем, восп^итывал в с^обственном д^оме."


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
         Verb("делать", 2, False),
         Verb("низвергать", 2, False),
         Verb("распростирать", 3, False),
         Verb("воздвигать", 3, False),
         Verb("пылать", 3, False),
         Verb("приходить", 3, False),
         Verb("умолять", 3, False),
         Verb("искупать", 3, False),
         Verb("приносить", 3, False),
         Verb("помогать", 3, False),
         Verb("искать", 3, False),
         Verb("разрушать", 3, False),
         Verb("возвращать", 3, False),
         Verb("принимать", 3, False),
         Verb("разить", 3, False),
         Verb("оказывать", 3, False)]

for y in verbs:
     print(y.get_form("present", 1, "male").text
           + " " + y.get_form("present", 2, "male").text
           + " " + y.get_form("present", 3, "male").text
           + " " + y.get_form("present", 1, "plural").text
           + " " + y.get_form("present", 2, "plural").text
           + " " + y.get_form("present", 3, "plural").text)

# print("Первое спряжение:")
# verbs = [Verb("желать", 2, True),
#          Verb("рисовать", 3, True),
#          Verb("доставать", 2, True),
#          Verb("писать", 2, True),
#          Verb("подсказывать", 2, True),
#          Verb("белеть", 2, True),
#          Verb("читать", 2, True),
#          Verb("брить", 2, True),
#          Verb("паять", 2, True),
#          Verb("краснеть", 2, True),
#          Verb("открывать", 2, True),
#          Verb("таять", 1, True),
#          Verb("бороться", 2, True),
#          Verb("сеять", 2, True),
#          Verb("танцевать", 2, True),
#          Verb("петь", 2, True),
#          Verb("сидеть", 2, True),
#          Verb("копать", 2, True),
#          Verb("летать", 2, True),
#          Verb("мешать", 2, True),
#          Verb("рыть", 2, True),
#          Verb("печатать", 2, True),
#          Verb("копировать", 2, True),
#          Verb("срывать", 2, True),
#          Verb("колоть", 2, True),
#          Verb("стелить", 2, True)]
# for y in verbs:
#     print(y.get_form("present", 1, "male").text
#           + " " + y.get_form("present", 2, "male").text
#           + " " + y.get_form("present", 3, "male").text
#           + " " + y.get_form("present", 1, "plural").text
#           + " " + y.get_form("present", 2, "plural").text
#           + " " + y.get_form("present", 3, "plural").text)
#
# print("\nВторое спряжение:")
# verbs = [Verb("возить", 2, False),
#          Verb("пилить", 3, False),
#          Verb("тратить", 2, False),
#          Verb("смотреть", 2, False),
#          Verb("видеть", 2, False),
#          Verb("терпеть", 2, False),
#          Verb("ненавидеть", 2, False),
#          Verb("обидеть", 2, True),
#          Verb("зависеть", 2, False),
#          Verb("вертеть", 2, False),
#          Verb("гнать", 2, False),
#          Verb("держать", 2, False),
#          Verb("слышать", 2, False),
#          Verb("дышать", 2, False)]
# for y in verbs:
#     print(y.get_form("present", 1, "male").text
#           + " " + y.get_form("present", 2, "male").text
#           + " " + y.get_form("present", 3, "male").text
#           + " " + y.get_form("present", 1, "plural").text
#           + " " + y.get_form("present", 2, "plural").text
#           + " " + y.get_form("present", 3, "plural").text)
#
# print("\nИзолированные глаголы:")
# verbs = [Verb("хотеть", 2, False),
#          Verb("бежать", 3, False),
#          Verb("чтить", 2, False),
#          Verb("надоесть", 2, False),
#          Verb("дать", 2, False),
#          Verb("есть", 1, False),
#          Verb("создать", 2, False),
#          Verb("добыть", 2, False),
#          Verb("забыть", 2, False),
#          Verb("ехать", 2, False),
#          Verb("идти", 2, False)]
# for y in verbs:
#     print(y.get_form("present", 1, "male").text
#           + " " + y.get_form("present", 2, "male").text
#           + " " + y.get_form("present", 3, "male").text
#           + " " + y.get_form("present", 1, "plural").text
#           + " " + y.get_form("present", 2, "plural").text
#           + " " + y.get_form("present", 3, "plural").text
#           )