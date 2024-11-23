string=input("Enter a sentence: ")
count=0
for char in string:
    if char in 'aeiouAEIOU':  
        count+=1
print(f"Number of vowels: {count}")
