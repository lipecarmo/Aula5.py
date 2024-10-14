while True:
    try:
        nota = float(input('Digite uma nota:'))
    except:
        print('Digite apenas numeros.')
    else:
        if nota < 0 or nota > 10:
            print('A nota digitada é invalida')
        else:
            print('Nota registrada.')
            break
nota = float(input('Digite uma nota:'))

# Função para calcular o tempo de chegada
def calcular_tempo(distancia, velocidade):
    tempo = distancia / velocidade  # Tempo em horas
    return tempo

# Distância em km
distancia = 21  # km

# Velocidade média em km/h
velocidade = float(input("Digite a velocidade média (em km/h): "))

# Chama a função para calcular o tempo
tempo = calcular_tempo(distancia, velocidade)

# Exibe o resultado
print(f"Tempo estimado de chegada: {tempo:.2f} horas")

Velocidade permitida
velocidade_permitida = float(input("Digite a velocidade permitida (em km/h): "))

# Velocidade do motorista
velocidade_motorista = float(input("Digite a velocidade do motorista (em km/h): "))

# Verifica se o motorista ultrapassou a velocidade
if velocidade_motorista > velocidade_permitida + 3:
    print("O motorista ultrapassou a velocidade permitida.")
else:
    print("O motorista está dentro da velocidade permitida.")


# Função para gerar o laudo médico
def gerar_laudo(nome, idade, sexo, diagnostico, tratamento):
    laudo = f"""
    Laudo Médico
    -------------
    Nome do Paciente: {nome}
    Idade: {idade} anos
    Sexo: {sexo}
    
    Diagnóstico: {diagnostico}
    Tratamento Recomendado: {tratamento}
    
    Data: {data_atual}
    Médico Responsável: Dr. Fernando Costa
    """
    return laudo

# Solicita informações do paciente
nome = input("Digite o nome do paciente: ")
idade = input("Digite a idade do paciente: ")
sexo = input("Digite o sexo do paciente (M/F): ")
diagnostico = input("Digite o diagnóstico: ")
tratamento = input("Digite o tratamento recomendado: ")

# Data atual (pode ser melhorada com a biblioteca datetime)
from datetime import datetime
data_atual = datetime.now().strftime("%d/%m/%Y")

# Gera e imprime o laudo
laudo = gerar_laudo(nome, idade, sexo, diagnostico, tratamento)
print(laudo)
