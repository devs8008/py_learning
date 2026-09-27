import time
from datetime import datetime, timedelta

def timmer_dec(func):
    def enhancer_fn(*args, **kwargs):
# Packs postional arguments into a tuple and passes them to the original function. This allows the decorator to work with functions that take any number of positional arguments. kwargs are packed into a dictionary and passed to the original function. This allows the decorator to work with functions that take any number of keyword arguments.
        start_time = time.time()
        func(*args, **kwargs)
        # Unpacks the tuple of positional arguments and passes them to the original function.
        end_time = time.time()
        print(f"Task time: {end_time - start_time} seconds")
    return enhancer_fn

@timmer_dec
def make_coffee(type, sleep_time):
    print(f"Making {type} coffee...")
    time.sleep(sleep_time)
    print("Coffee is ready!")

make_coffee("Latte", 2)

@timmer_dec
def make_tea(type, sleep_time):
    print(f"Making {type} tea...")
    time.sleep(sleep_time)
    print("Tea is ready!")

make_tea(type="Green", sleep_time=3)

# What if there was function that returns a value? We can modify the decorator to return the value returned by the original function. This way, the decorator can work with functions that return values.

def timmer_dec_with_return(func):
    def enhancer_fn(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        # This result variable captures the return value of the original function.
        end_time = time.time()
        print(f"Task time: {end_time - start_time} seconds")
        return result
        # We return the result variable so that the decorator returns the value returned by the original function.
    return enhancer_fn

@timmer_dec_with_return
def make_tea(type, sleep_time):
    print(f"Making {type} tea...")
    time.sleep(sleep_time)
    print("Tea is ready!")
    return f"The {type} tea is toooo hot rn to drink! Plz drink it by {datetime.now() + timedelta(minutes=5)}"

print(make_tea(type="Green", sleep_time=3))