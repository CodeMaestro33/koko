def collect_user_data():
    print("Welcome! Let's collect some information about you.")
    
    name = input("What is your name? ")
    age = input("What is your age? ")
    fav_book = input("What is your favorite book? ")
    fav_song = input("What is your favorite song? ")
    fav_movie = input("What is your favorite movie? ")
    
    user_data = {
        "Name": name,
        "Age": age,
        "Favorite Book": fav_book,
        "Favorite Song": fav_song,
        "Favorite Movie": fav_movie
    }
    
    return user_data

# Example usage
user_info = collect_user_data()
print("\nThank you for sharing your information!")
print("User Data:")
for key, value in user_info.items():
    print(f"{key}: {value}")

print ("hello work")
