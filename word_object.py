import re


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


def get_rhytmic_structure(word):
    rhytmic_structure = ""
    for x in range(word.syllables_count):
        if x == word.stress_position - 1:
            rhytmic_structure += "^"
        else:
            rhytmic_structure += "-"
    return rhytmic_structure
