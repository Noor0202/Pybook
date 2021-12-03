print("\n\t\t.....****....@@@...Intoducing a Pybook...@@@....****.....")
print("\n\t\t\t\t\t####...T.Y.B.Sc.( Comp Sci )...####")
print("\n\t\t\t\t\t\t\t\t  Secc - 1")
print("\n\t\t\t\t\t\tCS-3510 PYTHON PROGRAMMING")
print("\n\t\t\t\t\t\t\t\tSemester - V")
print("\n\t\t\t\t\t\t( From Academic Year 2021 )")
print("\n\n\t\tPresent By - Naved Shaikh & Shahnoor Maniyar ( NASA Creation )")
print("""\n \tWe are making this pybook just for our practice and for your understanding.
\tIn this pybook we have mentioned the answers to assignment number three and five in lab course 
\tas well as program line numbers for your convinens.
\tAnd we source code is also available for everyone any one can change the code or access the code
\tWe hope you all can enjoy the pybook.
\n\n So lets Start.....
""")

password = ""
while password != "NASA":
    print("Please Enter Correct Password To Continue....")
    password = input("Enter Password Here : ")
print("\n\t\t\t\t\t####...Thank You...####")

def index():
    print("\n\t Syllabus...")
    a = {"Assignment 3 : ": {"Set A": ("List", "Tuple", "Sets", "Dict"), "Set B": ("List", "Tuple", "Sets", "Dict")},
         "Assignment "
         "5 : ": ("Set "
                  "A",
                  "Set B")}
    for i in a:
        print("\n\t\t", i, a[i])
    c = ["\tExit (0)","\tSet A List", "\tSet A Tuple", "\tSet A Sets", "\tSet A Dict", "\tSet B List", "\tSet B Tuple",
         "\tSet B Sets",
         "\tSet B Dict", "\tSet A",
         " Set B"]
    print("\n\t Index...\n")
    n = 0
    for i in c:
        print("\t\t",n,"  "," - ",i)
        n = n + 1

def exit():
    print("\n\n\tWould You Like to Continue")
    print("\tPlease Mention Yes Or No Below\n")

def SetAlist():
    print("\n\tWelcome To Pybook")
    print("\n\tIn this Topic You are Going To Study A List")
    print("\n\tSo lets Beggine...\n")
    print("""\t\t* A Python list is a mutable sequence of data values called items or elements.\n\t\t  An item can be of any type.
\t\t* List is one of the most frequently used and very versatile data type used in Python.\n\t\t  The elements in the list are stored in a linear order one after other.
\t\t* A list is a collection of items or elements; the sequence of data in a list is ordered.
\t\t* The elements or items in a list can be accessed by their positions \n\t\t  i.e. indices. The index in lists always starts with 0 and ends with n-1, \n\t\t  if the list contains n elements. """)
    print("\n\tlets see some example from the lab-book....\n\n")
    print("Line No - 54")

    print("\n\t1) Write a Python program to sum all the items in a list.\n")

    a = [11,22,33,44,55,66,77,88,99]
    n=0
    for i in a:
        n += i
        #n = n + i
    print("\t\tList is : ", a, "\n\t\tSum all the items in a list is : ", n)

    print("\n\t\t\t OR \n")

    a=[10,20,30,40,50,60,70,80,90]
    b=sum(a)
    print("\t\tList is : ",a)
    print("\t\tSum all the items in a list is : ",b)

    print("\n\t\t\t OR \n")

    a=[1,2,3,4,5,6,7,8,9,0]
    print("\t\tList is : ",a,"\n\t\tSum all the items in a list is : ",sum(a))

    print("\nLine No - 77")

    print("\n\t2) Write a Python program to multiplies all the items in a list.\n")

    a=[1,2,3,4,5,6,7,8,9]
    n=1
    for i in a:
        n *= i
        #n = n * i
    print("\t\tList is : ", a, "\n\t\tMultiplication all the items in a list is : ", n)

    print("\nLine No - 88")

    print("""\n\t3) Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a
\t   given list of non-empty tuples.\n""")

    a = [(1,2),(8,5),(4,6),(7,9),(5,3),(7,1)]
    #for i in a:
    #    print(i[1])

    print("\n\n\t.....<<<<...@@@...Thank You, List is Over Here...@@@...>>>>.....")

