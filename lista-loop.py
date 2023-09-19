def ex01():
    nota = float(input("Insira uma nota: "))
    while nota<0.0 or nota>10.0:
        nota = float(input("Insira novamente a nota: "))
    print(f"A nota {nota} é valida!")

def ex02():
    nome = input("Insira seu nome: ")
    while len(nome) < 3:
        nome = input("Insira um nome válido: ")
    

    idade = int(input("Insira sua idade: "))
    while idade < 0 or idade > 150:
        idade = int(input("Insira uma idade válida: "))
    
    salario = float(input("Insira seu salário: "))
    while salario < 0:
        salario = float(input("Insira um salário válido: "))
    
    sexo = input("Insira o sexo (M)asculino/(F)eminino: ")[0].upper()
    while not (sexo == 'M' or sexo == 'F'):
        sexo = input("Insira o sexo (M)asculino/(F)eminino: ")[0].upper()
    
    estadoCivil = input("Insira o estado civil C-S-V-D: ")[0].upper()
    while not (estadoCivil == 'C' or estadoCivil == 'S' or estadoCivil == 'V' or estadoCivil == 'D'):
        estadoCivil = input("Insira um estado civil C-S-V-D válido: ")[0].upper()

def ex03():
    populationA = 80000
    increaseRateA = 0.03

    populationB = 200000
    increaseRateB = 0.015

    year = 0

    while(populationA < populationB):
        populationA += populationA*increaseRateA
        populationB += populationB*increaseRateB
        year += 1

    print(f"A população foi superada em {year} anos.")

def ex04():
    i = 1
    soma = int(input(f"Insira o {i} número: "))
    while i <5:
        i+=1
        soma += int(input(f"Insira o {i} número: "))
    print(f"Soma: {soma}")
    print(f"Média {soma/i}")


def ex05():
    numA = int(input("Insira o primeiro numero do intervalo: "))
    numB = int(input("Insira o segundo número do intervalo: "))

    i = numA
    while i < numB:
        print(i)
        i+=1
    print(numB)

def ex06():
    username = input("Insira o nome de usuário: ")
    password = input("Insira a senha: ")

    while username == password:
        password = input("Insira uma senha diferente do nome de usuário: ")


def ex07():
    numeroDesejado = int(input("Insira o número que deseja saber a tabuada: "))
    i = 1
    while i <= 10:
        print(f"{numeroDesejado * i} \n")
        i+=1

def ex08():
    i = 0
    a = 1
    b = 0
    
    while i < 10:
        c = a + b
        a = b
        b = c
        print(c)
        i += 1

def ex09():
    i = 0
    odd = 0
    even = 0 
    soma = 0
    while i < 10:
        number = int(input(f"Insira o {i+1} número: "))
        if(number % 2 == 0):
            even +=1
        else:
            odd +=1
        soma += number
        i += 1
    print(f"Média: {soma/i}")
    print(f"Impar: {odd}")
    print(f"Par: {even}")

def ex10():
    i = int(input("Insira o fatorial desejado a ser calculado: "))
    factorial = 1
    while i > 0:
        factorial *= i
        i -= 1
    print(factorial)

def ex11():
    givenNumber = int(input("Insira um número: "))
    numberOfDivisions = 0
    i = givenNumber

    while i > 0:
        if(givenNumber%i == 0):
            numberOfDivisions +=1
        i-=1
    if(numberOfDivisions != 2):
        print("NUMERO NÃO É PRIMO!")
    else:
        print("NÚMERO É PRIMO!!!!")
    
def ex11refac():
    givenNumber = int(input("Insira um número: "))
    i = 2

    while i < givenNumber:
        if givenNumber%i == 0:
            print("NÃO É PRIMO")
            break
        i += 1
    if i == givenNumber-1:
        print("É PRIMO")

def ex12():
    i = 1
    n = int(input("Insira a quantidade de notas que deseja calcular a média: "))
    somaNotas = float(input(f"Insira a {i} nota: "))


    while i < n:
        i += 1
        somaNotas += float(input(f"Insira a {i} nota: "))
    
    print(f"Média: {somaNotas/n}")

def ex13():
    