ELEVADORES_VALIDOS = ["A", "B", "C"]
PERIODOS_VALIDOS = ["M", "V", "N"]

dados = {"A": {"M": 0, "V": 0, "N": 0}, "B": {"M": 0, "V": 0, "N": 0}, "C": {"M": 0, "V": 0, "N": 0}}

while True:
    elevador = input(f"Qual elevador você utiliza com mais frequência {ELEVADORES_VALIDOS}: ").upper()
    periodo = input(f"Em qual periodo você mais utiliza o elevador {PERIODOS_VALIDOS}: ").upper()

    try:
        assert elevador in ELEVADORES_VALIDOS and periodo in PERIODOS_VALIDOS
        dados[elevador][periodo] += 1
    except AssertionError:
        print("Valores inválidos, pulando")

    if input("Deseja continuar [sim] ") != "sim":
        break

elevadores_total = [sum(list(list(dados.values())[0].values())), sum(list(list(dados.values())[1].values())), sum(list(list(dados.values())[2].values()))]
periodos_total = [sum([dados["A"]["M"], dados["B"]["M"], dados["C"]["M"]]), sum([dados["A"]["V"], dados["B"]["V"], dados["C"]["V"]]), sum([dados["A"]["N"], dados["B"]["N"], dados["C"]["N"]])]

print("="*30)
print("Elevador mais usado:", end=" ")
print(ELEVADORES_VALIDOS[elevadores_total.index(max(elevadores_total))])
print("Periodo mais usado:", end=" ")
print(PERIODOS_VALIDOS[periodos_total.index(max(periodos_total))])
print("Diferença de percentual entre o período mais usado e menos usado:", end=" ")
print(f"{round(1-(min(periodos_total)/max(periodos_total)), 2)*100}%")


