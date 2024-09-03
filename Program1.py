# List demonstration
def list_demo():
    # Creating a list of integers
    numbers = [1, 2, 3, 4, 5]
    
    # Accessing elements of a list
    print("List:")
    print(numbers)
    
    # Adding elements to a list
    numbers.append(6)
    print("After appending 6:", numbers)
    
    # Removing elements from a list
    numbers.remove(3)
    print("After removing 3:", numbers)
    
    # Iterating over a list
    print("Iterating over list:")
    for num in numbers:
        print(num)
    
    # Slicing a list
    print("Sliced list:", numbers[1:4])
    
    # List comprehension
    squares = [x ** 2 for x in numbers]
    print("List comprehension - Squares:", squares)
    
    print()

# Dictionary demonstration
def dict_demo():
    # Creating a dictionary of students and their ages
    students = {
        'Alice': 20,
        'Bob': 21,
        'Charlie': 19,
        'Diana': 22,
        'Eve': 20
    }
    
    # Accessing elements of a dictionary
    print("Dictionary:")
    print(students)
    
    # Adding elements to a dictionary
    students['Frank'] = 23
    print("After adding Frank:", students)
    
    # Removing elements from a dictionary
    del students['Charlie']
    print("After removing Charlie:", students)
    
    # Iterating over a dictionary
    print("Iterating over dictionary:")
    for name, age in students.items():
        print(f"{name}: {age}")
    
    print()

# Tuple demonstration
def tuple_demo():
    # Creating a tuple of colors
    colors = ('red', 'green', 'blue', 'yellow', 'orange')
    
    # Accessing elements of a tuple
    print("Tuple:")
    print(colors)
    
    # Tuple slicing
    print("Sliced tuple:", colors[1:4])
    
    # Iterating over a tuple
    print("Iterating over tuple:")
    for color in colors:
        print(color)
    
    print()

# Main function to demonstrate all data structures
def main():
    list_demo()
    dict_demo()
    tuple_demo()

if __name__ == "__main__":
    main()
