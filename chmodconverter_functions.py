def symbolic_to_numeric(symbolic: str) -> str:
    mapping = {'r': 4, 'w': 2, 'x': 1, '-': 0}
    result = []

    for i in range(0, len(symbolic), 3):
        part = symbolic[i:i+3]
        num = sum(mapping.get(char, 0) for char in part)
        result.append(str(num))

    return ''.join(result)

def numeric_to_symbolic(numeric: str) -> str:
    mapping = ['---', '--x', '-w-', '-wx', 'r--', 'r-x', 'rw-', 'rwx']
    result = ''.join([mapping[int(digit)] for digit in numeric])
    
    return result