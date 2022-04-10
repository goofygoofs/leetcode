def LCS(word_a, word_b):
    cell = [[0] * len(word_a) for i in range(len(word_b)) ] 
    for i in range(len(word_a)):
        for j in range(len(word_b)):
            if word_a[i] == word_b[j]:
                # the letters match
                cell[i][j] = cell[i-1][j-1] + 1
            else:
                # the letters don't match
                cell[i][j] = max(cell[i-1][j], cell[i][j-1])
    return cell

print(LCS('fish', 'fosh'))