def SetAtuple():
    print("\n\tWelcome To Pybook")
    print("\n\tIn this Topic You are Going To Study a Tuple ")
    print("\n\tSo lets Beggine...\n")
    print("""\t\t*  A tuple is a collection of objects which ordered and immutable.
\t\t*  A Python tuple is a sequence of data values called as items or elements.
\t\t*  A tuple is a collection of items which is ordered and unchangeable.
\t\t*  A tuple is a data structure that is an immutable or unchangeable, ordered sequence of elements/items.\n\t\t   Because tuples are immutable, their values cannot be modified.
\t\t*  A tuple is a heterogeneous data structure and used for grouping data.\n\t\t   Each element or value that is inside of a tuple is called an item.
\t\t*  A tuple is an immutable data type. An immutable data type means\n\t\t   that we cannot add or remove items from the tuple data structure.
\t\t*  In Python tuples are written with round brackets () and\n\t\t   values in tuples can also be accessed by their index values, which are integers starting from 0.
\t\t*  Tuples are the sequence or series values of different types separated by commas ().\n\t\t   Tuples are just like lists, but we can not change their values. """)
    print("\n\tlets see some example from the lab-book....\n\n")

    print("Line No - 113")

    print("\n\t1) Write a Python program to create a tuple.\n")

    a=(1,2,3,4,5,6,7,8,9)
    print("\t\tThis Is an example of tuple : ",a)
    print("\t\tType is : ",type(a))

    print("\n\t\t\t OR \n")

    b=()
    print("\t\tThis is an example of empty tuple : ",type(b))

    print("\n\t\t\t OR \n")

    c=(1,2,(3,4,5,(6,7,8,),(9,10)),11)
    print("\t\tThis is an example of nested tuple : ",c)
    print("\t\tType is : ",type(c))

    print("\n\t\t\t OR \n")

    d=tuple([5,4,6,2,1,8])
    print("\t\tThis is an example of tuple with typecasting : ", d)
    print("\t\tType is : ", type(d))


    print("\nLine No - 139")

    print("\n\t2) Write a Python program to create a tuple with different data types\n")

    a=(1,1.5,3+5j,True,"Hello World",[1,2,3],{1 : "Hello",2 : "World"},{1,2,3})
    print("\t\tAnswer : ",a)
    print("\t\tType is : ",type(a))

    print("\n\t\t\t OR \n")

    a=(1,1.5,2+5j,True,[1,2,3,4,5],{6,7,8,9},{1 : "Hello",2 : "World"},(8,5,2))
    print("\n\t\tTuple is : ",a)
    print("\n\t\tType of 'a' : ",type(a))
    for i in range(0, len(a)):
        print("\t\t\tType of a[",i,"]",type(a[i]))

    print("\nLine No - 155")

    print("\n\t3) Write a Python program to check whether an element exists within a tuple.\n")

    a=(8,5,4,6,7,1,9,2)
    b=eval(input("\t\tEnter Any Element : "))
    if(b in a):
        print("\t\t\t",b," is present in tuple : ",a)
    else:
        print("\t\t\t",b," is not present in tuple : ",a)

    print("\n\n\t.....<<<<...@@@...Thank You, Tuple is Over Here...@@@...>>>>.....")

def SetASets():
    print("\n\tWelcome To Pybook")
    print("\n\tIn this Topic You are Going To Study a Set")
    print("\n\tSo lets Beggine...\n")
    print("""\t\t*  A set is an unordered collection of items.\n\t\t   Every element is unique (no duplicates) and must be immutable (which cannot be changed).
\t\t*  However,the set itself is mutable. We can add or remove items from it.\n\t\t   Sets can be used to perform mathematical set operations like union, intersection, symmetric difference etc.
\t\t*  A set data structure in python programming includes an unordered collection of items without duplicates.\n\t\t   Sets are unindexed that means we cannot access set items by referring to an index.
\t\t*  Sets are changeable (mutable) i.e., we can change or update a set as and when required.\n\t\t   Type of elements in a set need not be the same, various mixed data type values can also be passed to the set.
\t\t*  The sets in python are typically used for mathematical operations\n\t\t   like union, intersection, difference and complement etc.""")

    print("\n\tlets see some example from the lab-book....\n\n")

    print("Line No - 180")

    print("\n\t1) Write a Python program to create a set.\n")

    a = {1,5,7,9,4,"Hello",'A',2.5}
    print("\t\tSet is : ",a)
    print("\t\tType of 'a' is : ",type(a))

    print("\n\t\t\t OR \n")

    b = (1,7,5,6,4,8)
    c = set(b)
    print("\t\tCreating Set By using typecasting : ", c)
    print("\t\tType of 'a' is : ", type(c))

    print("\nLine No - 195")

    print("\n\t2) Write a Python program to iterate over sets.\n")

    a = set("Hello World")
    print("\t\tIterating Using For Loop : ")
    for i in a :
        print("\t\t",i,end=' ')

    print("\nLine No - 204")

    print("\n\t3) Write a Python program to create set difference\n")

    a = {5,7,6,1,2,3,4}
    b = {8,5,2,1,4,6,9}
    print("\t\tDifferance By using '-' Sign ( a - b ) = ", a - b)  # this funtion is seperate b values which are in
    # the a and print remaining values of a
    print("\t\tDifferance By using '-' Sign ( b - a ) = ", b - a)  # this funtion is seperate a values which are in
    # the b and print remaining values of b

    print("\n\t\t\t OR \n")

    print("\t\tDifference By using b.differance(a) function = ", b.difference(a))  # or we can use difference funtion
    print("\t\tDifference By using a.differance(b) function = ", a.difference(b))

    print("\n\n\t.....<<<<...@@@...Thank You, Set is Over Here...@@@...>>>>.....")

