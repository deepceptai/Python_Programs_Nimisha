from Question import Question

question_prompt = [
    "What color is apple? \n a)Red \n b)Blue \n c)Purple \n\n ",
    "What color is Banana? \n a)Red \n b)Yellow \n c)Green \n\n ",
    "What color is strawberry? \n a)Blue \n b)Green \n c)Red \n\n ",
]

questions = [
    Question(question_prompt[0], "a"),
    Question(question_prompt[1], "b"),
    Question(question_prompt[2], "c")
]


def run(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("Your got " + str(score) + "/" + str(len(questions)) + " correct ")


run(questions)


