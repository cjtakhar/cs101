def Compute_Mean(numbers=[0,0,0]):
    n = len(numbers)

    total = 0
    for value in numbers:
        total = total + value

    Mean = total / n
    return Mean