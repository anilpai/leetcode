import time


def timing(given_function):
    '''
    Outputs the time a function takes to execute.
    '''

    def wrapper(*args, **kwargs):
        t1 = time.time()
        given_function(*args, **kwargs)
        t2 = time.time()
        return "Time it took to run the function : " + str(round(((t2-t1)*1000*1000), 2)) + " micro seconds \n"
    return wrapper
