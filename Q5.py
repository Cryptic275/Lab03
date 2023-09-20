x = int(input("Enter the number of repititions: "))

def rep(func):
    def wrapper():
        for i in range(x):
            func()
    return wrapper
@rep
def hello():
    print("Hello")

hello()