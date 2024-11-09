## objetivos: challenge.md

from getpass import getpass #não mostra a senha do user
import time #para pausar o código (line 23)

print("\033c", end="") #limpa a tela do cmd

print('Olá! Bem vindo a Nutrition\n')
print('Faça seu Registro')

reg_user = input('Seu nome: ')
reg_pass = getpass('Escolha uma senha segura (minimo 8 caracteres): ')

#tamanho da senha

tamanho_senha = len(reg_pass)
tamanho_minimo = 8

if tamanho_senha >= tamanho_minimo:
        print('Sua senha foi aceita, se lembre dela! Aguarde alguns segundos.\n')
else:
        print('Sua senha não atingiu os caractéres mínimos necessários, rode o código novamente!\n')
        time.sleep(3) #pausa por tempo definido em segundos
        exit()

time.sleep(3)

##confirmação de senha
def senhaconfirmacao():
    conf_senha = getpass('Confirme a sua senha antes de entrar novamente: ')
    if conf_senha == reg_pass:
        print('Sucesso!')
    else:
       print('incorreto, tente novamente')
       time.sleep(3)
       return senhaconfirmacao()

senhaconfirmacao()
time.sleep(3)

##Obter informações: altura (cm), idade, peso(kg) e nível de atividade corporal.
print("\033c", end="")

print(f'Agora {reg_user}, coletaremos suas informações\n')

altura = float(input('Coloque sua altura em metros e com . (ex: 1.70): '))
peso = int(input('Coloque seu peso em kg: '))
idade = int(input('Coloque sua idade: '))
sexo = input('Coloque seu sexo, masc ou fem: ')

time.sleep(2)
if altura >= 272 or peso >= 635 or idade >= 122:
     print('Dados incongruentes.')
else:
    print("\033c", end="")
    print('Observe a seguinte tabela de Nível de Atividade Corporal (NAC):\n')

    list_nac = print('1- Sedentário (nenhum ou pouquíssimo exercício)\n'
                      '2- Levemente ativo (prática de exercícios 1 a 3 vezes/semana)\n'
                      '3- Moderadamente ativo (exercícios durante 3 a 5 vezes/semana)\n'
                      '4- Muito ativo (exercícios feitos em 5 ou 6 vezes/semana)\n'
                      '5- Extremamente ativo (prática de exercícios diários intensos)\n')
    
    op_nac = int(input('Selecione uma opção que corresponde a sua atividade física (1-5): '))

time.sleep(2)



##calculadora IMC
def calc_imc():
        imc = (peso / (altura * altura))
        print(f'\nSeu IMC é igual a: {imc:.2f}')

        if imc < 18.5:
            print('Você está abaixo do peso.')
        elif imc >= 18.5 and imc <= 24.9:
                print('Você está no peso ideal!')
        elif imc >= 25 and imc <= 29.9:
                print('Você está levemente acima do peso ideal.')
        elif imc >= 30 and imc <= 34.9:
                print('Obesidade Nível 1. Cuidado')
        elif imc >= 35 and imc <= 39.9:
                print('Obesidade Nível 2. Cuidado')
        elif imc >= 40:
                print('Obesidade Nível 3. Cuidado')
        else:
            print('Não foi possível calcular seu IMC, verifique as informações.')
            exit()

##calculadora de calorias diarias
def calc_nac():

        ##calculo calorias diárias masculino
    if sexo == 'masc' or sexo == 'Masc' or sexo =='MASC':
        geb_masc = ((13.75*peso) + (5*altura*100) - (6.76*idade) + 66.5)
        if op_nac == 1:
                ccd_masc1 = ((geb_masc)*1.2)
                print(f'O tanto de calorias diárias que você deve consumir é {ccd_masc1:.2f} kcal.')
        elif op_nac == 2:
                ccd_masc2 = ((geb_masc)*1.375)
                print(f'O tanto de calorias diárias que você deve consumir é {ccd_masc2:.2f} kcal.')
        elif op_nac == 3:
                ccd_masc3 = ((geb_masc)*1.55)
                print(f'O tanto de calorias diárias que você deve consumir é {ccd_masc3:.2f} kcal.')
        elif op_nac == 4:
                ccd_masc4 = ((geb_masc)*1.725)
                print(f'O tanto de calorias diárias que você deve consumir é {ccd_masc4:.2f} kcal.')
        elif op_nac == 5:
                ccd_masc5 = ((geb_masc)*1.9)
                print(f'O tanto de calorias diárias que você deve consumir é {ccd_masc5:.2f} kcal')
        else:
                print('Sua opção não existe! Verifique as informações.')
            
        ##calculo sexo feminino
    elif sexo == 'fem' or sexo == 'Fem' or sexo =='FEM':
        geb_fem = ((9.56*peso) + (1.85*(altura*100)) - (4.68*idade) + 665)
        if op_nac == 1:
                ccd_fem1 = ((geb_fem)*1.2)
                print(f'O tanto de calorias diárias que você deve consumir é {ccd_fem1:.2f} kcal')
        elif op_nac == 2:
                ccd_fem2 = ((geb_fem)*1.375)
                print(f'O tanto de calorias diárias que você deve consumir é {ccd_fem2:.2f} kcal')
        elif op_nac == 3:
                ccd_fem3 = ((geb_fem)*1.55)
                print(f'O tanto de calorias diárias que você deve consumir é {ccd_fem3:.2f} kcal')
        elif op_nac == 4:
                ccd_fem4 = ((geb_fem)*1.725)
                print(f'O tanto de calorias diárias que você deve consumir é {ccd_fem4:.2f} kcal')
        elif op_nac == 5:
                ccd_fem5 = ((geb_fem)*1.9)
                print(f'O tanto de calorias diárias que você deve consumir é {ccd_fem5:.2f} kcal')
        else:
                print('Sua opção de NAC não existe! Verifique as informações.')
    else:
            print('As suas opções de sexo ou nível de atividade estão incorretas.')
            exit()


##operar a calculadora

def return_calc():
        print("\033c", end="")
        ret_calc = int(input(f'O que deseja {reg_user}? [1]Retornar a Calculadora ou [2]Sair: '))
        if ret_calc == 1:
                return calculadora()
        elif ret_calc == 2:
                print('Obrigado por utilizar nosso programa!')
                time.sleep(5)
                exit()
        else:
                print('Sua opção não é válida, tente novamente')
                time.sleep(5)
                return return_calc()

def calculadora():
        print("\033c", end="")
        op_calc = int(input(f'O que desejaria calcular {reg_user}? [1]IMC ou [2]Kcal Dária?: '))

        if op_calc == 1:
                calc_imc()
                time.sleep(6)
                return return_calc()
        elif op_calc == 2:
                calc_nac()
                time.sleep(6)
                return return_calc()
        else:
                print('Sua operção não existe')
                exit()

calculadora()
