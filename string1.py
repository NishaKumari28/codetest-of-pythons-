#wap to count total no of vowels and consonant in a string in python

a= input("Enter a string: ")
vow = "aeiouAEIOU"
vcount = 0
ccount = 0
for char in a:
        if char in vow:
            vcount += 1
        else:
            ccount += 1

print("total  vowels is :" ,vcount)
print("total consonants is :" ,ccount)


            
