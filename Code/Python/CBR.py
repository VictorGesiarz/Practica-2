import sys
import os
current_file_path = os.path.abspath(__file__)
code_directory = os.path.abspath(os.path.join(current_file_path, '..', '..'))
sys.path.append(code_directory)


from kmodes.kmodes import KModes
from Python.Case import Case
from Python.Book import Book
from Python.User import User
from Python.Clusters import Clusters
from typing import List
import numpy as np
import random 


class CBR:
    
    def __init__(self, cluster: Clusters, books: List[Book], user: User, MP=None, gamma = 0) -> None:
        self.cluster = cluster
        self.books = books
        self.gamma = gamma



    def __len__(self):
        return len(self.cluster)


    def __repr__(self) -> str:
        print("\n\n")
        print("This CBR contains the next cases: \n")
        for i in range(len(self)):
            print(f'{self.cluster[i]}, with an evaluation of {self.evaluations[i]}')
        print("\n\n")
        return ""

    # the ratings is used to test the system
    def run(self, new_problem: Case, ratings=None):
        cluster, retrieved_cases = self.__retrieve(new_problem)
        solutions, matrix_dist = self.__adapt(new_problem, retrieved_cases)

        if not ratings:
            for case in solutions:
                print(f"We recommend you to read: {case}")

        evaluations = self.__evaluate(ratings)
        
        self.__learn(cluster, new_problem, matrix_dist, solutions, evaluations)

        if ratings:
            return retrieved_cases

        return self.cluster
    

    def __retrieve(self, new_problem):

        """In this function we comnpare the cases we have with the new one and select the most similar."""
        cluster = self.cluster.predict([new_problem])[0]

        retrieved_cases = self.cluster.tree[cluster]

        # similarities = []

        # for case in cases:
        #     similarity = self.similarity_function(new_problem, case)
        #     similarities.append(similarity)
        
        # x = 3
        # sorted_indices = sorted(range(len(similarities)), key=lambda k: similarities[k])[:x]

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
        # print("-----------------------------------------------------------------------")
        # print(ratings_array)
        

        dist_w = 0.8

        eps = 0.00005 # Evitar divisiones entre 0
        matrix_dist_array = matrix_dist_array + eps

        x =  dist_w * (1 / matrix_dist_array) * min(matrix_dist_array)
        y = (1 - dist_w)* ratings_array / max(ratings_array)

        probabilities =  x + y 

        solutions = random.choices(retrieved_cases, weights=probabilities, k=3)

        return solutions, matrix_dist

    def __evaluate(self, evaluation=None):

        """In this function we will evaluate the given solution by asking the user how good it was."""
        
        if not evaluation:
            evaluation = input("Rate from 1 to 5 each of the recommendations: ").split()
            evaluation = [int(i) for i in evaluation]
        return evaluation


    def __learn(self, cluster, new_problem, matrix_dist, solutions, evaluations=[]):
        
        """In this function we save the new case with the corresponding solution and evaluation."""

        min_dist = min(matrix_dist)

        if min_dist > self.gamma:

            for i, case in enumerate(solutions):
                problem = new_problem.copy()
                problem.evaluation_mean = (problem.evaluation_mean * problem.evaluation_count + evaluations[i]) / (problem.evaluation_count + 1)
                problem.evaluation_count += 1

                # case = self.cluster.get_case(cluster, solution)
                problem.title = case.title
                problem.author = case.author
                self.cluster.add_case(cluster, problem)


    def similarity_function(self, new_problem: Case, case: Case):
        
        """Function to calculate the similarity between two cases. This function performs the Manhattan distance."""

        new_problem_values, new_problem_genres = new_problem.get_variables()
        case_values, case_genres = case.get_variables()
                
        # weights = [1/4, 1/4] + [1 for _ in range(2, len(new_problem_values))]

        # manhattan_similarity = sum(abs(new_problem_values[i] - case_values[i]) * weights[i] for i in range(len(new_problem_values)))

        # genres_similarity = sum(new_problem_genres) - np.dot(np.array(new_problem_genres), np.array(case_genres))

        new_problem_list = new_problem_values + new_problem_genres
        case_list = case_values + case_genres
        weights = [1/4, 1/4] + [1 for _ in range(2, len(new_problem_list))]

        return sum(abs(new_problem_list[i] - case_list[i]) * weights[i] for i in range(len(new_problem_list)))

        # return manhattan_similarity + genres_similarity