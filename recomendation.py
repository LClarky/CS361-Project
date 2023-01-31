import sys
import random

def read_book_data(filename):
    books = []
    with open(filename, "r") as f:
        for line in f:
            book, author, genres = line.strip().split(",")
            genres = genres.split("|")
            for genre in genres:
                books.append((book, author, genre))
    return books

def filter_books_by_genre(books, genres):
    return [book for book in books if book[2].lower() in genres]

def get_unique_genres(books):
    genres = set()
    for book in books:
        genres.add(book[2])
    return list(genres)

def list_genres(books_data):
    all_genres = set()
    for book in books_data:
        for genre in book[1]:
            all_genres.add(genre)
    print("All available genres: ",  ", ".join(all_genres))

if __name__ == "__main__":
    print("\n\nWelcome to my Book Recomendation Generator, You can enter as many genres as you like and when you are ready you can ")
    print(" Generarte a recomednation that suits your taste, dont worry if you add a genre you didnt want you can remove it.")
    print(" Note that if you enter a genre mispelled, remove it as it will mess up the recomendation, you can also list all the genres you can sort for.\n\n")
    books = read_book_data("books2.txt")
    selected_genres = set()
    while True:
        while True:
            print("1. Enter a genre")
            print("2. Remove a genre")
            print("3. List all genres")
            print("4. Sort books")
            print("5. Exit\n")
            print("Selected genres: ", [genre.capitalize() for genre in selected_genres])
            choice = input("Enter your choice: ")
            if choice == "1":
                genre = input("Enter genre: ").lower()
                selected_genres.add(genre)
            elif choice == "2":
                genre = input("Enter genre to remove: ").lower()
                if genre in selected_genres:
                    selected_genres.remove(genre)
                else:
                    print("Genre not found.")
            elif choice == "3":
                genres = get_unique_genres(books)
                print("Available genres:")
                for genre in genres:
                    print(genre)
            elif choice == "4":
                if len(selected_genres) == 0:
                    selected_book = random.choice(books)
                    print("A shot in the dark I like it here is", selected_book[0], "by" , selected_book[1])
                else:
                    filtered_books = filter_books_by_genre(books, selected_genres)
                    if filtered_books:
                        selected_book = random.choice(filtered_books)
                        print("\nI Think" , selected_book[0],"by" , selected_book[1], "will suit your taste" )
                        run_again = input("\ndo you want to run the program again(yes/no)")
                        if run_again == 'yes':
                            continue
                        else:
                            sys.exit()
                    else:
                        print("No books found.")
            elif choice == "5":
                sys.exit()
            else:
                print("Invalid choice.")
            break
