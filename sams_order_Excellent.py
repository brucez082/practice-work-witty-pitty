#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Bruce Zhang
#
# Created:     30/08/2021
# Copyright:   (c) Bruce Zhang 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#Allows the program to create a date and timestamp
import datetime
today = datetime.datetime.now()

#Create a subroutine for bread type

def print_lists(list, item):
    print("We have the following {}.".format(item))
    count = 0
    while count < len(list):
        print(count, " ", list[count])
        count += 1
    choice = item_check(list)
    choice = list[choice]
    return choice

def salads():
    saladlist = ["Cucumber salad", "Lettuce salad", "Tomatoes salad", "Red onion salad"]
    saladcount = 0
    print("We have the following salad, you can have as many as you want: ")
    while saladcount < len(saladlist):
        print(saladcount, " ", saladlist[saladcount])
        saladcount += 1
        salad_selected_list = []
    while True:
        print("What salad do you want, enter a number")
        saladtype = item_check(saladlist)
        saladwanted = salad_selected_list.append(saladlist[saladtype])
        quit = str(input("You have selected: {} Type Y if that's all you want".format(salad_selected_list)))
        if quit == "y":
            break
    return salad_selected_list

def item_check(item_list):
    while True:
        try:
            item_amount = len(item_list)
            item_type = int(input("Please enter your selected item type 0 - {}.".format(item_amount - 1)))
            if item_type >= 0 and item_type < len(item_list):
                break
            else:
                print("ERROR, please enter a number from 0 - .".len(item_list - 1))
        except:
            print("ERROR, please enter a number instead of text")
    return item_type

def output_order():
    breadorder = []    #empty list
    #this adds the person's entire order details to the list
    breadorder.append(first_name)
    breadorder.append(last_name)
    breadorder.append(total_name)
    breadorder.append(cellphone)
    breadorder.append(bread_selected)
    breadorder.append(meat_selected)
    breadorder.append(cheese_selected)
    breadorder.append(salad_selected)
    breadorder.append(dressing_selected)
    breadorder.append(today)
    outputFile = open("sams_order.txt", "a")  #opens the text file
    print("********** Order for {} - {} *******.".format(first_name, last_name, cellphone))
    outputFile.write("************ Order for {} - {} *******".format(first_name, last_name, cellphone))
    for order in breadorder:
        print(order)
        outputFile.write("{}\n".format(order))
    outputFile.write("*********** End of Order: {}. *******".format(today))
    print("*********** End of Order: {}. *******".format(today))   #test print
    outputFile.close() #closes the text file

def force_name(message, lower, upper):
    while True:
        name = str(input(message))
        if len(name) >= lower and len(name) <= upper and name.isalpha():
            break
        else:
            print("ERROR, please enter a valid name. And it has to be between {} to {} letter.".format(lower, upper))
    return name

def force_cellphone(message, lower, upper):
    while True:
        try:
            cellphone = int(input(message))
            if cellphone >= lower and cellphone <= upper:
                break
            else:
                print("ERROR, please enter a valid cellphone number between {} - {}.".format(lower, upper))
        except:
            print("ERROR, please enter a valid cellphone number instead of texts")
    return cellphone


#main program that makes calls to the other functions
first_name = force_name("Please enter in your fist name: ",2,30).title()
last_name = force_name("{}, please enter in your last name: ".format(first_name),2,30).title()
total_name = first_name + " " + last_name
cellphone = force_cellphone("{}, please enter in your cellphone number: ".format(total_name),0000000000,9999999999999)
breadlist = ["White", "Brown", "Italian", "Granary"]
meatlist = ["Buffalo chicken", "Carved Turkey", "The ultimate meatball", "The ultimate chicken & pepperoni sub"]
cheeselist = ["American cheese", "Swiss cheese", "Cheddar cheese", "Mozzarella cheese"]
dressinglist = ["Barbecue", "Creamy italian", "Honey mustard", "Buffalo"]
bread_selected = print_lists(breadlist, "breads")
meat_selected = print_lists(meatlist, "meats")
cheese_selected = print_lists(cheeselist, "cheeses")
salad_selected = salads()
dressing_selected = print_lists(dressinglist, "dressings")
output_order()


