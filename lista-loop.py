def ex01():
    nota = float(input("Insira uma nota: "))
    while nota<0.0 or nota>10.0:
        nota = float(input("Insira novamente a nota: "))
    print(f"A nota {nota} é valida!")

def ex02():
    nome = input("Insira seu nome: ")
    while len(nome) < 3:
        nome = input("Insira um nome válido(Acima de 1 caractere): ")

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
    compensation = float(input("Insira o salário referente a 1995: "))
    increaseRate = 1.5
    year = 1995

    while year < 2023:
        year+=1
        compensation+=compensation*increaseRate
        increaseRate *=2
    print(compensation)

def ex14():
    inputNumber = int(input("Insira um número: "))
    firstLevel = 0
    secondLevel = 0
    thirdLevel = 0
    fourthLevel = 0

    while inputNumber >= 0:
        if inputNumber > 0 and inputNumber < 25:
            firstLevel +=1
        elif inputNumber < 50:
            secondLevel +=1
        elif inputNumber < 75:
            thirdLevel +=1
        elif inputNumber <100:
            fourthLevel +=1
        inputNumber = int(input("Insira outro número: "))
    print(f"[0-25] = {firstLevel} | [26-50] = {secondLevel} | [51-75] = {thirdLevel} | [76-100] = {fourthLevel}. ")

def ex15():
    print("1 - José")
    votosJose = 0
    print("2 - João")
    votosJoao = 0
    print("3 - Jéssica")
    votosJessica = 0
    print("4 - Jandira")
    votosJandira = 0
    print("5 - NULO")
    votosNulo = 0
    print("6 - EM BRANCO")
    votosEmBranco = 0

    voto = int(input("Insira o código do candidato que deseja votar: "))
    votosTotal = 1

    while voto != 0:
        if voto < 0 and voto > 6:
            voto = (int(input("Voto inválido, insira um valor válido ou 0 para sair do programa: ")))
            votosTotal +=1
        elif voto == 1:
            votosJose += 1
        elif voto == 2:
            votosJoao += 1
        elif voto == 3:
            votosJessica += 1
        elif voto == 4:
            votosJandira += 1
        elif voto == 5:
            votosNulo += 1
        elif voto == 6:
            votosEmBranco += 1
        voto = int(input("Insira o código do candidato que deseja votar: "))
        votosTotal +=1

    print(f"Votos do João: {votosJoao} votos")
    print(f"Votos do José: {votosJose} votos")
    print(f"Votos da Jessica: {votosJessica} votos")
    print(f"Votos da Jandira: {votosJandira} votos")
    print(f"Votos em Branco: {votosEmBranco} votos")
    print(f"Votos Nulos: {votosNulo} votos")

    print(f"Percentagem de votos nulos sobre o total de votos: {(votosNulo/votosTotal)*100:.2f}%")
    print(f"A percentagem de votos em branco sobre o total de votos: {(votosEmBranco/votosTotal)*100:.2f}%")
