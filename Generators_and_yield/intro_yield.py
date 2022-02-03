def create_generator() -> int:
    my_list = range(4)
    for i in my_list:
        """yield works like return but this return a generator object,
        this means that the function will return a value just when this generator is called
        and all the code inside generator function is called by a .next() or a list comprehension
        which return all the data inside this execution and the function will continue with the execution 
        when another next() is used
        """

        yield (i + 1) * i

        """
        each yield will return the data that has after a next() call of the function
        
        the function .throw() and .close()
        stop the generator iteration for a condition established by me
        """

        yield f"2do yield {i}"


if __name__ == '__main__':
    gen = create_generator()
    print([i for i in gen])

    try:
        next(gen)

    except StopIteration:
        print("there is no more items")
