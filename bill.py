class Bill:

    cities = ["Bari", "Cagliari", "Firenze", "Genova", "Milano", "Napoli", "Palermo", "Roma", "Torino", "Venezia", "Tutte"]
    bet_types = {"Ambata":1, "Ambo":2, "Terno":3, "Quaterna":4, "Cinquina":5}

    def __init__(self, bill_num:int, city:str, bet_type:str, num_list:list, bet_amount:int):
        self.bill_num = bill_num
        self.city = city
        self.bet_type = bet_type
        self.num_list = num_list
        self.bet_amount = bet_amount


    def __str__(self):

        line = f"+{'-'*10}+{'-'*10}+{'-'*10}+{'-'*45}+{'-'*10}+\n"
        
        header = f"|{('TICKET N').center(10)}|{('CITY').center(10)}|{('BET').center(10)}|{('NUMBERS').center(45)}|{('$ AMOUNT').center(10)}|\n"
        
        ticket = "|"+f"{self.bill_num}".center(10) + "|" + f"{self.city}".center(10) + "|" + f"{self.bet_type}".center(10) + "|" + f"{self.num_list}".center(45) + "|" + f"{self.bet_amount}".center(10) + "|\n"
       
        return line + header + line + ticket + line
        
