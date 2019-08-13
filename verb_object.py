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


def get_form(verb, tense, person, gender, plural):
    if tense == "present":
        if not plural:
            if person == 1:
                if verb.reflexive:
                    if verb.conjugation == 1:
                        if re.search(".*еться$", verb.text, re.I):
                            if re.search(".*деться$", verb.text, re.I):
                                return WordStructure(verb.text[:-4] + "юсь", get_rhytmic_structure(verb)[:-1])
                            elif re.search(".*теться$", verb.text, re.I):
                                return WordStructure(verb.text[:-6] + "чусь", get_rhytmic_structure(verb)[:-1])
                            elif re.search(".*петься$", verb.text, re.I):
                                return WordStructure(verb.text[:-3] + "юсь",
                                                     get_rhytmic_structure(verb)[:-2] + "-^")
                            else:
                                return WordStructure(verb.text[:-2] + "юсь", get_rhytmic_structure(verb)[:-1])
                        elif re.search(".*аться$", verb.text, re.I):
                            if re.search(".*саться$", verb.text, re.I) \
                                    and verb.stress_position + 1 == verb.syllables_count:
                                return WordStructure(verb.text[:-6] + "шусь", get_rhytmic_structure(verb)[:-1])
                            elif re.search(".*певаться$", verb.text, re.I):
                                return WordStructure(verb.text[:-2] + "юсь", get_rhytmic_structure(verb) + "-")
                            elif re.search(".*[ое]ваться$", verb.text, re.I):
                                if re.search(".*оваться$", verb.text, re.I) \
                                        and verb.stress_position + 1 == verb.syllables_count:
                                    return WordStructure(verb.text[:-7] + "уюсь",
                                                         get_rhytmic_structure(verb)[:-3] + "^-")
                                elif re.search(".*еваться$", verb.text, re.I) \
                                        and verb.stress_position + 1 == verb.syllables_count:
                                    return WordStructure(verb.text[:-4] + "юсь",
                                                         get_rhytmic_structure(verb)[:-2] + "^-")
                                else:
                                    return WordStructure(verb.text[:-4] + "юсь", get_rhytmic_structure(verb)[:-1])
                            elif re.search(".*аваться$", verb.text, re.I):
                                return WordStructure(verb.text[:-4] + "юсь", get_rhytmic_structure(verb)[:-1])
                            elif re.search(".*скаться$", verb.text, re.I):
                                return WordStructure(verb.text[:-5] + "юсь", get_rhytmic_structure(verb)[:-1])
                            else:
                                return WordStructure(verb.text[:-4] + "юсь", get_rhytmic_structure(verb))
                        elif re.search(".*иться", verb.text, re.I):
                            if re.search(".*риться$", verb.text, re.I):
                                return WordStructure(verb.text[:-5] + "еюсь", get_rhytmic_structure(verb))
                            else:
                                return WordStructure(verb.text[:-3] + "юсь", get_rhytmic_structure(verb)[:-1])
                        elif re.search(".*яться$", verb.text, re.I):
                            if re.search(".*[ал]яться$", verb.text, re.I) \
                                    and verb.stress_position == verb.syllables_count:
                                return WordStructure(verb.text[:-3] + "юсь", get_rhytmic_structure(verb))
                            elif re.search(".*еяться$", verb.text, re.I):
                                return WordStructure(verb.text[:-5] + "юсь", get_rhytmic_structure(verb)[:-1])
                            else:
                                return WordStructure(verb.text[:-4] + "юсь", get_rhytmic_structure(verb))
                        elif re.search(".*оться$", verb.text, re.I):
                            return WordStructure(verb.text[:-3] + "юсь", get_rhytmic_structure(verb)[:-1])
                        elif re.search(".*ыться$", verb.text, re.I):
                            return WordStructure(verb.text[:-3] + "оюсь", get_rhytmic_structure(verb))
                    elif verb.conjugation == 2:
                        if re.search(".*иться$", verb.text, re.I):
                            if re.search(".*зиться$", verb.text, re.I):
                                return WordStructure(verb.text[:-6] + "жусь", get_rhytmic_structure(verb)[:-1])
                            elif re.search(".*диться$", verb.text, re.I):
                                return WordStructure(verb.text[:-6] + "жусь", get_rhytmic_structure(verb)[:-1])
                            elif re.search(".*титься$", verb.text, re.I):
                                return WordStructure(verb.text[:-6] + "чусь", get_rhytmic_structure(verb)[:-1])
                            elif re.search(".*ситься$", verb.text, re.I):
                                return WordStructure(verb.text[:-6] + "шусь", get_rhytmic_structure(verb)[:-1])
                            else:
                                return WordStructure(verb.text[:-5] + "юсь", get_rhytmic_structure(verb)[:-1])
                        elif re.search(".*еться$", verb.text, re.I):
                            if re.search(".*теться$", verb.text, re.I):
                                return WordStructure(verb.text[:-6] + "чусь", get_rhytmic_structure(verb)[:-1])
                            elif re.search(".*деться$", verb.text, re.I):
                                return WordStructure(verb.text[:-4] + "жусь", get_rhytmic_structure(verb)[:-1])
                            elif re.search(".*петься$", verb.text, re.I):
                                return WordStructure(verb.text[:-5] + "люсь", get_rhytmic_structure(verb)[:-1])
                            elif re.search(".*сеться$", verb.text, re.I):
                                return WordStructure(verb.text[:-4] + "шусь", get_rhytmic_structure(verb)[:-1])
                            else:
                                return WordStructure(verb.text[:-3] + "юсь", get_rhytmic_structure(verb)[:-1])
                        elif re.search(".*ать$", verb.text, re.I):
                            if re.search(".*[жш]ать$", verb.text, re.I):
                                return WordStructure(verb.text[:-3] + "у", get_rhytmic_structure(verb)[:-1])
                            elif re.search(".*гнать$", verb.text, re.I):
                                return WordStructure(verb.text[:-4] + "оню",
                                                     get_rhytmic_structure(verb)[:-1] + "-^")
                            else:
                                return WordStructure(verb.text[:-3] + "ю", get_rhytmic_structure(verb)[:-1])
                    else:
                        if re.search(".*есть$", verb.text, re.I):
                            if verb.text == "есть":
                                return WordStructure("ем", "^")
                            else:
                                return WordStructure(verb.text[:-3] + "даю", "-^")
                        elif re.search(".*дать$", verb.text, re.I):
                            return WordStructure(verb.text[:-2] + "ю", get_rhytmic_structure(verb))
                        elif re.search(".+быть$", verb.text, re.I):
                            return WordStructure(verb.text[:-2] + "ваю", get_rhytmic_structure(verb))
                        elif verb.text == "хотеть":
                            return WordStructure("хочу", "-^")
                        elif verb.text == "бежать":
                            return WordStructure("бегу", "-^")
                        elif verb.text == "чтить":
                            return WordStructure("чту", "^")
                        elif verb.text == "ехать":
                            return WordStructure("еду", "^-")
                        elif verb.text == "идти":
                            return WordStructure("иду", "-^")
                        elif verb.text == "быть":
                            return WordStructure("есть", "^")
                else:
                    if verb.conjugation == 1:
                        if re.search(".*еть$", verb.text, re.I):
                            if re.search(".*деть$", verb.text, re.I):
                                return WordStructure(verb.text[:-4] + "жу", get_rhytmic_structure(verb))
                            elif re.search(".*теть$", verb.text, re.I):
                                return WordStructure(verb.text[:-4] + "чу", get_rhytmic_structure(verb))
                            elif re.search(".*петь$", verb.text, re.I):
                                return WordStructure(verb.text[:-3] + "ою",
                                                     get_rhytmic_structure(verb)[:-2] + "-^")
                            else:
                                return WordStructure(verb.text[:-2] + "ю", get_rhytmic_structure(verb) + "-")
                        elif re.search(".*ать$", verb.text, re.I):
                            if re.search(".*сать$", verb.text, re.I) \
                                    and verb.stress_position == verb.syllables_count:
                                return WordStructure(verb.text[:-4] + "шу", get_rhytmic_structure(verb))
                            elif re.search(".*певать$", verb.text, re.I):
                                return WordStructure(verb.text[:-2] + "ю", get_rhytmic_structure(verb) + "-")
                            elif re.search(".*[ое]вать$", verb.text, re.I):
                                if verb.stress_position == verb.syllables_count:
                                    return WordStructure(verb.text[:-5] + "ую",
                                                         get_rhytmic_structure(verb)[:-2] + "^-")
                                else:
                                    return WordStructure(verb.text[:-5] + "ую", get_rhytmic_structure(verb))
                            elif re.search(".*авать$", verb.text, re.I):
                                return WordStructure(verb.text[:-4] + "ю", get_rhytmic_structure(verb))
                            elif re.search(".*скать$", verb.text, re.I):
                                return WordStructure(verb.text[:-5] + "щу", get_rhytmic_structure(verb))
                            else:
                                return WordStructure(verb.text[:-2] + "ю", get_rhytmic_structure(verb) + "-")
                        elif re.search(".*ить", verb.text, re.I):
                            if re.search(".*рить$", verb.text, re.I):
                                return WordStructure(verb.text[:-3] + "ею", get_rhytmic_structure(verb) + "-")
                            else:
                                return WordStructure(verb.text[:-3] + "ю", get_rhytmic_structure(verb))
                        elif re.search(".*ять$", verb.text, re.I):
                            if re.search(".*[ал]ять$", verb.text, re.I) \
                                    and verb.stress_position == verb.syllables_count:
                                return WordStructure(verb.text[:-2] + "ю", get_rhytmic_structure(verb) + "-")
                            else:
                                return WordStructure(verb.text[:-3] + "ю", get_rhytmic_structure(verb) + "-")
                        elif re.search(".*оть$", verb.text, re.I):
                            return WordStructure(verb.text[:-3] + "ю", get_rhytmic_structure(verb))
                        elif re.search(".*ыть$", verb.text, re.I):
                            return WordStructure(verb.text[:-3] + "ою", get_rhytmic_structure(verb) + "-")
                    elif verb.conjugation == 2:
                        if re.search(".*ить$", verb.text, re.I):
                            if re.search(".*зить$", verb.text, re.I):
                                return WordStructure(verb.text[:-4] + "жу", get_rhytmic_structure(verb))
                            elif re.search(".*дить$", verb.text, re.I):
                                return WordStructure(verb.text[:-4] + "жу", get_rhytmic_structure(verb))
                            elif re.search(".*тить$", verb.text, re.I):
                                return WordStructure(verb.text[:-4] + "чу", get_rhytmic_structure(verb))
                            elif re.search(".*сить$", verb.text, re.I):
                                return WordStructure(verb.text[:-4] + "шу", get_rhytmic_structure(verb))
                            else:
                                return WordStructure(verb.text[:-3] + "ю", get_rhytmic_structure(verb)[:-1] + "^")
                        elif re.search(".*еть$", verb.text, re.I):
                            if re.search(".*теть$", verb.text, re.I):
                                return WordStructure(verb.text[:-4] + "чу", get_rhytmic_structure(verb))
                            elif re.search(".*деть$", verb.text, re.I):
                                return WordStructure(verb.text[:-4] + "жу", get_rhytmic_structure(verb))
                            elif re.search(".*петь$", verb.text, re.I):
                                return WordStructure(verb.text[:-3] + "лю", get_rhytmic_structure(verb))
                            elif re.search(".*сеть$", verb.text, re.I):
                                return WordStructure(verb.text[:-4] + "шу", get_rhytmic_structure(verb))
                            else:
                                return WordStructure(verb.text[:-3] + "ю", get_rhytmic_structure(verb))
                        elif re.search(".*ать$", verb.text, re.I):
                            if re.search(".*[жш]ать$", verb.text, re.I):
                                return WordStructure(verb.text[:-3] + "у", get_rhytmic_structure(verb))
                            elif re.search(".*гнать$", verb.text, re.I):
                                return WordStructure(verb.text[:-4] + "оню",
                                                     get_rhytmic_structure(verb)[:-1] + "-^")
                            else:
                                return WordStructure(verb.text[:-3] + "ю", get_rhytmic_structure(verb))
                    else:
                        if re.search(".*есть$", verb.text, re.I):
                            if verb.text == "есть":
                                return WordStructure("ем", "^")
                            else:
                                return WordStructure(verb.text[:-3] + "даю", "-^")
                        elif re.search(".*дать$", verb.text, re.I):
                            return WordStructure(verb.text[:-2] + "ю", get_rhytmic_structure(verb))
                        elif re.search(".+быть$", verb.text, re.I):
                            return WordStructure(verb.text[:-2] + "ваю", get_rhytmic_structure(verb))
                        elif verb.text == "хотеть":
                            return WordStructure("хочу", "-^")
                        elif verb.text == "бежать":
                            return WordStructure("бегу", "-^")
                        elif verb.text == "чтить":
                            return WordStructure("чту", "^")
                        elif verb.text == "ехать":
                            return WordStructure("еду", "^-")
                        elif verb.text == "идти":
                            return WordStructure("иду", "-^")
                        elif verb.text == "быть":
                            return WordStructure("есть", "^")

            elif person == 2:
                if verb.reflexive:
                    if verb.conjugation == 1:
                        if re.search(".*еться$", verb.text, re.I):
                            if re.search(".*деться$", verb.text, re.I):
                                return WordStructure(verb.text[:-4] + "дишься", get_rhytmic_structure(verb))
                            elif re.search(".*теться$", verb.text, re.I):
                                return WordStructure(verb.text[:-4] + "тишься", get_rhytmic_structure(verb))
                            elif re.search(".*петься$", verb.text, re.I):
                                return WordStructure(verb.text[:-3] + "оёшься",
                                                     get_rhytmic_structure(verb)[:-1] + "-^")
                            else:
                                return WordStructure(verb.text[:-2] + "ешься", get_rhytmic_structure(verb) + "-")
                        elif re.search(".*аться$", verb.text, re.I):
                            if re.search(".*саться$", verb.text, re.I) \
                                    and verb.stress_position + 1 == verb.syllables_count:
                                return WordStructure(verb.text[:-6] + "шешься",
                                                     get_rhytmic_structure(verb)[:-3] + "^--")
                            elif re.search(".*певаться$", verb.text, re.I):
                                return WordStructure(verb.text[:-2] + "ешься", get_rhytmic_structure(verb) + "-")
                            elif re.search(".*[ое]ваться$", verb.text, re.I):
                                if re.search(".*оваться$", verb.text, re.I) \
                                        and verb.stress_position + 1 == verb.syllables_count:
                                    return WordStructure(verb.text[:-7] + "уешься",
                                                         get_rhytmic_structure(verb)[:-3] + "^--")
                                elif re.search(".*еваться$", verb.text, re.I) \
                                        and verb.stress_position + 1 == verb.syllables_count:
                                    return WordStructure(verb.text[:-4] + "ешься",
                                                         get_rhytmic_structure(verb)[:-2] + "^--")
                                else:
                                    return WordStructure(verb.text[:-7] + "аешься", get_rhytmic_structure(verb))
                            elif re.search(".*аваться$", verb.text, re.I):
                                return WordStructure(verb.text[:-4] + "ёшься", get_rhytmic_structure(verb))
                            elif re.search(".*скаться$", verb.text, re.I):
                                return WordStructure(verb.text[:-5] + "щешься",
                                                     get_rhytmic_structure(verb)[:-2] + "^-")
                            else:
                                return WordStructure(verb.text[:-4] + "ешься", get_rhytmic_structure(verb) + "-")
                        elif re.search(".*иться", verb.text, re.I):
                            if re.search(".*риться$", verb.text, re.I):
                                return WordStructure(verb.text[:-5] + "еешься", get_rhytmic_structure(verb) + "-")
                            else:
                                return WordStructure(verb.text[:-3] + "ешься",
                                                     get_rhytmic_structure(verb)[:-2] + "^-")
                        elif re.search(".*яться$", verb.text, re.I):
                            if re.search(".*[ал]яться", verb.text, re.I) \
                                    and verb.stress_position + 1 == verb.syllables_count:
                                return WordStructure(verb.text[:-4] + "ешься", get_rhytmic_structure(verb) + "-")
                            else:
                                return WordStructure(verb.text[:-5] + "ёшься", get_rhytmic_structure(verb))
                        elif re.search(".*оться$", verb.text, re.I):
                            return WordStructure(verb.text[:-3] + "ешься", get_rhytmic_structure(verb)[:-2] + "^-")
                        elif re.search(".*ыться$", verb.text, re.I):
                            return WordStructure(verb.text[:-3] + "оешься", get_rhytmic_structure(verb) + "-")
                    elif verb.conjugation == 2:
                        if re.search(".*иться$", verb.text, re.I):
                            if re.search(".*зиться$", verb.text, re.I):
                                return WordStructure(verb.text[:-6] + "зишься",
                                                     get_rhytmic_structure(verb)[:-2] + "^-")
                            if re.search(".*диться$", verb.text, re.I):
                                return WordStructure(verb.text[:-6] + "дишься",
                                                     get_rhytmic_structure(verb)[:-2] + "^-")
                            elif re.search(".*титься$", verb.text, re.I):
                                return WordStructure(verb.text[:-6] + "тишься",
                                                     get_rhytmic_structure(verb)[:-3] + "^--")
                            elif re.search(".*ситься$", verb.text, re.I):
                                return WordStructure(verb.text[:-6] + "сишься",
                                                     get_rhytmic_structure(verb)[:-2] + "^-")
                            else:
                                return WordStructure(verb.text[:-5] + "ишься", get_rhytmic_structure(verb)[:-3]
                                                     + "^--")
                        elif re.search(".*еться$", verb.text, re.I):
                            if re.search(".*теться$", verb.text, re.I):
                                return WordStructure(verb.text[:-6] + "тишься",
                                                     get_rhytmic_structure(verb)[:-3] + "^--")
                            elif re.search(".*деться$", verb.text, re.I):
                                return WordStructure(verb.text[:-6] + "дишься",
                                                     get_rhytmic_structure(verb)[:-3] + "^--")
                            elif re.search(".*петься$", verb.text, re.I):
                                return WordStructure(verb.text[:-5] + "ишься",
                                                     get_rhytmic_structure(verb)[:-3] + "^--")
                            elif re.search(".*сеться$", verb.text, re.I):
                                return WordStructure(verb.text[:-6] + "сишься",
                                                     get_rhytmic_structure(verb)[:-3] + "^--")
                            else:
                                return WordStructure(verb.text[:-5] + "ишься",
                                                     get_rhytmic_structure(verb)[:-3] + "^--")
                        elif re.search(".*аться$", verb.text, re.I):
                            if re.search(".*[жш]аться$", verb.text, re.I):
                                return WordStructure(verb.text[:-3] + "ишься",
                                                     get_rhytmic_structure(verb)[:-2] + "^-")
                            elif re.search(".*гнаться$", verb.text, re.I):
                                return WordStructure(verb.text[:-4] + "онишься", get_rhytmic_structure(verb) + "-")
                            else:
                                return WordStructure(verb.text[:-3] + "ишься", get_rhytmic_structure(verb))
                    else:
                        if re.search(".*есть$", verb.text, re.I):
                            if verb.text == "есть":
                                return WordStructure("ешься", "^")
                            else:
                                return WordStructure(verb.text[:-3] + "даешься", get_rhytmic_structure(verb))
                        elif re.search(".*дать$", verb.text, re.I):
                            return WordStructure(verb.text[:-2] + "ешься", get_rhytmic_structure(verb))
                        elif re.search(".+быть$", verb.text, re.I):
                            return WordStructure(verb.text[:-2] + "ваешься", get_rhytmic_structure(verb))
                        elif verb.text == "хотеться":
                            return WordStructure("хочешься", "^-")
                        elif verb.text == "бежаться":
                            return WordStructure("бежишься", "-^")
                        elif verb.text == "чтить":
                            return WordStructure("чтишь", "^")
                        elif verb.text == "ехаться":
                            return WordStructure("едешься", "^-")
                        elif verb.text == "идтись":
                            return WordStructure("идёшься", "-^")
                        elif verb.text == "быть":
                            return WordStructure("есть", "^")
                else:
                    if verb.conjugation == 1:
                        if re.search(".*еть$", verb.text, re.I):
                            if re.search(".*деть$", verb.text, re.I):
                                return WordStructure(verb.text[:-4] + "дишь", get_rhytmic_structure(verb))
                            elif re.search(".*теть$", verb.text, re.I):
                                return WordStructure(verb.text[:-4] + "тишь", get_rhytmic_structure(verb))
                            elif re.search(".*петь$", verb.text, re.I):
                                return WordStructure(verb.text[:-3] + "оёшь",
                                                     get_rhytmic_structure(verb)[:-1] + "-^")
                            else:
                                return WordStructure(verb.text[:-2] + "ешь", get_rhytmic_structure(verb) + "-")
                        elif re.search(".*ать$", verb.text, re.I):
                            if re.search(".*сать$", verb.text, re.I) \
                                    and verb.stress_position == verb.syllables_count:
                                return WordStructure(verb.text[:-4] + "шешь",
                                                     get_rhytmic_structure(verb)[:-2] + "^-")
                            elif re.search(".*певать$", verb.text, re.I):
                                return WordStructure(verb.text[:-2] + "ешь", get_rhytmic_structure(verb) + "-")
                            elif re.search(".*[ое]вать$", verb.text, re.I):
                                if verb.stress_position == verb.syllables_count:
                                    return WordStructure(verb.text[:-5] + "уешь", get_rhytmic_structure(verb)[:-2]
                                                         + "^-")
                                else:
                                    return WordStructure(verb.text[:-5] + "уешь", get_rhytmic_structure(verb))
                            elif re.search(".*авать$", verb.text, re.I):
                                return WordStructure(verb.text[:-4] + "ёшь", get_rhytmic_structure(verb))
                            elif re.search(".*скать$", verb.text, re.I):
                                return WordStructure(verb.text[:-5] + "щешь",
                                                     get_rhytmic_structure(verb)[:-2] + "^-")
                            else:
                                return WordStructure(verb.text[:-2] + "ешь", get_rhytmic_structure(verb) + "-")
                        elif re.search(".*ить", verb.text, re.I):
                            if re.search(".*рить$", verb.text, re.I):
                                return WordStructure(verb.text[:-3] + "еешь", get_rhytmic_structure(verb) + "-")
                            else:
                                return WordStructure(verb.text[:-3] + "ешь",
                                                     get_rhytmic_structure(verb)[:-2] + "^-")
                        elif re.search(".*ять$", verb.text, re.I):
                            if re.search(".*[ал]ять", verb.text, re.I) \
                                    and verb.stress_position == verb.syllables_count:
                                return WordStructure(verb.text[:-2] + "ешь", get_rhytmic_structure(verb) + "-")
                            else:
                                return WordStructure(verb.text[:-3] + "ешь", get_rhytmic_structure(verb))
                        elif re.search(".*оть$", verb.text, re.I):
                            return WordStructure(verb.text[:-3] + "ешь", get_rhytmic_structure(verb)[:-2] + "^-")
                        elif re.search(".*ыть$", verb.text, re.I):
                            return WordStructure(verb.text[:-3] + "оешь", get_rhytmic_structure(verb) + "-")
                    elif verb.conjugation == 2:
                        if re.search(".*ить$", verb.text, re.I):
                            if re.search(".*зить$", verb.text, re.I):
                                return WordStructure(verb.text[:-4] + "зишь",
                                                     get_rhytmic_structure(verb)[:-2] + "^-")
                            if re.search(".*дить$", verb.text, re.I):
                                return WordStructure(verb.text[:-4] + "дишь",
                                                     get_rhytmic_structure(verb)[:-2] + "^-")
                            elif re.search(".*тить$", verb.text, re.I):
                                return WordStructure(verb.text[:-4] + "тишь",
                                                     get_rhytmic_structure(verb)[:-2] + "^-")
                            elif re.search(".*сить$", verb.text, re.I):
                                return WordStructure(verb.text[:-4] + "сишь",
                                                     get_rhytmic_structure(verb)[:-2] + "^-")
                            else:
                                return WordStructure(verb.text[:-3] + "ишь",
                                                     get_rhytmic_structure(verb)[:-2] + "^-")
                        elif re.search(".*еть$", verb.text, re.I):
                            if re.search(".*теть$", verb.text, re.I):
                                return WordStructure(verb.text[:-4] + "тишь",
                                                     get_rhytmic_structure(verb)[:-2] + "^-")
                            elif re.search(".*деть$", verb.text, re.I):
                                return WordStructure(verb.text[:-4] + "дишь",
                                                     get_rhytmic_structure(verb)[:-2] + "^-")
                            elif re.search(".*петь$", verb.text, re.I):
                                return WordStructure(verb.text[:-3] + "ишь",
                                                     get_rhytmic_structure(verb)[:-2] + "^-")
                            elif re.search(".*сеть$", verb.text, re.I):
                                return WordStructure(verb.text[:-4] + "сишь",
                                                     get_rhytmic_structure(verb)[:-2] + "^-")
                            else:
                                return WordStructure(verb.text[:-3] + "ишь",
                                                     get_rhytmic_structure(verb)[:-2] + "^-")
                        elif re.search(".*ать$", verb.text, re.I):
                            if re.search(".*[жш]ать$", verb.text, re.I):
                                return WordStructure(verb.text[:-3] + "ишь",
                                                     get_rhytmic_structure(verb)[:-2] + "^-")
                            elif re.search(".*гнать$", verb.text, re.I):
                                return WordStructure(verb.text[:-4] + "онишь", get_rhytmic_structure(verb) + "-")
                            else:
                                return WordStructure(verb.text[:-3] + "ишь", get_rhytmic_structure(verb))
                    else:
                        if re.search(".*есть$", verb.text, re.I):
                            if verb.text == "есть":
                                return WordStructure("ешь", "^")
                            else:
                                return WordStructure(verb.text[:-3] + "даешь", get_rhytmic_structure(verb))
                        elif re.search(".*дать$", verb.text, re.I):
                            return WordStructure(verb.text[:-2] + "ешь", get_rhytmic_structure(verb))
                        elif re.search(".+быть$", verb.text, re.I):
                            return WordStructure(verb.text[:-2] + "ваешь", get_rhytmic_structure(verb))
                        elif verb.text == "хотеть":
                            return WordStructure("хочешь", "^-")
                        elif verb.text == "бежать":
                            return WordStructure("бежишь", "-^")
                        elif verb.text == "чтить":
                            return WordStructure("чтишь", "^")
                        elif verb.text == "ехать":
                            return WordStructure("едешь", "^-")
                        elif verb.text == "идти":
                            return WordStructure("идёшь", "-^")
                        elif verb.text == "быть":
                            return WordStructure("есть", "^")

            elif person == 3:
                if verb.reflexive:
                    if verb.conjugation == 1:
                        if re.search(".*еться$", verb.text, re.I):
                            if re.search(".*деться$", verb.text, re.I):
                                return WordStructure(verb.text[:-4] + "дится", get_rhytmic_structure(verb))
                            elif re.search(".*теться$", verb.text, re.I):
                                return WordStructure(verb.text[:-4] + "тится", get_rhytmic_structure(verb))
                            elif re.search(".*петься$", verb.text, re.I):
                                return WordStructure(verb.text[:-3] + "оётся",
                                                     get_rhytmic_structure(verb)[:-1] + "-^")
                            else:
                                return WordStructure(verb.text[:-2] + "ется", get_rhytmic_structure(verb) + "-")
                        elif re.search(".*аться$", verb.text, re.I):
                            if re.search(".*саться$", verb.text, re.I):
                                if verb.stress_position + 1 == verb.syllables_count:
                                    return WordStructure(verb.text[:-6] + "шется", get_rhytmic_structure(verb)[:-3]
                                                         + "^--")
                                else:
                                    return WordStructure(verb.text[:-4] + "шется", get_rhytmic_structure(verb))
                            elif re.search(".*певаться$", verb.text, re.I):
                                return WordStructure(verb.text[:-2] + "ется", get_rhytmic_structure(verb) + "-")
                            elif re.search(".*[ое]ваться$", verb.text, re.I):
                                if re.search(".*оваться$", verb.text, re.I) \
                                        and verb.stress_position + 1 == verb.syllables_count:
                                    return WordStructure(verb.text[:-7] + "уется", get_rhytmic_structure(verb)[:-3]
                                                         + "^--")
                                elif re.search(".*еваться$", verb.text, re.I) \
                                        and verb.stress_position + 1 == verb.syllables_count:
                                    return WordStructure(verb.text[:-5] + "ается", get_rhytmic_structure(verb)[:-2]
                                                         + "^-")
                                else:
                                    return WordStructure(verb.text[:-5] + "уется", get_rhytmic_structure(verb))
                            elif re.search(".*аваться$", verb.text, re.I):
                                return WordStructure(verb.text[:-4] + "ётся", get_rhytmic_structure(verb))
                            elif re.search(".*скаться$", verb.text, re.I):
                                return WordStructure(verb.text[:-5] + "щется",
                                                     get_rhytmic_structure(verb)[:-2] + "^-")
                            else:
                                return WordStructure(verb.text[:-4] + "ется", get_rhytmic_structure(verb) + "-")
                        elif re.search(".*иться$", verb.text, re.I):
                            if re.search(".*риться$", verb.text, re.I):
                                return WordStructure(verb.text[:-5] + "еется", get_rhytmic_structure(verb) + "-")
                            else:
                                return WordStructure(verb.text[:-3] + "ется",
                                                     get_rhytmic_structure(verb)[:-2] + "^-")
                        elif re.search(".*яться$", verb.text, re.I):
                            if re.search(".*[ал]яться$", verb.text,
                                         re.I) and verb.stress_position + 1 == verb.syllables_count:
                                return WordStructure(verb.text[:-4] + "ется", get_rhytmic_structure(verb) + "-")
                            else:
                                return WordStructure(verb.text[:-5] + "ётся", get_rhytmic_structure(verb))
                        elif re.search(".*оться$", verb.text, re.I):
                            return WordStructure(verb.text[:-3] + "ется", get_rhytmic_structure(verb)[:-2] + "^-")
                        elif re.search(".*ыться$", verb.text, re.I):
                            return WordStructure(verb.text[:-3] + "оется", get_rhytmic_structure(verb) + "-")
                    elif verb.conjugation == 2:
                        if re.search(".*иться$", verb.text, re.I):
                            if re.search(".*зиться$", verb.text, re.I):
                                if verb.text == "возиться":
                                    return WordStructure(verb.text[:-6] + "зится", get_rhytmic_structure(verb)[:-2]
                                                         + "^-")
                                else:
                                    return WordStructure(verb.text[:-6] + "зится", get_rhytmic_structure(verb))
                            if re.search(".*диться$", verb.text, re.I):
                                return WordStructure(verb.text[:-6] + "дится",
                                                     get_rhytmic_structure(verb)[:-2] + "^-")
                            elif re.search(".*титься$", verb.text, re.I):
                                return WordStructure(verb.text[:-6] + "тится",
                                                     get_rhytmic_structure(verb)[:-3] + "^--")
                            elif re.search(".*ситься$", verb.text, re.I):
                                return WordStructure(verb.text[:-6] + "сится",
                                                     get_rhytmic_structure(verb)[:-2] + "^-")
                            else:
                                return WordStructure(verb.text[:-5] + "ится",
                                                     get_rhytmic_structure(verb)[:-3] + "^--")
                        elif re.search(".*еться$", verb.text, re.I):
                            if re.search(".*теться$", verb.text, re.I):
                                return WordStructure(verb.text[:-6] + "тится",
                                                     get_rhytmic_structure(verb)[:-3] + "^--")
                            elif re.search(".*деться$", verb.text, re.I):
                                return WordStructure(verb.text[:-6] + "дится",
                                                     get_rhytmic_structure(verb)[:-3] + "^--")
                            elif re.search(".*петься$", verb.text, re.I):
                                return WordStructure(verb.text[:-6] + "пится",
                                                     get_rhytmic_structure(verb)[:-3] + "^--")
                            elif re.search(".*сеться$", verb.text, re.I):
                                return WordStructure(verb.text[:-4] + "сится",
                                                     get_rhytmic_structure(verb)[:-3] + "^--")
                            else:
                                return WordStructure(verb.text[:-3] + "ится",
                                                     get_rhytmic_structure(verb)[:-2] + "^-")
                        elif re.search(".*аться$", verb.text, re.I):
                            if re.search(".*[жш]аться$", verb.text, re.I):
                                return WordStructure(verb.text[:-3] + "ится",
                                                     get_rhytmic_structure(verb)[:-2] + "^-")
                            elif re.search(".*гнаться$", verb.text, re.I):
                                return WordStructure(verb.text[:-4] + "онится", get_rhytmic_structure(verb) + "-")
                            else:
                                return WordStructure(verb.text[:-3] + "ится", get_rhytmic_structure(verb))
                    else:
                        if re.search(".*есться$", verb.text, re.I):
                            if verb.text == "есть":
                                return WordStructure("естся", "^")
                            else:
                                return WordStructure(verb.text[:-3] + "дается", get_rhytmic_structure(verb))
                        elif re.search(".*дать$", verb.text, re.I):
                            return WordStructure(verb.text[:-2] + "ется", get_rhytmic_structure(verb))
                        elif re.search(".+быть$", verb.text, re.I):
                            return WordStructure(verb.text[:-2] + "вается", get_rhytmic_structure(verb))
                        elif verb.text == "хотеться":
                            return WordStructure("хочется", "^-")
                        elif verb.text == "бежаться":
                            return WordStructure("бежится", "-^")
                        elif verb.text == "чтиться":
                            return WordStructure("чтится", "^")
                        elif verb.text == "ехаться":
                            return WordStructure("едется", "^-")
                        elif verb.text == "идтись":
                            return WordStructure("идётся", "-^")
                        elif verb.text == "быть":
                            return WordStructure("есть", "^")
                else:
                    if verb.conjugation == 1:
                        if re.search(".*еть$", verb.text, re.I):
                            if re.search(".*деть$", verb.text, re.I):
                                return WordStructure(verb.text[:-4] + "дит", get_rhytmic_structure(verb))
                            elif re.search(".*теть$", verb.text, re.I):
                                return WordStructure(verb.text[:-4] + "тит", get_rhytmic_structure(verb))
                            elif re.search(".*петь$", verb.text, re.I):
                                return WordStructure(verb.text[:-3] + "оёт",
                                                     get_rhytmic_structure(verb)[:-1] + "-^")
                            else:
                                return WordStructure(verb.text[:-2] + "ет", get_rhytmic_structure(verb) + "-")
                        elif re.search(".*ать$", verb.text, re.I):
                            if re.search(".*сать$", verb.text, re.I):
                                if verb.stress_position == verb.syllables_count:
                                    return WordStructure(verb.text[:-4] + "шет", get_rhytmic_structure(verb)[:-2]
                                                         + "^-")
                                else:
                                    return WordStructure(verb.text[:-4] + "шет", get_rhytmic_structure(verb))
                            elif re.search(".*певать$", verb.text, re.I):
                                return WordStructure(verb.text[:-2] + "ет", get_rhytmic_structure(verb) + "-")
                            elif re.search(".*[ое]вать$", verb.text, re.I):
                                if verb.stress_position == verb.syllables_count:
                                    return WordStructure(verb.text[:-5] + "ует", get_rhytmic_structure(verb)[:-2]
                                                         + "^-")
                                else:
                                    return WordStructure(verb.text[:-5] + "ует", get_rhytmic_structure(verb))
                            elif re.search(".*авать$", verb.text, re.I):
                                return WordStructure(verb.text[:-4] + "ёт", get_rhytmic_structure(verb))
                            elif re.search(".*скать$", verb.text, re.I):
                                return WordStructure(verb.text[:-5] + "щет",
                                                     get_rhytmic_structure(verb)[:-2] + "^-")
                            else:
                                return WordStructure(verb.text[:-2] + "ет", get_rhytmic_structure(verb) + "-")
                        elif re.search(".*ить", verb.text, re.I):
                            if re.search(".*рить$", verb.text, re.I):
                                return WordStructure(verb.text[:-3] + "еет", get_rhytmic_structure(verb) + "-")
                            else:
                                return WordStructure(verb.text[:-3] + "ет", get_rhytmic_structure(verb)[:-2] + "^-")
                        elif re.search(".*ять$", verb.text, re.I):
                            if re.search(".*[ал]ять", verb.text, re.I) \
                                    and verb.stress_position == verb.syllables_count:
                                return WordStructure(verb.text[:-2] + "ет", get_rhytmic_structure(verb) + "-")
                            else:
                                return WordStructure(verb.text[:-3] + "ет", get_rhytmic_structure(verb))
                        elif re.search(".*оть$", verb.text, re.I):
                            return WordStructure(verb.text[:-3] + "ет", get_rhytmic_structure(verb)[:-2] + "^-")
                        elif re.search(".*ыть$", verb.text, re.I):
                            return WordStructure(verb.text[:-3] + "оет", get_rhytmic_structure(verb) + "-")
                    elif verb.conjugation == 2:
                        if re.search(".*ить$", verb.text, re.I):
                            if re.search(".*зить$", verb.text, re.I):
                                if verb.text == "возить":
                                    return WordStructure(verb.text[:-4] + "зит", get_rhytmic_structure(verb)[:-2]
                                                         + "^-")
                                else:
                                    return WordStructure(verb.text[:-4] + "зит", get_rhytmic_structure(verb))
                            if re.search(".*дить$", verb.text, re.I):
                                return WordStructure(verb.text[:-4] + "дит",
                                                     get_rhytmic_structure(verb)[:-2] + "^-")
                            elif re.search(".*тить$", verb.text, re.I):
                                return WordStructure(verb.text[:-4] + "тит",
                                                     get_rhytmic_structure(verb)[:-2] + "^-")
                            elif re.search(".*сить$", verb.text, re.I):
                                return WordStructure(verb.text[:-4] + "сит",
                                                     get_rhytmic_structure(verb)[:-2] + "^-")
                            else:
                                return WordStructure(verb.text[:-3] + "ит",
                                                     get_rhytmic_structure(verb)[:-2] + "^-")
                        elif re.search(".*еть$", verb.text, re.I):
                            if re.search(".*теть$", verb.text, re.I):
                                return WordStructure(verb.text[:-4] + "тит",
                                                     get_rhytmic_structure(verb)[:-2] + "^-")
                            elif re.search(".*деть$", verb.text, re.I):
                                return WordStructure(verb.text[:-4] + "дит",
                                                     get_rhytmic_structure(verb)[:-2] + "^-")
                            elif re.search(".*петь$", verb.text, re.I):
                                return WordStructure(verb.text[:-3] + "ит",
                                                     get_rhytmic_structure(verb)[:-2] + "^-")
                            elif re.search(".*сеть$", verb.text, re.I):
                                return WordStructure(verb.text[:-4] + "сит",
                                                     get_rhytmic_structure(verb)[:-2] + "^-")
                            else:
                                return WordStructure(verb.text[:-3] + "ит", get_rhytmic_structure(verb)[:-2] + "^-")
                        elif re.search(".*ать$", verb.text, re.I):
                            if re.search(".*[жш]ать$", verb.text, re.I):
                                return WordStructure(verb.text[:-3] + "ит", get_rhytmic_structure(verb)[:-2] + "^-")
                            elif re.search(".*гнать$", verb.text, re.I):
                                return WordStructure(verb.text[:-4] + "онит", get_rhytmic_structure(verb) + "-")
                            else:
                                return WordStructure(verb.text[:-3] + "ит", get_rhytmic_structure(verb))
                    else:
                        if re.search(".*есть$", verb.text, re.I):
                            if verb.text == "есть":
                                return WordStructure("ест", "^")
                            else:
                                return WordStructure(verb.text[:-3] + "дает", get_rhytmic_structure(verb))
                        elif re.search(".*дать$", verb.text, re.I):
                            return WordStructure(verb.text[:-2] + "ет", get_rhytmic_structure(verb))
                        elif re.search(".+быть$", verb.text, re.I):
                            return WordStructure(verb.text[:-2] + "вает", get_rhytmic_structure(verb))
                        elif verb.text == "хотеть":
                            return WordStructure("хочет", "^-")
                        elif verb.text == "бежать":
                            return WordStructure("бежит", "-^")
                        elif verb.text == "чтить":
                            return WordStructure("чтит", "^")
                        elif verb.text == "ехать":
                            return WordStructure("едет", "^-")
                        elif verb.text == "идти":
                            return WordStructure("идёт", "-^")
                        elif verb.text == "быть":
                            return WordStructure("есть", "^")

        else:
            if person == 1:
                if verb.reflexive:
                    if verb.conjugation == 1:
                        if re.search(".*еться$", verb.text, re.I):
                            if re.search(".*деться$", verb.text, re.I):
                                return WordStructure(verb.text[:-4] + "димся", get_rhytmic_structure(verb))
                            elif re.search(".*теться$", verb.text, re.I):
                                return WordStructure(verb.text[:-4] + "тимся", get_rhytmic_structure(verb))
                            elif re.search(".*петься$", verb.text, re.I):
                                return WordStructure(verb.text[:-3] + "оёмся",
                                                     get_rhytmic_structure(verb)[:-1] + "-^")
                            else:
                                return WordStructure(verb.text[:-2] + "емся", get_rhytmic_structure(verb) + "-")
                        elif re.search(".*аться$", verb.text, re.I):
                            if re.search(".*саться$", verb.text, re.I) \
                                    and verb.stress_position + 1 == verb.syllables_count:
                                return WordStructure(verb.text[:-6] + "шемся",
                                                     get_rhytmic_structure(verb)[:-3] + "^--")
                            elif re.search(".*певаться$", verb.text, re.I):
                                return WordStructure(verb.text[:-2] + "емся", get_rhytmic_structure(verb) + "-")
                            elif re.search(".*[ое]ваться$", verb.text, re.I):
                                if re.search(".*оваться$", verb.text, re.I) \
                                        and verb.stress_position + 1 == verb.syllables_count:
                                    return WordStructure(verb.text[:-7] + "уемся",
                                                         get_rhytmic_structure(verb)[:-3] + "^--")
                                elif re.search(".*еваться$", verb.text, re.I) \
                                        and verb.stress_position + 1 == verb.syllables_count:
                                    return WordStructure(verb.text[:-5] + "аемся",
                                                         get_rhytmic_structure(verb)[:-2] + "^--")
                                else:
                                    return WordStructure(verb.text[:-5] + "уемся", get_rhytmic_structure(verb))
                            elif re.search(".*аваться$", verb.text, re.I):
                                return WordStructure(verb.text[:-4] + "ёмся", get_rhytmic_structure(verb))
                            elif re.search(".*скаться$", verb.text, re.I):
                                return WordStructure(verb.text[:-5] + "щемся",
                                                     get_rhytmic_structure(verb)[:-2] + "^-")
                            else:
                                return WordStructure(verb.text[:-4] + "емся", get_rhytmic_structure(verb) + "-")
                        elif re.search(".*иться", verb.text, re.I):
                            if re.search(".*риться$", verb.text, re.I):
                                return WordStructure(verb.text[:-5] + "еемся", get_rhytmic_structure(verb) + "-")
                            else:
                                return WordStructure(verb.text[:-5] + "емся",
                                                     get_rhytmic_structure(verb)[:-2] + "^-")
                        elif re.search(".*яться$", verb.text, re.I):
                            if re.search(".*[ал]яться$", verb.text, re.I) \
                                    and verb.stress_position + 1 == verb.syllables_count:
                                return WordStructure(verb.text[:-4] + "емся", get_rhytmic_structure(verb) + "-")
                            else:
                                return WordStructure(verb.text[:-5] + "ёмся", get_rhytmic_structure(verb))
                        elif re.search(".*оться$", verb.text, re.I):
                            return WordStructure(verb.text[:-3] + "емся", get_rhytmic_structure(verb)[:-2] + "^-")
                        elif re.search(".*ыться$", verb.text, re.I):
                            return WordStructure(verb.text[:-3] + "оемся", get_rhytmic_structure(verb) + "-")
                    elif verb.conjugation == 2:
                        if re.search(".*иться$", verb.text, re.I):
                            if re.search(".*озиться$", verb.text, re.I):
                                return WordStructure(verb.text[:-6] + "зимся",
                                                     get_rhytmic_structure(verb)[:-3] + "^--")
                            elif re.search(".*зиться$", verb.text, re.I):
                                return WordStructure(verb.text[:-6] + "зимся", get_rhytmic_structure(verb))
                            elif re.search(".*диться$", verb.text, re.I):
                                return WordStructure(verb.text[:-6] + "димся",
                                                     get_rhytmic_structure(verb)[:-3] + "^--")
                            elif re.search(".*титься$", verb.text, re.I):
                                return WordStructure(verb.text[:-6] + "тимся",
                                                     get_rhytmic_structure(verb)[:-3] + "^--")
                            elif re.search(".*ситься$", verb.text, re.I):
                                return WordStructure(verb.text[:-6] + "симся",
                                                     get_rhytmic_structure(verb)[:-3] + "^--")
                            else:
                                return WordStructure(verb.text[:-5] + "имся",
                                                     get_rhytmic_structure(verb)[:-3] + "^--")
                        elif re.search(".*еться$", verb.text, re.I):
                            if re.search(".*теться$", verb.text, re.I):
                                return WordStructure(verb.text[:-6] + "тимся",
                                                     get_rhytmic_structure(verb)[:-3] + "^--")
                            elif re.search(".*деться$", verb.text, re.I):
                                return WordStructure(verb.text[:-6] + "димся",
                                                     get_rhytmic_structure(verb)[:-3] + "^--")
                            elif re.search(".*петься$", verb.text, re.I):
                                return WordStructure(verb.text[:-6] + "пимся",
                                                     get_rhytmic_structure(verb)[:-3] + "^--")
                            elif re.search(".*сеться$", verb.text, re.I):
                                return WordStructure(verb.text[:-6] + "симся",
                                                     get_rhytmic_structure(verb)[:-3] + "^--")
                            else:
                                return WordStructure(verb.text[:-5] + "имся",
                                                     get_rhytmic_structure(verb)[:-3] + "^--")
                        elif re.search(".*аться$", verb.text, re.I):
                            if re.search(".*[жш]аться$", verb.text, re.I):
                                if re.search(".*ижаться$", verb.text, re.I):
                                    return WordStructure(verb.text[:-3] + "аемся",
                                                         get_rhytmic_structure(verb) + "-")
                                else:
                                    return WordStructure(verb.text[:-3] + "имся",
                                                         get_rhytmic_structure(verb)[:-2] + "^-")
                            elif re.search(".*гнаться$", verb.text, re.I):
                                return WordStructure(verb.text[:-4] + "онимся", get_rhytmic_structure(verb) + "-")
                            else:
                                return WordStructure(verb.text[:-3] + "имся", get_rhytmic_structure(verb) + "-")
                    else:
                        if re.search(".*есться$", verb.text, re.I):
                            if verb.text == "есться":
                                return WordStructure("едимся", "-^")
                            else:
                                return WordStructure(verb.text[:-3] + "даемся", get_rhytmic_structure(verb))
                        elif re.search(".*даться$", verb.text, re.I):
                            return WordStructure(verb.text[:-2] + "емся", get_rhytmic_structure(verb) + "-")
                        elif re.search(".+быться$", verb.text, re.I):
                            return WordStructure(verb.text[:-2] + "ваемся", get_rhytmic_structure(verb))
                        elif verb.text == "хотеться":
                            return WordStructure("хотимся", "-^")
                        elif verb.text == "бежаться":
                            return WordStructure("бежимся", "-^")
                        elif verb.text == "чтиться":
                            return WordStructure("чтимся", "^")
                        elif verb.text == "ехаться":
                            return WordStructure("едемся", "^-")
                        elif verb.text == "идтись":
                            return WordStructure("идёмся", "-^")
                        elif verb.text == "быть":
                            return WordStructure("есть", "^")
                else:
                    if verb.conjugation == 1:
                        if re.search(".*еть$", verb.text, re.I):
                            if re.search(".*деть$", verb.text, re.I):
                                return WordStructure(verb.text[:-4] + "дим", get_rhytmic_structure(verb))
                            elif re.search(".*теть$", verb.text, re.I):
                                return WordStructure(verb.text[:-4] + "тим", get_rhytmic_structure(verb))
                            elif re.search(".*петь$", verb.text, re.I):
                                return WordStructure(verb.text[:-3] + "оём",
                                                     get_rhytmic_structure(verb)[:-1] + "-^")
                            else:
                                return WordStructure(verb.text[:-2] + "ем", get_rhytmic_structure(verb) + "-")
                        elif re.search(".*ать$", verb.text, re.I):
                            if re.search(".*сать$", verb.text, re.I) \
                                    and verb.stress_position == verb.syllables_count:
                                return WordStructure(verb.text[:-4] + "шем",
                                                     get_rhytmic_structure(verb)[:-2] + "^-")
                            elif re.search(".*певать$", verb.text, re.I):
                                return WordStructure(verb.text[:-2] + "ем", get_rhytmic_structure(verb) + "-")
                            elif re.search(".*[ое]вать$", verb.text, re.I):
                                if verb.stress_position == verb.syllables_count:
                                    return WordStructure(verb.text[:-5] + "уем",
                                                         get_rhytmic_structure(verb)[:-2] + "^-")
                                else:
                                    return WordStructure(verb.text[:-5] + "уем", get_rhytmic_structure(verb))
                            elif re.search(".*авать$", verb.text, re.I):
                                return WordStructure(verb.text[:-4] + "ём", get_rhytmic_structure(verb))
                            elif re.search(".*скать$", verb.text, re.I):
                                return WordStructure(verb.text[:-5] + "щем",
                                                     get_rhytmic_structure(verb)[:-2] + "^-")
                            else:
                                return WordStructure(verb.text[:-2] + "ем", get_rhytmic_structure(verb) + "-")
                        elif re.search(".*ить", verb.text, re.I):
                            if re.search(".*рить$", verb.text, re.I):
                                return WordStructure(verb.text[:-3] + "еем", get_rhytmic_structure(verb) + "-")
                            else:
                                return WordStructure(verb.text[:-3] + "ем", get_rhytmic_structure(verb)[:-2] + "^-")
                        elif re.search(".*ять$", verb.text, re.I):
                            if re.search(".*[ал]ять", verb.text, re.I) \
                                    and verb.stress_position == verb.syllables_count:
                                return WordStructure(verb.text[:-2] + "ем", get_rhytmic_structure(verb) + "-")
                            else:
                                return WordStructure(verb.text[:-3] + "ем", get_rhytmic_structure(verb))
                        elif re.search(".*оть$", verb.text, re.I):
                            return WordStructure(verb.text[:-3] + "ем", get_rhytmic_structure(verb)[:-2] + "^-")
                        elif re.search(".*ыть$", verb.text, re.I):
                            return WordStructure(verb.text[:-3] + "оем", get_rhytmic_structure(verb) + "-")
                    elif verb.conjugation == 2:
                        if re.search(".*ить$", verb.text, re.I):
                            if re.search(".*озить$", verb.text, re.I):
                                return WordStructure(verb.text[:-4] + "зим",
                                                     get_rhytmic_structure(verb)[:-2] + "^-")
                            elif re.search(".*зить$", verb.text, re.I):
                                return WordStructure(verb.text[:-4] + "зим", get_rhytmic_structure(verb))
                            elif re.search(".*дить$", verb.text, re.I):
                                return WordStructure(verb.text[:-4] + "дим",
                                                     get_rhytmic_structure(verb)[:-2] + "^-")
                            elif re.search(".*тить$", verb.text, re.I):
                                return WordStructure(verb.text[:-4] + "тим",
                                                     get_rhytmic_structure(verb)[:-2] + "^-")
                            elif re.search(".*сить$", verb.text, re.I):
                                return WordStructure(verb.text[:-4] + "сим",
                                                     get_rhytmic_structure(verb)[:-2] + "^-")
                            else:
                                return WordStructure(verb.text[:-3] + "им", get_rhytmic_structure(verb)[:-2] + "^-")
                        elif re.search(".*еть$", verb.text, re.I):
                            if re.search(".*теть$", verb.text, re.I):
                                return WordStructure(verb.text[:-4] + "тим",
                                                     get_rhytmic_structure(verb)[:-2] + "^-")
                            elif re.search(".*деть$", verb.text, re.I):
                                return WordStructure(verb.text[:-4] + "дим",
                                                     get_rhytmic_structure(verb)[:-2] + "^-")
                            elif re.search(".*петь$", verb.text, re.I):
                                return WordStructure(verb.text[:-3] + "им", get_rhytmic_structure(verb)[:-2] + "^-")
                            elif re.search(".*сеть$", verb.text, re.I):
                                return WordStructure(verb.text[:-4] + "сим",
                                                     get_rhytmic_structure(verb)[:-2] + "^-")
                            else:
                                return WordStructure(verb.text[:-3] + "им", get_rhytmic_structure(verb)[:-2] + "^-")
                        elif re.search(".*ать$", verb.text, re.I):
                            if re.search(".*[жш]ать$", verb.text, re.I):
                                if re.search(".*ижать$", verb.text, re.I):
                                    return WordStructure(verb.text[:-3] + "аем", get_rhytmic_structure(verb) + "-")
                                else:
                                    return WordStructure(verb.text[:-3] + "им",
                                                         get_rhytmic_structure(verb)[:-2] + "^-")
                            elif re.search(".*гнать$", verb.text, re.I):
                                return WordStructure(verb.text[:-4] + "оним", get_rhytmic_structure(verb) + "-")
                            else:
                                return WordStructure(verb.text[:-3] + "им", get_rhytmic_structure(verb) + "-")
                    else:
                        if re.search(".*есть$", verb.text, re.I):
                            if verb.text == "есть":
                                return WordStructure("едим", "-^")
                            else:
                                return WordStructure(verb.text[:-3] + "даем", get_rhytmic_structure(verb))
                        elif re.search(".*дать$", verb.text, re.I):
                            return WordStructure(verb.text[:-2] + "ем", get_rhytmic_structure(verb) + "-")
                        elif re.search(".+быть$", verb.text, re.I):
                            return WordStructure(verb.text[:-2] + "ваем", get_rhytmic_structure(verb))
                        elif verb.text == "хотеть":
                            return WordStructure("хотим", "-^")
                        elif verb.text == "бежать":
                            return WordStructure("бежим", "-^")
                        elif verb.text == "чтить":
                            return WordStructure("чтим", "^")
                        elif verb.text == "ехать":
                            return WordStructure("едем", "^-")
                        elif verb.text == "идти":
                            return WordStructure("идём", "-^")
                        elif verb.text == "быть":
                            return WordStructure("есть", "^")

            elif person == 2:
                if verb.reflexive:
                    if verb.conjugation == 1:
                        if re.search(".*еться$", verb.text, re.I):
                            if re.search(".*деться$", verb.text, re.I):
                                return WordStructure(verb.text[:-4] + "дитесь", get_rhytmic_structure(verb) + "-")
                            elif re.search(".*теться$", verb.text, re.I):
                                return WordStructure(verb.text[:-4] + "титесь", get_rhytmic_structure(verb) + "-")
                            elif re.search(".*петься$", verb.text, re.I):
                                return WordStructure(verb.text[:-3] + "оётесь",
                                                     get_rhytmic_structure(verb)[:-1] + "-^-")
                            else:
                                return WordStructure(verb.text[:-2] + "етесь", get_rhytmic_structure(verb) + "--")
                        elif re.search(".*аться$", verb.text, re.I):
                            if re.search(".*саться$", verb.text,
                                         re.I) and verb.stress_position + 1 == verb.syllables_count:
                                return WordStructure(verb.text[:-6] + "шетесь", get_rhytmic_structure(verb)[:-3]
                                                     + "^--")
                            elif re.search(".*певаться$", verb.text, re.I):
                                return WordStructure(verb.text[:-2] + "етесь", get_rhytmic_structure(verb) + "--")
                            elif re.search(".*[ое]ваться$", verb.text, re.I):
                                if re.search(".*оваться$", verb.text, re.I) \
                                        and verb.stress_position + 1 == verb.syllables_count:
                                    return WordStructure(verb.text[:-7] + "уетесь", get_rhytmic_structure(verb)[:-3]
                                                         + "^--")
                                if re.search(".*еваться$", verb.text, re.I) \
                                        and verb.stress_position + 1 == verb.syllables_count:
                                    return WordStructure(verb.text[:-5] + "аетесь", get_rhytmic_structure(verb)[:-2]
                                                         + "^--")
                                else:
                                    return WordStructure(verb.text[:-5] + "уетесь",
                                                         get_rhytmic_structure(verb) + "-")
                            elif re.search(".*аваться$", verb.text, re.I):
                                return WordStructure(verb.text[:-4] + "ётeсь", get_rhytmic_structure(verb) + "-")
                            elif re.search(".*скаться$", verb.text, re.I):
                                return WordStructure(verb.text[:-5] + "щетесь",
                                                     get_rhytmic_structure(verb)[:-2] + "^--")
                            else:
                                return WordStructure(verb.text[:-4] + "етесь", get_rhytmic_structure(verb) + "-")
                        elif re.search(".*иться$", verb.text, re.I):
                            if re.search(".*риться$", verb.text, re.I):
                                return WordStructure(verb.text[:-5] + "еетесь", get_rhytmic_structure(verb) + "-")
                            else:
                                return WordStructure(verb.text[:-5] + "етесь",
                                                     get_rhytmic_structure(verb)[:-2] + "^-")
                        elif re.search(".*яться$", verb.text, re.I):
                            if re.search(".*[ал]яться$", verb.text,
                                         re.I) and verb.stress_position + 1 == verb.syllables_count:
                                return WordStructure(verb.text[:-4] + "етесь", get_rhytmic_structure(verb) + "-")
                            else:
                                return WordStructure(verb.text[:-5] + "ётесь", get_rhytmic_structure(verb))
                        elif re.search(".*оться$", verb.text, re.I):
                            return WordStructure(verb.text[:-3] + "етесь", get_rhytmic_structure(verb)[:-2] + "^--")
                        elif re.search(".*ыться$", verb.text, re.I):
                            return WordStructure(verb.text[:-3] + "оетесь", get_rhytmic_structure(verb) + "--")
                    elif verb.conjugation == 2:
                        if re.search(".*иться$", verb.text, re.I):
                            if re.search(".*озиться$", verb.text, re.I):
                                return WordStructure(verb.text[:-6] + "зитесь",
                                                     get_rhytmic_structure(verb)[:-3] + "^--")
                            if re.search(".*зиться$", verb.text, re.I):
                                return WordStructure(verb.text[:-6] + "зитесь",
                                                     get_rhytmic_structure(verb)[:-3] + "-^-")
                            elif re.search(".*диться$", verb.text, re.I):
                                return WordStructure(verb.text[:-6] + "дитесь",
                                                     get_rhytmic_structure(verb)[:-3] + "^--")
                            elif re.search(".*титься$", verb.text, re.I):
                                return WordStructure(verb.text[:-6] + "титесь",
                                                     get_rhytmic_structure(verb)[:-3] + "^--")
                            elif re.search(".*ситься$", verb.text, re.I):
                                return WordStructure(verb.text[:-6] + "ситесь",
                                                     get_rhytmic_structure(verb)[:-3] + "^--")
                            else:
                                return WordStructure(verb.text[:-5] + "итесь",
                                                     get_rhytmic_structure(verb)[:-3] + "^--")
                        elif re.search(".*еться$", verb.text, re.I):
                            if re.search(".*теться$", verb.text, re.I):
                                return WordStructure(verb.text[:-6] + "титесь",
                                                     get_rhytmic_structure(verb)[:-3] + "^--")
                            elif re.search(".*деться$", verb.text, re.I):
                                return WordStructure(verb.text[:-6] + "дитесь",
                                                     get_rhytmic_structure(verb)[:-3] + "^--")
                            elif re.search(".*петься$", verb.text, re.I):
                                return WordStructure(verb.text[:-6] + "питесь",
                                                     get_rhytmic_structure(verb)[:-3] + "^--")
                            elif re.search(".*сеться$", verb.text, re.I):
                                return WordStructure(verb.text[:-6] + "ситесь",
                                                     get_rhytmic_structure(verb)[:-3] + "^--")
                            else:
                                return WordStructure(verb.text[:-5] + "итесь",
                                                     get_rhytmic_structure(verb)[:-3] + "^--")
                        elif re.search(".*аться$", verb.text, re.I):
                            if re.search(".*[жш]аться$", verb.text, re.I):
                                return WordStructure(verb.text[:-3] + "итесь",
                                                     get_rhytmic_structure(verb)[:-2] + "^--")
                            elif re.search(".*гнаться$", verb.text, re.I):
                                return WordStructure(verb.text[:-4] + "онитесь", get_rhytmic_structure(verb) + "--")
                            else:
                                return WordStructure(verb.text[:-3] + "итесь",
                                                     get_rhytmic_structure(verb)[:-2] + "^--")
                    else:
                        if re.search(".*есться$", verb.text, re.I):
                            if verb.text == "есться":
                                return WordStructure("едитесь", "-^-")
                            else:
                                return WordStructure(verb.text[:-3] + "даетесь", "^--")
                        elif re.search(".*дать$", verb.text, re.I):
                            return WordStructure(verb.text[:-2] + "етесь", get_rhytmic_structure(verb)[:-2] + "^--")
                        elif re.search(".+быть$", verb.text, re.I):
                            return WordStructure(verb.text[:-2] + "ваетесь",
                                                 get_rhytmic_structure(verb)[:-2] + "^-")
                        elif verb.text == "хотеться":
                            return WordStructure("хотитесь", "-^-")
                        elif verb.text == "бежаться":
                            return WordStructure("бежитесь", "-^-")
                        elif verb.text == "чтиться":
                            return WordStructure("чтитесь", "^-")
                        elif verb.text == "ехаться":
                            return WordStructure("едетесь", "^--")
                        elif verb.text == "идтися":
                            return WordStructure("идётесь", "-^-")
                        elif verb.text == "быть":
                            return WordStructure("есть", "^")

                else:
                    if verb.conjugation == 1:
                        if re.search(".*еть$", verb.text, re.I):
                            if re.search(".*деть$", verb.text, re.I):
                                return WordStructure(verb.text[:-4] + "дите", get_rhytmic_structure(verb) + "-")
                            elif re.search(".*теть$", verb.text, re.I):
                                return WordStructure(verb.text[:-4] + "тите", get_rhytmic_structure(verb) + "-")
                            elif re.search(".*петь$", verb.text, re.I):
                                return WordStructure(verb.text[:-3] + "оёте",
                                                     get_rhytmic_structure(verb)[:-1] + "-^-")
                            else:
                                return WordStructure(verb.text[:-2] + "ете", get_rhytmic_structure(verb) + "--")
                        elif re.search(".*ать$", verb.text, re.I):
                            if re.search(".*сать$", verb.text, re.I) \
                                    and verb.stress_position == verb.syllables_count:
                                return WordStructure(verb.text[:-4] + "шете", get_rhytmic_structure(verb)[:-2]
                                                     + "^--")
                            elif re.search(".*певать$", verb.text, re.I):
                                return WordStructure(verb.text[:-2] + "ете", get_rhytmic_structure(verb) + "--")
                            elif re.search(".*[ое]вать$", verb.text, re.I):
                                if verb.stress_position == verb.syllables_count:
                                    return WordStructure(verb.text[:-5] + "уете", get_rhytmic_structure(verb)[:-2]
                                                         + "^--")
                                else:
                                    return WordStructure(verb.text[:-5] + "уете", get_rhytmic_structure(verb) + "-")
                            elif re.search(".*авать$", verb.text, re.I):
                                return WordStructure(verb.text[:-4] + "ётe", get_rhytmic_structure(verb) + "-")
                            elif re.search(".*скать$", verb.text, re.I):
                                return WordStructure(verb.text[:-5] + "щете",
                                                     get_rhytmic_structure(verb)[:-2] + "^--")
                            else:
                                return WordStructure(verb.text[:-2] + "ете", get_rhytmic_structure(verb) + "--")
                        elif re.search(".*ить", verb.text, re.I):
                            if re.search(".*рить$", verb.text, re.I):
                                return WordStructure(verb.text[:-3] + "еете", get_rhytmic_structure(verb) + "--")
                            else:
                                return WordStructure(verb.text[:-3] + "ете",
                                                     get_rhytmic_structure(verb)[:-2] + "^--")
                        elif re.search(".*ять$", verb.text, re.I):
                            if re.search(".*[ал]ять", verb.text, re.I) \
                                    and verb.stress_position == verb.syllables_count:
                                return WordStructure(verb.text[:-2] + "ете", get_rhytmic_structure(verb) + "--")
                            else:
                                return WordStructure(verb.text[:-3] + "ете", get_rhytmic_structure(verb) + "-")
                        elif re.search(".*оть$", verb.text, re.I):
                            return WordStructure(verb.text[:-3] + "ете", get_rhytmic_structure(verb)[:-2] + "^--")
                        elif re.search(".*ыть$", verb.text, re.I):
                            return WordStructure(verb.text[:-3] + "оете", get_rhytmic_structure(verb) + "--")
                    elif verb.conjugation == 2:
                        if re.search(".*ить$", verb.text, re.I):
                            if re.search(".*озить$", verb.text, re.I):
                                return WordStructure(verb.text[:-4] + "зите",
                                                     get_rhytmic_structure(verb)[:-2] + "^--")
                            if re.search(".*зить$", verb.text, re.I):
                                return WordStructure(verb.text[:-4] + "зите",
                                                     get_rhytmic_structure(verb)[:-2] + "-^-")
                            elif re.search(".*дить$", verb.text, re.I):
                                return WordStructure(verb.text[:-4] + "дите",
                                                     get_rhytmic_structure(verb)[:-2] + "^--")
                            elif re.search(".*тить$", verb.text, re.I):
                                return WordStructure(verb.text[:-4] + "тите",
                                                     get_rhytmic_structure(verb)[:-2] + "^--")
                            elif re.search(".*сить$", verb.text, re.I):
                                return WordStructure(verb.text[:-4] + "сите",
                                                     get_rhytmic_structure(verb)[:-2] + "^--")
                            else:
                                return WordStructure(verb.text[:-3] + "ите",
                                                     get_rhytmic_structure(verb)[:-2] + "^--")
                        elif re.search(".*еть$", verb.text, re.I):
                            if re.search(".*теть$", verb.text, re.I):
                                return WordStructure(verb.text[:-4] + "тите",
                                                     get_rhytmic_structure(verb)[:-2] + "^--")
                            elif re.search(".*деть$", verb.text, re.I):
                                return WordStructure(verb.text[:-4] + "дите",
                                                     get_rhytmic_structure(verb)[:-2] + "^--")
                            elif re.search(".*петь$", verb.text, re.I):
                                return WordStructure(verb.text[:-3] + "ите",
                                                     get_rhytmic_structure(verb)[:-2] + "^--")
                            elif re.search(".*сеть$", verb.text, re.I):
                                return WordStructure(verb.text[:-4] + "сите",
                                                     get_rhytmic_structure(verb)[:-2] + "^--")
                            else:
                                return WordStructure(verb.text[:-3] + "ите",
                                                     get_rhytmic_structure(verb)[:-2] + "^--")
                        elif re.search(".*ать$", verb.text, re.I):
                            if re.search(".*[жш]ать$", verb.text, re.I):
                                return WordStructure(verb.text[:-3] + "ите",
                                                     get_rhytmic_structure(verb)[:-2] + "^--")
                            elif re.search(".*гнать$", verb.text, re.I):
                                return WordStructure(verb.text[:-4] + "оните", get_rhytmic_structure(verb) + "--")
                            else:
                                return WordStructure(verb.text[:-3] + "ите",
                                                     get_rhytmic_structure(verb)[:-2] + "^--")
                    else:
                        if re.search(".*есть$", verb.text, re.I):
                            if verb.text == "есть":
                                return WordStructure("едите", "-^-")
                            else:
                                return WordStructure(verb.text[:-3] + "даете", "^--")
                        elif re.search(".*дать$", verb.text, re.I):
                            return WordStructure(verb.text[:-2] + "ете", get_rhytmic_structure(verb)[:-2] + "^--")
                        elif re.search(".+быть$", verb.text, re.I):
                            return WordStructure(verb.text[:-2] + "ваете", get_rhytmic_structure(verb)[:-2] + "^-")
                        elif verb.text == "хотеть":
                            return WordStructure("хотите", "-^-")
                        elif verb.text == "бежать":
                            return WordStructure("бежите", "-^-")
                        elif verb.text == "чтить":
                            return WordStructure("чтите", "^-")
                        elif verb.text == "ехать":
                            return WordStructure("едете", "^--")
                        elif verb.text == "идти":
                            return WordStructure("идёте", "-^-")
                        elif verb.text == "быть":
                            return WordStructure("есть", "^")

            elif person == 3:
                if verb.reflexive:
                    if verb.conjugation == 1:
                        if re.search(".*еться$", verb.text, re.I):
                            if re.search(".*деться$", verb.text, re.I):
                                return WordStructure(verb.text[:-4] + "дятся", get_rhytmic_structure(verb))
                            elif re.search(".*теться$", verb.text, re.I):
                                return WordStructure(verb.text[:-4] + "тятся",
                                                     get_rhytmic_structure(verb)[:-2] + "^-")
                            elif re.search(".*петься$", verb.text, re.I):
                                return WordStructure(verb.text[:-3] + "оются",
                                                     get_rhytmic_structure(verb)[:-1] + "-^")
                            else:
                                return WordStructure(verb.text[:-2] + "ются", get_rhytmic_structure(verb) + "-")
                        elif re.search(".*аться$", verb.text, re.I):
                            if re.search(".*саться$", verb.text,
                                         re.I) and verb.stress_position + 1 == verb.syllables_count:
                                return WordStructure(verb.text[:-6] + "шутся",
                                                     get_rhytmic_structure(verb)[:-3] + "^--")
                            elif re.search(".*певаться$", verb.text, re.I):
                                return WordStructure(verb.text[:-2] + "ются", get_rhytmic_structure(verb) + "-")
                            elif re.search(".*[ое]ваться$", verb.text, re.I):
                                if re.search(".*оваться$", verb.text, re.I) \
                                        and verb.stress_position + 1 == verb.syllables_count:
                                    return WordStructure(verb.text[:-7] + "уются", get_rhytmic_structure(verb)[:-3]
                                                         + "^--")
                                if re.search(".*еваться$", verb.text, re.I) \
                                        and verb.stress_position + 1 == verb.syllables_count:
                                    return WordStructure(verb.text[:-5] + "аются", get_rhytmic_structure(verb)[:-2]
                                                         + "^--")
                                else:
                                    return WordStructure(verb.text[:-5] + "аются", get_rhytmic_structure(verb))
                            elif re.search(".*аваться$", verb.text, re.I):
                                return WordStructure(verb.text[:-4] + "ются", get_rhytmic_structure(verb))
                            elif re.search(".*скаться$", verb.text, re.I):
                                return WordStructure(verb.text[:-5] + "щутся",
                                                     get_rhytmic_structure(verb)[:-2] + "^-")
                            else:
                                return WordStructure(verb.text[:-4] + "ются", get_rhytmic_structure(verb) + "-")
                        elif re.search(".*иться$", verb.text, re.I):
                            if re.search(".*риться$", verb.text, re.I):
                                return WordStructure(verb.text[:-5] + "еются", get_rhytmic_structure(verb) + "-")
                            else:
                                return WordStructure(verb.text[:-5] + "ются",
                                                     get_rhytmic_structure(verb)[:-2] + "^-")
                        elif re.search(".*яться$", verb.text, re.I):
                            if re.search(".*[ал]яться", verb.text, re.I) \
                                    and verb.stress_position + 1 == verb.syllables_count:
                                return WordStructure(verb.text[:-4] + "ются", get_rhytmic_structure(verb) + "-")
                            else:
                                return WordStructure(verb.text[:-5] + "ются", get_rhytmic_structure(verb))
                        elif re.search(".*оться$", verb.text, re.I):
                            return WordStructure(verb.text[:-3] + "ятся", get_rhytmic_structure(verb)[:-2] + "^-")
                        elif re.search(".*ыться$", verb.text, re.I):
                            return WordStructure(verb.text[:-3] + "оются", get_rhytmic_structure(verb) + "-")
                    elif verb.conjugation == 2:
                        if re.search(".*иться$", verb.text, re.I):
                            if re.search(".*азиться$", verb.text, re.I):
                                return WordStructure(verb.text[:-6] + "зятся",
                                                     get_rhytmic_structure(verb)[:-2] + "-^")
                            if re.search(".*зиться$", verb.text, re.I):
                                return WordStructure(verb.text[:-6] + "зятся",
                                                     get_rhytmic_structure(verb)[:-3] + "^--")
                            if re.search(".*диться$", verb.text, re.I):
                                return WordStructure(verb.text[:-6] + "дятся",
                                                     get_rhytmic_structure(verb)[:-3] + "^--")
                            elif re.search(".*титься$", verb.text, re.I):
                                return WordStructure(verb.text[:-6] + "тятся",
                                                     get_rhytmic_structure(verb)[:-3] + "^--")
                            elif re.search(".*ситься$", verb.text, re.I):
                                return WordStructure(verb.text[:-6] + "сятся",
                                                     get_rhytmic_structure(verb)[:-3] + "^--")
                            else:
                                return WordStructure(verb.text[:-5] + "ятся",
                                                     get_rhytmic_structure(verb)[:-3] + "^--")
                        elif re.search(".*еться$", verb.text, re.I):
                            if re.search(".*теться$", verb.text, re.I):
                                return WordStructure(verb.text[:-6] + "тятся",
                                                     get_rhytmic_structure(verb)[:-3] + "^--")
                            elif re.search(".*деться$", verb.text, re.I):
                                return WordStructure(verb.text[:-6] + "дятся",
                                                     get_rhytmic_structure(verb)[:-3] + "^--")
                            elif re.search(".*петься$", verb.text, re.I):
                                return WordStructure(verb.text[:-6] + "пятся",
                                                     get_rhytmic_structure(verb)[:-3] + "^--")
                            elif re.search(".*сеться$", verb.text, re.I):
                                return WordStructure(verb.text[:-6] + "сятся",
                                                     get_rhytmic_structure(verb)[:-3] + "^--")
                            else:
                                return WordStructure(verb.text[:-3] + "ят",
                                                     get_rhytmic_structure(verb)[:-3] + "^--")
                        elif re.search(".*аться$", verb.text, re.I):
                            if re.search(".*[жш]аться$", verb.text, re.I):
                                return WordStructure(verb.text[:-3] + "атся",
                                                     get_rhytmic_structure(verb)[:-2] + "^-")
                            elif re.search(".*гнаться$", verb.text, re.I):
                                return WordStructure(verb.text[:-4] + "онятся", get_rhytmic_structure(verb) + "-")
                            else:
                                return WordStructure(verb.text[:-3] + "ятся", get_rhytmic_structure(verb))
                    else:
                        if re.search(".*есться$", verb.text, re.I):
                            if verb.text == "есться":
                                return WordStructure("едятся", "-^")
                            else:
                                return WordStructure(verb.text[:-3] + "даются", get_rhytmic_structure(verb))
                        elif re.search(".*даться$", verb.text, re.I):
                            return WordStructure(verb.text[:-2] + "ются", get_rhytmic_structure(verb))
                        elif re.search(".+быться$", verb.text, re.I):
                            return WordStructure(verb.text[:-2] + "ваются", get_rhytmic_structure(verb))
                        elif verb.text == "хотеться":
                            return WordStructure("хотятся", "-^")
                        elif verb.text == "бежаться":
                            return WordStructure("бегутся", "-^")
                        elif verb.text == "чтиться":
                            return WordStructure("чтятся", "^")
                        elif verb.text == "ехаться":
                            return WordStructure("едутся", "^-")
                        elif verb.text == "идтися":
                            return WordStructure("идутся", "-^")
                        elif verb.text == "быть":
                            return WordStructure("есть", "^")

                else:
                    if verb.conjugation == 1:
                        if re.search(".*еть$", verb.text, re.I):
                            if re.search(".*деть$", verb.text, re.I):
                                return WordStructure(verb.text[:-4] + "дят", get_rhytmic_structure(verb))
                            elif re.search(".*теть$", verb.text, re.I):
                                return WordStructure(verb.text[:-4] + "тят",
                                                     get_rhytmic_structure(verb)[:-2] + "^-")
                            elif re.search(".*петь$", verb.text, re.I):
                                return WordStructure(verb.text[:-3] + "оют",
                                                     get_rhytmic_structure(verb)[:-1] + "-^")
                            else:
                                return WordStructure(verb.text[:-2] + "ют", get_rhytmic_structure(verb) + "-")
                        elif re.search(".*ать$", verb.text, re.I):
                            if re.search(".*сать$", verb.text, re.I) \
                                    and verb.stress_position == verb.syllables_count:
                                return WordStructure(verb.text[:-4] + "шут",
                                                     get_rhytmic_structure(verb)[:-2] + "^-")
                            elif re.search(".*певать$", verb.text, re.I):
                                return WordStructure(verb.text[:-2] + "ют", get_rhytmic_structure(verb) + "-")
                            elif re.search(".*[ое]вать$", verb.text, re.I):
                                if verb.syllables_count == verb.stress_position:
                                    return WordStructure(verb.text[:-5] + "уют", get_rhytmic_structure(verb)[:-2]
                                                         + "^-")
                                else:
                                    return WordStructure(verb.text[:-5] + "уют", get_rhytmic_structure(verb))
                            elif re.search(".*авать$", verb.text, re.I):
                                return WordStructure(verb.text[:-4] + "ют", get_rhytmic_structure(verb))
                            elif re.search(".*скать$", verb.text, re.I):
                                return WordStructure(verb.text[:-5] + "щут",
                                                     get_rhytmic_structure(verb)[:-2] + "^-")
                            else:
                                return WordStructure(verb.text[:-2] + "ют", get_rhytmic_structure(verb) + "-")
                        elif re.search(".*ить", verb.text, re.I):
                            if re.search(".*рить$", verb.text, re.I):
                                return WordStructure(verb.text[:-3] + "еют", get_rhytmic_structure(verb) + "-")
                            else:
                                return WordStructure(verb.text[:-3] + "ют", get_rhytmic_structure(verb)[:-2] + "^-")
                        elif re.search(".*ять$", verb.text, re.I):
                            if re.search(".*[ал]ять", verb.text, re.I) \
                                    and verb.stress_position == verb.syllables_count:
                                return WordStructure(verb.text[:-2] + "ют", get_rhytmic_structure(verb) + "-")
                            else:
                                return WordStructure(verb.text[:-3] + "ют", get_rhytmic_structure(verb))
                        elif re.search(".*оть$", verb.text, re.I):
                            return WordStructure(verb.text[:-3] + "ят", get_rhytmic_structure(verb)[:-2] + "^-")
                        elif re.search(".*ыть$", verb.text, re.I):
                            return WordStructure(verb.text[:-3] + "оют", get_rhytmic_structure(verb) + "-")
                    elif verb.conjugation == 2:
                        if re.search(".*ить$", verb.text, re.I):
                            if re.search(".*азить$", verb.text, re.I):
                                return WordStructure(verb.text[:-4] + "зят",
                                                     get_rhytmic_structure(verb)[:-2] + "-^")
                            if re.search(".*зить$", verb.text, re.I):
                                return WordStructure(verb.text[:-4] + "зят",
                                                     get_rhytmic_structure(verb)[:-2] + "^-")
                            if re.search(".*дить$", verb.text, re.I):
                                return WordStructure(verb.text[:-4] + "дят",
                                                     get_rhytmic_structure(verb)[:-2] + "^-")
                            elif re.search(".*тить$", verb.text, re.I):
                                return WordStructure(verb.text[:-4] + "тят",
                                                     get_rhytmic_structure(verb)[:-2] + "^-")
                            elif re.search(".*сить$", verb.text, re.I):
                                return WordStructure(verb.text[:-4] + "сят",
                                                     get_rhytmic_structure(verb)[:-2] + "^-")
                            else:
                                return WordStructure(verb.text[:-3] + "ят",
                                                     get_rhytmic_structure(verb)[:-2] + "^-")
                        elif re.search(".*еть$", verb.text, re.I):
                            if re.search(".*теть$", verb.text, re.I):
                                return WordStructure(verb.text[:-4] + "тят",
                                                     get_rhytmic_structure(verb)[:-2] + "^-")
                            elif re.search(".*деть$", verb.text, re.I):
                                return WordStructure(verb.text[:-4] + "дят",
                                                     get_rhytmic_structure(verb)[:-2] + "^-")
                            elif re.search(".*петь$", verb.text, re.I):
                                return WordStructure(verb.text[:-3] + "ят",
                                                     get_rhytmic_structure(verb)[:-2] + "^-")
                            elif re.search(".*сеть$", verb.text, re.I):
                                return WordStructure(verb.text[:-4] + "сят",
                                                     get_rhytmic_structure(verb)[:-2] + "^-")
                            else:
                                return WordStructure(verb.text[:-3] + "ят",
                                                     get_rhytmic_structure(verb)[:-2] + "^-")
                        elif re.search(".*ать$", verb.text, re.I):
                            if re.search(".*[жш]ать$", verb.text, re.I):
                                return WordStructure(verb.text[:-3] + "ат", get_rhytmic_structure(verb)[:-2] + "^-")
                            elif re.search(".*гнать$", verb.text, re.I):
                                return WordStructure(verb.text[:-4] + "онят", get_rhytmic_structure(verb) + "-")
                            else:
                                return WordStructure(verb.text[:-3] + "ят", get_rhytmic_structure(verb))
                    else:
                        if re.search(".*есть$", verb.text, re.I):
                            if verb.text == "есть":
                                return WordStructure("едят", "-^")
                            else:
                                return WordStructure(verb.text[:-3] + "дают", get_rhytmic_structure(verb))
                        elif re.search(".*дать$", verb.text, re.I):
                            return WordStructure(verb.text[:-2] + "ют", get_rhytmic_structure(verb))
                        elif re.search(".+быть$", verb.text, re.I):
                            return WordStructure(verb.text[:-2] + "вают", get_rhytmic_structure(verb))
                        elif verb.text == "хотеть":
                            return WordStructure("хотят", "-^")
                        elif verb.text == "бежать":
                            return WordStructure("бегут", "-^")
                        elif verb.text == "чтить":
                            return WordStructure("чтят", "^")
                        elif verb.text == "ехать":
                            return WordStructure("едут", "^-")
                        elif verb.text == "идти":
                            return WordStructure("идут", "-^")
                        elif verb.text == "быть":
                            return WordStructure("есть", "^")

    elif tense == "past":
        if not plural:
            if re.search(".*(ид|й)ти$", verb.text, re.I):
                if verb.text == "идти":
                    if gender == "male":
                        return WordStructure("шёл", "^")
                    elif gender == "female":
                        return WordStructure("шла", "^")
                    else:
                        return WordStructure("шло", "^")
                else:
                    if gender == "male":
                        return WordStructure(verb.text[:-3] + "шёл", get_rhytmic_structure(verb))
                    elif gender == "female":
                        return WordStructure(verb.text[:-3] + " шла", get_rhytmic_structure(verb))
                    else:
                        return WordStructure(verb.text[:-3] + " шло", get_rhytmic_structure(verb))
            elif re.search(".*сться$", verb.text, re.I):
                if gender == "male":
                    return WordStructure(verb.text[:-5] + "лся", get_rhytmic_structure(verb))
                elif gender == "female":
                    return WordStructure(verb.text[:-5] + "лась", get_rhytmic_structure(verb))
                else:
                    return WordStructure(verb.text[:-5] + "лось", get_rhytmic_structure(verb))
            elif re.search(".*сть$", verb.text, re.I):
                if gender == "male":
                    return WordStructure(verb.text[:-3] + "л", get_rhytmic_structure(verb))
                elif gender == "female":
                    return WordStructure(verb.text[:-3] + "ла", get_rhytmic_structure(verb) + "-")
                else:
                    return WordStructure(verb.text[:-3] + "ло", get_rhytmic_structure(verb) + "-")
            elif re.search(".*ся$", verb.text, re.I):
                if gender == "male":
                    return WordStructure(verb.text[:-4] + "лся", get_rhytmic_structure(verb))
                elif gender == "female":
                    return WordStructure(verb.text[:-4] + "лась", get_rhytmic_structure(verb))
                else:
                    return WordStructure(verb.text[:-4] + "лось", get_rhytmic_structure(verb))
            else:
                if verb.perfective:
                    if re.search(".*ереть$", verb.text, re.I) and verb.stress_position == verb.syllables_count:
                        if gender == "male":
                            return WordStructure(verb.text[:-5] + "ёр", get_rhytmic_structure(verb)[:-1] + "^")
                        elif gender == "female":
                            return WordStructure(verb.text[:-5] + "ёрла", get_rhytmic_structure(verb)[:-2] + "^-")
                        else:
                            return WordStructure(verb.text[:-5] + "ёрло", get_rhytmic_structure(verb)[:-2] + "^-")
                    if re.search(".*еть$", verb.text, re.I) and verb.stress_position == verb.syllables_count:
                        if gender == "male":
                            return WordStructure(verb.text[:-2] + "л", get_rhytmic_structure(verb)[:-1] + "^")
                        elif gender == "female":
                            return WordStructure(verb.text[:-2] + "ла", get_rhytmic_structure(verb)[:-1] + "^-")
                        else:
                            return WordStructure(verb.text[:-2] + "ло", get_rhytmic_structure(verb)[:-1] + "^-")
                    elif re.search(".*[аиуя]ть$", verb.text, re.I):
                        if verb.stress_position == verb.syllables_count:
                            if re.search(".*нять$", verb.text, re.I):
                                if gender == "male":
                                    return WordStructure(verb.text[:-2] + "л",
                                                         get_rhytmic_structure(verb)[:-2] + "^-")
                                elif gender == "female":
                                    return WordStructure(verb.text[:-2] + "ла",
                                                         get_rhytmic_structure(verb)[:-1] + "-^")
                                else:
                                    return WordStructure(verb.text[:-2] + "ло",
                                                         get_rhytmic_structure(verb)[:-1] + "-^")
                            else:
                                if gender == "male":
                                    return WordStructure(verb.text[:-2] + "л",
                                                         get_rhytmic_structure(verb)[:-1] + "^")
                                elif gender == "female":
                                    return WordStructure(verb.text[:-2] + "ла",
                                                         get_rhytmic_structure(verb)[:-1] + "^-")
                                else:
                                    return WordStructure(verb.text[:-2] + "ло",
                                                         get_rhytmic_structure(verb)[:-1] + "^-")
                        else:
                            if gender == "male":
                                return WordStructure(verb.text[:-2] + "л", get_rhytmic_structure(verb))
                            elif gender == "female":
                                return WordStructure(verb.text[:-2] + "ла", get_rhytmic_structure(verb) + "-")
                            else:
                                return WordStructure(verb.text[:-2] + "ло", get_rhytmic_structure(verb) + "-")
                    elif re.search(".*ести$", verb.text, re.I):
                        if gender == "male":
                            return WordStructure(verb.text[:-4] + "ёс", get_rhytmic_structure(verb)[:-2] + "^")
                        elif gender == "female":
                            return WordStructure(verb.text[:-4] + "есла", get_rhytmic_structure(verb))
                        else:
                            return WordStructure(verb.text[:-4] + "есло", get_rhytmic_structure(verb))
                    elif re.search(".*очь$", verb.text, re.I):
                        if gender == "male":
                            return WordStructure(verb.text[:-3] + "ог", get_rhytmic_structure(verb))
                        elif gender == "female":
                            return WordStructure(verb.text[:-3] + "огла", get_rhytmic_structure(verb)[:-1] + "-^")
                        else:
                            return WordStructure(verb.text[:-3] + "огло", get_rhytmic_structure(verb)[:-1] + "-^")
                    else:
                        if gender == "male":
                            return WordStructure(verb.text[:-2] + "л", get_rhytmic_structure(verb))
                        elif gender == "female":
                            return WordStructure(verb.text[:-2] + "ла", get_rhytmic_structure(verb) + "-")
                        else:
                            return WordStructure(verb.text[:-2] + "ло", get_rhytmic_structure(verb) + "-")
                else:
                    if gender == "male":
                        return WordStructure(verb.text[:-2] + "л", get_rhytmic_structure(verb))
                    elif gender == "female":
                        return WordStructure(verb.text[:-2] + "ла", get_rhytmic_structure(verb) + "-")
                    else:
                        return WordStructure(verb.text[:-2] + "ло", get_rhytmic_structure(verb) + "-")
        else:
            if re.search(".*ти$", verb.text, re.I):
                if verb.text == "идти":
                    return WordStructure("шли", "^")
                elif re.search(".*(й|ид)ти$", verb.text, re.I):
                    return WordStructure(verb.text[:-3] + "шли", get_rhytmic_structure(verb))
                else:
                    return WordStructure(verb.text[:-2] + "ли", get_rhytmic_structure(verb))
            elif re.search(".*очь$", verb.text, re.I):
                return WordStructure(verb.text[:-3] + "огли", get_rhytmic_structure(verb)[:-1] + "-^")
            elif re.search(".*нять$", verb.text, re.I) and verb.perfective:
                return WordStructure(verb.text[:-4] + "няли", get_rhytmic_structure(verb)[:-2] + "^--")
            elif re.search(".*ереть$", verb.text, re.I):
                return WordStructure(verb.text[:-5] + "ёрлись", get_rhytmic_structure(verb)[:-2] + "^-")
            elif re.search(".*сться$", verb.text, re.I):
                return WordStructure(verb.text[:-5] + "лись", get_rhytmic_structure(verb))
            elif re.search(".*сть$", verb.text, re.I):
                return WordStructure(verb.text[:-3] + "ли", get_rhytmic_structure(verb) + "-")
            elif re.search(".*ся$", verb.text, re.I):
                return WordStructure(verb.text[:-4] + "лись", get_rhytmic_structure(verb))
            else:
                return WordStructure(verb.text[:-2] + "ли", get_rhytmic_structure(verb) + "-")

    elif tense == "future":
        if verb.perfective:
            if not plural:
                if person == 1:
                    if re.search(".*(ид|й)ти$", verb.text, re.I):
                        if verb.text == "идти":
                            return WordStructure("приду", "^")
                        elif re.search(".*йти$", verb.text, re.I):
                            return WordStructure(verb.text[:-2] + "ду", get_rhytmic_structure(verb))
                        else:
                            return WordStructure(verb.text[:-3] + "ду", get_rhytmic_structure(verb))
                    elif re.search(".*сть$", verb.text, re.I):
                        return WordStructure(verb.text[:-3] + "щу", get_rhytmic_structure(verb))
                    elif re.search(".*ся$", verb.text, re.I):
                        if re.search(".*чься$", verb.text, re.I):
                            return WordStructure(verb.text[:-4] + "кусь", get_rhytmic_structure(verb)[:-2] + "-^")
                        else:
                            return WordStructure(verb.text[:-2] + "сь", get_rhytmic_structure(verb))
                    else:
                        if re.search(".*ереть$", verb.text, re.I) and verb.stress_position == verb.syllables_count:
                            return WordStructure(verb.text[:-5] + "ру",
                                                 get_rhytmic_structure(verb)[:-2] + "^")
                        if re.search(".*еть$", verb.text, re.I) and verb.stress_position == verb.syllables_count:
                            if re.search(".*петь$", verb.text, re.I):
                                return WordStructure(verb.text[:-3] + "ою", get_rhytmic_structure(verb)[:-1] + "-^")
                            else:
                                return WordStructure(verb.text[:-2] + "лю", get_rhytmic_structure(verb))
                        elif re.search(".*[аиуя]ть$", verb.text, re.I):
                            if verb.stress_position == verb.syllables_count:
                                if re.search(".*нять$", verb.text, re.I):
                                    return WordStructure(verb.text[:-4] + "му",
                                                         get_rhytmic_structure(verb))
                                elif re.search(".*пить$", verb.text, re.I):
                                    return WordStructure(verb.text[:-3] + "лю",
                                                         get_rhytmic_structure(verb))
                                elif re.search(".*шить$", verb.text, re.I):
                                    return WordStructure(verb.text[:-3] + "шу",
                                                         get_rhytmic_structure(verb))
                                elif re.search(".*з[иа]ть$", verb.text, re.I):
                                    return WordStructure(verb.text[:-4] + "жу",
                                                         get_rhytmic_structure(verb))
                                elif re.search(".*нуть$", verb.text, re.I):
                                    return WordStructure(verb.text[:-2],
                                                         get_rhytmic_structure(verb))
                                else:
                                    return WordStructure(verb.text[:-2] + "ю",
                                                         get_rhytmic_structure(verb) + "-")
                            else:
                                if re.search(".*уть$", verb.text, re.I):
                                    return WordStructure(verb.text[:-2], get_rhytmic_structure(verb))
                                elif re.search(".*шить$", verb.text, re.I):
                                    return WordStructure(verb.text[:-4] + "шу",
                                                         get_rhytmic_structure(verb))
                                else:
                                    return WordStructure(verb.text[:-2] + "ю", get_rhytmic_structure(verb))
                        elif re.search(".*ести$", verb.text, re.I):
                            return WordStructure(verb.text[:-4] + "есу", get_rhytmic_structure(verb)[:-2] + "-^")
                        elif re.search(".*очь$", verb.text, re.I):
                            return WordStructure(verb.text[:-3] + "огу", get_rhytmic_structure(verb)[:-1] + "-^")
                        else:
                            return WordStructure(verb.text[:-2] + "лю", get_rhytmic_structure(verb))
                if person == 2:
                    if re.search(".*(ид|й)ти$", verb.text, re.I):
                        if verb.text == "идти":
                            return WordStructure("придёшь", "^")
                        elif re.search(".*йти$", verb.text, re.I):
                            return WordStructure(verb.text[:-2] + "дёшь", get_rhytmic_structure(verb))
                        else:
                            return WordStructure(verb.text[:-3] + "дёшь", get_rhytmic_structure(verb))
                    elif re.search(".*сть$", verb.text, re.I):
                        return WordStructure(verb.text[:-3] + "щешь", get_rhytmic_structure(verb))
                    elif re.search(".*ся$", verb.text, re.I):
                        if re.search(".*чься$", verb.text, re.I):
                            return WordStructure(verb.text[:-4] + "чёшься", get_rhytmic_structure(verb)[:-2] + "-^-")
                        else:
                            return WordStructure(verb.text[:-2] + "ешься", get_rhytmic_structure(verb))
                    else:
                        if re.search(".*ереть$", verb.text, re.I) and verb.stress_position == verb.syllables_count:
                            return WordStructure(verb.text[:-5] + "рёшь",
                                                 get_rhytmic_structure(verb)[:-2] + "^")
                        if re.search(".*еть$", verb.text, re.I) and verb.stress_position == verb.syllables_count:
                            if re.search(".*петь$", verb.text, re.I):
                                return WordStructure(verb.text[:-3] + "оёшь", get_rhytmic_structure(verb)[:-1] + "-^")
                            else:
                                return WordStructure(verb.text[:-2] + "лишь", get_rhytmic_structure(verb))
                        elif re.search(".*[аиуя]ть$", verb.text, re.I):
                            if verb.stress_position == verb.syllables_count:
                                if re.search(".*нять$", verb.text, re.I):
                                    return WordStructure(verb.text[:-4] + "мешь",
                                                         get_rhytmic_structure(verb)[:-2] + "^-")
                                elif re.search(".*пить$", verb.text, re.I):
                                    return WordStructure(verb.text[:-3] + "ишь",
                                                         get_rhytmic_structure(verb)[:-2] + "^-")
                                elif re.search(".*шить$", verb.text, re.I):
                                    return WordStructure(verb.text[:-3] + "шишь",
                                                         get_rhytmic_structure(verb))
                                elif re.search(".*зить$", verb.text, re.I):
                                    return WordStructure(verb.text[:-4] + "зишь",
                                                         get_rhytmic_structure(verb))
                                elif re.search(".*зать$", verb.text, re.I):
                                    return WordStructure(verb.text[:-4] + "жешь",
                                                         get_rhytmic_structure(verb)[:-2] + "^-")
                                elif re.search(".*нуть$", verb.text, re.I):
                                    return WordStructure(verb.text[:-4] + "нёшь",
                                                         get_rhytmic_structure(verb))
                                else:
                                    return WordStructure(verb.text[:-2] + "ешь",
                                                         get_rhytmic_structure(verb) + "-")
                            else:
                                if re.search(".*уть$", verb.text, re.I):
                                    return WordStructure(verb.text[:-3] + "ешь", get_rhytmic_structure(verb))
                                elif re.search(".*шить$", verb.text, re.I):
                                    return WordStructure(verb.text[:-4] + "шишь",
                                                         get_rhytmic_structure(verb))
                                else:
                                    return WordStructure(verb.text[:-2] + "ешь", get_rhytmic_structure(verb) + "-")
                        elif re.search(".*ести$", verb.text, re.I):
                            return WordStructure(verb.text[:-4] + "есёшь", get_rhytmic_structure(verb)[:-2] + "-^")
                        elif re.search(".*очь$", verb.text, re.I):
                            return WordStructure(verb.text[:-3] + "ожешь", get_rhytmic_structure(verb)[:-1] + "^-")
                        else:
                            return WordStructure(verb.text[:-2] + "ешь", get_rhytmic_structure(verb))
                if person == 3:
                    if re.search(".*(ид|й)ти$", verb.text, re.I):
                        if verb.text == "идти":
                            return WordStructure("придёт", "^")
                        elif re.search(".*йти$", verb.text, re.I):
                            return WordStructure(verb.text[:-2] + "дёт", get_rhytmic_structure(verb))
                        else:
                            return WordStructure(verb.text[:-3] + "дёт", get_rhytmic_structure(verb))
                    elif re.search(".*сть$", verb.text, re.I):
                        return WordStructure(verb.text[:-3] + "щет", get_rhytmic_structure(verb))
                    elif re.search(".*ся$", verb.text, re.I):
                        if re.search(".*чься$", verb.text, re.I):
                            return WordStructure(verb.text[:-4] + "чётся", get_rhytmic_structure(verb)[:-2] + "-^-")
                        else:
                            return WordStructure(verb.text[:-2] + "ется", get_rhytmic_structure(verb))
                    else:
                        if re.search(".*ереть$", verb.text, re.I) and verb.stress_position == verb.syllables_count:
                            return WordStructure(verb.text[:-5] + "рёт",
                                                 get_rhytmic_structure(verb)[:-2] + "^")
                        if re.search(".*еть$", verb.text, re.I) and verb.stress_position == verb.syllables_count:
                            if re.search(".*петь$", verb.text, re.I):
                                return WordStructure(verb.text[:-3] + "оёт", get_rhytmic_structure(verb)[:-1] + "-^")
                            else:
                                return WordStructure(verb.text[:-2] + "лит", get_rhytmic_structure(verb))
                        elif re.search(".*[аиуя]ть$", verb.text, re.I):
                            if verb.stress_position == verb.syllables_count:
                                if re.search(".*нять$", verb.text, re.I):
                                    return WordStructure(verb.text[:-4] + "мет",
                                                         get_rhytmic_structure(verb)[:-2] + "^-")
                                elif re.search(".*пить$", verb.text, re.I):
                                    return WordStructure(verb.text[:-3] + "ит",
                                                         get_rhytmic_structure(verb)[:-2] + "^-")
                                elif re.search(".*шить$", verb.text, re.I):
                                    return WordStructure(verb.text[:-3] + "шит",
                                                         get_rhytmic_structure(verb))
                                elif re.search(".*зить$", verb.text, re.I):
                                    return WordStructure(verb.text[:-4] + "зит",
                                                         get_rhytmic_structure(verb))
                                elif re.search(".*зать$", verb.text, re.I):
                                    return WordStructure(verb.text[:-4] + "жет",
                                                         get_rhytmic_structure(verb)[:-2] + "^-")
                                elif re.search(".*нуть$", verb.text, re.I):
                                    return WordStructure(verb.text[:-4] + "нёт",
                                                         get_rhytmic_structure(verb))
                                else:
                                    return WordStructure(verb.text[:-2] + "ет",
                                                         get_rhytmic_structure(verb) + "-")
                            else:
                                if re.search(".*уть$", verb.text, re.I):
                                    return WordStructure(verb.text[:-3] + "ет", get_rhytmic_structure(verb))
                                elif re.search(".*шить$", verb.text, re.I):
                                    return WordStructure(verb.text[:-4] + "шит",
                                                         get_rhytmic_structure(verb))
                                else:
                                    return WordStructure(verb.text[:-2] + "ет", get_rhytmic_structure(verb) + "-")
                        elif re.search(".*ести$", verb.text, re.I):
                            return WordStructure(verb.text[:-4] + "есёт", get_rhytmic_structure(verb)[:-2] + "-^")
                        elif re.search(".*очь$", verb.text, re.I):
                            return WordStructure(verb.text[:-3] + "ожет", get_rhytmic_structure(verb)[:-1] + "^-")
                        else:
                            return WordStructure(verb.text[:-2] + "ет", get_rhytmic_structure(verb))
            else:
                if person == 1:
                    if re.search(".*(ид|й)ти$", verb.text, re.I):
                        if verb.text == "идти":
                            return WordStructure("придём", "-^")
                        elif re.search(".*йти$", verb.text, re.I):
                            return WordStructure(verb.text[:-2] + "дём", get_rhytmic_structure(verb))
                        else:
                            return WordStructure(verb.text[:-3] + "дём", get_rhytmic_structure(verb))
                    elif re.search(".*сть$", verb.text, re.I):
                        return WordStructure(verb.text[:-3] + "щем", get_rhytmic_structure(verb))
                    elif re.search(".*ся$", verb.text, re.I):
                        if re.search(".*чься$", verb.text, re.I):
                            return WordStructure(verb.text[:-4] + "чёмся", get_rhytmic_structure(verb)[:-2] + "-^-")
                        else:
                            return WordStructure(verb.text[:-2] + "емся", get_rhytmic_structure(verb))
                    else:
                        if re.search(".*ереть$", verb.text, re.I) and verb.stress_position == verb.syllables_count:
                            return WordStructure(verb.text[:-5] + "рём",
                                                 get_rhytmic_structure(verb)[:-2] + "^")
                        if re.search(".*еть$", verb.text, re.I) and verb.stress_position == verb.syllables_count:
                            if re.search(".*петь$", verb.text, re.I):
                                return WordStructure(verb.text[:-3] + "оём", get_rhytmic_structure(verb)[:-1] + "-^")
                            else:
                                return WordStructure(verb.text[:-2] + "лим", get_rhytmic_structure(verb))
                        elif re.search(".*[аиуя]ть$", verb.text, re.I):
                            if verb.stress_position == verb.syllables_count:
                                if re.search(".*нять$", verb.text, re.I):
                                    return WordStructure(verb.text[:-4] + "мем",
                                                         get_rhytmic_structure(verb)[:-2] + "^-")
                                elif re.search(".*пить$", verb.text, re.I):
                                    return WordStructure(verb.text[:-3] + "им",
                                                         get_rhytmic_structure(verb)[:-2] + "^-")
                                elif re.search(".*шить$", verb.text, re.I):
                                    return WordStructure(verb.text[:-3] + "шим",
                                                         get_rhytmic_structure(verb))
                                elif re.search(".*зить$", verb.text, re.I):
                                    return WordStructure(verb.text[:-4] + "зим",
                                                         get_rhytmic_structure(verb))
                                elif re.search(".*зать$", verb.text, re.I):
                                    return WordStructure(verb.text[:-4] + "жем",
                                                         get_rhytmic_structure(verb)[:-2] + "^-")
                                elif re.search(".*нуть$", verb.text, re.I):
                                    return WordStructure(verb.text[:-4] + "нём",
                                                         get_rhytmic_structure(verb))
                                else:
                                    return WordStructure(verb.text[:-2] + "ем",
                                                         get_rhytmic_structure(verb) + "-")
                            else:
                                if re.search(".*уть$", verb.text, re.I):
                                    return WordStructure(verb.text[:-3] + "ем", get_rhytmic_structure(verb))
                                elif re.search(".*шить$", verb.text, re.I):
                                    return WordStructure(verb.text[:-4] + "шим",
                                                         get_rhytmic_structure(verb))
                                else:
                                    return WordStructure(verb.text[:-2] + "ем", get_rhytmic_structure(verb) + "-")
                        elif re.search(".*ести$", verb.text, re.I):
                            return WordStructure(verb.text[:-4] + "есём", get_rhytmic_structure(verb)[:-2] + "-^")
                        elif re.search(".*очь$", verb.text, re.I):
                            return WordStructure(verb.text[:-3] + "ожем", get_rhytmic_structure(verb)[:-1] + "^-")
                        else:
                            return WordStructure(verb.text[:-2] + "ем", get_rhytmic_structure(verb))
                if person == 2:
                    if re.search(".*(ид|й)ти$", verb.text, re.I):
                        if verb.text == "идти":
                            return WordStructure("придёте", "^-")
                        elif re.search(".*йти$", verb.text, re.I):
                            return WordStructure(verb.text[:-2] + "дёте", get_rhytmic_structure(verb) + "-")
                        else:
                            return WordStructure(verb.text[:-3] + "дёте", get_rhytmic_structure(verb) + "-")
                    elif re.search(".*сть$", verb.text, re.I):
                        return WordStructure(verb.text[:-3] + "щете", get_rhytmic_structure(verb))
                    elif re.search(".*ся$", verb.text, re.I):
                        if re.search(".*чься$", verb.text, re.I):
                            return WordStructure(verb.text[:-4] + "чётесь", get_rhytmic_structure(verb)[:-2] + "-^-")
                        else:
                            return WordStructure(verb.text[:-2] + "етесь", get_rhytmic_structure(verb))
                    else:
                        if re.search(".*ереть$", verb.text, re.I) and verb.stress_position == verb.syllables_count:
                            return WordStructure(verb.text[:-5] + "рёте",
                                                 get_rhytmic_structure(verb)[:-2] + "^-")
                        if re.search(".*еть$", verb.text, re.I) and verb.stress_position == verb.syllables_count:
                            if re.search(".*петь$", verb.text, re.I):
                                return WordStructure(verb.text[:-3] + "оёте",
                                                     get_rhytmic_structure(verb)[:-1] + "-^-")
                            else:
                                return WordStructure(verb.text[:-2] + "лите", get_rhytmic_structure(verb) + "-")
                        elif re.search(".*[аиуя]ть$", verb.text, re.I):
                            if verb.stress_position == verb.syllables_count:
                                if re.search(".*нять$", verb.text, re.I):
                                    return WordStructure(verb.text[:-4] + "мете",
                                                         get_rhytmic_structure(verb)[:-2] + "^--")
                                elif re.search(".*пить$", verb.text, re.I):
                                    return WordStructure(verb.text[:-3] + "ите",
                                                         get_rhytmic_structure(verb)[:-2] + "^--")
                                elif re.search(".*шить$", verb.text, re.I):
                                    return WordStructure(verb.text[:-3] + "шите",
                                                         get_rhytmic_structure(verb) + "-")
                                elif re.search(".*зить$", verb.text, re.I):
                                    return WordStructure(verb.text[:-4] + "зите",
                                                         get_rhytmic_structure(verb) + "-")
                                elif re.search(".*зать$", verb.text, re.I):
                                    return WordStructure(verb.text[:-4] + "жете",
                                                         get_rhytmic_structure(verb)[:-2] + "^--")
                                elif re.search(".*нуть$", verb.text, re.I):
                                    return WordStructure(verb.text[:-4] + "нёте",
                                                         get_rhytmic_structure(verb) + "-")
                                else:
                                    return WordStructure(verb.text[:-2] + "ете",
                                                         get_rhytmic_structure(verb) + "--")
                            else:
                                if re.search(".*уть$", verb.text, re.I):
                                    return WordStructure(verb.text[:-3] + "ете", get_rhytmic_structure(verb) + "-")
                                elif re.search(".*шить$", verb.text, re.I):
                                    return WordStructure(verb.text[:-4] + "шите",
                                                         get_rhytmic_structure(verb) + "-")
                                else:
                                    return WordStructure(verb.text[:-2] + "ете", get_rhytmic_structure(verb) + "--")
                        elif re.search(".*ести$", verb.text, re.I):
                            return WordStructure(verb.text[:-4] + "есёте", get_rhytmic_structure(verb)[:-2] + "-^-")
                        elif re.search(".*очь$", verb.text, re.I):
                            return WordStructure(verb.text[:-3] + "ожете", get_rhytmic_structure(verb)[:-1] + "^--")
                        else:
                            return WordStructure(verb.text[:-2] + "ете", get_rhytmic_structure(verb) + "-")
                if person == 3:
                    if re.search(".*(ид|й)ти$", verb.text, re.I):
                        if verb.text == "идти":
                            return WordStructure("придут", "-^")
                        elif re.search(".*йти$", verb.text, re.I):
                            return WordStructure(verb.text[:-2] + "дут", get_rhytmic_structure(verb))
                        else:
                            return WordStructure(verb.text[:-3] + "дут", get_rhytmic_structure(verb))
                    elif re.search(".*сть$", verb.text, re.I):
                        return WordStructure(verb.text[:-3] + "щут", get_rhytmic_structure(verb))
                    elif re.search(".*ся$", verb.text, re.I):
                        if re.search(".*чься$", verb.text, re.I):
                            return WordStructure(verb.text[:-4] + "кутся", get_rhytmic_structure(verb)[:-2] + "-^-")
                        else:
                            return WordStructure(verb.text[:-2] + "утся", get_rhytmic_structure(verb))
                    else:
                        if re.search(".*ереть$", verb.text, re.I) and verb.stress_position == verb.syllables_count:
                            return WordStructure(verb.text[:-5] + "рут",
                                                 get_rhytmic_structure(verb)[:-2] + "^")
                        if re.search(".*еть$", verb.text, re.I) and verb.stress_position == verb.syllables_count:
                            if re.search(".*петь$", verb.text, re.I):
                                return WordStructure(verb.text[:-3] + "оют", get_rhytmic_structure(verb)[:-1] + "-^")
                            else:
                                return WordStructure(verb.text[:-2] + "ят", get_rhytmic_structure(verb))
                        elif re.search(".*[аиуя]ть$", verb.text, re.I):
                            if verb.stress_position == verb.syllables_count:
                                if re.search(".*нять$", verb.text, re.I):
                                    return WordStructure(verb.text[:-4] + "мут",
                                                         get_rhytmic_structure(verb)[:-2] + "^-")
                                elif re.search(".*пить$", verb.text, re.I):
                                    return WordStructure(verb.text[:-4] + "пают",
                                                         get_rhytmic_structure(verb)[:-2] + "-^-")
                                elif re.search(".*шить$", verb.text, re.I):
                                    return WordStructure(verb.text[:-3] + "шат",
                                                         get_rhytmic_structure(verb))
                                elif re.search(".*зить$", verb.text, re.I):
                                    return WordStructure(verb.text[:-4] + "зят",
                                                         get_rhytmic_structure(verb))
                                elif re.search(".*зать$", verb.text, re.I):
                                    return WordStructure(verb.text[:-4] + "жут",
                                                         get_rhytmic_structure(verb)[:-2] + "^-")
                                elif re.search(".*нуть$", verb.text, re.I):
                                    return WordStructure(verb.text[:-4] + "нут",
                                                         get_rhytmic_structure(verb))
                                else:
                                    return WordStructure(verb.text[:-2] + "ют",
                                                         get_rhytmic_structure(verb) + "-")
                            else:
                                if re.search(".*уть$", verb.text, re.I):
                                    return WordStructure(verb.text[:-3] + "ут", get_rhytmic_structure(verb))
                                elif re.search(".*шить$", verb.text, re.I):
                                    return WordStructure(verb.text[:-4] + "шат",
                                                         get_rhytmic_structure(verb))
                                else:
                                    return WordStructure(verb.text[:-2] + "ют", get_rhytmic_structure(verb) + "-")
                        elif re.search(".*ести$", verb.text, re.I):
                            return WordStructure(verb.text[:-4] + "есут", get_rhytmic_structure(verb)[:-2] + "-^")
                        elif re.search(".*очь$", verb.text, re.I):
                            return WordStructure(verb.text[:-3] + "огут", get_rhytmic_structure(verb)[:-1] + "^-")
                        else:
                            return WordStructure(verb.text[:-2] + "ут", get_rhytmic_structure(verb))
        else:
            if not plural:
                if person == 1:
                    return WordStructure("буду " + verb.text, "--" + get_rhytmic_structure(verb))
                if person == 2:
                    return WordStructure("будешь " + verb.text, "--" + get_rhytmic_structure(verb))
                if person == 3:
                    return WordStructure("будет " + verb.text, "--" + get_rhytmic_structure(verb))
            else:
                if person == 1:
                    return WordStructure("будем " + verb.text, "--" + get_rhytmic_structure(verb))
                if person == 2:
                    return WordStructure("будете " + verb.text, "--" + get_rhytmic_structure(verb))
                if person == 3:
                    return WordStructure("будут " + verb.text, "--" + get_rhytmic_structure(verb))


