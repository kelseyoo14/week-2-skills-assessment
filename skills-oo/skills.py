# Part 1: Discussion
# What are the three main design advantages that object orientation can provide?

# The 3 main advantages of object orientation are encapsulation, abstraction, and polymorphism.

# Encapsulation offers the ability to keep variables(attributes) and functions(methods) together in the 
# same namespace, where they can be easily found and called on to interact with each other.
# Abstraction offers the ability to easily make similar but different types of encapsulated data/functions.
# Polymorphism offers the ability to easily condense functionality without using lots of conditionals.

# Objects orientation offers enough structure to easily replicated similar data/functionaily, but to switch
# and interchange parts where needed.

# Explain each concept.

# 1. What is a class?
# A class is a mold for easily replicating data/functionality. From a class, we can instantiate specific 
# instances whose structures is inherited from the class 'mold' under which is is made, but that have 
# unique properties specific to each instance.

# 2. What is an instance attribute?
# An instance attribute is a variable that is specific to the instance it belongs to, and cannot be inherited
# by other instances under the same class.

# 3. What is a method?
# A method is basically a function for classes. It is encapsulated functionality to be used on the data of the
# classes(es) it is under.

# 4. What is an instance in object orientation?
# An instance is a specific encapsulation of data. Instances are objects, and inherit many of their properties 
# and functionality from the classes they are created from.

# 5. How is a class attribute different than an instance attribute? Give an example of when you might use each.
# Class attributes are created under a class, and instance's can inherit these attributes from the classes they
# are created under. An instance attribute though is specific to the instance it is created under, and cannot
# be inherited by other instances under the same classes. Multiple instances can inherit a class attribute,
# but an instance attributes are unique to each instance.


# Parts 2 through 5:
# Create your classes and class methods


class Student(object):
    def __init__(self, first_name, last_name, address):

        self.information = {'first_name': first_name,
                            'last_name': last_name,
                            'address': address}


class Question(object):
    def __init__(self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer
        self.question_info = {'question': question,
                    'correct_answer': correct_answer}

    def ask_and_evaluate(self):
        question = self.question_info['question']
        user_answer = raw_input(question + " > ")
        if self.question_info['correct_answer'] == user_answer:
            return True
        else:
            return False




class Exam(object):
    def __init__(self, name):
        # self.name = name
        self.information = {'name': name,
                            'questions': []}

    def add_question(self, question, correct_answer):
        new_question = Question(question, correct_answer)
        self.information['questions'].append(new_question.question_info)


    def administer(self):
        num_of_questions = 0
        score = 0
        for question in self.information['questions']:
            user_answer = raw_input(question['question'] + "> ")
            if question['correct_answer'] == user_answer:
                score += 1
            num_of_questions += 1
        return score/float(num_of_questions)

class Quiz(Exam):
    def administer(self):
        num_of_questions = 0
        score = 0
        for question in self.information['questions']:
            user_answer = raw_input(question['question'] + "> ")
            if question['correct_answer'] == user_answer:
                score += 1
            num_of_questions += 1
        score = score/num_of_questions
        if score > 0.50:
            return True
        else:
            return False




def take_test(exam, student):
    score = exam.administer()
    student.score = score
    return student.score



def example():
    example_exam = Exam('example_final')
    example_student = Student("le first", "le last", "Hackbright, CA")

    example_exam.add_question('testing1', 'test1')
    example_exam.add_question('testing2', 'test2')
    example_exam.add_question('testing3', 'test3')

    return take_test(example_exam, example_student)


print example()

