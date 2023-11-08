

def minSubArrayLen( target, nums):
    print("input list",nums)
    if len(nums) < 1: return 0
    nums.sort();
    for i in range(len(nums)):
        sumx = 0
        for j in range(i):
            sumx += nums[len(nums)-1-j]
        if sumx >= target: return  i   
        
 
def lengthOfLongestSubstring(s):
    i=0
    j=0
    nodupslice1=""
    nodupslicelen1=0
    nodupslice2=""
    nodupslicelen2=0
    while i < len(s) -1:
        j = i + 1
        print(j)
        while s[j-1:j] != s[j:j+1]: j = j+1
        print(j)
        nodupslice1 = s[i:j-1]
        nodupslicelen1 = j-i+1
        print(nodupslice1)
        print(nodupslicelen1)
        if nodupslicelen1 > nodupslicelen2:
            nodupslicelen2 = nodupslicelen1
            nodupslice2 = nodupslice1
            print(nodupslice2)
              
        i = j + 1     
         
    return  nodupslice2   

def findSubstring(s, words):
    lenofword = len(words[0])
    lenofwords= len(words)
    lenofconcatstr = lenofword * lenofwords
    
    sindex=0
    eindex=lenofconcatstr
    windowstr=''
    listindex=[]
    isperword=True
    
    while eindex < len(s):
        windowstr = s[sindex:eindex]
        isperword=True
        for x in range(len(words)):
            n=windowstr.index(words[n])
            if n>0: windowstr = windowstr[0:n] + windowstr[n+lenofword:]
            else: 
                isperword=False
                break
        if isperword: listindex.append(sindex)   
        sindex = sindex + lenofword
        eindex = eindex + lenofword 
            
    return listindex    

#x List<List(9)>
def isvalidsudoku(x):
    
    #valid rows
    print("validate rows")
    for i in range(9):
        print(x[i])
        isvalid = isvalidsudokuarray(x[i])
        if isvalid==False: return False
    
    #valid cols
    print("validate columns")
    colarray = []
    for col in range(9):
        colarray = [x[row][col] for row in range(9)]
        print(colarray)
        isvalid = isvalidsudokuarray(colarray)
        if isvalid==False: return False        
    
    #valid 3X3 cells 
    print("validate subcells")
    cellarray = []
    r = 0
    c = 0
    
    for r in range(0,9,3):
        for c in range(0,9,3):
            cellarray = [x[n][m] for n in range(r,r+3) for m in range(c,c+3)]
            print(cellarray)
            isvalid = isvalidsudokuarray(cellarray)
            if isvalid == False:return False
     
        
        
    return True

    
def isvalidsudokuarray(s):
    isdigit = False
    numbers = ['1','2','3','4','5','6','7','8','9']
    sc = s.copy()
    sc.sort()
    print(sc)
    i=0

    while i + 1 < len(sc):
        if not isdigit and sc[i] in numbers:isdigit=True
        if  sc[i] == sc[i+1] and sc[i] in numbers: return False
        i = i + 1
    return isdigit    
          
        
        
    
target = 9
nums = [2,3,1,2,4,3]        
x=minSubArrayLen(target,nums)
print(x)

s='abccrddrtyuf'
x=lengthOfLongestSubstring(s)
print(x)

x=[["8",".","7",".",".","1",".",".","."]
  ,["6",".",".","1","9","5",".",".","."]
  ,[".","9","8",".",".",".",".","6","."]
  ,["8",".",".",".","6",".",".",".","3"]
  ,["4",".",".","8",".","3",".",".","1"]
  ,["7",".",".",".","2",".",".",".","6"]
  ,[".","6",".",".",".",".","2","8","."]
  ,[".",".",".","4","1","9",".",".","5"]
  ,[".",".",".",".","8",".",".","7","9"]]

isvalid = isvalidsudoku(x)
print(isvalid)