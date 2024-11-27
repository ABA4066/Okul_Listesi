okulliste=dict()
print("Çıkmak için ad ve nota \"q\" yazın")
while True:
    x=input("Öğrenci adı girin\n")
    y=input("Öğrencinin notunu girin\n")
    if x=="q" and y=="q":
        break
    okulliste[x] = y
print(okulliste,"\n")

m=int(input("Öğrencinin notunu bulmak istiyorsanız 1'e basın. Çıkmak için \"q\" yazın.\n"))
if m==1:
    while True:
        n=input("Öğrenci Adı girin\n")
        if n == "q":
            break
        print(okulliste[n])