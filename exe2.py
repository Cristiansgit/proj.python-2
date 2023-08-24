print('Bem Vindo a Sorveteria do Cristian')           
print(44*'-'+'CARDÁPIO'+ 44*'-')                                   
print('|CÓDIGO   |     DESCRIÇÃO        | TAMANHO P(500ML)  | TAMANHO M (1000ML)  | TAMANHO G(2000ML) |')
print('|'+94*'-'+'|')
print('| TR      | SABORES TRADICIONAIS |    R$ 6.00        |    R$ 10.00         |    R$ 18.00       |')
print('| ES      | SABORES ESPECIAIS    |    R$ 7.00        |    R$ 12.00         |    R$ 21.00       |')
print('| PR      | SABORES PREMIUM      |    R$ 8.00        |    R$ 14.00         |    R$ 24.00       |')
print('|'+94*'_'+'|')

acumulador = 0
while True :
  codigo = input('Digite o código desejado (TR/ES/PR) : ')
  codigo = codigo.upper()
  if codigo != 'TR' and codigo != 'ES' and codigo != 'PR':
    print('           OPÇÃO DE CÓDIGO INVALIDA')
    continue  # em caso de tamanho invalido volta para o começo do while !

  tamanho = input('Digite o tamanho desejado (P/M/G) : ')
  tamanho = tamanho.upper()
  if  tamanho != 'P' and  tamanho != 'M' and tamanho != 'G':
    print('           OPÇÃO DE TAMANHO INVALIDA')
    continue # em caso de tamanho invalido volta para o começo do while !

  if codigo == 'TR'  and tamanho == 'P':
    print('Você escolheu os sabores tradicionais tamanho: P')
    print(50*'-')
    acumulador = acumulador + 6.00 #pega o valor do acumulador e soma com: 6.00

  elif  codigo == 'TR' and tamanho == 'M':
    print('Você escolheu os sabores tradicionais tamanho: M ')
    print(50*'-')
    acumulador = acumulador + 10.00 #pega o valor do acumulador e soma com: 10.00

  elif  codigo == 'TR' and tamanho == 'G':
    print('Você escolheu os sabores tradicionais tamanho: G ')
    print(50*'-')
    acumulador = acumulador + 18.00 #pega o valor do acumulador e soma com: 18.00

  elif  codigo == 'ES' and tamanho == 'P':
    print('Você escolheu os sabores especial tamanho: P ')
    print(50*'-')
    acumulador = acumulador + 7.00 #pega o valor do acumulador e soma com: 7.00

  elif  codigo == 'ES' and tamanho == 'M':
    print('Você escolheu os sabores especial tamanho: M ')
    print(50*'-')
    acumulador = acumulador + 12.00 #pega o valor do acumulador e soma com: 12.00

  elif  codigo == 'ES' and tamanho == 'G':
    print('Você escolheu os sabores especial tamanho: G ')
    print(50*'-')
    acumulador = acumulador + 21.00 #pega o valor do acumulador e soma com: 21.00

  elif  codigo == 'PR' and tamanho == 'P':
    print('Você escolheu os sabores premium tamanho: P ')
    print(50*'-')
    acumulador = acumulador + 8.00 #pega o valor do acumulador e soma com: 8.00

  elif  codigo == 'PR' and tamanho == 'M':
    print('Você escolheu os sabores premium tamanho: M ')
    print(50*'-')
    acumulador = acumulador + 14.00  #pega o valor do acumulador e soma com: 14.00

  elif  codigo == 'PR' and tamanho == 'G':
    print('Você escolheu os sabores premium tamanho: G ')
    print(50*'-')
    acumulador = acumulador + 24.00 #pega o valor do acumulador e soma com: 24.00

  pedir_novamente = input('deseja pedir outro sorvete (S/N)?')
  pedir_novamente = pedir_novamente.upper()
  if pedir_novamente == 'S': # se apertada letra S volta para o começo .
    print(50*'-')
    continue # volta para o começo

  else:
    print(50*'-')
    print('o valor total e de R$: {:.2f}'.format(acumulador)) #imprime o valor total da compra
    break #encerra o programa
