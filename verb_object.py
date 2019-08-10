import re
from word_object import Word, WordStructure, get_rhytmic_structure


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

    def get_form(self, tense, person, gender, plural):
        if tense == "present":
            if not plural:
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
        elif tense == "past":
            if not plural:
                if self.text == "идти":
                    if gender == "male":
                        return WordStructure("шёл", "^")
                    elif gender == "female":
                        return WordStructure("шла", "^")
                    else:
                        return WordStructure("шло", "^")
                elif re.search(".*сть$", self.text, re.I):
                    if gender == "male":
                        return WordStructure(self.text[:-3] + "л", get_rhytmic_structure(self))
                    elif gender == "female":
                        return WordStructure(self.text[:-3] + "ла", get_rhytmic_structure(self) + "-")
                    else:
                        return WordStructure(self.text[:-3] + "ло", get_rhytmic_structure(self) + "-")
                else:
                    if gender == "male":
                        return WordStructure(self.text[:-2] + "л", get_rhytmic_structure(self))
                    elif gender == "female":
                        return WordStructure(self.text[:-2] + "ла", get_rhytmic_structure(self) + "-")
                    else:
                        return WordStructure(self.text[:-2] + "ло", get_rhytmic_structure(self) + "-")
            else:
                if self.text == "идти":
                    return WordStructure("шли", "^")
                elif re.search(".*сть$", self.text, re.I):
                    return WordStructure(self.text[:-3] + "ли", get_rhytmic_structure(self) + "-")
                else:
                    return WordStructure(self.text[:-2] + "ли", get_rhytmic_structure(self) + "-")
