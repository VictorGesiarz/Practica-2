import sys
import os
current_file_path = os.path.abspath(__file__)
code_directory = os.path.abspath(os.path.join(current_file_path, '..', '..'))
sys.path.append(code_directory)

from Python.Case import Case
from Python.Book import Book
from Python.User import User, UserInteraction
from Python.Clusters import Clusters
from Python.Constants import *
from typing import List
import numpy as np
import random 


class CBR:
    
    def __init__(self, cluster: Clusters, books: List[Book], user: User, UI: UserInteraction=None, gamma = 0) -> None:
        self.cluster = cluster
        self.books = books
        self.gamma = gamma

        self.UI = UI
        self.MP = self.UI.MP


    def __len__(self):
        return len(self.cluster)


    def __repr__(self) -> str:
        print("\n\n")
        print("This CBR contains the next cases: \n")
        for i in range(len(self)):
            print(f'{self.cluster[i]}, with an evaluation of {self.evaluations[i]}')
        print("\n\n")
        return ""


    def run(self, new_problem: Case, ratings=None):
        cluster, retrieved_cases = self.__retrieve(new_problem)
        solutions, matrix_dist = self.__adapt(new_problem, retrieved_cases)

        if not ratings:
            self.__print_recommendations(solutions)

        evaluations = self.__evaluate(solutions, ratings)
        
        self.__learn(cluster, new_problem, matrix_dist, solutions, evaluations)

        if ratings:
            return retrieved_cases

        return self.cluster
    

    def __print_recommendations(self, solutions):
        section_title = self.MP.read("Titles", "Recommendations Title")
        print(self.MP.h1(section_title))
        print(self.MP.l(style="h2", width=H2_WIDTH))

        for case in solutions:
            title = case.title
            for book in self.books:
                if book.title == title:
                    break
            print(self.MP.p(f'{book}', width=H2_WIDTH, padding=1))

        print(self.MP.l(style="h2", width=H2_WIDTH))
        print()
        

    def __retrieve(self, new_problem):

        """In this function we comnpare the cases we have with the new one and select the most similar."""
        cluster = self.cluster.predict([new_problem])[0]

        retrieved_cases = self.cluster.tree[cluster]

        return cluster, retrieved_cases


    def __adapt(self, new_problem, retrieved_cases):

        """In this function we take the case with the best solution."""

        matrix_dist = []
        rating_list = []        
        
        for case in retrieved_cases:
            matrix_dist.append(self.similarity_function(new_problem, case))
                    
            rating_list.append(case.evaluation_mean)
        
        rating_list = np.nan_to_num(rating_list, nan=0)  # Replace NaN values with 0

        matrix_dist_array = np.array(matrix_dist)
        ratings_array = np.array(rating_list)
        
        dist_w = 1

        eps = 0.00005 # Evitar divisiones entre 0
        matrix_dist_array = matrix_dist_array + eps

        x = dist_w * (1 / matrix_dist_array) * min(matrix_dist_array)
        y = (1 - dist_w) * ratings_array / max(ratings_array)
        probabilities = x + y 

        solutions = []

        for _ in range(3):
            index = random.choices(range(len(retrieved_cases)), weights=probabilities, k=1)[0]
            solutions.append(retrieved_cases[index])
            probabilities[index] = 0

        return solutions, matrix_dist


    def __evaluate(self, solutions, evaluations=None):

        """In this function we will evaluate the given solution by asking the user how good it was."""
        
        if not evaluations:
            evaluations = []
            for solution in solutions:
                evaluation = self.UI.ask_range_question("Evaluate", additional_message=solution.title)
                evaluations.append(evaluation)
        return evaluations


    def __learn(self, cluster, new_problem, matrix_dist, solutions, evaluations=[]):
        
        """In this function we save the new case with the corresponding solution and evaluation."""

        min_dist = min(matrix_dist)

        max_index = -1
        if min_dist >= self.gamma:
            max_index = evaluations.index(max(evaluations))

            reference_case = solutions[max_index]
            case_to_add = new_problem.copy()
            case_to_add.evaluation_mean = (case_to_add.evaluation_mean * case_to_add.evaluation_count + evaluations[max_index]) / (case_to_add.evaluation_count + 1)
            case_to_add.evaluation_count += 1
            case_to_add.title = reference_case.title
            case_to_add.author = reference_case.author
            self.cluster.add_case(cluster, case_to_add)

            print(self.MP.e(f"CASE ADDED TO DATA BASE, with solution {case_to_add.title}"))

        for i, case in enumerate(solutions):
            if i != max_index:
                case.evaluation_mean = (case.evaluation_mean * case.evaluation_count + evaluations[i]) / (case.evaluation_count + 1)
                case.evaluation_count += 1


    def utility_mesure(self, case):
        ...


    def similarity_function(self, new_problem: Case, case: Case):
        
        """Function to calculate the similarity between two cases. This function performs the Manhattan distance."""

        new_problem_values, new_problem_genres = new_problem.get_variables()
        case_values, case_genres = case.get_variables()

        new_problem_list = new_problem_values + new_problem_genres
        case_list = case_values + case_genres
        weights = [1/4, 1/4] + [1 for _ in range(2, len(new_problem_list))]

        return sum(abs(new_problem_list[i] - case_list[i]) * weights[i] for i in range(len(new_problem_list)))
