import time
import numpy as np

N = 10_000_000

python_list = list(range(N))
start = time.perf_counter()
squared_loop = [x*x for x in python_list]
loop_time = time.perf_counter() - start
print(f"python loop: {loop_time:.3f}")

numpy_array = np.arange(N)
start = time.perf_counter()
squared_vec = numpy_array ** 2
vec_time = time.perf_counter() - start

print(f"NumPy vectorized: {vec_time:.3f} seconds")

print(f"NumPy is {loop_time / vec_time:.1f}x faster")