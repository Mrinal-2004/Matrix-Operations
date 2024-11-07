'''In this program we write code for exponation (or power) of a matrix
'''

def matrix_input(row,column): #this function return a matrix
    matrix=[] #create a empty matrix
    for i in range(row):
        column_matrix=[]  #column of this matrix empty (define)
        for j in range(column):
            element=int(input('Enter the %d row and %d column element :' % (i+1,j+1))) 
            column_matrix.append(element)
        matrix.append(column_matrix)
    return matrix 

def matrix_output(matrix): #this function shows the matrix in terminal window
    row=len(matrix) #check the rows of the matrix
    column=len(matrix[0]) #cheack the column of the matrix
    for i in range(row):
        for j in range(column):
            print('   ',matrix[i][j], end='\t')
        print()

def matrix_multiply(matrix_1,matrix_2): #function for multiply two matrixes
    row1=len(matrix_1)
    column1=len(matrix_1[0])
    row2=len(matrix_2)
    column2=len(matrix_2[0])
    matrix_multiply=[] #Define a matrix which is later multiplication matrix
    for i in range(row1): #Initialy store zero for all entry
        column=[]  #column of this matrix empty (define)
        for j in range(column2):
            column.append(0)
        matrix_multiply.append(column)

    '''Multiplication process start'''
    for i in range(row1):
        for j in range(column2):
            matrix_multiply[i][j]=0
            for k in range(row2):
                element=int(matrix_multiply[i][j])+int(matrix_1[i][k])*int(matrix_2[k][j])
                matrix_multiply[i][j]=element

    return matrix_multiply

def matrix_exponation(matrix,n): #function for find the exponation
    l=len(matrix)
    matrix_expo=matrix_multiply(matrix,matrix) #initial multiplication
    for i in range(n-2):# two matrix multiply before
        matrix_expo=matrix_multiply(matrix_expo,matrix)
    
    return matrix_expo

row=int(input('Enter the nos of row and column:'))
list=matrix_input(row,row)
print('The matrix look like:')
matrix_output(list)

string=input('Are you want to continue...(Y/N):')

while string=='Y'or string=='y':
    n=int(input('Enter the exponent:'))
    list1=matrix_exponation(list,n)
    print('The matrix to the power ',n,'is:')
    matrix_output(list1)
    string=input('Are you want to continue...(Y/N):')
