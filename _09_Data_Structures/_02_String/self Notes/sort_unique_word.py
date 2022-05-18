# normal 
strr = input("Enter string: ")
words = [word.lower() for word in strr.split()]
words.sort()

print("In sorting order: ")
for word in words:
   print(word)


#usng function
def unique_word(str3):
    words = [word.lower() for word in str3.split()]
    words.sort()

    print("In sorting order: ")
    for word in words:
        print(word)
    
          
str3 =input("Enter the string:")
unique_word(str3)