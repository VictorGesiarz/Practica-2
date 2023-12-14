from Case import Case
from Book import Book
from User import User
from typing import List
import numpy as np


class CBR:
    
    def __init__(self, cases: List[Case], books: List[Book], user: User, MP) -> None:
        self.cases = cases
        self.books = books

        self.length = len(cases)


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
        
        evaluation = input("Rate from 1 to 5 each of the recommendations: ").split()
        evaluation = [int(i) for i in evaluation]
        return evaluation


    def __learn(self, new_problem, solutions, evaluations=[]):
        
        """In this function we save the new case with the corresponding solution and evaluation."""

        for i, solution in enumerate(solutions):
            problem = new_problem.copy()
            problem.evaluation_mean = (problem.evaluation_mean * problem.evaluation_count + evaluations[i]) / (problem.evaluation_count + 1)
            problem.evaluation_count += 1

            problem.title = self.cases[solution].title
            problem.author = self.cases[solution].author
            self.cases.append(problem)

            self.length += 1


    def similarity_function(self, new_problem: Case, case: Case):
        
        """Function to calculate the similarity between two cases. This function performs the Manhattan distance."""

        new_problem_values, new_problem_genres = new_problem.get_variables()
        case_values, case_genres = case.get_variables()
                
        weights = [1/4, 1/4] + [1 for _ in range(2, len(new_problem_values))]

        manhattan_similarity = sum(abs(new_problem_values[i] - case_values[i]) * weights[i] for i in range(len(new_problem_values)))

        genres_similarity = sum(new_problem_genres) - np.dot(np.array(new_problem_genres), np.array(case_genres))

        new_problem_list = new_problem_values + new_problem_genres
        case_list = case_values + case_genres
        weights = [1/4, 1/4] + [1 for _ in range(2, len(new_problem_list))]

        return sum(abs(new_problem_list[i] - case_list[i]) * weights[i] for i in range(len(new_problem_list)))

        # return manhattan_similarity + genres_similarity