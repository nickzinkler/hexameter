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
        self.reflexive = re.search(".*с[яь]$", self.text, re.I)

    def get_conjugation(self):
        if re.search(".*(есть)|(дать)|(быть)($|с[ья])", self.text, re.I):
            return 3
        for x in ["хотеть", "бежать", "чтить", "ехать", "идти"]:
            if x == self.text:
                return 3
        for x in ["брить", "стелить"]:
            if re.search(x + "($|с[ья])", self.text, re.I):
                return 1
        for x in ["смотреть", "видеть", "ненавидеть", "зависеть", "терпеть",
                  "обидеть", "вертеть", "слышать", "держать", "гнать", "дышать"]:
            if re.search(x + "($|с[ья]$)", self.text, re.I):
                return 2
        if re.search("ить($|с[ья])", self.text, re.I):
            return 2
        return 1

    def get_form(self, tense, person, gender, plural):
        if tense == "present":
            if not plural:
                if person == 1:
                    if self.reflexive:
                        if self.conjugation == 1:
                            if re.search(".*еться$", self.text, re.I):
                                if re.search(".*деться$", self.text, re.I):
                                    return WordStructure(self.text[:-4] + "юсь", get_rhytmic_structure(self)[:-1])
                                elif re.search(".*теться$", self.text, re.I):
                                    return WordStructure(self.text[:-6] + "чусь", get_rhytmic_structure(self)[:-1])
                                elif re.search(".*петься$", self.text, re.I):
                                    return WordStructure(self.text[:-3] + "юсь", get_rhytmic_structure(self)[:-2] + "-^")
                                else:
                                    return WordStructure(self.text[:-2] + "юсь", get_rhytmic_structure(self)[:-1])
                            elif re.search(".*аться$", self.text, re.I):
                                if re.search(".*саться$", self.text, re.I) \
                                        and self.stress_position + 1 == self.syllables_count:
                                    return WordStructure(self.text[:-6] + "шусь", get_rhytmic_structure(self)[:-1])
                                elif re.search(".*певаться$", self.text, re.I):
                                    return WordStructure(self.text[:-2] + "юсь", get_rhytmic_structure(self) + "-")
                                elif re.search(".*[ое]ваться$", self.text, re.I):
                                    if re.search(".*оваться$", self.text, re.I) \
                                            and self.stress_position + 1 == self.syllables_count:
                                        return WordStructure(self.text[:-7] + "уюсь",
                                                             get_rhytmic_structure(self)[:-3] + "^-")
                                    elif re.search(".*еваться$", self.text, re.I) \
                                            and self.stress_position + 1 == self.syllables_count:
                                        return WordStructure(self.text[:-4] + "юсь",
                                                             get_rhytmic_structure(self)[:-2] + "^-")
                                    else:
                                        return WordStructure(self.text[:-4] + "юсь", get_rhytmic_structure(self)[:-1])
                                elif re.search(".*аваться$", self.text, re.I):
                                    return WordStructure(self.text[:-4] + "юсь", get_rhytmic_structure(self)[:-1])
                                elif re.search(".*скаться$", self.text, re.I):
                                    return WordStructure(self.text[:-5] + "юсь", get_rhytmic_structure(self)[:-1])
                                else:
                                    return WordStructure(self.text[:-4] + "юсь", get_rhytmic_structure(self))
                            elif re.search(".*иться", self.text, re.I):
                                if re.search(".*риться$", self.text, re.I):
                                    return WordStructure(self.text[:-5] + "еюсь", get_rhytmic_structure(self))
                                else:
                                    return WordStructure(self.text[:-3] + "юсь", get_rhytmic_structure(self)[:-1])
                            elif re.search(".*яться$", self.text, re.I):
                                if re.search(".*[ал]яться$", self.text, re.I) \
                                        and self.stress_position == self.syllables_count:
                                    return WordStructure(self.text[:-3] + "юсь", get_rhytmic_structure(self))
                                elif re.search(".*еяться$", self.text, re.I):
                                    return WordStructure(self.text[:-5] + "юсь", get_rhytmic_structure(self)[:-1])
                                else:
                                    return WordStructure(self.text[:-4] + "юсь", get_rhytmic_structure(self))
                            elif re.search(".*оться$", self.text, re.I):
                                return WordStructure(self.text[:-3] + "юсь", get_rhytmic_structure(self)[:-1])
                            elif re.search(".*ыться$", self.text, re.I):
                                return WordStructure(self.text[:-3] + "оюсь", get_rhytmic_structure(self))
                        elif self.conjugation == 2:
                            if re.search(".*иться$", self.text, re.I):
                                if re.search(".*зиться$", self.text, re.I):
                                    return WordStructure(self.text[:-6] + "жусь", get_rhytmic_structure(self)[:-1])
                                elif re.search(".*диться$", self.text, re.I):
                                    return WordStructure(self.text[:-6] + "жусь", get_rhytmic_structure(self)[:-1])
                                elif re.search(".*титься$", self.text, re.I):
                                    return WordStructure(self.text[:-6] + "чусь", get_rhytmic_structure(self)[:-1])
                                elif re.search(".*ситься$", self.text, re.I):
                                    return WordStructure(self.text[:-6] + "шусь", get_rhytmic_structure(self)[:-1])
                                else:
                                    return WordStructure(self.text[:-5] + "юсь", get_rhytmic_structure(self)[:-1])
                            elif re.search(".*еться$", self.text, re.I):
                                if re.search(".*теться$", self.text, re.I):
                                    return WordStructure(self.text[:-6] + "чусь", get_rhytmic_structure(self)[:-1])
                                elif re.search(".*деться$", self.text, re.I):
                                    return WordStructure(self.text[:-4] + "жусь", get_rhytmic_structure(self)[:-1])
                                elif re.search(".*петься$", self.text, re.I):
                                    return WordStructure(self.text[:-5] + "люсь", get_rhytmic_structure(self)[:-1])
                                elif re.search(".*сеться$", self.text, re.I):
                                    return WordStructure(self.text[:-4] + "шусь", get_rhytmic_structure(self)[:-1])
                                else:
                                    return WordStructure(self.text[:-3] + "юсь", get_rhytmic_structure(self)[:-1])
                            elif re.search(".*ать$", self.text, re.I):
                                if re.search(".*[жш]ать$", self.text, re.I):
                                    return WordStructure(self.text[:-3] + "у", get_rhytmic_structure(self)[:-1])
                                elif re.search(".*гнать$", self.text, re.I):
                                    return WordStructure(self.text[:-4] + "оню",
                                                         get_rhytmic_structure(self)[:-1] + "-^")
                                else:
                                    return WordStructure(self.text[:-3] + "ю", get_rhytmic_structure(self)[:-1])
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
                    else:
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
                                if re.search(".*сать$", self.text, re.I) \
                                        and self.stress_position == self.syllables_count:
                                    return WordStructure(self.text[:-4] + "шу", get_rhytmic_structure(self))
                                elif re.search(".*певать$", self.text, re.I):
                                    return WordStructure(self.text[:-2] + "ю", get_rhytmic_structure(self) + "-")
                                elif re.search(".*[ое]вать$", self.text, re.I):
                                    if self.stress_position == self.syllables_count:
                                        return WordStructure(self.text[:-5] + "ую",
                                                             get_rhytmic_structure(self)[:-2] + "^-")
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
                                if re.search(".*[ал]ять$", self.text, re.I) \
                                        and self.stress_position == self.syllables_count:
                                    return WordStructure(self.text[:-2] + "ю", get_rhytmic_structure(self) + "-")
                                else:
                                    return WordStructure(self.text[:-3] + "ю", get_rhytmic_structure(self) + "-")
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
                                    return WordStructure(self.text[:-4] + "оню",
                                                         get_rhytmic_structure(self)[:-1] + "-^")
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
                    if self.reflexive:
                        if self.conjugation == 1:
                            if re.search(".*еться$", self.text, re.I):
                                if re.search(".*деться$", self.text, re.I):
                                    return WordStructure(self.text[:-4] + "дишься", get_rhytmic_structure(self))
                                elif re.search(".*теться$", self.text, re.I):
                                    return WordStructure(self.text[:-4] + "тишься", get_rhytmic_structure(self))
                                elif re.search(".*петься$", self.text, re.I):
                                    return WordStructure(self.text[:-3] + "оёшься", get_rhytmic_structure(self)[:-1] + "-^")
                                else:
                                    return WordStructure(self.text[:-2] + "ешься", get_rhytmic_structure(self) + "-")
                            elif re.search(".*аться$", self.text, re.I):
                                if re.search(".*саться$", self.text, re.I) \
                                        and self.stress_position +1 == self.syllables_count:
                                    return WordStructure(self.text[:-6] + "шешься", get_rhytmic_structure(self)[:-2] + "^-")
                                elif re.search(".*певаться$", self.text, re.I):
                                    return WordStructure(self.text[:-2] + "ешься", get_rhytmic_structure(self) + "-")
                                elif re.search(".*[ое]ваться$", self.text, re.I):
                                    if re.search(".*оваться$", self.text, re.I) \
                                            and self.stress_position + 1 == self.syllables_count:
                                        return WordStructure(self.text[:-7] + "уешься",
                                                             get_rhytmic_structure(self)[:-2] + "^-")
                                    elif re.search(".*еваться$", self.text, re.I) \
                                            and self.stress_position + 1 == self.syllables_count:
                                        return WordStructure(self.text[:-4] + "ешься",
                                                             get_rhytmic_structure(self)[:-2] + "^-")
                                    else:
                                        return WordStructure(self.text[:-7] + "аешься", get_rhytmic_structure(self))
                                elif re.search(".*аваться$", self.text, re.I):
                                    return WordStructure(self.text[:-4] + "ёшься", get_rhytmic_structure(self))
                                elif re.search(".*скаться$", self.text, re.I):
                                    return WordStructure(self.text[:-5] + "щешься", get_rhytmic_structure(self)[:-2] + "^-")
                                else:
                                    return WordStructure(self.text[:-4] + "ешься", get_rhytmic_structure(self) + "-")
                            elif re.search(".*иться", self.text, re.I):
                                if re.search(".*риться$", self.text, re.I):
                                    return WordStructure(self.text[:-5] + "еешься", get_rhytmic_structure(self) + "-")
                                else:
                                    return WordStructure(self.text[:-3] + "ешься", get_rhytmic_structure(self)[:-2] + "^-")
                            elif re.search(".*яться$", self.text, re.I):
                                if re.search(".*[ал]яться", self.text, re.I) \
                                        and self.stress_position + 1 == self.syllables_count:
                                    return WordStructure(self.text[:-4] + "ешься", get_rhytmic_structure(self) + "-")
                                else:
                                    return WordStructure(self.text[:-5] + "ёшься", get_rhytmic_structure(self))
                            elif re.search(".*оться$", self.text, re.I):
                                return WordStructure(self.text[:-3] + "ешься", get_rhytmic_structure(self)[:-2] + "^-")
                            elif re.search(".*ыться$", self.text, re.I):
                                return WordStructure(self.text[:-3] + "оешься", get_rhytmic_structure(self) + "-")
                        elif self.conjugation == 2:
                            if re.search(".*иться$", self.text, re.I):
                                if re.search(".*зиться$", self.text, re.I):
                                    return WordStructure(self.text[:-6] + "зишься", get_rhytmic_structure(self)[:-2] + "^-")
                                if re.search(".*диться$", self.text, re.I):
                                    return WordStructure(self.text[:-6] + "дишься", get_rhytmic_structure(self)[:-2] + "^-")
                                elif re.search(".*титься$", self.text, re.I):
                                    return WordStructure(self.text[:-6] + "тишься", get_rhytmic_structure(self)[:-2] + "^-")
                                elif re.search(".*ситься$", self.text, re.I):
                                    return WordStructure(self.text[:-6] + "сишься", get_rhytmic_structure(self)[:-2] + "^-")
                                else:
                                    return WordStructure(self.text[:-5] + "ишься", get_rhytmic_structure(self)[:-2]
                                                         + "^-")
                            elif re.search(".*еться$", self.text, re.I):
                                if re.search(".*теться$", self.text, re.I):
                                    return WordStructure(self.text[:-6] + "тишься", get_rhytmic_structure(self)[:-2] + "^-")
                                elif re.search(".*деться$", self.text, re.I):
                                    return WordStructure(self.text[:-6] + "дишься", get_rhytmic_structure(self)[:-2] + "^-")
                                elif re.search(".*петься$", self.text, re.I):
                                    return WordStructure(self.text[:-5] + "ишься", get_rhytmic_structure(self)[:-2] + "^-")
                                elif re.search(".*сеться$", self.text, re.I):
                                    return WordStructure(self.text[:-6] + "сишься", get_rhytmic_structure(self)[:-2] + "^-")
                                else:
                                    return WordStructure(self.text[:-5] + "ишься", get_rhytmic_structure(self)[:-2] + "^-")
                            elif re.search(".*аться$", self.text, re.I):
                                if re.search(".*[жш]аться$", self.text, re.I):
                                    return WordStructure(self.text[:-3] + "ишься", get_rhytmic_structure(self)[:-2] + "^-")
                                elif re.search(".*гнаться$", self.text, re.I):
                                    return WordStructure(self.text[:-4] + "онишься", get_rhytmic_structure(self) + "-")
                                else:
                                    return WordStructure(self.text[:-3] + "ишься", get_rhytmic_structure(self))
                        else:
                            if re.search(".*есть$", self.text, re.I):
                                if self.text == "есть":
                                    return WordStructure("ешься", "^")
                                else:
                                    return WordStructure(self.text[:-3] + "даешься", get_rhytmic_structure(self))
                            elif re.search(".*дать$", self.text, re.I):
                                return WordStructure(self.text[:-2] + "ешься", get_rhytmic_structure(self))
                            elif re.search(".+быть$", self.text, re.I):
                                return WordStructure(self.text[:-2] + "ваешься", get_rhytmic_structure(self))
                            elif self.text == "хотеться":
                                return WordStructure("хочешься", "^-")
                            elif self.text == "бежаться":
                                return WordStructure("бежишься", "-^")
                            elif self.text == "чтить":
                                return WordStructure("чтишь", "^")
                            elif self.text == "ехаться":
                                return WordStructure("едешься", "^-")
                            elif self.text == "идтись":
                                return WordStructure("идёшься", "-^")
                            elif self.text == "быть":
                                return WordStructure("есть", "^")
                    else:
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
                    if self.reflexive:
                        if self.conjugation == 1:
                            if re.search(".*еться$", self.text, re.I):
                                if re.search(".*деться$", self.text, re.I):
                                    return WordStructure(self.text[:-4] + "дится", get_rhytmic_structure(self))
                                elif re.search(".*теться$", self.text, re.I):
                                    return WordStructure(self.text[:-4] + "тится", get_rhytmic_structure(self))
                                elif re.search(".*петься$", self.text, re.I):
                                    return WordStructure(self.text[:-3] + "оётся",
                                                         get_rhytmic_structure(self)[:-1] + "-^")
                                else:
                                    return WordStructure(self.text[:-2] + "ется", get_rhytmic_structure(self) + "-")
                            elif re.search(".*аться$", self.text, re.I):
                                if re.search(".*саться$", self.text, re.I):
                                    if self.stress_position + 1 == self.syllables_count:
                                        return WordStructure(self.text[:-6] + "шется", get_rhytmic_structure(self)[:-2]
                                                             + "^-")
                                    else:
                                        return WordStructure(self.text[:-4] + "шется", get_rhytmic_structure(self))
                                elif re.search(".*певаться$", self.text, re.I):
                                    return WordStructure(self.text[:-2] + "ется", get_rhytmic_structure(self) + "-")
                                elif re.search(".*[ое]ваться$", self.text, re.I):
                                    if re.search(".*оваться$", self.text, re.I) \
                                            and self.stress_position + 1 == self.syllables_count:
                                        return WordStructure(self.text[:-7] + "уется", get_rhytmic_structure(self)[:-2]
                                                             + "^-")
                                    elif re.search(".*еваться$", self.text, re.I) \
                                            and self.stress_position + 1 == self.syllables_count:
                                        return WordStructure(self.text[:-5] + "ается", get_rhytmic_structure(self)[:-2]
                                                             + "^-")
                                    else:
                                        return WordStructure(self.text[:-5] + "уется", get_rhytmic_structure(self))
                                elif re.search(".*аваться$", self.text, re.I):
                                    return WordStructure(self.text[:-4] + "ётся", get_rhytmic_structure(self))
                                elif re.search(".*скаться$", self.text, re.I):
                                    return WordStructure(self.text[:-5] + "щется",
                                                         get_rhytmic_structure(self)[:-2] + "^-")
                                else:
                                    return WordStructure(self.text[:-4] + "ется", get_rhytmic_structure(self) + "-")
                            elif re.search(".*иться$", self.text, re.I):
                                if re.search(".*риться$", self.text, re.I):
                                    return WordStructure(self.text[:-5] + "еется", get_rhytmic_structure(self) + "-")
                                else:
                                    return WordStructure(self.text[:-3] + "ется", get_rhytmic_structure(self)[:-2] + "^-")
                            elif re.search(".*яться$", self.text, re.I):
                                if re.search(".*[ал]яться$", self.text,
                                             re.I) and self.stress_position + 1 == self.syllables_count:
                                    return WordStructure(self.text[:-4] + "ется", get_rhytmic_structure(self) + "-")
                                else:
                                    return WordStructure(self.text[:-5] + "ётся", get_rhytmic_structure(self))
                            elif re.search(".*оться$", self.text, re.I):
                                return WordStructure(self.text[:-3] + "ется", get_rhytmic_structure(self)[:-2] + "^-")
                            elif re.search(".*ыться$", self.text, re.I):
                                return WordStructure(self.text[:-3] + "оется", get_rhytmic_structure(self) + "-")

                        elif self.conjugation == 2:
                            if re.search(".*иться$", self.text, re.I):
                                if re.search(".*зиться$", self.text, re.I):
                                    if self.text == "возиться":
                                        return WordStructure(self.text[:-6] + "зится", get_rhytmic_structure(self)[:-2]
                                                             + "^-")
                                    else:
                                        return WordStructure(self.text[:-6] + "зится", get_rhytmic_structure(self))
                                if re.search(".*диться$", self.text, re.I):
                                    return WordStructure(self.text[:-6] + "дится",
                                                         get_rhytmic_structure(self)[:-2] + "^-")
                                elif re.search(".*титься$", self.text, re.I):
                                    return WordStructure(self.text[:-6] + "тится",
                                                         get_rhytmic_structure(self)[:-2] + "^-")
                                elif re.search(".*ситься$", self.text, re.I):
                                    return WordStructure(self.text[:-6] + "сится",
                                                         get_rhytmic_structure(self)[:-2] + "^-")
                                else:
                                    return WordStructure(self.text[:-5] + "ится", get_rhytmic_structure(self)[:-2] + "^-")
                            elif re.search(".*еться$", self.text, re.I):
                                if re.search(".*теться$", self.text, re.I):
                                    return WordStructure(self.text[:-6] + "тится",
                                                         get_rhytmic_structure(self)[:-2] + "^-")
                                elif re.search(".*деться$", self.text, re.I):
                                    return WordStructure(self.text[:-6] + "дится",
                                                         get_rhytmic_structure(self)[:-2] + "^-")
                                elif re.search(".*петься$", self.text, re.I):
                                    return WordStructure(self.text[:-5] + "ится", get_rhytmic_structure(self)[:-2] + "^-")
                                elif re.search(".*сеться$", self.text, re.I):
                                    return WordStructure(self.text[:-4] + "сится",
                                                         get_rhytmic_structure(self)[:-2] + "^-")
                                else:
                                    return WordStructure(self.text[:-3] + "ится", get_rhytmic_structure(self)[:-2] + "^-")
                            elif re.search(".*аться$", self.text, re.I):
                                if re.search(".*[жш]аться$", self.text, re.I):
                                    return WordStructure(self.text[:-3] + "ится", get_rhytmic_structure(self)[:-2] + "^-")
                                elif re.search(".*гнаться$", self.text, re.I):
                                    return WordStructure(self.text[:-4] + "онится", get_rhytmic_structure(self) + "-")
                                else:
                                    return WordStructure(self.text[:-3] + "ится", get_rhytmic_structure(self))

                        else:
                            if re.search(".*есться$", self.text, re.I):
                                if self.text == "есть":
                                    return WordStructure("естся", "^")
                                else:
                                    return WordStructure(self.text[:-3] + "дается", get_rhytmic_structure(self))
                            elif re.search(".*дать$", self.text, re.I):
                                return WordStructure(self.text[:-2] + "ется", get_rhytmic_structure(self))
                            elif re.search(".+быть$", self.text, re.I):
                                return WordStructure(self.text[:-2] + "вается", get_rhytmic_structure(self))
                            elif self.text == "хотеться":
                                return WordStructure("хочется", "^-")
                            elif self.text == "бежаться":
                                return WordStructure("бежится", "-^")
                            elif self.text == "чтиться":
                                return WordStructure("чтится", "^")
                            elif self.text == "ехаться":
                                return WordStructure("едется", "^-")
                            elif self.text == "идтись":
                                return WordStructure("идётся", "-^")
                            elif self.text == "быть":
                                return WordStructure("есть", "^")
                    else:
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
                    if self.reflexive:
                        if self.conjugation == 1:
                            if re.search(".*еться$", self.text, re.I):
                                if re.search(".*деться$", self.text, re.I):
                                    return WordStructure(self.text[:-4] + "димся", get_rhytmic_structure(self))
                                elif re.search(".*теться$", self.text, re.I):
                                    return WordStructure(self.text[:-4] + "тимся", get_rhytmic_structure(self))
                                elif re.search(".*петься$", self.text, re.I):
                                    return WordStructure(self.text[:-3] + "оёмся", get_rhytmic_structure(self)[:-1] + "-^")
                                else:
                                    return WordStructure(self.text[:-2] + "емся", get_rhytmic_structure(self) + "-")
                            elif re.search(".*аться$", self.text, re.I):
                                if re.search(".*саться$", self.text, re.I) \
                                        and self.stress_position + 1 == self.syllables_count:
                                    return WordStructure(self.text[:-6] + "шемся", get_rhytmic_structure(self)[:-2] + "^-")
                                elif re.search(".*певаться$", self.text, re.I):
                                    return WordStructure(self.text[:-2] + "емся", get_rhytmic_structure(self) + "-")
                                elif re.search(".*[ое]ваться$", self.text, re.I):
                                    if re.search(".*оваться$", self.text, re.I) \
                                            and self.stress_position + 1 == self.syllables_count:
                                        return WordStructure(self.text[:-7] + "уемся",
                                                             get_rhytmic_structure(self)[:-2] + "^-")
                                    elif re.search(".*еваться$", self.text, re.I) \
                                            and self.stress_position + 1 == self.syllables_count:
                                        return WordStructure(self.text[:-5] + "аемся",
                                                             get_rhytmic_structure(self)[:-2] + "^-")
                                    else:
                                        return WordStructure(self.text[:-5] + "уемся", get_rhytmic_structure(self))
                                elif re.search(".*аваться$", self.text, re.I):
                                    return WordStructure(self.text[:-4] + "ёмся", get_rhytmic_structure(self))
                                elif re.search(".*скаться$", self.text, re.I):
                                    return WordStructure(self.text[:-5] + "щемся", get_rhytmic_structure(self)[:-2] + "^-")
                                else:
                                    return WordStructure(self.text[:-4] + "емся", get_rhytmic_structure(self) + "-")
                            elif re.search(".*иться", self.text, re.I):
                                if re.search(".*риться$", self.text, re.I):
                                    return WordStructure(self.text[:-5] + "еемся", get_rhytmic_structure(self) + "-")
                                else:
                                    return WordStructure(self.text[:-5] + "емся", get_rhytmic_structure(self)[:-2] + "^-")
                            elif re.search(".*яться$", self.text, re.I):
                                if re.search(".*[ал]яться$", self.text, re.I) \
                                        and self.stress_position + 1 == self.syllables_count:
                                    return WordStructure(self.text[:-4] + "емся", get_rhytmic_structure(self) + "-")
                                else:
                                    return WordStructure(self.text[:-5] + "ёмся", get_rhytmic_structure(self))
                            elif re.search(".*оться$", self.text, re.I):
                                return WordStructure(self.text[:-3] + "емся", get_rhytmic_structure(self)[:-2] + "^-")
                            elif re.search(".*ыться$", self.text, re.I):
                                return WordStructure(self.text[:-3] + "оемся", get_rhytmic_structure(self) + "-")

                        elif self.conjugation == 2:
                            if re.search(".*иться$", self.text, re.I):
                                if re.search(".*озиться$", self.text, re.I):
                                    return WordStructure(self.text[:-6] + "зимся", get_rhytmic_structure(self)[:-2] + "^-")
                                elif re.search(".*зиться$", self.text, re.I):
                                    return WordStructure(self.text[:-6] + "зимся", get_rhytmic_structure(self))
                                elif re.search(".*диться$", self.text, re.I):
                                    return WordStructure(self.text[:-6] + "димся", get_rhytmic_structure(self)[:-2] + "^-")
                                elif re.search(".*титься$", self.text, re.I):
                                    return WordStructure(self.text[:-6] + "тимся", get_rhytmic_structure(self)[:-2] + "^-")
                                elif re.search(".*ситься$", self.text, re.I):
                                    return WordStructure(self.text[:-6] + "симся", get_rhytmic_structure(self)[:-2] + "^-")
                                else:
                                    return WordStructure(self.text[:-5] + "имся", get_rhytmic_structure(self)[:-2] + "^-")
                            elif re.search(".*еться$", self.text, re.I):
                                if re.search(".*теться$", self.text, re.I):
                                    return WordStructure(self.text[:-6] + "тимся", get_rhytmic_structure(self)[:-2] + "^-")
                                elif re.search(".*деться$", self.text, re.I):
                                    return WordStructure(self.text[:-6] + "димся", get_rhytmic_structure(self)[:-2] + "^-")
                                elif re.search(".*петься$", self.text, re.I):
                                    return WordStructure(self.text[:-6] + "пимся", get_rhytmic_structure(self)[:-2] + "^-")
                                elif re.search(".*сеться$", self.text, re.I):
                                    return WordStructure(self.text[:-6] + "симся", get_rhytmic_structure(self)[:-2] + "^-")
                                else:
                                    return WordStructure(self.text[:-5] + "имся", get_rhytmic_structure(self)[:-2] + "^-")
                            elif re.search(".*аться$", self.text, re.I):
                                if re.search(".*[жш]аться$", self.text, re.I):
                                    if re.search(".*ижаться$", self.text, re.I):
                                        return WordStructure(self.text[:-3] + "аемся", get_rhytmic_structure(self) + "-")
                                    else:
                                        return WordStructure(self.text[:-3] + "имся", get_rhytmic_structure(self)[:-2] + "^-")
                                elif re.search(".*гнаться$", self.text, re.I):
                                    return WordStructure(self.text[:-4] + "онимся", get_rhytmic_structure(self) + "-")
                                else:
                                    return WordStructure(self.text[:-3] + "имся", get_rhytmic_structure(self) + "-")

                        else:
                            if re.search(".*есться$", self.text, re.I):
                                if self.text == "есться":
                                    return WordStructure("едимся", "-^")
                                else:
                                    return WordStructure(self.text[:-3] + "даемся", get_rhytmic_structure(self))
                            elif re.search(".*даться$", self.text, re.I):
                                return WordStructure(self.text[:-2] + "емся", get_rhytmic_structure(self) + "-")
                            elif re.search(".+быться$", self.text, re.I):
                                return WordStructure(self.text[:-2] + "ваемся", get_rhytmic_structure(self))
                            elif self.text == "хотеться":
                                return WordStructure("хотимся", "-^")
                            elif self.text == "бежаться":
                                return WordStructure("бежимся", "-^")
                            elif self.text == "чтиться":
                                return WordStructure("чтимся", "^")
                            elif self.text == "ехаться":
                                return WordStructure("едемся", "^-")
                            elif self.text == "идтись":
                                return WordStructure("идёмся", "-^")
                            elif self.text == "быть":
                                return WordStructure("есть", "^")

                    else:
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
                    if self.reflexive:
                        if self.conjugation == 1:
                            if re.search(".*еться$", self.text, re.I):
                                if re.search(".*деться$", self.text, re.I):
                                    return WordStructure(self.text[:-4] + "дитесь", get_rhytmic_structure(self) + "-")
                                elif re.search(".*теться$", self.text, re.I):
                                    return WordStructure(self.text[:-4] + "титесь", get_rhytmic_structure(self) + "-")
                                elif re.search(".*петься$", self.text, re.I):
                                    return WordStructure(self.text[:-3] + "оётесь",
                                                         get_rhytmic_structure(self)[:-1] + "-^-")
                                else:
                                    return WordStructure(self.text[:-2] + "етесь", get_rhytmic_structure(self) + "--")
                            elif re.search(".*аться$", self.text, re.I):
                                if re.search(".*саться$", self.text,
                                             re.I) and self.stress_position + 1 == self.syllables_count:
                                    return WordStructure(self.text[:-6] + "шетесь", get_rhytmic_structure(self)[:-2]
                                                         + "^--")
                                elif re.search(".*певаться$", self.text, re.I):
                                    return WordStructure(self.text[:-2] + "етесь", get_rhytmic_structure(self) + "--")
                                elif re.search(".*[ое]ваться$", self.text, re.I):
                                    if re.search(".*оваться$", self.text, re.I) \
                                            and self.stress_position + 1 == self.syllables_count:
                                        return WordStructure(self.text[:-7] + "уетесь", get_rhytmic_structure(self)[:-2]
                                                             + "^--")
                                    if re.search(".*еваться$", self.text, re.I) \
                                            and self.stress_position + 1 == self.syllables_count:
                                        return WordStructure(self.text[:-5] + "аетесь", get_rhytmic_structure(self)[:-2]
                                                             + "^--")
                                    else:
                                        return WordStructure(self.text[:-5] + "уетесь", get_rhytmic_structure(self) + "-")
                                elif re.search(".*аваться$", self.text, re.I):
                                    return WordStructure(self.text[:-4] + "ётeсь", get_rhytmic_structure(self) + "-")
                                elif re.search(".*скаться$", self.text, re.I):
                                    return WordStructure(self.text[:-5] + "щетесь",
                                                         get_rhytmic_structure(self)[:-2] + "^--")
                                else:
                                    return WordStructure(self.text[:-4] + "етесь", get_rhytmic_structure(self) + "--")
                            elif re.search(".*иться$", self.text, re.I):
                                if re.search(".*риться$", self.text, re.I):
                                    return WordStructure(self.text[:-5] + "еетесь", get_rhytmic_structure(self) + "--")
                                else:
                                    return WordStructure(self.text[:-5] + "етесь",
                                                         get_rhytmic_structure(self)[:-2] + "^--")
                            elif re.search(".*яться$", self.text, re.I):
                                if re.search(".*[ал]яться$", self.text,
                                             re.I) and self.stress_position + 1 == self.syllables_count:
                                    return WordStructure(self.text[:-4] + "етесь", get_rhytmic_structure(self) + "--")
                                else:
                                    return WordStructure(self.text[:-5] + "ётесь", get_rhytmic_structure(self) + "-")
                            elif re.search(".*оться$", self.text, re.I):
                                return WordStructure(self.text[:-3] + "етесь", get_rhytmic_structure(self)[:-2] + "^--")
                            elif re.search(".*ыться$", self.text, re.I):
                                return WordStructure(self.text[:-3] + "оетесь", get_rhytmic_structure(self) + "--")

                        elif self.conjugation == 2:
                            if re.search(".*иться$", self.text, re.I):
                                if re.search(".*озиться$", self.text, re.I):
                                    return WordStructure(self.text[:-6] + "зитесь",
                                                         get_rhytmic_structure(self)[:-2] + "^--")
                                if re.search(".*зиться$", self.text, re.I):
                                    return WordStructure(self.text[:-6] + "зитесь",
                                                         get_rhytmic_structure(self)[:-2] + "-^-")
                                elif re.search(".*диться$", self.text, re.I):
                                    return WordStructure(self.text[:-6] + "дитесь",
                                                         get_rhytmic_structure(self)[:-2] + "^--")
                                elif re.search(".*титься$", self.text, re.I):
                                    return WordStructure(self.text[:-6] + "титесь",
                                                         get_rhytmic_structure(self)[:-2] + "^--")
                                elif re.search(".*ситься$", self.text, re.I):
                                    return WordStructure(self.text[:-6] + "ситесь",
                                                         get_rhytmic_structure(self)[:-2] + "^--")
                                else:
                                    return WordStructure(self.text[:-5] + "итесь",
                                                         get_rhytmic_structure(self)[:-2] + "^--")
                            elif re.search(".*еться$", self.text, re.I):
                                if re.search(".*теться$", self.text, re.I):
                                    return WordStructure(self.text[:-6] + "титесь",
                                                         get_rhytmic_structure(self)[:-2] + "^--")
                                elif re.search(".*деться$", self.text, re.I):
                                    return WordStructure(self.text[:-6] + "дитесь",
                                                         get_rhytmic_structure(self)[:-2] + "^--")
                                elif re.search(".*петься$", self.text, re.I):
                                    return WordStructure(self.text[:-6] + "питесь",
                                                         get_rhytmic_structure(self)[:-2] + "^--")
                                elif re.search(".*сеться$", self.text, re.I):
                                    return WordStructure(self.text[:-6] + "ситесь",
                                                         get_rhytmic_structure(self)[:-2] + "^--")
                                else:
                                    return WordStructure(self.text[:-5] + "итесь",
                                                         get_rhytmic_structure(self)[:-2] + "^--")
                            elif re.search(".*аться$", self.text, re.I):
                                if re.search(".*[жш]аться$", self.text, re.I):
                                    return WordStructure(self.text[:-3] + "итесь",
                                                         get_rhytmic_structure(self)[:-2] + "^--")
                                elif re.search(".*гнаться$", self.text, re.I):
                                    return WordStructure(self.text[:-4] + "онитесь", get_rhytmic_structure(self) + "--")
                                else:
                                    return WordStructure(self.text[:-3] + "итесь",
                                                         get_rhytmic_structure(self)[:-2] + "^--")

                        else:
                            if re.search(".*есться$", self.text, re.I):
                                if self.text == "есться":
                                    return WordStructure("едитесь", "-^-")
                                else:
                                    return WordStructure(self.text[:-3] + "даетесь", "^--")
                            elif re.search(".*дать$", self.text, re.I):
                                return WordStructure(self.text[:-2] + "етесь", get_rhytmic_structure(self)[:-2] + "^--")
                            elif re.search(".+быть$", self.text, re.I):
                                return WordStructure(self.text[:-2] + "ваетесь", get_rhytmic_structure(self)[:-2] + "^-")
                            elif self.text == "хотеться":
                                return WordStructure("хотитесь", "-^-")
                            elif self.text == "бежаться":
                                return WordStructure("бежитесь", "-^-")
                            elif self.text == "чтиться":
                                return WordStructure("чтитесь", "^-")
                            elif self.text == "ехаться":
                                return WordStructure("едетесь", "^--")
                            elif self.text == "идтися":
                                return WordStructure("идётесь", "-^-")
                            elif self.text == "быть":
                                return WordStructure("есть", "^")

                    else:
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
                    if self.reflexive:
                        if self.conjugation == 1:
                            if re.search(".*еться$", self.text, re.I):
                                if re.search(".*деться$", self.text, re.I):
                                    return WordStructure(self.text[:-4] + "дятся", get_rhytmic_structure(self))
                                elif re.search(".*теться$", self.text, re.I):
                                    return WordStructure(self.text[:-4] + "тятся",
                                                         get_rhytmic_structure(self)[:-2] + "^-")
                                elif re.search(".*петься$", self.text, re.I):
                                    return WordStructure(self.text[:-3] + "оются",
                                                         get_rhytmic_structure(self)[:-1] + "-^")
                                else:
                                    return WordStructure(self.text[:-2] + "ются", get_rhytmic_structure(self) + "-")
                            elif re.search(".*аться$", self.text, re.I):
                                if re.search(".*саться$", self.text,
                                             re.I) and self.stress_position + 1 == self.syllables_count:
                                    return WordStructure(self.text[:-6] + "шутся",
                                                         get_rhytmic_structure(self)[:-2] + "^-")
                                elif re.search(".*певаться$", self.text, re.I):
                                    return WordStructure(self.text[:-2] + "ются", get_rhytmic_structure(self) + "-")
                                elif re.search(".*[ое]ваться$", self.text, re.I):
                                    if re.search(".*оваться$", self.text, re.I) \
                                            and self.stress_position + 1 == self.syllables_count:
                                        return WordStructure(self.text[:-7] + "уются", get_rhytmic_structure(self)[:-2]
                                                             + "^-")
                                    if re.search(".*еваться$", self.text, re.I) \
                                            and self.stress_position + 1 == self.syllables_count:
                                        return WordStructure(self.text[:-5] + "аются", get_rhytmic_structure(self)[:-2]
                                                             + "^-")
                                    else:
                                        return WordStructure(self.text[:-5] + "аются", get_rhytmic_structure(self))
                                elif re.search(".*аваться$", self.text, re.I):
                                    return WordStructure(self.text[:-4] + "ются", get_rhytmic_structure(self))
                                elif re.search(".*скаться$", self.text, re.I):
                                    return WordStructure(self.text[:-5] + "щутся",
                                                         get_rhytmic_structure(self)[:-2] + "^-")
                                else:
                                    return WordStructure(self.text[:-4] + "ются", get_rhytmic_structure(self) + "-")
                            elif re.search(".*иться$", self.text, re.I):
                                if re.search(".*риться$", self.text, re.I):
                                    return WordStructure(self.text[:-5] + "еются", get_rhytmic_structure(self) + "-")
                                else:
                                    return WordStructure(self.text[:-5] + "ются", get_rhytmic_structure(self)[:-2] + "^-")
                            elif re.search(".*яться$", self.text, re.I):
                                if re.search(".*[ал]яться", self.text, re.I) \
                                        and self.stress_position + 1 == self.syllables_count:
                                    return WordStructure(self.text[:-4] + "ются", get_rhytmic_structure(self) + "-")
                                else:
                                    return WordStructure(self.text[:-5] + "ются", get_rhytmic_structure(self))
                            elif re.search(".*оться$", self.text, re.I):
                                return WordStructure(self.text[:-3] + "ятся", get_rhytmic_structure(self)[:-2] + "^-")
                            elif re.search(".*ыться$", self.text, re.I):
                                return WordStructure(self.text[:-3] + "оются", get_rhytmic_structure(self) + "-")

                        elif self.conjugation == 2:
                            if re.search(".*иться$", self.text, re.I):
                                if re.search(".*азиться$", self.text, re.I):
                                    return WordStructure(self.text[:-6] + "зятся",
                                                         get_rhytmic_structure(self)[:-2] + "-^")
                                if re.search(".*зиться$", self.text, re.I):
                                    return WordStructure(self.text[:-6] + "зятся",
                                                         get_rhytmic_structure(self)[:-2] + "^-")
                                if re.search(".*диться$", self.text, re.I):
                                    return WordStructure(self.text[:-6] + "дятся",
                                                         get_rhytmic_structure(self)[:-2] + "^-")
                                elif re.search(".*титься$", self.text, re.I):
                                    return WordStructure(self.text[:-6] + "тятся",
                                                         get_rhytmic_structure(self)[:-2] + "^-")
                                elif re.search(".*ситься$", self.text, re.I):
                                    return WordStructure(self.text[:-6] + "сятся",
                                                         get_rhytmic_structure(self)[:-2] + "^-")
                                else:
                                    return WordStructure(self.text[:-5] + "ятся", get_rhytmic_structure(self)[:-2] + "^-")
                            elif re.search(".*еться$", self.text, re.I):
                                if re.search(".*теться$", self.text, re.I):
                                    return WordStructure(self.text[:-6] + "тятся",
                                                         get_rhytmic_structure(self)[:-2] + "^-")
                                elif re.search(".*деться$", self.text, re.I):
                                    return WordStructure(self.text[:-6] + "дятся",
                                                         get_rhytmic_structure(self)[:-2] + "^-")
                                elif re.search(".*петься$", self.text, re.I):
                                    return WordStructure(self.text[:-6] + "пятся", get_rhytmic_structure(self)[:-2] + "^-")
                                elif re.search(".*сеться$", self.text, re.I):
                                    return WordStructure(self.text[:-6] + "сятся",
                                                         get_rhytmic_structure(self)[:-2] + "^-")
                                else:
                                    return WordStructure(self.text[:-3] + "ят", get_rhytmic_structure(self)[:-2] + "^-")
                            elif re.search(".*аться$", self.text, re.I):
                                if re.search(".*[жш]аться$", self.text, re.I):
                                    return WordStructure(self.text[:-3] + "атся", get_rhytmic_structure(self)[:-2] + "^-")
                                elif re.search(".*гнаться$", self.text, re.I):
                                    return WordStructure(self.text[:-4] + "онятся", get_rhytmic_structure(self) + "-")
                                else:
                                    return WordStructure(self.text[:-3] + "ятся", get_rhytmic_structure(self))

                        else:
                            if re.search(".*есться$", self.text, re.I):
                                if self.text == "есться":
                                    return WordStructure("едятся", "-^")
                                else:
                                    return WordStructure(self.text[:-3] + "даются", get_rhytmic_structure(self))
                            elif re.search(".*даться$", self.text, re.I):
                                return WordStructure(self.text[:-2] + "ются", get_rhytmic_structure(self))
                            elif re.search(".+быться$", self.text, re.I):
                                return WordStructure(self.text[:-2] + "ваются", get_rhytmic_structure(self))
                            elif self.text == "хотеться":
                                return WordStructure("хотятся", "-^")
                            elif self.text == "бежаться":
                                return WordStructure("бегутся", "-^")
                            elif self.text == "чтиться":
                                return WordStructure("чтятся", "^")
                            elif self.text == "ехаться":
                                return WordStructure("едутся", "^-")
                            elif self.text == "идтися":
                                return WordStructure("идутся", "-^")
                            elif self.text == "быть":
                                return WordStructure("есть", "^")

                    else:
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
