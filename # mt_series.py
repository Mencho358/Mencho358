# mt_series.py

import math

def inv_tanh(x: float) -> float:
    result = 0.0
    for n in range(50):
        term = math.pow(x, 2 * n + 1) / (2 * n + 1)
        result += term
    return result

# Sample test code
if __name__ == '__main__':
    print(f'inv_tanh(0) = {inv_tanh(0)}') 
    # expected output: inv_tanh(0) = 0.0

    print(f'inv_tanh(0.5) = {inv_tanh(0.5)}') 
    # expected output: inv_tanh(0.5) = 0.5493061443340544

    print(f'inv_tanh(-0.25) = {inv_tanh(-0.25)}') 
    # expected output: inv_tanh(-0.25) = -0.25541281188299525
