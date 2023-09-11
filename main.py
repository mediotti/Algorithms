import math

def ex1():
    a = input("Primeiro valor: ")
    b = input("Segundo valor: ")

    maior = a if a > b else b

    print(f"O maior valor é {maior}")

def ex2():
    ano = int(input("Ano de nascimento: "))
    if(2023-ano>=16):
        print("Pode votar")
    else:
        print("Não pode votar")

def ex3():
    senha = input("Insira a senha: ")

    if (senha == "1234"):
        print("ACESSO PERMITIDO")
    else:
        print("ACESSO NEGADO!")

def ex4():
    number_of_apples = int(input("Insert the quantity of apples acquired: "))

    apple_price = 0.30 if number_of_apples<12 else 0.25

    print(f"Result: {number_of_apples * apple_price}")

def ex5():
    a = int(input("Insert the first number: "))
    b = int(input("Insert the second number: "))
    c = int(input("Insert the third number: "))

    numbers_array = [a, b, c]

    n = len(numbers_array)

    for i in range(n):
        all_sorted = True
        for j in range(n-i-1):
            if numbers_array[j] > numbers_array[j+1]:
                numbers_array[j], numbers_array[j+1] = numbers_array[j+1], numbers_array[j]
                all_sorted = False
        if all_sorted:
            break

    print(numbers_array)

def ex6():
    height = float(input("Insert your height in meters: "))
    gender = int(input("Insert your gender (1 - Women | 2 - Men): "))

    if gender == 1 or gender == 2:
        ideal_weight = int(62.1*height-44.7 if gender == 1 else 72.7*height-58)
        print(f"Your ideal weight: {ideal_weight} kg")
    else:
        print("Wrong gender option!")

def ex7():
    sides = int(input("Insert the number of sides from a desired regular polygon: "))
    size = float(input("Insert the size of those sides: "))

    if(sides == 3):
        area, shape = float(((math.pow(sides, 3))*math.sqrt(3)/4)), "triangle"
    elif(sides == 4):
        area, shape = float(size*size), "rectangle"
    elif(sides == 5):
        area, shape = 0, "pentagon"

    print(f"The shape is a {shape} and it's area equals to: {area}")

def ex8():
    sides = int(input("Insert the number of sides from a desired regular polygon: "))
    size = float(input("Insert the size of those sides: "))

    if(sides < 3):
        print("Not a polygon")
        return
    elif(sides == 3):
        area, shape = float(((math.pow(sides, 3))*math.sqrt(3)/4)), "triangle"
    elif(sides == 4):
        area, shape = float(size*size), "rectangle"
    elif(sides == 5):
        print("Pentagon")
        return
    elif(sides > 5):
        print("Unindentified polygon")
        return
    print(f"The shape is a {shape} and it's area equals to: {area}")


def ex9():
    a = int(input("Insert the first number: "))
    b = int(input("Insert the second number: "))
    c = int(input("Insert the third number: "))

    numbers_array = [a, b, c]
    n = len(numbers_array)

    for i in range(n):
        all_sorted = True
        for j in range(n-i-1):
            if numbers_array[j] < numbers_array[j+1]:
                numbers_array[j], numbers_array[j+1] = numbers_array[j+1], numbers_array[j]
                all_sorted = False
        if all_sorted:
            break

    print(f"The highest number is: {numbers_array[0]}")

def salaryIRPF():
    salary = float(input("Insert your salary: "))
    if(salary<=2112.0):
        print("Isento")
    elif(salary>2112.0 and salary<=2826.65):
        print("Alíquota: 7,5%")
    elif(salary>2826.65 and salary<= 3751.05):
        print("Alíquota: 15%")
    elif(salary>3751.05 and salary <= 4664.68):
        print("Alíquota: 22,5%")
    elif(salary>4664.68):
        print("Alíquota: 27,5%")

def ex10():
    a = int(input("Insert the first side size: "))
    b = int(input("Insert the second side size: "))
    c = int(input("Insert the third side size: "))

    numbers_array = [a, b, c]
    equal_sides = 1
    n = 1

    while n < len(numbers_array):
        if numbers_array[n-1] == numbers_array[n]:
            equal_sides += 1
        n += 1

    if(equal_sides == 3):
        print("Equilátero")
    elif(equal_sides == 2):
        print("Isósceles")
    elif(equal_sides == 1):
        print("Escaleno")

def ex11():
    a = int(input("Insert the first angle: "))
    b = int(input("Insert the second angle: "))
    c = int(input("Insert the third angle: "))

    angles_array = [a, b, c]
    n = 1
    triangle_type = ""

    while n <= len(angles_array):
        if angles_array[n-1] == 90:
            triangle_type = "Retangulo"
            break
        triangle_type = "Obtusangulo" if angles_array[n-1] > 90 else "Acutangulo"
        n += 1

    print(triangle_type)

def ex12():
    # Se um carro estiver entre 80 e 100 km/h, cobre R$5,00 para cada km/h acima de 80km/h
    # //                    entre 100 e 120 -> R$10,00
    # //                    acima de 120 -> R$20,00

    velocidade = int(input("Insira a velocidade do veículo: "))
    if(velocidade > 80 and velocidade < 100):
        excedente = velocidade - 80
        multa=excedente*5
    elif(velocidade < 120):
        excedente = velocidade - 100
        multa= ((100-80)*5) + excedente*10
    else:
        excedente = velocidade - 120
        multa = ((100-80)*5) + ((120-100)*10) + excedente*20

    if(multa <= 0):
        print("Não há multa")
    else:
        print(f"Sua multa é {multa}")

def salario():
    isEmployee = input("Você trabalha? Insira a sua resposta(s/n): ").lower()

    while isEmployee[0] != 'n' and isEmployee[0] != 's':
        isEmployee = input("Insira uma opção valida: ").lower()
        
    salario = float(input("Insira o seu salário: "))
    if salario <= 2112:
        aliquota = 0
    elif salario <=2826.65:
        aliquota = 7.5
    elif salario <= 3751.05:
        aliquota = 15
    elif salario <= 4664.68:
        aliquota = 22.5
    elif salario >= 4664.68:
        aliquota = 27.5
    print(f"Seu salário será {salario-((aliquota/100)*salario)}")

def senha():
    senha = 'senhaforte'
    tentativaSenha = input("Insira sua senha: ")
    tentativaNumero = 3

    while tentativaSenha != senha and tentativaNumero > 0 :
        tentativaSenha = input("Senha errada. Insira novamente sua senha: ")
        tentativaNumero -= 1
    if(tentativaSenha == senha):
        print("Acesso liberado")
    else:
        print("TENTATIVAS ESGOTADAS")

def calculadora():
    option = input("Deseja acessar a calculadora? (s/n): ").lower()
    while option[0] != 's':
        if option[0] == 'n':
            return
        option = input('Opção invalida, insira s ou n: ').lower()
    a = float(input("Insira o primeiro valor: "))
    b = float(input("Insira o segundo valor: "))

    operation = input("Insira a operação desejada (+ | - | / | *): ")
    while operation != '+' and operation != '-' and operation != '/' and operation != '*':
        operation = input('Opção inválida, insira uma operação (+ | - | / | *): ')
    
    if operation == '+':
        print(f"Resposta: {a + b}")
    elif operation == '-':
        print(f"Resposta: {a - b}")
    elif operation == '*':
        print(f"Resposta: {a * b}")
    elif operation == '/':
        print(f"Resposta: {a / b}")
    
calculadora()