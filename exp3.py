#Experiment3:Data Types And Operations

integer_value=int(input("Enter an integer:"))
float_value=float(input("Enter a floating-point number:"))
text_value=input("Enter a String:")
bool_text=input("Enter Boolean Value(True/False):").strip().lower()
boolean_value=(bool_text=="true")

print("\n---Values and Data Types---")
print(integer_value,type(integer_value))
print(float_value,type(float_value))
print(text_value,type(text_value))
print(boolean_value,type(boolean_value))

print("\n---Arithmetic Operations---")
print("Sum=",integer_value+float_value)
print("Product=",integer_value*float_value)

print("\n---String Operations---")
print("Concatenation=",text_value+"Python")
print("Repetition=",text_value*2)
print("Length=",len(text_value))

print("\n---Boolean Operation---")
print("NOT value=",not boolean_value)