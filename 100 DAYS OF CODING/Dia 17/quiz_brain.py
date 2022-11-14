class QuizBrain:
    def __init__(self, list):
        self.question_number = 0
        self.questions_list = list
        self.score = 0
    
    def hay_preguntas(self):
        if(self.question_number < len(self.questions_list)):
            return True 
        return False

    def next_question(self):
        pregunta = self.questions_list[self.question_number]
        respuesta = input(f"Q.{self.question_number + 1}: {pregunta.text} (True/False): ")
        self.checkiar_respuesta(pregunta,respuesta)
            

    def checkiar_respuesta(self, pregunta, respuesta):       
        if(pregunta.answer.lower() == respuesta.lower()):
            self.score += 1
            print(f"Correcto! :)\nScore: {self.score}")
        else:
            print(f"La respuesta correcta es: {pregunta.incorrect_answer[0]},\nScore: {self.score}")
        self.question_number += 1