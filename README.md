# DEMO VIDEO: https://www.youtube.com/watch?v=5jRrkIm-cmQ

## Description
Our database will consist of a table with movies, a table of Genres, a table of Cast Members, a table of Languages, and possibly other tables, and all of these entities will be linked with one another in several relationships. MovieRec will allow users to get information about a movie or list of movies by searching for it by name, genre, language, keywords, which will be a term-frequency, inverse-document frequency-based implementation), cast members, and possibly other attributes.

The results will be a list of movies, and each movie entry will contain information about genre, keywords, cast members, and language. The user will be able to select available movies into a watchlist, and from the movies in the watchlist, the user will be recommended 5 other movies to watch based on a similarity score.

## Usefulness:
The program is useful in the sense that it provides a way for users to find other movies that complement ones that the user is interested in. In today’s streaming culture, a very common feeling that many people experience after watching an amazing movie or TV show is a sense of “emptiness” which stems from the fact that a very satisfying source of entertainment has just ended. Our program is designed to reduce this feeling of “emptiness” and to bridge the gap between the first fantastic movie and the next. Also, it will be convenient for users to have a centralized interface for finding information about movies, such as language, cast members, imdB and tmDB rating, and the application will have a convenient searching feature that allows users to search for movies by name, genre, language and other attributes.

TasteDive, an already existing website, groups movies into collections based on genre and topic, but it does not provide recommendations to users based on a list of movies that they themselves selected. Our recommendation model differs in the way it suggests the next movie. It allows users to select a list of movies, and then based on the movies in the list, will provide recommendations. As the number of movies in the list increases, the results will be the most similar to all of the movies in the wishlist.

Imdb is a popular source of information and ratings about movies, our service is differentiated from it because we offer an easy recommendation service, as well as the fact that we will display both imdb and tmbd (a competitor of imdb)'s rankings, providing a convenient interface for getting both rankings. 

## Dataset:
The data will come from “The Movies Dataset” from Kaggle (https://www.kaggle.com/rounakbanik/the-movies-dataset?select=keywords.csv) which provides a multitude of attributes for movies pulled from the IMDB movie database, such as language, imdB score, tmdb score, keywords, genre, cast and crew members, among other attributes. This data is split up into multiple associated tables. Since the dataset is in the form of multiple tables across multiple csv files, we will use pandas to load the csv files into a pandas database, and then implement a parsing algorithm to extract data and will create Classes to store the data (such as Movie class, CastMember class, Crew class, etc.) After retrieving the data, we will populate the tables in our SQL database with relevant SQL queries.

## Web app functionality: 
Recommendation Service: user can input/add movies into a 'watchlist' for the recommendation algorithm to perform on. When the list of movies is submitted for the program to generate recommendations, the program will take into account the attributes of all the movies, perform vectorization of the movie descriptions, and will use a similarity/distance metric in order to generate suggestions that best match the listed movies. 

User can add, update this 'watchlist', delete movies from this watch list, and so users have CRUD capabilities over this watchlist. 

Search: Search Bar that allows for the user to search movies to add to wishlist and view information about. Search (Query) by Title, Genre, Language, Associated Keywords (a Term-frequency inverse document frequency (TFIDF-based searching mechanism) and Filter/Rank (Order By) Ratings.

Functionality: 
What data is stored?

Some data we plan on storing include movie names, cast & crew members, ratings, genres, languages movies are in, keywords, and descriptions for each movie.

Potential Schema/Entities:

Movie: 

-ID

-Title

-Keywords

-Description

Cast Members (Actors):

-ID

-Name

Crew:

-ID

-Name

-Role/Occupation

Genre:

-Genre ID

-Genre Name

Ratings:

-Movie ID

-imdb rating

-tmdb rating

-Language:

-id

-Language Name

