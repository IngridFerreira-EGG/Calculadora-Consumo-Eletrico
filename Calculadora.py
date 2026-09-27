#Entrada
aparelho = input("Aparelho: ")
potencia = int(input("Potencia do aparelho[W]: "))
consumo_horas = float(input("Quantas horas por dia o aparelho e usado: "))
consumo_dias = int(input("Quantos dias por mes o aparelho e usado: "))
preco_kwh = float(input("Preço do kWh na cidade: "))

#Processamento
consumo_kwh = float((potencia * consumo_horas * consumo_dias)/1000)
preco_consumo = float(consumo_kwh * preco_kwh)

#Saída
mensagem= f"""Aparelho: {aparelho}
Consumo estimado(kWh): {consumo_kwh}
Gasto estimado(R$): {preco_consumo}"""

print(mensagem)
