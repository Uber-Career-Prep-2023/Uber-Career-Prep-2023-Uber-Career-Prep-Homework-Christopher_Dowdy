'''
Inuition: 
- Brute force we can traverse through entire matrix searching for a 1
- if we find a 1, we can then expand our dimensions to form the maximum square 
  of 1's at this coordinate
- this is going to be pretty bad TC, I think the problem can be solved with 2-D DP
   but not sure the right way to do it.
Technique: Brute force matrix traversal
TC: O(n^2*m^2)
SC: O(1)
'''

def largest_squares_of_1s(matrix): 
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    max_square = 0
    
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == '1':
                length = 1
                flag = True
                while i + length < rows and j + length < cols and flag:
                    for k in range(j, j + length + 1):
                        if matrix[i + length][k] == '0':
                            flag = False
                            break
                    for k in range(i, i + length + 1):
                        if matrix[k][j + length] == '0':
                            flag = False
                            break
                    if flag:
                        length += 1
                max_square = max(max_square, length)
    
    return max_square

def test_suite():
    matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    assert largest_squares_of_1s(matrix) == 2

    matrix = [["0","1"],["1","0"]]
    assert largest_squares_of_1s(matrix) == 1

    matrix = [["0"]]
    assert largest_squares_of_1s(matrix) == 0

test_suite()

# time spent: 45 mins