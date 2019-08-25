import re
from word_object import Word, WordStructure, get_rhytmic_structure


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

    def get_possessive_base(self, grammatical_gender, case):
        if re.search(".*[еиа]й$|ь$", self.text, re.I):
            if grammatical_gender == "male":
                word = WordStructure(self.text[:-1] + "ев", get_rhytmic_structure(self) + "-")
            elif grammatical_gender == "female":
                word = WordStructure(self.text[:-1] + "ева", get_rhytmic_structure(self) + "--")
            else:
                word = WordStructure(self.text[:-1] + "ево", get_rhytmic_structure(self) + "--")
        elif re.search(".*(а|ья)$", self.text, re.I):
            if grammatical_gender == "male":
                word = WordStructure(self.text[:-1] + "ин", get_rhytmic_structure(self) + "-")
            elif grammatical_gender == "female":
                word = WordStructure(self.text[:-1] + "ина", get_rhytmic_structure(self) + "--")
            else:
                word = WordStructure(self.text[:-1] + "ино", get_rhytmic_structure(self) + "--")
        elif re.search(".*ав$", self.text, re.I):
            if grammatical_gender == "male":
                word = WordStructure(self.text + "лев", get_rhytmic_structure(self) + "-")
            elif grammatical_gender == "female":
                word = WordStructure(self.text + "лева", get_rhytmic_structure(self) + "--")
            else:
                word = WordStructure(self.text + "лево", get_rhytmic_structure(self) + "--")
        elif re.search(".*ия$", self.text, re.I):
            if grammatical_gender == "male":
                word = WordStructure(self.text[:-1] + "ин", get_rhytmic_structure(self) + "-")
            elif grammatical_gender == "female":
                word = WordStructure(self.text[:-1] + "ина", get_rhytmic_structure(self) + "--")
            else:
                word = WordStructure(self.text[:-1] + "ино", get_rhytmic_structure(self) + "--")
        else:
            if grammatical_gender == "male":
                word = WordStructure(self.text + "ов", get_rhytmic_structure(self) + "-")
            elif grammatical_gender == "female":
                word = WordStructure(self.text + "ова", get_rhytmic_structure(self) + "--")
            else:
                word = WordStructure(self.text + "ово", get_rhytmic_structure(self) + "--")

        if case == "n":
            return word
        elif case == "g":
            if grammatical_gender == "male":
                return WordStructure(word.text + "а", word.rhytmic_structure + "-")
            elif grammatical_gender == "female":
                return WordStructure(word.text[:-1] + "ой", word.rhytmic_structure)
            else:
                return WordStructure(word.text + "го", word.rhytmic_structure + "-")
        elif case == "d":
            if grammatical_gender == "male":
                return WordStructure(word.text + "у", word.rhytmic_structure + "-")
            elif grammatical_gender == "female":
                return WordStructure(word.text[:-1] + "ой", word.rhytmic_structure)
            else:
                return WordStructure(word.text + "му", word.rhytmic_structure + "-")
        elif case == "a":
            if grammatical_gender == "male":
                return WordStructure(word.text + "а", word.rhytmic_structure + "-")
            elif grammatical_gender == "female":
                return WordStructure(word.text[:-1] + "у", word.rhytmic_structure)
            else:
                return word
        elif case == "i":
            if grammatical_gender == "male":
                return WordStructure(word.text + "ым", word.rhytmic_structure + "-")
            elif grammatical_gender == "female":
                return WordStructure(word.text[:-1] + "ой", word.rhytmic_structure)
            else:
                return WordStructure(word.text[:-1] + "ым", word.rhytmic_structure)
        elif case == "p":
            if grammatical_gender == "male":
                return WordStructure(word.text + "ом", word.rhytmic_structure + "-")
            elif grammatical_gender == "female":
                return WordStructure(word.text[:-1] + "ой", word.rhytmic_structure)
            else:
                return WordStructure(word.text + "м", word.rhytmic_structure)

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
