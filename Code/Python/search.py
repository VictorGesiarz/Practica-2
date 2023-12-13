import pandas as pd
import numpy as np

def search(text, database, column):
    database = pd.read_csv(database)
    return database[database[column].str.contains(text, case=False)]

def search_manhattan(text, database, column):
    """Searches for a string in a column of a database and returns the results with the minimum Manhattan distance"""
    
    database = pd.read_csv(database)
    database[column] = database[column].astype(str)

def levenshtein_distance(word1, word2):
    m = len(word1)
    n = len(word2)
    dp = np.zeros((m+1, n+1))

    for i in range(m+1):
        dp[i][0] = i

    for j in range(n+1):
        dp[0][j] = j

    for i in range(1, m+1):
        for j in range(1, n+1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])

    return dp[m][n]

# word1 = "hello"
# word2 = "hola"
# distance = levenshtein_distance(word1, word2)
# print(f"The Levenshtein distance between '{word1}' and '{word2}' is {distance}")
    
    
def search_levenshtein(text, database, column):
    """Searches for a string in a column of a database and returns the results with the minimum Levenshtein distance"""
    
    database = pd.read_csv(database)
    database[column] = database[column].astype(str)
    
    distances = []
    for i in range(len(database)):
        distances.append(levenshtein_distance(text, database[column][i]))
    
    database['levenshtein_distance'] = distances
    
    return database[database['levenshtein_distance'] == min(distances)]



from transformers import DistilBertTokenizer, DistilBertModel
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

def find_book_by_name(user_input, book_dataset):
    # Load pre-trained BERT model and tokenizer
    model_name = "distilbert-base-nli-stsb-mean-tokens"
    tokenizer = DistilBertTokenizer.from_pretrained(model_name)
    model = SentenceTransformer(model_name)

    # Encode user input
    input_embedding = model.encode(user_input, convert_to_tensor=True)

    # Compute cosine similarity between user input and each book title
    similarities = []
    for book_title in book_dataset:
        title_embedding = model.encode(book_title, convert_to_tensor=True)
        similarity = cosine_similarity(input_embedding, title_embedding)
        similarities.append(similarity.item())

    # Find the index of the book with the highest similarity
    max_similarity_index = similarities.index(max(similarities))

    # Return the book with the highest similarity
    return book_dataset[max_similarity_index]

# Example usage
book_dataset = ["The Catcher in the Rye", "To Kill a Mockingbird", "1984", "Pride and Prejudice", "The Great Gatsby"]
user_input = input("Enter a book name (you can't write exactly): ")
result = find_book_by_name(user_input, book_dataset)
print(f"The closest match to '{user_input}' is: {result}")
