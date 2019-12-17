#!/usr/bin/env python3.8

#in this script we will iterate over the lists
#for this purpose we will have multiple user dictionaries
#and we will will store the link to those dictionaries -
#into a list ...

user1 = {"admin" : True, "active" : True, "name" : "Hazik"}
user2 = {"admin" : True, "active" : False, "name" : "Izzy"}
user3 = {"admin" : False, "active" : True, "name" : "Hassan"}

users = [user1, user2, user3]
prefix = ""
count = 0

for items in users:
    if items['admin'] and items['active']:
        prefix = "ACTIVE - (ADMIN) "
    elif items['active']:
        prefix = "ACTIVE - "
    elif items['admin']:
        prefix = "(ADMIN )"
    #counter to print the number of lines - will run the number
    #of times the loop iterates
    count+=1
    print (str(count) + prefix + items['name'])