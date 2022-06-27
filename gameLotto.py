from bill import Bill
import support_function

class Lotto:

    def __init__(self):
        self.extracted_numbers = dict()    
        self.ticket_list = []

    def extraction(self):
        """This function generates the extraction,
        5 numbers for each city except for 'Tutte' """
        cities = Bill.cities
        for city in cities[:-1]:
            self.extracted_numbers[city] = support_function.numbers_generation(5)
        return self.extracted_numbers

        
    def ticket_creation(self):
        """This funcion generates a list of n Tickets,
        each one is a Bill object with an index i, city, bet type and numbers to bet"""
        n = support_function.input_bill_num()
        for i in range(1,n+1):
            city = support_function.input_city_choice()
            bet_type = support_function.input_bet_choice()
            numbers_to_bet = support_function.input_ticket_number_generation()
            bet_amount = support_function.input_bet_amount()
            ticket = Bill(i, city, bet_type, numbers_to_bet, bet_amount)
            self.ticket_list.append(ticket)
        return self.ticket_list


    def check_win(self):
        """This function cycles on every ticket in the ticket list
        and checks if any of them is winner. It returns a dictionary:
        key: winning_ticket, value: number of winning combination"""
        winning_bills = dict()
        for ticket in self.ticket_list:
            if ticket.city != "Tutte": #check the tickets with only one city betted
                winning_numbers = []
                #check each number in the tickets num list:
                #if it was extracted in the same city extraction, append it to a winning number list                  
                for number in ticket.num_list:
                    if number in self.extracted_numbers[ticket.city]:
                        winning_numbers.append(number)
                #the minimum quantity of numbers for win depends on the bet type choosed
                #see the bet type choosed, search for this key on the bet_types attribute dict and take this value 
                num_for_win = ticket.bet_types[ticket.bet_type]
                winning_numbers_quantity = len(winning_numbers)
                if winning_numbers_quantity >= num_for_win:
                    #counting the number of combination of n winning number taken k times
                    winning_combination = support_function.combination_calc(winning_numbers_quantity,num_for_win)
                    winning_bills[ticket] = winning_combination
                
            else: #if the ticket city is "Tutte", we have to check every city of the extraction
                for value in self.extracted_numbers.values():
                    winning_numbers = []
                    for number in ticket.num_list:
                        if number in value:
                            winning_numbers.append(number)
                    num_for_win = ticket.bet_types[ticket.bet_type]
                    if len(winning_numbers) >= num_for_win:
                        winning_combination = support_function.combination_calc(winning_numbers_quantity,num_for_win)
                        winning_bills[ticket] = winning_combination
        return winning_bills
    

    def win_amount_calc(self):
        """This function gives a dictionary of winning tickets with both total and net amount,
        based on the win_table multiplication odds
        Key: winning_tickets, value: [total_win, net_win] """
        #table for multiplication odds, based on bet type and quantity of numbers betted
        win_table = {"Ambata": [11.23, 5.61, 3.74, 2.8, 2.24, 1.87, 1.6, 1.4, 1.24, 1.12],
             "Ambo": [0, 250, 83.33, 41.66, 25, 16.66, 11.9, 8.92, 6.94, 5.55],
             "Terno":[0, 0, 4500, 1125, 450, 225, 128.57, 80.35, 53.57, 37.5],
             "Quaterna":[0, 0, 0, 120000, 24000, 8000, 3428.57, 1714.28, 952.38, 571.42],
             "Cinquina": [0, 0, 0, 0, 6000000, 1000000, 285714.28, 107142.85, 47619.04, 23809.52]}
        winning_bills = self.check_win() #dictionary of winning ticket with amount of winning combination
        winning_bills_with_amount = dict()
        tax_rate = 0.08
        win_tax_cap = 500

        if len(winning_bills) > 0: #if there is any winning ticket
            for ticket in winning_bills.keys():
                #check how many numbers you have betted for the ticket and take the corrispondent odd from win table
                quantity_of_numbers_betted = len(ticket.num_list) 
                multiplication_odd = win_table[ticket.bet_type][quantity_of_numbers_betted-1]
                #calcs the total and net amount
                total_win = round(multiplication_odd * ticket.bet_amount * winning_bills[ticket], 2)
                net_win = round(total_win - (total_win * tax_rate),2)
                if total_win > win_tax_cap:
                    winning_bills_with_amount[ticket] = [total_win, net_win]
                else:
                    winning_bills_with_amount[ticket] = [total_win, total_win]
            return winning_bills_with_amount
        else:
            return 0


    def check_win_output(self):
        """This function prints the winner ticket, if there is any, and the amount won"""
        winning_bills_with_amount = self.win_amount_calc()
        if winning_bills_with_amount == 0:
            print("Sorry, you lost!")
        else:
            for ticket, amount in winning_bills_with_amount.items():
                print(f"Congrats! You won a total amount of: {amount[0]} $ (net: {amount[1]} $) with this ticket\n")
                print(ticket)

    
    def extracted_numbers_print(self):
        for k,v in self.extracted_numbers.items():
            print(k,v)
