TURNOS_VALIDOS = ["M", "V", "N"]
CATEROGIAS_VALIDAS = ["G", "O"]
SALARIO_MINIMO = 1320

PORCENTAGENS = {"G": {"N": 0.1, "M": 0.15, "V": 0.15}, "O": {"N": 0.9, "M": 0.14, "V": 0.14}}

nome = input("Seu nome: ")
horas = int(input("Quantidade de horas trabalhadas no mês: "))
turno = input(f"Turno {TURNOS_VALIDOS}: ")
categoria = input(f"Categoria {CATEROGIAS_VALIDAS}: ")

try:
    assert turno in TURNOS_VALIDOS and categoria in CATEROGIAS_VALIDAS
    assert len(nome) > 0 and horas > 0
except AssertionError:
    print("Dados inválidos, finalizando programa")
    exit()

dados = [nome, horas, turno, categoria]

valor_da_hora_trabalhada = PORCENTAGENS[categoria][turno]

salario = (valor_da_hora_trabalhada * SALARIO_MINIMO) * horas

print(f"{nome}, O seu salário é de R${salario}")
