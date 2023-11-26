import pandas as pd
import ast


# - - - - - - - - - - - - - - - - - - - READ DATA - - - - - - - - - - - - - - - - - - - 

print("- - - - - - - - - - LOADING DATA - - - - - - - - - - \n\n")

books = pd.read_csv('./Python/Data/Books_preprocessed_generated_data.csv')
books['genres'] = books['genres'].apply(ast.literal_eval)
books['subgenres'] = books['subgenres'].apply(ast.literal_eval)
books['ages'] = books['ages'].apply(ast.literal_eval)

genres = set()
subgenres = set()
for i, row in books.iterrows():
    genre = row['genres']
    subgenre = row['subgenres']
    for j in genre:
        genres.add(j.lower())
    for k in subgenre:
        subgenres.add(k.lower())


authors = pd.read_csv('./Python/Data/Authors.csv')
authors['books'] = authors['books'].apply(ast.literal_eval)
authors['genres'] = authors['genres'].apply(ast.literal_eval)
authors['subgenres'] = authors['subgenres'].apply(ast.literal_eval)


sagas = pd.read_csv('./Python/Data/Sagas.csv')
sagas["books"] = sagas["books"].apply(ast.literal_eval)
        
print("- - - - - - - - - - DATA LOADED - - - - - - - - - - \n\n")


with open('./Clips/Instances.clp', 'w') as f:

    f.write("(definstances instances\n")



    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
    # - - - - - - - - - - - - - - - - - - - WRITE GENRES - - - - - - - - - - - - - - - - - - - 
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

    print("- - - - - - - - - - WRITING GENRES - - - - - - - - - - \n\n")
    

    f.write("; - - - - - - - - - - - - - - - - - - - GENRES - - - - - - - - - - - - - - - - - - - \n\n")

    f.write("\t; List of genres\n\n")
    for i in genres:
        f.write(f'\t({"-".join(i.split())} of Genre)\n')

    f.write('\n')

    f.write("\t; List of subgenres\n\n")  
    for j in subgenres:
        f.write(f'\t({"-".join(j.split())} of Subgenre)\n')

    f.write("\n")
    


    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
    # - - - - - - - - - - - - - - - - - - - WRITE SAGAS - - - - - - - - - - - - - - - - - - - 
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

    print("- - - - - - - - - - WRITING SAGAS - - - - - - - - - - \n\n")


    f.write("; - - - - - - - - - - - - - - - - - - - SAGAS - - - - - - - - - - - - - - - - - - - \n\n")

    for i, row in sagas.iterrows():
        string = '-'.join(row["saga"].lower().split())
        f.write(f'\t({string} of Saga\n')
        f.write(f'\t\t(name "{row["saga"]}")\n')
        string = ' '.join('-'.join(book.lower().split()) for book in row["books"])
        f.write(f'\t\t(books [{string}])\n')
        f.write(f'\t\t(number-of-books {row["number"]})\n')
        f.write(f'\t\t(is-finished "{row["finished"]}")\n')
        f.write('\t)\n\n')



    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
    # - - - - - - - - - - - - - - - - - - - WRITE AUTHORS - - - - - - - - - - - - - - - - - - - 
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

    print("- - - - - - - - - - WRITING AUTHORS - - - - - - - - - - \n\n")


    f.write("; - - - - - - - - - - - - - - - - - - - AUTHORS - - - - - - - - - - - - - - - - - - - \n\n")
    
    for i, row in authors.iterrows():
        string = '-'.join(row["author"].lower().split())
        f.write(f'\t({string} of Authorfffdf\n')
        f.write(f'\t\t(name "{row["saga"]}")\n')
        string = ' '.join('-'.join(book.lower().split()) for book in row["books"])
        f.write(f'\t\t(books [{string}])\n')
        f.write(f'\t\t(number-of-books {row["number"]})\n')
        f.write(f'\t\t(is-finished "{row["finished"]}")\n')
        f.write('\t)\n\n')
    


    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
    # - - - - - - - - - - - - - - - - - - - WRITE BOOKS - - - - - - - - - - - - - - - - - - - 
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
    
    print("- - - - - - - - - - WRITING BOOKS - - - - - - - - - - \n\n")
    
    
    f.write("; - - - - - - - - - - - - - - - - - - - BOOKS - - - - - - - - - - - - - - - - - - - \n\n")
    
    for i, row in books.iterrows():

        if i == 10: break
        
        string = '-'.join(row["title"].split())
        f.write(f'\t([{string}] of Book\n')
        f.write(f'\t\t(title "{row["title"]}")\n')
        
        text = str(row['genres']).lower().replace(" ", "-").replace(",-", " ").replace("\'", "")
        f.write(f'\t\t(genres {text})\n')
        
        text = str(row['genres']).lower().replace(" ", "-").replace(",-", " ").replace("\'", "\"")

        f.write(f'\t\t(genres-str {text})\n')
        
        string = " ".join(f'{"-".join(subgenre.lower().split())}' for subgenre in row["subgenres"])
        f.write(f'\t\t(subgenres [{string}])\n')

        string = " ".join(f'"{"-".join(subgenre.lower().split())}"' for subgenre in row["subgenres"])
        f.write(f'\t\t(subgenres-str [{string}])\n')


        string = '-'.join(row["author"].split())
        f.write(f'\t\t(author {string})\n')
        string = ' '.join(f'"{age}"' for age in row['ages'])
        f.write(f"\t\t(oriented-age [{string}])\n")
        f.write(f'\t\t(period {row["period"]})\n')
        f.write(f'\t\t(film {row["film"]})\n')
        f.write(f'\t\t(narrator {row["narrator"]})\n')
        f.write(f'\t\t(saga {"no" if row["saga"] == "No" else "yes"})\n')
        f.write(f'\t\t(book-length {row["pages"]})\n')
        f.write(f'\t\t(published-date {int(row["publishDate"])})\n')
        f.write(f'\t\t(punctuation {row["rating"]})\n')
        f.write(f'\t\t(num-ratings {row["numRatings"]})\n')
        f.write(f'\t\t(classic {row["classics"]})\n')
        f.write(f'\t\t(happiness {row["hapiness"]})\n')
        f.write(f'\t\t(drama {row["drama"]})\n')
        f.write(f'\t\t(comedy {row["comedy"]})\n')
        f.write(f'\t\t(predictable {row["predictable"]})\n')
        f.write(f'\t\t(violence {row["violence"]})\n')
        f.write(f'\t\t(conventional {row["conventional"]})\n')
        f.write(f'\t)\n\n')

    f.write(")")

