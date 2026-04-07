'''
  PSEUDO CODE:

  START PROGRAM
    initialize library as empty list
    print welcome message
    LOOP forever:
      show menu to user
      get user choice
      if choice is 1 → call add_book()
      if choice is 2 → call save_library()
      if choice is 3 → call load_library()
      if choice is 4 → call visualize_library()
      if choice is 5 → print goodbye and EXIT loop
      else → print invalid choice
  END PROGRAM

  FUNCTION add_book():
    ask user to enter book title → save in title
    ask user to enter book author → save in author
    ask user to enter book category → save in category
    create dictionary with title, author, category
    append dictionary to library list
    print "Book added successfully!"
  END FUNCTION

  FUNCTION save_library():
    TRY:
      open file "library.json" in write mode
      write library list to file in JSON format
      print "Library saved successfully!"
    EXCEPT any error:
      print the error message
  END FUNCTION

  FUNCTION load_library():
    TRY:
      open file "library.json" in read mode
      read JSON data from file
      save data back into library list
      print "Library loaded successfully!"
    EXCEPT file not found:
      print "No saved library found. Starting fresh."
    EXCEPT JSON decode error:
      print "File is corrupted or invalid."
    EXCEPT any other error:
      print the error message
  END FUNCTION

  FUNCTION visualize_library():
    create empty dictionary called categories
    LOOP through every book in library:
      get category of current book
      if category already in categories:
        add 1 to its count
      else:
        set its count to 1
    print "--- Library by Category ---"
    LOOP through categories:
      print category name + (*) multiplied by its count
  END FUNCTION

  FUNCTION main():
    initialize library as empty list
    print "Welcome to Your Personal Library Manager!"
    LOOP forever:
      print menu:
        1. Add a book
        2. Save library to file
        3. Load library from file
        4. Visualize library by category
        5. Quit
      get user choice
      if choice == 1 → call add_book()
      if choice == 2 → call save_library()
      if choice == 3 → call load_library()
      if choice == 4 → call visualize_library()
      if choice == 5 → print "Goodbye!" and EXIT loop
      else → print "Invalid choice. Please try again."
  END FUNCTION

  call main()
'''

# Import the json library to handle reading and writing JSON files
import json

# Global list to store all books - accessible by all functions
library = []


# This function asks the user for book details and adds it to the library
def add_book():
    
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    category = input("Enter book category: ")

    # Create a dictionary for the book with three keys: title, author, category
    book = {'title': title, 'author': author, 'category': category}

    # Add the book dictionary to the library list
    library.append(book)

    print("---> Book added successfully! <---")


# This function saves the library list to a JSON file
def save_library():
  
  try:
    
    # Open the file in write mode and dump the library list as JSON
    with open("library.json", "w") as file:
      json.dump(library, file)

    print("---> Library saved successfully! <---")

  # Catch any error that happens during the file operation
  except Exception as e:
    
    print(e)


# This function loads the library list from a JSON file
def load_library():
  
  # global keyword allows us to modify the library variable outside this function
  global library

  try:
    
    # Open the file in read mode and load the JSON data back into library
    with open("library.json", "r") as file:
        
      data = json.load(file)
      library = data

    print("---> Library loaded successfully! <---")

  # Handle case where the file doesn't exist yet
  except FileNotFoundError:
    print("!!! No saved library found. Starting fresh. !!!")
    
  # Handle case where the file exists but its content is not valid JSON
  except json.JSONDecodeError:
    print("!!! File is corrupted or invalid. !!!")
    
  # Handle any other unexpected errors
  except Exception as e:
    print(e)


# This function displays a text-based histogram of books per category
def visualize_library():
  
  # Empty dictionary to count books in each category
  categories = {}

  # Loop through every book and count how many books are in each category
  for book in library:
    
    category = book['category']
    if category in categories:
      
      # If category already exists, add 1 to its count
      categories[category] += 1  
      
    else:
      # If category is new, set its count to 1
      categories[category] = 1

  print("========================================")
  print("--- Library by Category ---")
  print("========================================")

  # Print each category with asterisks representing the number of books
  for category, count in categories.items():
    print(f"{category}: {'*' * count}")


# This is the main function that runs the whole application
def main():
  
  print("========================================")
  print("Welcome to Your Personal Library Manager!")
  print("========================================")
  
  # Keep looping until the user chooses to quit
  while True:
    
    print("\nWhat would you like to do?")
    print("1. Add a book")
    print("2. Save library to file")
    print("3. Load library from file")
    print("4. Visualize library by category")
    print("5. Quit")

    choice = input("Enter choice: ")

    if choice == "1":
      add_book()

    elif choice == "2":
      save_library()

    elif choice == "3":
      load_library()

    elif choice == "4":
      visualize_library()

    elif choice == "5":
      print("---> Goodbye! <---")
      break

    # Handle any invalid input from the user
    else:
      print("!!! Invalid choice. Please try again. !!!")

# Entry point of the program
if __name__ == "__main__":
  
  main()
