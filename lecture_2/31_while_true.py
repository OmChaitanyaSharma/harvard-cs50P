#in while true loop continue is considered at true and false is break is considered as false


while True:
    n=int(input("whats the number of times cat want to meow : "))
    if n<=0:
        continue
    else :
        break

for i in range(n):
    print("meow meow meow !")
