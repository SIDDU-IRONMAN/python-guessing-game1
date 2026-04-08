import datetime
print(" ----WELCOME TO OUR LAVADALO  ATM ------ ")

print(" PLEASE INSERT YOUR CARD ")


print(" 1.BALANCE CHECK ")
print(" 2.DEPOSIT MONEY")
print(" 3.WHITHDRA MONEY")
print(" 4. SSTATEMENT CHECK")
print(" 5.EXIT ")

bal = 10000
choice = int(input(" enter a your option : "))
if choice == 1:
    
    print("the current balance is " , bal)
    
elif choice == 2:
 deposited = int(input("DEPOSIT YOUR MONEY : ")) 
 print("THE DIPOSITED MONEY IS SCUCESS  AND ", deposited  and "your current balance is $",bal + deposited)
 
elif choice == 3:
    withdra = int(input(" withdra "))
    print("YOUR MONEY SCUCESSFULLY WITHDRAL ", withdra and "AND YOUR CURRENT BALANCE IS $",bal - withdra)
elif choice == 4:
    now = datetime.datetime.now()
    dt_string = now.strftime("%d/%m/%y")
    print("YOUR STATEMENT   and  balance is " , bal,dt_string)

elif choice == 5:
    print("EXITED")




