#!/usr/bin/env python3.8

# # # prints the string "Hello world"
# # print ("Hello world")
# # ################################################################

# # # assigning variables and orinting their value
# # name = "John"
# # print (name)
# # print (f"{name} is nice")

# # #--------------------------------------------------------

# # firstname = "John"
# # lastname = "Smith"

# # print (f"My full name is {firstname} {lastname}")

# # #combining two variables
# # fullname = firstname+ " " +lastname
# # print (fullname)

# # #--------------------------------------------------------

# # #removing extra spaces from sides
# # favLang = " Python "
# # print (favLang.rstrip())    #remove from the end
# # print (favLang.lstrip())    #remove from the start
# # print (favLang.strip())    #remove from both sides

# #-----------------------------------------------------------
# # #task for printing and basic arithematic
# # url = "http://www.google.com"
# # ip_address = "192.168.1.100"
# # mon = 10
# # tue = 20
# # wed = 30
# # thu = 40
# # fri = 50

# # sum_of_weekdays = mon + tue + wed + thu + fri
# # weekly_hits = sum_of_weekdays / 5

# #----------------------------------------------------------
# #taking input
# name = input("what is your full name ?\n")
# print ("Hello " + name)

# # to make the initials uppercase 
# print("Hello " + name.title()) # .title makes the initial uppercase

# # to take the input and convert it to integer for number

# age = int(input("what is your age ?\n"))
# print (f"Hi ! {name.title()} and i know now that your age is {age}")

#----------------------------------------------------------
#lists
# servers = ['server101','server201','server301']
# num_list = [75857]
# empty_list = []
# print (servers +  empty_list + num_list)

# print (servers[0].title())  #prints the first index
# print (servers[-1].title()) #prints the last index

# #replacing a value in the list
# servers[1] = 'zumba'
# print (servers)

# #to sort the list
# servers.sort()
# print(servers)  #sorted list

# #to print the list in reverse order
# servers.reverse()
# print (servers)     #print in reverse order

# #to find the length of the list
# print (len(servers))    #print the length of the servers list


# # to have user input in the list

# lst = [] #have an empty list to be appended

# #enter the value for the number of inputs
# n = int(input("enter the number for the list values\n"))

# for i in range(0,n):    #iterate the number of times it is required
#     linoopies = input("enter the names : ") #get the names
#     lst.append(linoopies) #append the names in the empty list
# print (lst) #print the list of names

#-----------------------------------------------------------
#tuples
    #use parenthesis instead of square brackets and the length
    #of the tuple doesn't change
#------------------------------------------------------------

# conditionals:

#name = "Alice"

# name = input("enter Alice to be matched\n\nor any other name to false the condition\n")
# if name == "Alice":     #testing condition of name against the name = Alice
#     print ("Hi, " + name)   #print the message if condition is true
# else:   #run this block if condition is false
#     print ("the condition is not met and the name is " + name)  #print if the condition is not met

#-------------------------------------------------------------
# iteration / loops

zoo_animals = ['Zebra','Rhino','Guraffe','Owl']

#loop to iterate through the list

for animal in zoo_animals:
    print(animal)

vegetables = ["Carrots","Peas","Lettuce","Tomatoes"]    #list of vegetables

for veg in vegetables:  #veg is the value of list items on each repetition & vegetables is the list
    print("i love " + veg)
