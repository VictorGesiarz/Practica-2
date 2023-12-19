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
    
    def __init__(self, cluster: Clusters, books: List[Book], user: User, UI: UserInteraction=None, gamma = 3, forget_rate = 25, forget_minimum = 2.5, rating_weight = 0.8) -> None:
        self.cluster = cluster
        self.books = books
        self.user = user

        self.gamma = gamma
        
        self.forget_rate = forget_rate
        self.forget_minimum = forget_minimum
        self.rating_weight = rating_weight

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
    

    def __find_user_books(self):
        user_books = []
        user_books_title = []
        for book in self.books:
            if book.saga == 0:
                continue

            if book.title not in self.user.books_read:
                continue

            if book.followed_by and book.followed_by not in self.user.books_read:
                user_books_title.append(book.title)
            
            if book.preceeded_by and book.preceeded_by not in self.user.books_read:
                user_books_title.append(book.title)

        for case in self.cluster.cases:          
            if case.title  in user_books_title:
                user_books.append(case)

        return user_books


    def __retrieve(self, new_problem):

        """In this function we comnpare the cases we have with the new one and select the most similar."""   
        cluster = self.cluster.predict([new_problem])[0]

        retrieved_cases = self.cluster.tree[cluster]

        if new_problem.saga == 1:
            user_books = self.__find_user_books()
            retrieved_cases = list(set(user_books + retrieved_cases))

        return cluster, retrieved_cases


    def __adapt(self, new_problem, retrieved_cases):

        """In this function we take the case with the best solution."""

        matrix_dist = []
        rating_list = []        

        num_var = len(GENRES) + 5
        
        weights = [1/4, 1/4] + [1 for _ in range(2, num_var)]
        
        p1 = 5
        p2 = 3
        p3 = 2            

        if new_problem.genres[GENRES.index("fantasy")]:
            weights[GENRES.index("sorcery")] = p1
            weights[GENRES.index("magic")] = p1
            weights[GENRES.index("sword")] = p2
            weights[GENRES.index("high")] = p2
            weights[GENRES.index("realism")] = 1/p1
            weights[GENRES.index("science")] = 1/p1
            weights[GENRES.index("speculative")] = 1/p2
        
        if new_problem.genres[GENRES.index("science")]:
            weights[GENRES.index("time travel")] = p1
            weights[GENRES.index("techno")] = p1

        if new_problem.genres[GENRES.index("romance")]:
            weights[GENRES.index("erotic")] = p2

        if new_problem.genres[GENRES.index("horror")]:
            weights[GENRES.index("vampire")] = p2

        if new_problem.genres[GENRES.index("thriller")]:
            weights[GENRES.index("detective")] = p2
            weights[GENRES.index("crime")] = p2
            weights[GENRES.index("mystery")] = p2

        if new_problem.genres[GENRES.index("historical")]:
            weights[GENRES.index("war")] = p1
            weights[GENRES.index("military")] = p1
            weights[GENRES.index("cyberpunk")] = 1/p1

        if new_problem.genres[GENRES.index("childrens")]:
            weights[GENRES.index("picture book")] = p1

        if new_problem.genres[GENRES.index("drama")]:
            weights[GENRES.index("tragedy")] = p1

        if new_problem.genres[GENRES.index("comedy")]:
            weights[GENRES.index("satire")] = p1
            weights[GENRES.index("humour")] = p1
            weights[GENRES.index("black")] = p3

        if new_problem.genres[GENRES.index("mystery")]:
            weights[GENRES.index("detective")] = p1
            weights[GENRES.index("crime")] = p1

        if new_problem.genres[GENRES.index("utopian")]:
            weights[GENRES.index("dystopia")] = 1/p1

        if new_problem.genres[GENRES.index("dystopia")]:
            weights[GENRES.index("utopian")] = 1/p1

        if 0 < new_problem.user_age < 10 or new_problem.genres[GENRES.index("childrens")]:
            weights[GENRES.index("erotic")] = 1000
            new_problem.genres[GENRES.index("childrens")] = 5
    

        for case in retrieved_cases:
            if 0 < new_problem.user_age < 14:
                if case.pages != 0:
                    continue

            matrix_dist.append(self.similarity_function(new_problem, case, weights))
                    
            rating_list.append(case.evaluation_mean)
        
        rating_list = np.nan_to_num(rating_list, nan=0)  # Replace NaN values with 0

        matrix_dist_array = np.array(matrix_dist)
        ratings_array = np.array(rating_list)
        
        dist_w = self.rating_weight

        eps = 0.00005 # Evitar divisiones entre 0
        matrix_dist_array = matrix_dist_array + eps

        x = dist_w * (1 / matrix_dist_array) * min(matrix_dist_array)
        y = (1 - dist_w) * ratings_array / max(ratings_array)
        probabilities = x + y 

        solutions = []
        solutions_titles = []

        i = 0

        while i < 3:
            index = random.choices(range(len(retrieved_cases)), weights=probabilities, k=1)[0]
            title = retrieved_cases[index].title
            if title not in solutions_titles:
                i += 1
                solutions_titles.append(title)
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

        if min_dist >= self.gamma:
            max_index = evaluations.index(max(evaluations))

            reference_case = solutions[max_index]
            case_to_add = new_problem.copy()
            case_to_add.evaluation_mean = (case_to_add.evaluation_mean * case_to_add.evaluation_count + evaluations[max_index]) / (case_to_add.evaluation_count + 1)
            case_to_add.evaluation_count += 1
            case_to_add.title = reference_case.title
            case_to_add.author = reference_case.author
            self.cluster.add_case(cluster, case_to_add)

            # print(self.MP.e(f"CASE ADDED TO DATA BASE, with solution {case_to_add.title}"))

        else:
            for i, case in enumerate(solutions):
                if i != max_index:
                    case.evaluation_mean = (case.evaluation_mean * case.evaluation_count + evaluations[i]) / (case.evaluation_count + 1)
                    case.evaluation_count += 1


    def __is_useless(self, case):
        count = case.evaluation_count
        mean = case.evaluation_mean

        if count > self.forget_rate and mean < self.forget_minimum:
            return True
        return False


    def similarity_function(self, new_problem: Case, case: Case, weights: List[float]=None):
        
        """Function to calculate the similarity between two cases. This function performs the Manhattan distance."""

        new_problem_values, new_problem_genres = new_problem.get_variables()
        case_values, case_genres = case.get_variables()

        new_problem_list = new_problem_values + new_problem_genres
        case_list = case_values + case_genres
        if not weights:
            weights = [1/4, 1/4] + [1 for _ in range(2, len(new_problem_list))]

        return sum(abs(new_problem_list[i] - case_list[i]) * weights[i] for i in range(len(new_problem_list)))
