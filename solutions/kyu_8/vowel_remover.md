# Vowel remover

## Description

Create a function called `shortcut` to remove the lowercase vowels (a, e, i, o, u ) in a given string.

## Solution

```python
def shortcut( s ):
    a=["a","e","i","o","u"]
    for i in range(len(a)):
        s=s.replace(a[i],"")
    return s
```
##Difficulty
8 kyu

##Explanation
The function shortcut(s) takes a string s as input and aims to remove all vowels (a, e, i, o, u) from the string. It achieves this using a loop that iterates through each vowel and uses the str.replace() method to remove occurrences of that vowel from the string. 

##Examples
```python
print(shortcut("hello"))  # Output: "hll"
print(shortcut("python"))  # Output: "pythn"
print(shortcut("codewars"))  # Output: "cdwrs" 
```
##Algorithm Complexity
The time complexity of this code is O(n*m), where n is the length of the input string s, and m is the number of vowels (which is constant, in this case, always 5 - a, e, i, o, u). This is because for each vowel, the str.replace() method scans through the string once. In the worst case, it needs to scan the entire string for each vowel. 
