def even_number_of_evens(numbers: list):
    """
    Should Raise a TypeError if a list in not passed into the function
    error message: "A list was not passed into the function"
    if the list is empty it will return False
    if the number of even numbers is odd - return False
    if the numner of even numbers is even - return True
    """
    if not isinstance(numbers, list):
        raise TypeError("A list was not passed into the function")
    else:
        if len(numbers) == 0:
            return False
        count_evens = 0
        for num in numbers:
            if num % 2 == 0:
                count_evens += 1
        return True if count_evens % 2 == 0 else False
        






if __name__ == "__main__":
    print(even_number_of_evens(5))