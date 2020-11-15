# print("Hi Alex, - Your favourite colour is red")
# print("Goodbye Alex")

#We dont want to keep tying ALex or any longer words - #could make spelling mistakes

#We use variables
#How to name a variable, the "=", quotation  marks
# print("\n")
# personName = "Alex"
# faveColour = "Red"
# print("Hi", personName, " - your favourite colour is ",faveColour )

# danstone scott redmond
print("\n")
# personName = "John"
# faveColour = "Green"
# print("Hi", personName, " - your favourite colour is ",faveColour )

#There is an easier way
#We can use the input command. This allows a user to input their own name
print("\n")
personName = input("Enter your name: ")
faveColour = input("Enter your favourite colour: ")
#####use int so that I can only input numbers#####
faveAge = int(input("What is your age?"))
print("Hi", personName, "- your favourite colour is ",faveColour, "your age is ", faveAge)
print("Goodbye", personName)

