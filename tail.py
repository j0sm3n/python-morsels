def tail(sequence, n):
    result = []
    sequence = list(sequence)
    if 0 >= n >= len(sequence):
        return result
    else:
        for i in range(len(sequence) - n, len(sequence)):
            result.append(sequence[i])
        return result


squares = (n**2 for n in range(10))
print(tail(squares, 3))
