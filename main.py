import gameLotto
import bill

#simulation with random tickets generation
game = gameLotto.Lotto()
game.ticket_list = game.ticket_creation()
for i in game.ticket_list:
    print(i)
game.extraction()
game.extracted_numbers_print()
print("")
game.check_win_output()


#simulation with selfmade tickets
'''
game = gameLotto.Lotto()
game.extraction()
print(game.extracted_numbers)
print("")
game.ticket_list = [bill.Bill(1, "Roma", "Ambata",[x for x in range(1,10)], 1),
                    bill.Bill(2, "Tutte", "Ambo",[x for x in range(1,10)],500)]

game.check_win_output()
'''