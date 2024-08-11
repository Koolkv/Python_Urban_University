def get_matrix(n, m, value):
    matrix = []
    n_counter = 0
    while n > n_counter:
        m_counter = 0
        empty = []
        matrix.append(empty)
        n_counter += 1
        while m > m_counter:
            empty.append(value)
            m_counter += 1

    return matrix
print (get_matrix(2, 5, 8))