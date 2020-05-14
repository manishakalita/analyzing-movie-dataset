# --------------
from csv import reader


def explore_data(dataset, start, end, rows_and_columns=False):
    """Explore the elements of a list.
    
    Print the elements of a list starting from the index 'start'(included) upto the index 'end'         (excluded).
    
    Keyword arguments:
    dataset -- list of which we want to see the elements
    start -- index of the first element we want to see, this is included
    end -- index of the stopping element, this is excluded 
    rows_and_columns -- this parameter is optional while calling the function. It takes binary          values, either True or False. If true, print the dimension of the list, else dont.
    """
    if rows_and_columns is True:
        print(dataset[start:end])
        print(len(dataset))
    else:
        print(dataset[start:end])   
    
        
     


def duplicate_and_unique_movies(dataset, index_):
    """Check the duplicate and unique entries.
    
    We have nested list. This function checks if the rows in the list is unique or duplicated based     on the element at index 'index_'.
    It prints the Number of duplicate entries, along with some examples of duplicated entry.
    
    Keyword arguments:
    dataset -- two dimensional list which we want to explore
    index_ -- column index at which the element in each row would be checked for duplicacy 
    
    """
    count = 0
    list_ = []
    for x in range(len(dataset)):
        for y in range(len(dataset)):
            if x == y:
                continue
            else:
                if dataset[x][index_] == dataset[y][index_]:
                    list_.append(dataset[x])
                    list_.append(dataset[y])
                    count = count + 1
    print(int(count/2))
    return (list_)
    


def movies_lang(dataset, index_, lang_):
    """Extract the movies of a particular language.
    
    Of all the movies available in all languages, this function extracts all the movies in a            particular laguage.
    Once you ahve extracted the movies, call the explore_data() to print first few rows.

    Keyword arguments:
    dataset -- list containing the details of the movie
    index_ -- index which is to be compared for langauges
    lang_ -- desired language for which we want to filter out the movies
    
    Returns:
    movies_ -- list with details of the movies in selected language
    
    """
    movies=[]
    for r in dataset:
        if r[index_]==lang_:
            movies.append(r)
    return movies
        
    



def rate_bucket(dataset, rate_low, rate_high):
    """Extract the movies within the specified ratings.
    
    This function extracts all the movies that has rating between rate_low and high_rate.
    Once you ahve extracted the movies, call the explore_data() to print first few rows.
    
    Keyword arguments:
    dataset -- list containing the details of the movie
    rate_low -- lower range of rating
    rate_high -- higher range of rating
    
    Returns:
    rated_movies -- list of the details of the movies with required ratings
    """
    rated_movies=[]
    for row in dataset:
        if (float(row[-4])<=rate_high) and (float(row[-4])>=rate_low):
            rated_movies.append(row)
    return rated_movies




# Read the data file and store it as a list 'movies'
opened_file = open(path, encoding="utf8")
read_file = reader(opened_file)
movies = list(read_file)



# The first row is header. Extract and store it in 'movies_header'.
movies_header=movies[0]

# Subset the movies dataset such that the header is removed from the list and store it back in movies

movies=movies[1:]


# Delete wrong data

# Explore the row #4553. You will see that as apart from the id, description, status and title, no other information is available.
# Hence drop this row.
movies.remove(movies[4553])


# Using explore_data() with appropriate parameters, view the details of the first 5 movies.
print(explore_data(movies,0,5))



# Our dataset might have more than one entry for a movie. Call duplicate_and_unique_movies() with index of the name to check the same.
print(duplicate_and_unique_movies(movies, -2))



# We saw that there are 3 movies for which the there are multiple entries. 
# Create a dictionary, 'reviews_max' that will have the name of the movie as key, and the maximum number of reviews as values.
reviews_max={}
for i in (range(len(movies))):
    reviews_max.update({movies[i][-2]:movies[i][-3]})

print(reviews_max)


# Create a list 'movies_clean', which will filter out the duplicate movies and contain the rows with maximum number of reviews for duplicate movies, as stored in 'review_max'. 

temp = duplicate_and_unique_movies(movies,-2)
movies_clean =[]
for row in temp:
        movies_clean.append([row[-2],row[-3]])
print(movies_clean)



# Calling movies_lang(), extract all the english movies and store it in movies_en.
movies_en=movies_lang(movies,3,'en')
print(movies_en)



# Call the rate_bucket function to see the movies with rating higher than 8.
high_rated_movies=rate_bucket(movies_en, 8, 10)