def SetADict():
    print("\n\tWelcome To Pybook")
    print("\n\tIn this Topic You are Going To Study a Dictionary")
    print("\n\tSo lets Beggine...\n")
    print("""\t\t*  The dictionary data structure is used to store key value pairs indexed by keys.\n\t\t   A dictionary is an associative data structure, means that elements/items are stored in a non linear fashion.
\t\t*  Python dictionary is an unordered collection of items or elements.\n\t\t   Items stored in a dictionary are not kept in any particular order.
\t\t*  The Python dictionary is a sequence of data values called as items or elements.
\t\t*  While other compound data types have only value as an element, a dictionary has a key:value pair.\n\t\t   Each value is associated with a key.
\t\t*  Dictionaries are optimized to retrieve values when the key is known.\n\t\t   A key and and it's value are separated by colon (:) between them.
\t\t*  The items or elements in a dictionary are separated by commas and all the elements must be enclosed in curly braces. """)
    print("\n\tlets see some example from the lab-book....\n\n")

    print("Line No - 234")

    print("\n\t1) Write a Python script to sort (ascending and descending) a dictionary by value.\n")

    a = {1 : "Hello",3 : "World",4 : "Welcome",2 : "Patience"}
    print("\t\tDictionary Before Sorting is : ",a)
    b = sorted(a.items())
    print("\n\t\tDictionary After Sorting in Ascending Order : ", b)
    print("\n\t\tDictionary After Sorting in Descending Order : ", b[: : -1])

    print("\nLine No - 244")

    print("\n\t2) Write a Python script to add a key to a dictionary\n")

    a = {1: "Hello", 3: "World", 4: "Welcome", 2: "Patience"}
    print("\n\t\t Dictionary is : ",a)
    a.update({5: "Pybook"})
    print("\n\t\t New Updated Dictionary is : ",a)

    print("\nLine No - 253")

    print("\n\t3) Write a Python program to iterate over dictionaries using for loops.\n")

    a = {1: "Hello", 3: "World", 4: "Welcome", 2: "Patience"}
    print("\t\tIterating Using For Loop : ")
    for i in a.items():
        print("\t\t",i)
    print("\n\n\t.....<<<<...@@@...Thank You, Dictionary is Over Here...@@@...>>>>.....")

def SetBList():
    print("\n\tWelcome To Pybook")
    print("\n\tIn this Topic You are Going To Study a List From Set B ")
    print("\n\t In This Section We Not Include Definations If You Want to See Then Please Check Set A List, "
          "Topic No - 1")
    print("\n\tSo lets Beggine The Question And Answers....\n")

    print("Line No - 270")

    print("\n\t1. Write a Python program to remove duplicates from a list.\n")

    a = [1,2,3,2,1,5,6,3,5,4,7,8]
    b = set(a)
    c = list(b)
    print("\t\tList With Duplicate Elements : ",a)
    print("\t\tRemoving Duplicate Elements : ",c)

    print("\nLine No - 280")

    print("\n\tWrite a Python program to check a list is empty or not.\n")

    a = [5,2,4,6,8,4,6]
    if(len(a)==0):
        print("\t\tList is Empty : ",a)
    else:
        print("\t\tList is Not empty : ",a)

    print("\n\t\t\t OR \n")

    a = [ ]
    if (len(a) == 0):
        print("\t\tList is Empty : ",a)
    else:
        print("\t\tList is Not empty : ",a)

    print("\n\n\t.....<<<<...@@@...Thank You, Set - B List is Over Here...@@@...>>>>.....")

