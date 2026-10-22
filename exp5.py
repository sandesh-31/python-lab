text=input("Enter a string: ")

print("First character      :",text[0]if text else "Empty string")
print("Last character       :",text[-1]if text else "Empty string")
print("First five characters:",text[:5])
print("Reversed string      :",text[::-1])

print("Uppercase:",text.upper())
print("Lowercase:",text.lower())

sub=input("Enter a character/substring to count: ")
print("Occurrence count:",text.count(sub))

old=input("Enter word to replace: ")
new=input("Enter new word: ")
print("After replacement:",text.replace(old,new))

words=text.split()
print("Split words:",words)
print("Joined with'-':","-".join(words))

start_sub=input("Enter starting substring to check: ")
end_sub=input("Enter ending substring to check: ")
print("Starts with given substring:", text.startswith(start_sub))
print("Ends with given substring :", text.endswith(end_sub))