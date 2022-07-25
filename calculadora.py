def bemvindo():
    print('''
Sejá bem vindo(a) a Calculadora Simples!
''')

def calculo():

    operation=input('''
Digite a operação desejada: 
+ for addition
- for subtraction
* for multiplication
/ for division
** for power
%  for modulo
''')

    try:
        num1 = eval(input('Digite o primeiro número: '))
        num2 = eval(input('Digite o segundo número: '))        

    except Exception: 
        print('Erro ao executar o calculo')
        return 0

#Adição
    if operation == '+':
        print(f'{num1}+{num2}={num1+num2}')

#Subtração
    elif operation == '-':
        print(f'{num1}-{num2}={num1-num2}')

#Multiplicação 
    elif operation == '*':
        print(f'{num1}*{num2}={num1*num2}')

#Divisão 
    elif operation =='/':
        try:
            print(f'{num1}/{num2}={num1/num2}')
        except ZeroDivisionError:
            print('Não é possível dividir por zero')
        except Exception: 
            print('Erro ao executar a divisão')
       
#Potência 
    elif operation == '**':
        print(f'{num1}**{num2}={num1**num2}')
       
#Porcentagem
    elif operation == '%':
        print(f'{num1}%{num2}={num1%num2}')

    else: 
        print('Você digitou um operador inválido, execute novamente!')

    continuar()

def  continuar():
    calc_continuar = input('''
Deseja calcular novamente? 
Digite S para SIM ou N para NÃO.
''')

    if calc_continuar.upper() == 'S':
        calculo()
    elif calc_continuar.upper() == 'N':
        print('Cálculo encerrado.')
    else:
        continuar()
        
bemvindo()

calculo()

