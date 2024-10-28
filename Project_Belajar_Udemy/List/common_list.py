# Davidson Rafael Krisman Nugroho
# 6:36 Mon, Oct 28 2024
# List - Common List Patterns

basket = ['a', 'x', 'c', 'b', 'e', 'r', 'z'] # Create a list named basket with random alphabet in it
print(len(basket)) # Print the length of the list
basket.sort() # Sort the basket list from a-z
basket.reverse() # reversed the list from last to the first
print(basket[:]) # Copy a list basket
print(basket) # Print the list basket

print(list(range(1, 101))) # It make a list from 1 to 100
print(list(range(101))) # It make a list from 0 to 100

# sentence = ' ' we dont need a variable with an empty string to make a sentence from a list
# for item in basket:
#     sentence += item + ' ' | Output : a x c b e r z 
# sentence.join(['hi', 'my', 'name', 'is', 'david']) | Output : hi my name is david
my_sentence = ' '.join(['hi', 'my', 'name', 'is', 'david']) # It make a sentence from a list ( Common used {empty string}.join(list) )
print(my_sentence) # print the sentence
