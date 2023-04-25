class Form:
    def __init__(self, grade, topic):
        self.grade = grade
        self.topic = topic
        self.questions = list()

    def add_question(self, question: Question):
        pass

    def print(self):
        s = ''
        s += f'Тест для {self.grade} по теме {self.topic}\n'
        for question in self.questions:
            s+= question.print() + '\n'

        return s


class Question:
    def __init__(self):
        self.text = ''
        self.variants = list()
        self.correct_answer = ''

    def print(self):
        pass

    def set_answer(self, answer):
        if answer in self.variants:
            self.correct_answer = answer
        else:
            print('Несуществующий вариант ответа')

    def add_variant(self, variant):
        self.variants.append(variant)

    def add_variants(self, variants):
        self.variants.extend(variants)

    def remove_variant(self):
        if self.variants:
            self.variants.pop()

    def set_text(self, text):
        self.text = text

class SingleAnswerQuestion(Question):
    pass

class MultipleAnswerQuestion(Question):
    pass

class OpenAnswerQuestion(Question):
    pass