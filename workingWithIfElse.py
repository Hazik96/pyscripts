#!/usr/bin/env python3.8

#working with if else conditionals 
#we are going to define a dictionary and then match cases

user = {"admin" : True, "active" : False, "name" : "Hazik"}
prefix=""

if user['admin'] and user['active']:
    prefix = "ACTIVE - (ADMIN)"
elif user['admin']:
    prefix = "(ADMIN )"
elif user['active']:
    prefix = "ACTIVE - "

print (prefix + user['name'])