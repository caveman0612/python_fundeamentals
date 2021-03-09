# while True:
#     try:
#         num = int(input("input num"))
#         divisor = int(input("input divisor"))
#         print(num/divisor)
#     except Exception as e:
#         print(f"{e} has occurred")

class bankAccount:
    def __init__(self, name, balance = 0.0):
        self.name = name
        self.balance = balance
        try :
            f = open(f"{self.name}_log.txt", "r")
        except FileNotFoundError:
            self.log("account created")
        finally:
            f.close()


    def getBalance(self):
        self.log("Balance checked at " + str(self.balance))
        return self.balance

    def setBalance(self, newBalance):
        self.log("Balance changed to " + str(newBalance))
        self.balance = round(float(newBalance), 2)

    def log(self, message):
        with open(f"{self.name}_log.txt", "a") as file:
            file.write(message + "\n")

kyle = bankAccount("kyle")
print(kyle.balance)
kyle.setBalance(100.3)
print(kyle.balance)

