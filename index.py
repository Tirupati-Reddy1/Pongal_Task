# # 1. Create a function that takes two numbers as arguments and returns their sum.

def sum_two_Arguments():
    x=int(input("Enter X value: "))
    y=int(input("Enter y value: "))
    return x+y
print("1) FIRST QUESTION")    
result=sum_two_Arguments()
print("sum of two arguments is :",result)

# ======================================================================
#  2. Write a function that takes an integer minutes and converts it to seconds.

def min_sec_conversion():
    x1=int(input("Enter minutes: "))
    return x1*60
print("2) MINUTES TO SECONDS CONVERSION")
result1=min_sec_conversion()
print("seconds is:",result1)
# ============================================================================
#  3. Create a function that takes two arguments. Both arguments are integers, a and b. Return true if one of them is 10 or if their sum is 10.

print("3) CHECKING EITHER VALUE IS TRUE OR FALSE")
def check_number():
    x2=int(input("Enter a x2 value:"))
    x3=int(input("Enter a x3 value:"))
    if x2==10 or x3==10 or (x2+x3)==10:
        return True
    else:
        return False
result3=check_number()

print("Conditions are met: ",result3)

# ===========================================================================================

#  4. Create a function that takes two strings as arguments and returns either true or false
#  depending on whether the total number of characters in the first string is equal to the total
#  number of characters in the second string.

print("4) STRINGS LENGTH EQUAL ARE NOT")
def strings_equal():
    x4=str(input("Enter first string: "))
    x5=str(input("Enter second string: "))
    if len(x4)==len(x5):
        return True
    else:
        return False
res=strings_equal()

print("result=",res)

# ================================================================================================

#  5. Create a function that takes an array of numbers and returns the largest number.

def Largest_Number(arr):
    if not arr:
        return None
    Largest=arr[0]
    for number in arr:
        if number>Largest:
            Largest=number
    return Largest
arr=[5,7,9,1,2]    
res1=Largest_Number(arr)
print("5) LARGEST IN ARRAY")
print("given array:",arr, "Largest is:",res1)
# =====================================================================================================


#  6. Create a function that takes two strings as arguments and returns the number of times the first
#  character (the single character) is found in the second string.

def length_character_in_string(alphabet,text):
    count=text.count(alphabet)
    return count
alphabet=str(input("Enter Alphabet: "))
text=str(input("Enter Character: "))
res2=length_character_in_string(alphabet,text)
print("6) CHARACTER COUNT IN TEXT: ",res2)

# ======================================================================


#  7. Create a function that takes a string and returns the number (count) of vowels contained within it

def vowel_check(str1):
    vowels="aeiouAEIOU"
    count=0
    for i in vowels:
        if i in str1:
            count+=1
    return count
str1="WelCOmE to PytHOn"
res5=vowel_check(str1)  
print("7) CHECKS VOWEL IN TEXT")
print("given string is: ",str1 ,"count is:",res5)


# =================================================================================

#  8. Given a string, create a function to reverse the string.


def reverse_str(text2):
    return text2[::-1]
text2="WELCOME TO PYTHON"
res6=reverse_str(text2)
print("8) STRING REVERSE")
print("given text is: ",text2 ,"output is:",res6 )

# =========================================================================================

#  9. Write a program that defines a function to multiply an integer by 2. Then, loop from 0 to a given
#  integer n, passing each value to the function and printing the result

def multiply_by_2(x):
    return x*2
n = int(input("Enter the number :"))
for i in range(n+1):
    value = multiply_by_2(i)
    print(value)

# ===============================================================================================
 
# 10.Program to find greatest of three numbers


def greatest_number(num4):
    greatest=num4[0]
    for i in num4:
        if i>greatest:
            greatest=i
    return greatest
num4=[5,9,2]
res7=greatest_number(num4)
print("10) GREATEST OF THREE NUMBERS")
print("given input is: ",num4 ,"Output is: ", res7)   

# #  11.Program to find factorial of number.

def factorial_of_num(num7):
    factorial=1
    for i in range(1,num7+1):
        factorial=factorial*i
    return factorial
