from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for questions in question_data:
    question_bank.append(Question(questions['question'],questions['correct_answer'],questions['incorrect_answers']))
    
    

brain = QuizBrain(question_bank)

while brain.hay_preguntas():
    brain.next_question()

if(brain.hay_preguntas() == False):
    print(f"Completaste el quiz!\nTu score final es: {brain.score}")
else:
    print(f"Tu score fue de: {brain.score}")