def get_imperative(verb, single_or_plural):
    if single_or_plural == "single":
        if verb.conjugation == 1:
            if verb.perfective:
                if re.search(".*петь", verb.text, re.I):
                    return WordStructure(verb.text[:-3] + "ой", get_rhytmic_structure(verb))
                elif re.search(".*ереть", verb.text, re.I):
                    return WordStructure(verb.text[:-5] + "ри", get_rhytmic_structure(verb))
                elif re.search(".*нять", verb.text, re.I):
                    return WordStructure(verb.text[:-4] + "ми", get_rhytmic_structure(verb))
                elif re.search(".*зать", verb.text, re.I):
                    return WordStructure(verb.text[:-4] + "жи", get_rhytmic_structure(verb))
                elif re.search(".*ать", verb.text, re.I):
                    return WordStructure(verb.text[:-2] + "й", get_rhytmic_structure(verb))
                elif re.search(".*(н|гн)уть", verb.text, re.I):
                    return WordStructure(verb.text[:-3] + "и", get_rhytmic_structure(verb))
                elif re.search(".*йти", verb.text, re.I):
                    return WordStructure(verb.text[:-2] + "ди", get_rhytmic_structure(verb))
                elif re.search(".*[дс]ти", verb.text, re.I):
                    return WordStructure(verb.text[:-2] + "и", get_rhytmic_structure(verb))
                elif re.search(".*чься", verb.text, re.I):
                    return WordStructure(verb.text[:-4] + "кись", get_rhytmic_structure(verb)[:-2] + "-^")
                else:
                    return WordStructure(verb.text[:-2] + "й", get_rhytmic_structure(verb))
            else:
                if re.search(".*оваться$", verb.text, re.I):
                    return WordStructure(verb.text[:-7] + "уйся", get_rhytmic_structure(verb)[:-3] + "^-")
                elif re.search(".*овать$", verb.text, re.I):
                    if verb.stress_position == verb.syllables_count:
                        return WordStructure(verb.text[:-5] + "уй", get_rhytmic_structure(verb)[:-2] + "^")
                    else:
                        return WordStructure(verb.text[:-5] + "уй", get_rhytmic_structure(verb)[:-1])
                elif re.search(".*евать$", verb.text, re.I):
                    return WordStructure(verb.text[:-5] + "уй", get_rhytmic_structure(verb)[:-2] + "^")
                elif re.search(".*саться", verb.text, re.I):
                    return WordStructure(verb.text[:-6] + "шись", get_rhytmic_structure(verb)[:-1])
                elif re.search(".*сать", verb.text, re.I):
                    return WordStructure(verb.text[:-4] + "ши", get_rhytmic_structure(verb))
                elif re.search(".*деть$", verb.text, re.I) and verb.syllables_count == verb.stress_position:
                    return WordStructure(verb.text[:-3] + "и", get_rhytmic_structure(verb))
                elif re.search(".*[аея]ть(ся$|$)", verb.text, re.I):
                    if re.search(".*еяться$", verb.text, re.I) and verb.syllables_count != verb.stress_position:
                        return WordStructure(verb.text[:-5] + "йся", get_rhytmic_structure(verb)[:-3] + "^-")
                    elif re.search(".*[яа]ться$", verb.text, re.I) and verb.syllables_count != verb.stress_position:
                        return WordStructure(verb.text[:-4] + "йся", get_rhytmic_structure(verb))
                    elif re.search(".*ять$", verb.text, re.I) and verb.syllables_count != verb.stress_position:
                        return WordStructure(verb.text[:-3] + "й", get_rhytmic_structure(verb)[:-2] + "^")
                    elif re.search(".*еть$", verb.text, re.I) and verb.syllables_count == verb.stress_position:
                        return WordStructure(verb.text[:-3] + "ей", get_rhytmic_structure(verb))
                    else:
                        return WordStructure(verb.text[:-2] + "й", get_rhytmic_structure(verb))
                elif re.search(".*лить$", verb.text, re.I):
                    return WordStructure(verb.text[:-3] + "и", get_rhytmic_structure(verb))
                elif re.search(".*иться$", verb.text, re.I):
                    return WordStructure(verb.text[:-5] + "ейся", get_rhytmic_structure(verb))
                elif re.search(".*ить$", verb.text, re.I):
                    return WordStructure(verb.text[:-3] + "ей", get_rhytmic_structure(verb))
                elif re.search(".*ыть$", verb.text, re.I):
                    return WordStructure(verb.text[:-3] + "ой", get_rhytmic_structure(verb))
                elif re.search(".*оть$", verb.text, re.I):
                    return WordStructure(verb.text[:-3] + "и", get_rhytmic_structure(verb))
                else:
                    return WordStructure(verb.text[:-2], get_rhytmic_structure(verb))
        elif verb.conjugation == 2:
            if verb.perfective:
                if re.search(".*шить", verb.text, re.I):
                    return WordStructure(verb.text[:-3] + "ь", get_rhytmic_structure(verb)[:-1])
                else:
                    return WordStructure(verb.text[:-3] + "и", get_rhytmic_structure(verb))
            else:
                if re.search(".*титься$", verb.text, re.I):
                    return WordStructure(verb.text[:-5] + "ься", get_rhytmic_structure(verb)[:-1])
                elif re.search(".*тить$", verb.text, re.I):
                    return WordStructure(verb.text[:-3] + "ь", get_rhytmic_structure(verb)[:-1])
                elif re.search(".*[пт]еться$", verb.text, re.I):
                    return WordStructure(verb.text[:-5] + "ись", get_rhytmic_structure(verb)[:-1])
                elif re.search(".*[еа]ть$", verb.text, re.I):
                    if verb.syllables_count == verb.stress_position:
                        return WordStructure(verb.text[:-3] + "и", get_rhytmic_structure(verb))
                    else:
                        return WordStructure(verb.text[:-3] + "ь", get_rhytmic_structure(verb)[:-1])
                elif re.search(".*иться$", verb.text, re.I):
                    return WordStructure(verb.text[:-4] + "сь", get_rhytmic_structure(verb)[:-1])
                elif re.search(".*ить$", verb.text, re.I):
                    return WordStructure(verb.text[:-2], get_rhytmic_structure(verb))
                elif re.search(".*гнать$", verb.text, re.I):
                    return WordStructure(verb.text[:-4] + "они", get_rhytmic_structure(verb))
                else:
                    return WordStructure(verb.text[:-2], get_rhytmic_structure(verb))
        else:
            if re.search(".*есть$", verb.text, re.I):
                if verb.text == "есть":
                    return WordStructure("ешь", "^")
                else:
                    return WordStructure(verb.text[:-3] + "шь", "-^")
            elif re.search(".*дать$", verb.text, re.I):
                return WordStructure(verb.text[:-2] + "й", get_rhytmic_structure(verb))
            elif re.search(".+быть$", verb.text, re.I):
                return WordStructure(verb.text[:-2] + "вай", get_rhytmic_structure(verb))
            elif verb.text == "хотеть":
                return WordStructure("хоти", "-^")
            elif verb.text == "бежать":
                return WordStructure("беги", "-^")
            elif verb.text == "чтить":
                return WordStructure("чти", "^")
            elif verb.text == "ехать":
                return WordStructure("едь", "^")
            elif verb.text == "идти":
                return WordStructure("иди", "-^")
            elif verb.text == "быть":
                return WordStructure("будь", "^")
            else:
                return WordStructure("ошибка" "------")
    elif single_or_plural == "plural":
        if verb.conjugation == 1:
            if verb.perfective:
                if re.search(".*петь", verb.text, re.I):
                    return WordStructure(verb.text[:-3] + "ойте", get_rhytmic_structure(verb) + "-")
                elif re.search(".*ереть", verb.text, re.I):
                    return WordStructure(verb.text[:-5] + "рите", get_rhytmic_structure(verb)[:-2] + "^-")
                elif re.search(".*нять", verb.text, re.I):
                    return WordStructure(verb.text[:-4] + "мите", get_rhytmic_structure(verb) + "-")
                elif re.search(".*зать", verb.text, re.I):
                    return WordStructure(verb.text[:-4] + "жите", get_rhytmic_structure(verb) + "-")
                elif re.search(".*ать", verb.text, re.I):
                    return WordStructure(verb.text[:-2] + "йте", get_rhytmic_structure(verb) + "-")
                elif re.search(".*(н|гн)уть", verb.text, re.I):
                    return WordStructure(verb.text[:-3] + "ите", get_rhytmic_structure(verb) + "-")
                elif re.search(".*йти", verb.text, re.I):
                    return WordStructure(verb.text[:-2] + "дите", get_rhytmic_structure(verb) + "-")
                elif re.search(".*[дс]ти", verb.text, re.I):
                    return WordStructure(verb.text[:-2] + "ите", get_rhytmic_structure(verb) + "-")
                elif re.search(".*чься", verb.text, re.I):
                    return WordStructure(verb.text[:-4] + "китесь", get_rhytmic_structure(verb)[:-2] + "-^-")
                else:
                    return WordStructure(verb.text[:-2] + "йте", get_rhytmic_structure(verb) + "-")
            else:
                if re.search(".*оваться$", verb.text, re.I):
                    return WordStructure(verb.text[:-7] + "уйтесь", get_rhytmic_structure(verb)[:-3] + "^-")
                elif re.search(".*овать$", verb.text, re.I):
                    if verb.stress_position == verb.syllables_count:
                        return WordStructure(verb.text[:-5] + "уйте", get_rhytmic_structure(verb)[:-2] + "^-")
                    else:
                        return WordStructure(verb.text[:-5] + "уйте", get_rhytmic_structure(verb)[:-1] + "-")
                elif re.search(".*евать$", verb.text, re.I):
                    return WordStructure(verb.text[:-5] + "уйте", get_rhytmic_structure(verb)[:-2] + "^-")
                elif re.search(".*саться", verb.text, re.I):
                    return WordStructure(verb.text[:-6] + "шитесь", get_rhytmic_structure(verb)[:-1] + "-")
                elif re.search(".*сать", verb.text, re.I):
                    return WordStructure(verb.text[:-4] + "шите", get_rhytmic_structure(verb) + "-")
                elif re.search(".*деть$", verb.text, re.I) and verb.syllables_count == verb.stress_position:
                    return WordStructure(verb.text[:-3] + "ите", get_rhytmic_structure(verb) + "-")
                elif re.search(".*[аея]ть(ся$|$)", verb.text, re.I):
                    if re.search(".*еяться$", verb.text, re.I) and verb.syllables_count != verb.stress_position:
                        return WordStructure(verb.text[:-5] + "йтесь", get_rhytmic_structure(verb)[:-3] + "^-")
                    elif re.search(".*[яа]ться$", verb.text, re.I) and verb.syllables_count != verb.stress_position:
                        return WordStructure(verb.text[:-4] + "йтесь", get_rhytmic_structure(verb))
                    elif re.search(".*ять$", verb.text, re.I) and verb.syllables_count != verb.stress_position:
                        return WordStructure(verb.text[:-3] + "йте", get_rhytmic_structure(verb)[:-2] + "^-")
                    elif re.search(".*еть$", verb.text, re.I) and verb.syllables_count == verb.stress_position:
                        return WordStructure(verb.text[:-3] + "ейте", get_rhytmic_structure(verb) + "-")
                    else:
                        return WordStructure(verb.text[:-2] + "йте", get_rhytmic_structure(verb) + "-")
                elif re.search(".*лить$", verb.text, re.I):
                    return WordStructure(verb.text[:-3] + "ите", get_rhytmic_structure(verb) + "-")
                elif re.search(".*иться$", verb.text, re.I):
                    return WordStructure(verb.text[:-5] + "ейтесь", get_rhytmic_structure(verb) + "-")
                elif re.search(".*ить$", verb.text, re.I):
                    return WordStructure(verb.text[:-3] + "ейте", get_rhytmic_structure(verb) + "-")
                elif re.search(".*ыть$", verb.text, re.I):
                    return WordStructure(verb.text[:-3] + "ойте", get_rhytmic_structure(verb) + "-")
                elif re.search(".*оть$", verb.text, re.I):
                    return WordStructure(verb.text[:-3] + "ите", get_rhytmic_structure(verb) + "-")
                else:
                    return WordStructure(verb.text[:-2] + "те", get_rhytmic_structure(verb) + "-")
        elif verb.conjugation == 2:
            if verb.perfective:
                if re.search(".*шить", verb.text, re.I):
                    return WordStructure(verb.text[:-3] + "ьте", get_rhytmic_structure(verb)[:-1] + "-")
                else:
                    return WordStructure(verb.text[:-3] + "ите", get_rhytmic_structure(verb) + "-")
            else:
                if re.search(".*титься$", verb.text, re.I):
                    return WordStructure(verb.text[:-5] + "ьтесь", get_rhytmic_structure(verb)[:-1])
                elif re.search(".*тить$", verb.text, re.I):
                    return WordStructure(verb.text[:-3] + "ьте", get_rhytmic_structure(verb)[:-1] + "-")
                elif re.search(".*[пт]еться$", verb.text, re.I):
                    return WordStructure(verb.text[:-5] + "итесь", get_rhytmic_structure(verb)[:-1] + "-")
                elif re.search(".*[еа]ть$", verb.text, re.I):
                    if verb.syllables_count == verb.stress_position:
                        return WordStructure(verb.text[:-3] + "ите", get_rhytmic_structure(verb) + "-")
                    else:
                        return WordStructure(verb.text[:-3] + "ьте", get_rhytmic_structure(verb)[:-1] + "-")
                elif re.search(".*иться$", verb.text, re.I):
                    return WordStructure(verb.text[:-4] + "тесь", get_rhytmic_structure(verb)[:-1])
                elif re.search(".*ить$", verb.text, re.I):
                    return WordStructure(verb.text[:-2] + "те", get_rhytmic_structure(verb) + "-")
                elif re.search(".*гнать$", verb.text, re.I):
                    return WordStructure(verb.text[:-4] + "оните", get_rhytmic_structure(verb) + "-")
                else:
                    return WordStructure(verb.text[:-2] + "те", get_rhytmic_structure(verb) + "-")
        else:
            if re.search(".*есть$", verb.text, re.I):
                if verb.text == "есть":
                    return WordStructure("ешьте", "^-")
                else:
                    return WordStructure(verb.text[:-3] + "шьте", "-^-")
            elif re.search(".*дать$", verb.text, re.I):
                return WordStructure(verb.text[:-2] + "йте", get_rhytmic_structure(verb) + "-")
            elif re.search(".+быть$", verb.text, re.I):
                return WordStructure(verb.text[:-2] + "вайте", get_rhytmic_structure(verb) + "-")
            elif verb.text == "хотеть":
                return WordStructure("хотите", "-^-")
            elif verb.text == "бежать":
                return WordStructure("бегите", "-^-")
            elif verb.text == "чтить":
                return WordStructure("чтите", "^-")
            elif verb.text == "ехать":
                return WordStructure("едьте", "^-")
            elif verb.text == "идти":
                return WordStructure("идите", "-^-")
            elif verb.text == "быть":
                return WordStructure("будьте", "^-")
            else:
                return WordStructure("ошибка" "------")
