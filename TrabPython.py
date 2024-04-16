import math 

def main():
    while True:
        prob = input("""1 para Probabilidade Binomial Individual e 2 para Probabilidade Binomial Acumulada: 
Digite 0 para sair\n""")
        
        
        if prob == '0':
            break

        if prob == '1':
            n = int(input("Digite a quantidade de casos totais(n) : "))
            x = int(input("Digite a quantidade de casos favoráveis(x): "))
            p = float(input("Digite a porcentagem de casos favoráveis(p): "))
            p2 = p / 100
            q = 1 - p2
            qexp = n - x
            combination = math.factorial(n) // (math.factorial(n - x) * math.factorial(x))
            result = (combination * pow(p2, x) * pow(q, qexp))*100
            print("A probabilidade é de: {:.2f}".format(result))
            print("\n")

        elif prob == '2':
            n = int(input("Digite a quantidade de casos totais(n): "))
            x_min = int(input("Digite o limite inferior de casos favoráveis(X deve ser no minimo igual ou maior este numero): "))
            x_max = int(input("Digite o limite superior de casos favoráveis(X deve ser no maximo igual ou menor a este numero): "))
            p = float(input("Digite a porcentagem de casos favoráveis(p): "))
            p2 = p / 100
            q = 1 - p2
            cumulative_prob = 0
            for i in range(x_min, x_max + 1):
                combination = math.factorial(n) // (math.factorial(n - i) * math.factorial(i))
                result = (combination * pow(p2, i) * pow(q, n - i))*100
                cumulative_prob += result
            print("A probabilidade acumulada para", i, "casos favoráveis é de: {:.2f}".format(cumulative_prob))
            print("\n")
        else:
            print("Opção inválida.")



if __name__ == '__main__':
    main()
