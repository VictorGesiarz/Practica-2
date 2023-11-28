from Books import Book
from User import User


class CBR():
    
    def __init__(self, cases: list[Book], user: User, similarity_function=False) -> None:
        self.cases = cases
        self.solutions = [case.title for case in cases]
        self.problems = [case.vector for case in cases]
        self.evaluations = [[] for _ in cases]

        self.length = len(cases)
        
        self.similarity_function = self.Manhattan if not similarity_function else similarity_function


    def __repr__(self) -> str:
        print("\n\n")
        print("This CBR contains the next cases: \n")
        for i in range(self.length):
            print(f'{self.cases[i]}, with an evaluation of {self.evaluations[i]}')
        print("\n\n")
        return ""
    

    def run(self, new_problem: Book):

        vector = new_problem.vector

        retrieved_cases = self.__retrieve(vector)
        solution = self.__adapt(retrieved_cases)

        new_problem.title = self.solutions[solution]
        print(f"We recommend you to read: {self.cases[solution]}")

        evaluation = self.__evaluate()
        self.__learn(new_problem, solution, evaluation)
    

    def __retrieve(self, new_problem):

        """In this function we comnpare the cases we have with the new one and select the most similar."""

        similarities = []
        for case in self.problems:
            similarity = self.similarity_function(new_problem, case)
            similarities.append(similarity)
        
        x = 3
        sorted_indices = sorted(range(len(similarities)), key=lambda k: similarities[k])[:x]

        return sorted_indices


    def __adapt(self, retrieved_cases):

        """In this function we take the case with the best solution."""

        # averages = []
        # for case in retrieved_cases:
        #     averages.append(sum(evaluation for evaluation in self.evaluations[case]) / len(self.evaluations[case]))

        # index = averages.index(max(averages))

        return retrieved_cases[0]


    def __evaluate(self):

        """In this function we will evaluate the given solution by asking the user how good it was."""
        
        evaluacion = int(input("In a scale from 1 to 5, how good was the recommendation based on your what you were looking for? "))
        return evaluacion


    def __learn(self, new_problem, solution, evaluation=[]):
        
        """In this function we save the new case with the corresponding solution and evaluation."""

        self.cases.append(new_problem)
        self.problems.append(new_problem.vector)
        self.solutions.append(self.solutions[solution])
        self.evaluations.append([evaluation])

        self.length += 1


    def Manhattan(self, new_problem, case):
        
        """Function to calculate the similarity between two cases. This function performs the Manhattan distance."""

        weights = [1 for _ in range(len(new_problem))]

        return sum(abs(new_problem[i] - case[i]) * weights[i] for i in range(len(new_problem)))