dog_breeds_available_for_adoption = ["french_bulldog", "dalmatian", "shihtzu", "poodle", "collie"]
dog_breed_I_want = "dalmatian"

def find_dog_breed(dog_breeds, target_breed):
    """
    Finds a specific dog breed in a list of available dog breeds for adoption.

    Parameters:
    dog_breeds (list): A list of dog breeds available for adoption.
    target_breed (str): The dog breed to search for.

    Returns:
    None

    Prints the list of dog breeds and a message if the target breed is found.
    """
    for dog_breed in dog_breeds:
        print(dog_breed)
        if dog_breed == target_breed:
            print("They have the dog I want!")
            break

# Call the function
find_dog_breed(dog_breeds_available_for_adoption, dog_breed_I_want)
