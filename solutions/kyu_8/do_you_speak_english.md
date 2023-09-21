# Do you speak "English"?

## Description

Given a string of arbitrary length with any ASCII characters. Write a function to determine whether the string contains the whole word "English".

The order of characters is important -- a string "abcEnglishdef" is correct but "abcnEglishsef" is not correct.

Upper or lower case letter does not matter -- "eNglisH" is also correct.

Return value as boolean values, true for the string to contain "English", false for it does not.

## Solution

```python
def sp_eng(sentence): 
    sentence = sentence.lower()
    if sentence.find("english") != -1:
        return True
    return False
