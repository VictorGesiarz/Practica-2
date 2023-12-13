from Case import Case
from User import User
from typing import List

class CBR:
    
    def __init__(self, cases: List[Case], user: User) -> None:
        self.cases = cases
        self.evaluations = [[] for _ in cases]

        self.length = len(cases)
        
        self.similarity_function = self.Manhattan


    def __repr__(self) -> str:
        print("\n\n")
        print("This CBR contains the next cases: \n")
        for i in range(self.length):
            print(f'{self.cases[i]}, with an evaluation of {self.evaluations[i]}')
        print("\n\n")
        return ""
    

    def run(self, new_problem: Case):

        retrieved_cases = self.__retrieve(new_problem)
        solutions = self.__adapt(retrieved_cases)

        for i in solutions:
            print(f"We recommend you to read: {self.cases[i]}")

        evaluations = self.__evaluate()
        self.__learn(new_problem, solutions, evaluations)
    

    def __retrieve(self, new_problem):

        """In this function we comnpare the cases we have with the new one and select the most similar."""

        similarities = []
        for case in self.cases:
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

        return retrieved_cases


    def __evaluate(self):

        """In this function we will evaluate the given solution by asking the user how good it was."""
        
        evaluacion = int(input("Rate from 1 to 5 each of the recommendations: ")).split()
        return evaluacion


    def __learn(self, new_problem, solutions, evaluations=[]):
        
        """In this function we save the new case with the corresponding solution and evaluation."""

        for i in solutions:
            self.cases.append(new_problem)
            self.evaluations.append([evaluations[i]])   # GUARDAR LA MEDIA Y EL NUMERO DE EVALUACIONES PARA LUEGO PODER ACTUALIZARLO SI HACEMOS MAS EVALUACIONES

            self.length += 1


    def Manhattan(self, new_problem: Case, case: Case):
        
        """Function to calculate the similarity between two cases. This function performs the Manhattan distance."""

        weights = [1 for _ in range(len(new_problem))]

        new_problem_values = new_problem.get_list()
        case_values = case.get_list()
        
        return sum(abs(new_problem_values[i] - case_values[i]) * weights[i] for i in range(len(new_problem)))