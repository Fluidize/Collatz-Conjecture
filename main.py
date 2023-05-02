import matplotlib.pyplot as plt
import numpy as np
import scipy
inp = float(input("Starting number: "))
output_values = [inp]
def gen_array(num):
    global iter_count5
    if num % 2 == 0:
        num /= 2
    elif num % 2 == 1:
        num = (num*3) + 1
    output_values.append(num)
    if num != 1:
        gen_array(num=num)
gen_array(inp)
print(f"It took {len(output_values)} iterations to reach 1.")
x = [x for x in range(len(output_values))]
y = output_values
ln_reg = scipy.stats.linregress(x, y)
plt.plot(x, y)
plt.show()