num7=5
output=factorial_of_num(num7)
print("11) FACTORIAL OF NUMBER")
print("input is:",num7 ,"Output is:",output)

# =============================================================================

#  12.Calculate the Power of a Number(using loop only).

# def power_of_number(num8):
#     for i in range(1,num8+1):
#         i=i*i
#     return i
# num8=12
# output1=power_of_number(num8)
# print("11) POWER OF NUMBER")
# print("input is:",num8 ,"Output is:",output1)


def power_of_number(base,exponent):
    itarable=1
    for i in range(abs(exponent)):
        itarable*=base
    return itarable
base=int(input("Enter base value:")) 
exponent=int(input("Enter exponent value:"))
output2=power_of_number(base,exponent)
print("11) POWER OF NUMBER")
print("output is: ",output2)

# ====================================================================

#  13.Program to Check Whether a Number is Prime or Not

def is_prime(numb):
    if numb<=1:
        return "Not a prime"
    for i in range(2,int(numb**0.5)+1):
        if numb%i==0:
            return "Not a prime"
    return "Its a prime number"
numb=int(input("Enter a number: ")) 
output3=is_prime(numb)
print("13) CHECKING NUMBER IS PRIME OR NOT")
print("output is: ",output3)      

# ==================================================================================

#  14.Program to find a missing number in first n natural numbers

print("14) FINDING MISSING NUMBER IN NUMBERS")
def missing_num_finging(x10):
    n=len(x10)+1
    expected_sum=n*(n+1)//2
    actual_sum=sum(x10)
    missing=expected_sum-actual_sum
    return missing
x10=[1,3,4,5]
output4=missing_num_finging(x10)
print("given input is: ",x10  ,"output is: ",output4)

# ============================================================================

# 15.Program to insert an element in an array at a given index.

def array_element_insertion(element,array,index):
    if index<0 or index>len(array):
        return "Enter vallid index number...!"
    array.insert(index,element)
    return array
array=list(map(int,input("Enter Array: ").split()))
index=int(input("Enter Index number: "))
element=int(input("Enter element : "))
result=array_element_insertion(element,array,index)
print(result)

# =======================================================================================

# 16.Count occurrence of number

def count_occurrence(array1,element):
    count=0
    if element not in array1:
        return "Elemet Not There...!"
    for num in array1:
        if num==element:
            count+=1
    return count
array1=list(map(int,input("Enter Array seperated by spaces:").split()))  
element=int(input("Enter Element: "))
result5=count_occurrence(array1,element)
print("Occurances: ",result5)

# =================================================================================================
#  1. Print Pattern using loop.
n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j, end=" ")
    print()

#  2. Create a function that takes an array of arrays with numbers. Return a new (single) array with the largest numbers of each.

def largest_in_subarray(numbers):
    found=[]
    for i in numbers:
        largest=max(i)
        found.append(largest)
    return found
numbers=[[7,5,9],[9,1,8],[7,8,9]]
result=largest_in_subarray(numbers)
print(result)

#  3. Create a function that takes an array of items, removes all duplicate items and returns a new
#  array in the same sequential order as the old array (minus duplicates).

def removes_duplicates(numbers):
    new_arr=[]
    for i in numbers:
        if i not in new_arr:
            new_arr.append(i)
    return new_arr
numbers=['hi','helloo','how are you','helloo']
result=removes_duplicates(numbers)
print("for input: ",numbers,"output: ",result)

#  4. Program to arrange numbers in ascending order

def ascending_order(numbers):
    order=sorted(numbers)
    return order
numbers=list(map(int,input("Enter numbers seperated by spaces: ").split()))
result=ascending_order(numbers)
print("for input:",numbers,"output:",result)

# 5. Program to count vowels and consonants in a given String.

def vowels_consonents_count(str):
    vowels=0
    consonents=0
    group="aeiouAEIOU"
    for i in str:
        if i in group:
            vowels+=1
        else:
            consonents+=1
    return "vowels is: ",vowels,"Consonents is:",consonents
str="eiouAEIOU"
result=vowels_consonents_count(str)
print(result)


    
