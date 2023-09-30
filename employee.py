"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:

    # Commision Value Meaning 
    #
    # 1 - No commission
    # 2 = Bonus commission
    # 3 = Contract commission


    def __init__(self, name,is_salary,wage,hours,commission,contracts,commission_pay):
        self.name = name
        self.is_salary = is_salary
        self.wage = wage
        self.commission = commission
        self.hours = hours
        self.contracts = contracts
        self.commission_pay = commission_pay


    def get_pay(self):

        pay = 0

        if self.is_salary:
            pay += self.wage
        else:
            pay += self.wage * self.hours

        if self.commission == 2:
            pay+= self.commission_pay            
        
        elif self.commission == 3:
            pay+= self.commission_pay * self.contracts

        return pay


            

    def __str__(self):
        string = ""
        if self.is_salary:

            string+= self.name+ " works on a monthly salary of " + str(self.wage)
        else:
            string += self.name + " works on a contract of " + str(self.hours) + " hours at " + str(self.wage) + "/hour"

        if self.commission == 2:
            string +=  " and receives a bonus commission of " + str(self.commission_pay  )     

        elif self.commission == 3:
            string += " and receives a commission for " + str(self.contracts) + " contract(s) at " + str(self.commission_pay) + "/contract"

        string += ". Their total pay is " + str(self.get_pay()) +"."
        return string


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie',True,4000,0,1,0,0)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie',False,25,100,1,0,0)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee',True,3000,0, 3,4,200)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan',False,25,150, 3,3,220)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie',True,2000,0, 2,0,1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel',False,30, 120, 2,0,600 )

print(billie)
print(billie.__str__ == "Billie works on a monthly salary of 4000. Their total pay is 4000.")
print(charlie)
print(charlie.__str__ == "Billie works on a monthly salary of 4000. Their total pay is 4000.")
print(renee)
print(renee.__str__ == "Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract. Their total pay is 3800.")
print(jan)
print(jan.__str__ == "Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract. Their total pay is 4410.")
print(robbie)
print(robbie.__str__ == "Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500. Their total pay is 3500.")
print(ariel)
print(ariel.__str__ == "Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600. Their total pay is 4200.")