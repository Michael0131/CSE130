import json

try:
    with open("testingArea\\movie_authenitcator\\movies.json", 'r') as file:
        data = json.load(file)
except FileNotFoundError:
    print("Unable to locate file.")
    exit()

movies = data.get('movies', [])
passwords = data.get('passwords', [])

movie_input = input("Enter movie title: ")
password_input =input("Enter your password: ")

if movie_input in movies:
    index = movies.index(movie_input)
    if passwords[index] == password_input:
        print("Access granted! You love this movie.")
    else:
        print("Incorrect password for this movie.")
else:
    print("Movie not found.")
     

