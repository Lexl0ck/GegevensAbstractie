from movietheatre import *

test = Movietheatre()

print("original list of films:")
for film in test.listFilms():
    print(film)

print("\nSort by name and print again:")
for film in test.film_table.sortObjectList(test.listFilms(), Film.getTitle):
    print(film)

print("\nSort by ID and print again:")
for film in test.film_table.sortObjectList(test.listFilms(), Film.getID):
    print(film)

print("\nSort by rating and print again:")
for film in test.film_table.sortObjectList(test.listFilms(), Film.getRating):
    print(film)
