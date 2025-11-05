import multiprocessing

def multiplier(x: int) -> int:
    return x * 2

with multiprocessing.Pool() as pool:
    result = pool.map(multiplier, range(10))
    print(result)