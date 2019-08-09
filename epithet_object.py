import re
from word_object import Word, WordStructure

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