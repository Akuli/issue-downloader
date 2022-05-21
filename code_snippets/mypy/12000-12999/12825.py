from threading import Lock

# Use this lock to ensure that only one thread is executing a function
# at any time.
my_lock = Lock()

def with_lock(f):
    '''A decorator which provides a lock.'''
    def inner(*args, **kwargs):
        # Provide the lock as the first argument.
        return f(my_lock, *args, **kwargs)
    return inner

@with_lock
def sum_threadsafe(lock, numbers):
    '''Add a list of numbers together in a thread-safe manner.'''
    with lock:
        return sum(numbers)

# We don't need to pass in the lock ourselves thanks to the decorator.
sum_threadsafe([1.1, 2.2, 3.3])

from threading import Lock
from typing import Concatenate, ParamSpec, TypeVar, Callable

P = ParamSpec('P')
R = TypeVar('R')


def with_lock(f: Callable[Concatenate[Lock, P], R]) -> Callable[P, R]: ...