def SetBTuple():
    print("\n\tWelcome To Pybook")
    print("\n\tIn this Topic You are Going To Study a Tuple From Set B ")
    print("\n\t In This Section We Not Include Definations If You Want to See Then Please Check Set A Tuple,"
          "Topic No - 2")
    print("\n\tSo lets Beggine The Question And Answers....\n")

    print("Line No - 307")

    print("\n\t1. Write a Python program to convert a list to a tuple. \n")

    a = [1,5,7,8,9,6,4,2,3]
    print("\t\tList is : ",a)
    print("\t\t",type(a))
    b = tuple(a)
    print("\t\tConverting Above List to Tuple : ",b)
    print("\t\t", type(b))

    print("\nLine No - 318")

    print("\n\t2. Write a Python program to remove an item from a tuple\n")

    a = (1,2,5,4,8,9,6,)
    # tuple is immutable that means we cant change the elements.
    # but here question is given...???
    # so answering the question we use slicing technique.
    # suppose we want to remove 4 form the tuple..then we use following method...
    b = a[:3] + a[4:]
    print("\t\tTuple Before Change : ",a)
    print("\t\t",type(a))
    print("\t\tUpdated Tuple is : ",b)
    print("\t\t",type(b))


    print("\nLine No - 334")

    print("\n\t3. Write a Python program to slice a tuple. \n")

    a = (8,5,2,4,"Hello",[5,6,2],{8,5})
    print("\t\tTuple Before Slicing is : ",a)
    b = a[:5]
    c = a[5:]
    d = a[::-1]
    #there are various slicing methods we see some of them
    print("\t\tSlicing elements from 0 to 5 : ",b)
    print("\t\tSlicing elements from 5 to end : ", c)
    print("\t\tReverce The Tuple by Using Slicing : ", d)

    print("\nLine No - 348")

    print("\n\t4. Write a Python program to find the length of a tuple. \n")

    a = (4,5,3,"Hello","Welcome")
    print("\t\t Tuple is : ",a)
    print("\t\t Length of Above Tuple is : ",len(a))

    print("\n\n\t.....<<<<...@@@...Thank You, Set - B Tuple is Over Here...@@@...>>>>.....")


def SetBSet():
    print("\n\tWelcome To Pybook")
    print("\n\tIn this Topic You are Going To Study a Set From Set B ")
    print("\n\t In This Section We Not Include Definations If You Want to See Then Please Check Set A Sets,"
          "Topic No - 3")
    print("\n\tSo lets Beggine The Question And Answers....\n")

    print("Line No - 366")

    print("\n\t1. Write a Python program to check if a set is a subset of another set.\n")

    a = {8,5,2,1,4,6,7,}
    b = {1,2,3,4,5,6,7,8,9}
    c = a.issubset(b)
    print("\t\t",a)
    print("\t\t",b)
    if (c == True):
        print("\n\t\t A is Subset of B")
    else:
        print("\n\t\t A is Not a Subset of B")

    print("\nLine No - 380")

    print("\n\t2. Write a Python program to find maximum and the minimum value in a set. \n")

    a = {1,5,6,4,7,8,9,2,3,1}
    print("\t\tSet : ",a)
    print("\n\t\tMaximum Element of The Set A is : ",max(a))
    print("\t\tMinimum Element of The Set A is : ",min(a))


    print("\nLine No - 390")

    print("\n\t3. Write a Python program to find the length of a set. \n")

    a = {8,4,6,2,1,7,3}
    print("\t\t Set is : ",a)
    print("\n\t\t Length of Above Set is : ",len(a))


    print("\n\n\t.....<<<<...@@@...Thank You, Set - B Set is Over Here...@@@...>>>>.....")

