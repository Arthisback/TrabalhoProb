import math 
prob = input("1 para Probabilidade Binomial Individual e 2 para Probabilidade Binomial Acumulada")
if prob==1:
    n = input(" Digite a quantidade de casos totais:")
    x = input(" Digite a quantidade de casos favoraveis")
    p = input(" Digite a porcentagem de casos favoraveis")
    p2= p/100
    q= 100-p2
    qexp= n-x
    combination= math.factorial(n) // (math.factorial(n - x) * math.factorial(x))
    result= combination*pow(p2,x)*pow(q,qexp)
    print("A probabilidade é de:  ",result)


