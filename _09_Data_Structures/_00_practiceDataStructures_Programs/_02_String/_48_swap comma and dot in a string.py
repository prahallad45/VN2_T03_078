'''
# swap comma and dot in a string
Topics
CRUD - update
State- input string
Behaviour - swap comma and dot

# mathematical approach
step1 - get the input data
step2 - check the comma and dot elements and replace it
step3 - return the output in the console

'''
print("___1.using the Built in approach___")

x = "mani, karna went to movie. Both saw the film,ate popcorn,drank some water.Returned to home."
maketrans = x.maketrans
final = x.translate(maketrans(",.", ".,", " "))
print("input string:", x)
print("after swapping:", final.replace(",", ','))


print("___4.using functions approach___")


def replace(str1):
    maketrans = str1.maketrans
    final = str1.translate(maketrans(",.", ".,", " "))
    return final.replace(",", ",")


string = "1, 2.35, 4.2"
print("input string:", string)
print("after updating the string:", replace(string))
