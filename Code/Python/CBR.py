
class CBR():
    
    def __init__(self, cases, similarity_function) -> None:
        self.solutions = [case[0] for case in cases]
        self.problems = [case[1:] for case in cases]
        self.evaluations = [None for _ in cases]
        
        self.similarity_function = similarity_function


    def run(self, new_case):
        retrieved_case = self.__retrieve(new_case)
        solution = self.__adapt(retrieved_case)
        evaluation = self.__evaluate()
        self.__learn(new_case, solution, evaluation)
    

    def __retrieve(self, new_case):

        """In this function we comnpare the cases we have with the new one and select the most similar."""

        similarities = []
        for case in self.problems:
            similarity = function(new_case, case)
            similarities.append(similarity)

        index = similarities.index(min(similarities))

        return self.problems[index]


    def __adapt(self, retrieved_case):

        """In this function we take the case with the best solution."""

        ...


    def __evaluate(self):

        """In this function we will evaluate the given solution by asking the user how good it was."""
        
        evaluacion = input("In a scale from 1 to 5, how good was the recommendation based on your what you were looking for? ")
        return evaluacion


    def __learn(self, new_case, solution, evaluation=None):
        
        """In this function we save the new case with the corresponding solution and evaluation."""

        ...

