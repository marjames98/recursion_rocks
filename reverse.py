# You will have to figure out what parameters to include
# 🚨 All functions must use recursion 🚨

# Write a recursive function called `reverse` that accepts a ss and returns a reversed ss.

# my solution (not working properly)
# def reverse(ss):
#     reverse = "", "a", "ab", "computer"
#     for ch in ss:
#         reverse = ch + reverse
#     return reverse
    
# pete's solution 
def reverse(input, already_reversed = ''):
    if len(input) == 0:
        return already_reversed

    new_already_reversed = input[0] + already_reversed
    new_input = input[1:]
    
    return reverse(new_input, new_already_reverse) 

print(reverse("computer")) 

# print(reverse(""))
# # => "a"
# print(reverse("ab")) 
# # => "ba"
# print(reverse("computer")) 
# # => "retupmoc"
# print(reverse(reverse("computer"))) 
# # => "computer"

# DONE/ GETTING ERRORS 