import numpy as np

def calculate(list):
    calc_map: dict[str, callable] = {
        "mean": np.mean,
        "variance": np.var,
        "standard deviation": np.std,
        "max": np.max,
        "min": np.min,
        "sum": np.sum,
    }
    
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    arr: np.array = np.array(list)
    matrix: np.array = arr.reshape(3, 3)

    calculations: dict[str, list] = {
        x: [f(matrix, axis=0).tolist(), f(matrix, axis=1).tolist(), f(arr).tolist()]
        for x, f in calc_map.items()
    }
    
    return calculations