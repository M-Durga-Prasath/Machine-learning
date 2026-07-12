import time
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

def function():
    print("This function does absolutely nothing and is just here as a placeholder.")
    time.sleep(7)
    
def timer(func):

    def wrapper():
        start = time.time()

        func()

        end = time.time()
        print(f"Elapsed time: {end - start:.2f} seconds")

    return wrapper

# timed_function = timer(function)
# timed_function()

@timer
def function2():
    print("This function does absolutely nothing and is just here as a placeholder. part 2")
    time.sleep(8)
    
# function2()

logger.info('hello')
logger.debug('not hello')