def SetBDect():
    print("\n\tWelcome To Pybook")
    print("\n\tIn this Topic You are Going To Study a Dictionary From Set B ")
    print("\n\t In This Section We Not Include Definations If You Want to See Then Please Check Set A Dict,"
          "Topic No - 4")
    print("\n\tSo lets Beggine The Question And Answers....\n")

    print("Line No - 408")

    print("\n\t1. Write a Python script to generate and print a dictionary that contains a number (between 1 and n) "
          "\n\tin the form (x, x*x). \n")
    # in short you have to make a dictionary which contain number keys between 1 yo n and value as a square of that
    # number
    a = int(input("\t\tEnter Number Between (1 - 10) : "))
    b = dict()
    for i in range(0, a + 1):
        b[i] = i * i
    print("\t\tDictionary is : ",b)


    print("\nLine No - 421")

    print("\n\t2. Write a Python script to merge two Python dictionaries\n")

    a = {1 : "Hello", 2 : "World", 3 : "Welcome"}
    b = {4 : "How", 5 : "Are", 6 : "You"}
    #for merge two dict we can use update funtion
    a.update(b)
    print("\t\tMerged Dictionary is : ",a)

    print("\nLine No - 431")

    print("\n\t3. Write a Python program to get a dictionary from an object's fields.\n")
    #i am not learn object so i get this program from the net
    class dictObj(object):
        def __init__(self):
            self.x = 'Hello'
            self.y = 'World'
            self.z = 'Welcome'

        def do_nothing(self):
            pass
    test = dictObj()
    print("\t\tDictionary is : ",test.__dict__)

    print("\n\n\t.....<<<<...@@@...Thank You, Set - B Dictionary is Over Here...@@@...>>>>.....")
    print("\n\t.....<<<<...@@@...Thank You, Assignment 3 is Over Here...@@@...>>>>.....")
    print("\n\t.....<<<<...@@@...Thank You, For Cooperate us...@@@...>>>>.....")

while(1):
    index()
    print("\n Please Mentioned Above Topics Number below")
    b=eval(input("\n Which Topic You Want to Learn - "))

    if(b==1):
        SetAlist()
        exit()
        z = input("\t\tMention Your Answer Here : ")
        if (z == "Yes"):
            continue
        else:
            print("\n\n\t.....<<<<...@@@...Thank You, We Hope, You Enjoy The Code...@@@...>>>>.....")
        break

    elif(b==2):
        SetAtuple()
        exit()
        z = input("\t\tMention Your Answer Here : ")
        if (z == "Yes"):
            continue
        else:
            print("\n\n\t.....<<<<...@@@...Thank You, We Hope, You Enjoy The Code...@@@...>>>>.....")
        break

    elif(b==3):
        SetASets()
        exit()
        z = input("\t\tMention Your Answer Here : ")
        if (z == "Yes"):
            continue
        else:
            print("\n\n\t.....<<<<...@@@...Thank You, We Hope, You Enjoy The Code...@@@...>>>>.....")
            break

    elif(b==4):
        SetADict()
        exit()
        z = input("\t\tMention Your Answer Here : ")
        if (z == "Yes"):
            continue
        else:
            print("\n\n\t.....<<<<...@@@...Thank You, We Hope, You Enjoy The Code...@@@...>>>>.....")
        break

    elif (b == 5):
        SetBList()
        exit()
        z = input("\t\tMention Your Answer Here : ")
        if (z == "Yes"):
            continue
        else:
            print("\n\n\t.....<<<<...@@@...Thank You, We Hope, You Enjoy The Code...@@@...>>>>.....")
        break

    elif (b == 6):
        SetBTuple()
        exit()
        z = input("\t\tMention Your Answer Here : ")
        if (z == "Yes"):
            continue
        else:
            print("\n\n\t.....<<<<...@@@...Thank You, We Hope, You Enjoy The Code...@@@...>>>>.....")
        break

    elif (b == 7):
        SetBSet()
        exit()
        z = input("\t\tMention Your Answer Here : ")
        if (z == "Yes"):
            continue
        else:
            print("\n\n\t.....<<<<...@@@...Thank You, We Hope, You Enjoy The Code...@@@...>>>>.....")
        break

    elif (b == 8):
        SetBDect()
        exit()
        z = input("\t\tMention Your Answer Here : ")
        if (z == "Yes"):
            continue
        else:
            print("\n\n\t.....<<<<...@@@...Thank You, We Hope, You Enjoy The Code...@@@...>>>>.....")
        break

    elif(b==0):
        print("\n\n\t.....<<<<...@@@...Thank You, We Hope You, Enjoy The Code...@@@...>>>>.....")
        break

    else:
        print("\n\n\t****...Please Enter Correct Index Number...****")