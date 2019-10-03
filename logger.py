def logger(func):
    def wrapper():
        print('Start logging')
        func()
        print('Done logging')
    return wrapper

@logger
def sample():
    print('This inside logger')

sample()
