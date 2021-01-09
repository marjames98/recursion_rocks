# You will have to figure out what parameters to include
# 🚨 All functions must use recursion 🚨

# Write a recursive function called `reverse` that accepts a ss and returns a reversed ss.

def reverse(ss):
    reverse = "", "a", "ab", "computer"
    for ch in ss:
        reverse = ch + reverse
    return reverse
    

print(reverse(""))

# print(reverse("")) 
# # => ""
# print(reverse("a")) 
# # => "a"
# print(reverse("ab")) 
# # => "ba"
# print(reverse("computer")) 
# # => "retupmoc"
# print(reverse(reverse("computer"))) 
# # => "computer"