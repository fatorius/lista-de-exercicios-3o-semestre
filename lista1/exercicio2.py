ELEVADORES_VALIDOS = ["A", "B", "C"]
PERIODOS_VALIDOS = ["M", "V", "N"]

dados = {"A": {"M": 0, "V": 0, "N": 0}, "A": {"B": 0, "V": 0, "N": 0}, "C": {"M": 0, "V": 0, "N": 0}}

while True:
    elevador = input(f"Qual elevador você utiliza com mais frequência {ELEVADORES_VALIDOS}: ")
    periodo = input(f"Em qual periodo você mais utiliza o elevador {PERIODOS_VALIDOS}: ")

    try:
        assert elevador in ELEVADORES_VALIDOS and periodo in PERIODOS_VALIDOS
        dados.append([elevador, periodo])
    except AssertionError:
        print("Valores inválidos, pulando")

    if input("Deseja continuar [sim]") != "sim":
        break

