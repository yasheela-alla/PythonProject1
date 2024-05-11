class Quiz:
    def question1(self):
        return "b) A generator object"

    def question2(self):
        return "x ** y"

    def question3(self):
        return "b) To define the constructor of the class"

    def question4(self):
        return "my_list[1]"

    def question5(self):
        return "c) Lists can contain duplicate elements"


def display_question(question_number, question, options):
    print(f"\nQuestion {question_number}: {question}")
    for index, option in enumerate(options, start=1):
        print(f"{index}. {option}")
    answer = int(input("Enter the number of your answer: ").strip())
    return answer


def main():
    quiz = Quiz()
    correct_answers = 0

    answer1 = display_question(1, "What does the `range()` function in Python return?",
                               ["A list of integers", "A generator object", "A tuple of integers",
                                "A dictionary of integers"])
    if answer1 == 2:
        print("Correct!")
        correct_answers += 1
    else:
        print("Incorrect! The correct answer is:", quiz.question1())

    answer2 = display_question(2, "What is the output of the following code snippet?\n\nx = 5\ny = 2\nprint(x ** y)",
                               ["25", "10", "7", "50"])
    if answer2 == 1:
        print("Correct!")
        correct_answers += 1
    else:
        print("Incorrect! The correct answer is:", quiz.question2())

    answer3 = display_question(3, "What is the purpose of the `__init__` method in Python classes?",
                               ["To initialize the class variables", "To define the constructor of the class",
                                "To perform cleanup actions when an object is deleted",
                                "To return the string representation of the object"])
    if answer3 == 2:
        print("Correct!")
        correct_answers += 1
    else:
        print("Incorrect! The correct answer is:", quiz.question3())

    answer4 = display_question(4,
                               "What will be the output of the following code?\n\nmy_list = ['apple', 'banana', 'cherry']\nprint(my_list[1])",
                               ["apple", "banana", "cherry", "None of the above"])
    if answer4 == 2:
        print("Correct!")
        correct_answers += 1
    else:
        print("Incorrect! The correct answer is:", quiz.question4())

    answer5 = display_question(5, "Which of the following statements is true about Python lists?",
                               ["Lists can only store homogeneous data types", "Lists are immutable",
                                "Lists can contain duplicate elements",
                                "Lists are implemented as linked lists in Python"])
    if answer5 == 3:
        print("Correct!")
        correct_answers += 1
    else:
        print("Incorrect! The correct answer is:", quiz.question5())

    print(f"\nYour final score: {correct_answers} out of 5")


if __name__ == "__main__":
    main()

