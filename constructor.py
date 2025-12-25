class Lamborghini:
    def __init__(self,color,model,payment):
        self.color = color
        self.model = model
        self.payment = payment

lambo1 = Lamborghini(
    input("Enter Color : "),
    input("Enter model : "),
    input("Enter Payment : ")
                    )

lambo2 = Lamborghini(
    input("Enter Color : "),
    input("Enter model : "),
    input("Enter Payment : ")
                    )

print("Data for first order :\n")
print(lambo1.color ,end="\n")
print(lambo1.model ,end="\n")
print(lambo1.payment ,end="\n")

print("Data for second order :\n")
print(lambo2.color ,end="\n")
print(lambo2.model ,end="\n")
print(lambo2.payment ,end="\n")


