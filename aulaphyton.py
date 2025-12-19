##
##╔═══════════════════════════════════════════════════════════════╗
##║                    PROGRAMA DE FATURAMENTO                    ║
##╠═══════════════════════════════════════════════════════════════╣
##║  Autor: Alexandre Batista                                     ║
##║  Descrição: Programa que calcula faturamento, custos,         ║
##║             impostos e lucro baseado em operações comerciais. ║
##║             Também demonstra o uso do operador módulo (%).    ║
##╚═══════════════════════════════════════════════════════════════╝
##

# declaracao de variáveis 
faturamento = 1200
custo = 750.0
teve_lucro = True  # Variável boolean 

# Operacoes 
novas_vendas = 100
faturamento = faturamento + novas_vendas

imposto = faturamento * 0.1 
lucro = faturamento - custo - imposto
margem_lucro = lucro / faturamento

# Exibicao

print("O faturamento foi de ", faturamento)
print("O custo foi de ",custo)
print("O imposto foi de ", imposto)
print("o lucro foi de ", lucro)
print("A margem de lucro foi ", round(margem_lucro,3))
print(10 % 3)


# o MOd %  é um operador (resto da divisao)

tempo_contrato = 170  #em meses 
tempo_anos = 170/12 

print("Tempo em anos é: ", int(tempo_anos))

tempo_meses = 170 % 12 

print("Tempo em meses: ", tempo_meses)