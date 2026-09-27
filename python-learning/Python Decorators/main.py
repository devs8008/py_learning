import time
def brew_coffee():
    start_time = time.time()
    print("Brewing coffee...")
    time.sleep(2)
    print("Coffee is ready!")
    end_time = time.time()
    print(f"Task time: {end_time - start_time} seconds")
brew_coffee()

# Here this bbrew_coffee function violates single responsibility principle because it is doing two things, brewing coffee and measuring time. We can use a decorator to separate the timing functionality from the brewing functionality.   

# This is a decorator function that takes another function as an argument and returns a new function that enhances the original function with additional functionality. In this case, the decorator measures the time taken by the original function to execute.
def timer_dec(func):
    def enhancer_fn():
        start_time = time.time()
        func()
        end_time = time.time()
        print(f"Task time: {end_time - start_time} seconds")
    return enhancer_fn

@timer_dec
def make_macha():
    print("Making macha...")
    time.sleep(3)
    print("Macha is ready!")

make_macha()

# What if we had a function that takes arguments? We can modify the decorator to accept any number of positional and keyword arguments using *args and **kwargs. This way, the decorator can work with functions that have different signatures.