from itertools import combinations
from random import sample

import bill


def input_bill_num():
    """This function asks for the number of bills to generate,
    gives it to bill_num function and prints the outputs"""
    try:
        bills = int(input("How many bills do you want to generate? (type 0 to exit): "))
        res = bill_num(bills)
        if res == 0:
            print("Thanks for playing")
            exit()
        if res == -1:
            print("The max number of bill is 5")
            return input_bill_num()
        else:
            return res
    except:
        print("You must insert a number")
        input_bill_num()


def bill_num(x):
    """This function checks if the input of input_bill_num is valid"""
    assert type(x)==int
    if 0 < x < 6 and type(x)==int:
        return x
    elif x == 0:
        return 0
    else:
        return -1

        
def input_city_choice():
    """This function asks the name of the city to play
    and returns the functions that controls its validity"""
    print(bill.Bill.cities)
    city = input("Please insert the city for this bill, choosing from the above list: ").capitalize()
    if city_choice(city) == -1:
        print("This is an invalid city")
        return input_city_choice()
    else:
        return city


def city_choice(city):
    """This function controls the validity of the city of input_city_choice func"""
    if city in bill.Bill.cities:
        return city
    else:
        return -1


def input_bet_choice():
    """This function asks for the kind of bet to play and prints the outputs"""
    print(bill.Bill.bet_types)
    bet_type = input("Please insert the type of bet for this bill, choosing from the above list: ").capitalize()
    res = bet_choice(bet_type)
    if res == -1:
        print("This is an invalid bet")
        return input_bet_choice()
    else:
        return res


def bet_choice(bet_type):
    """This function controls the validity of the bet choice of input_bet_choice func"""
    if bet_type in bill.Bill.bet_types.keys():
        return bet_type
    else:
        return -1


def input_ticket_number_generation():
    """This function asks how many numbers to bet, prints the outputs
    and call numbers_generation function"""
    try:
        total_numbers_to_bet = int(input("Please insert how many numbers do you want to bet (2-10): "))
        res = ticket_number_generation(total_numbers_to_bet)
        if res == -1:
            print("Invalid number")
            return input_ticket_number_generation()
        else:
            return numbers_generation(total_numbers_to_bet)
    except:
        print("You must insert a number")
        input_ticket_number_generation()


def ticket_number_generation(total_numbers_to_bet):
    """This function controls the total numbers to bet it's between 1 and 10"""
    if 1 < total_numbers_to_bet < 11:
        return 1
    else:
        return -1


def numbers_generation(n):
    """This function extracts n random numbers from the sample 1-90"""
    numbers = sample(range(1,91), n)
    return numbers


def input_bet_amount():
    """This function takes the amount to bet"""
    try:
        amount = int(input("Please insert the amount to bet for this bill: "))
        res = bet_amount(amount)
        if res == 0:
            print("This is an invalid bet")
            return input_bet_amount()
        else:
            return res
    except:
        print("You must insert a number")
        input_bet_amount()

def bet_amount(x):
    """This function checks if the bet amount is valid"""
    if x >=1:
        return x
    else:
        return 0


def combination_calc(n,k):
    """This function calcs the numbers of combinations of n number taken k times"""       
    comb = combinations([x for x in range (1,n+1)], k)
    x = list(comb)
    return len(x)




