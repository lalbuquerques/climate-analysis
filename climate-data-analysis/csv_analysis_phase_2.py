import os
import csv
from datetime import datetime
from collections import defaultdict
import matplotlib.pyplot as plt

# Função para carregar dados do arquivo CSV
def carregar_dados(arquivo):
    dados = []
    with open(arquivo, mode='r', encoding='utf-8') as file:
        leitor = csv.DictReader(file, delimiter=',')
        for linha in leitor:
            try:
                # Convertendo dados relevantes para os tipos apropriados
                linha['Data'] = datetime.strptime(linha['data'], '%d/%m/%Y')
                linha['Precipitação'] = float(linha['precip']) if linha['precip'] else 0.0
                linha['Temp_Max'] = float(linha['maxima']) if linha['maxima'] else None
                linha['Temp_Min'] = float(linha['minima']) if linha['minima'] else None
                linha['Umidade'] = float(linha['um_relativa']) if linha['um_relativa'] else None
                linha['Vento'] = float(linha['vel_vento']) if linha['vel_vento'] else None
                dados.append(linha)
            except ValueError as e:
                print(f"Erro ao processar a linha: {linha}. Erro: {e}")
                continue
    return dados

# Função para visualizar os dados em um intervalo de tempo
def visualizar_dados(dados, inicio, fim, tipo):
    try:
        inicio = datetime.strptime(inicio, '%Y-%m')
        fim = datetime.strptime(fim, '%Y-%m')
    except ValueError as e:
        print(f"Formato de data inválido: {e}")
        return

    tipos = {
        1: ['Data', 'Precipitação', 'Temp_Max', 'Temp_Min', 'Umidade', 'Vento'],
        2: ['Data', 'Precipitação'],
        3: ['Data', 'Temp_Max', 'Temp_Min'],
        4: ['Data', 'Umidade', 'Vento']
    }
    
    campos = tipos.get(tipo, tipos[1])
    
    # Cabeçalho para os dados exibidos
    print({campo: campo for campo in campos})
    
    # Filtrando e exibindo os dados no intervalo especificado
    for registro in dados:
        if inicio <= registro['Data'] <= fim:
            print({campo: registro[campo] for campo in campos})

# Função para encontrar o mês mais chuvoso
def mes_mais_chuvoso(dados):
    precipitacao_mensal = defaultdict(float)
    
    for registro in dados:
        mes_ano = registro['Data'].strftime('%Y-%m')
        precipitacao_mensal[mes_ano] += registro['Precipitação']
    
    mes_mais_chuvoso = max(precipitacao_mensal, key=precipitacao_mensal.get)
    
    return mes_mais_chuvoso, precipitacao_mensal[mes_mais_chuvoso]

# Função para calcular a média da temperatura mínima para um mês específico nos últimos 11 anos
def media_temp_minima(dados, mes):
    temp_minima_anos = defaultdict(list)
    
    for registro in dados:
        if registro['Data'].year >= 2006 and registro['Data'].strftime('%B') == mes:
            ano_mes = f"{mes}{registro['Data'].year}"
            if registro['Temp_Min'] is not None:
                temp_minima_anos[ano_mes].append(registro['Temp_Min'])
    
    medias = {ano: sum(temp) / len(temp) for ano, temp in temp_minima_anos.items()}
    
    return medias

# Função para gerar o gráfico de barras
def grafico_temp_minima(medias):
    anos = list(medias.keys())
    temperaturas = list(medias.values())
    
    plt.bar(anos, temperaturas, color='blue')
    plt.xlabel('Ano')
    plt.ylabel('Média da Temperatura Mínima (°C)')
    plt.title('Média da Temperatura Mínima em determinado mês (2006-2016)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Função para calcular a média geral da temperatura mínima
def media_geral_temp_minima(medias):
    total_temp = sum(medias.values())
    total_anos = len(medias)
    return total_temp / total_anos

# Parte principal do código
if __name__ == "__main__":
    # Obtém o diretório do script atual e junta com o nome do arquivo CSV
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, 'dados_climaticos.csv')
    
    # Carregar dados do CSV
    dados = carregar_dados(file_path)
    
    # Menu e opções
    while True:
        print("\nMenu:")
        print("1. Visualizar intervalo de dados")
        print("2. Mês mais chuvoso")
        print("3. Média da temperatura mínima de um mês específico nos últimos 11 anos")
        print("4. Gráfico da média da temperatura mínima de um mês específico nos últimos 11 anos")
        print("5. Média geral da temperatura mínima de um mês específico nos últimos 11 anos")
        print("0. Sair")
        
        opcao = int(input("Escolha uma opção: "))
        
        if opcao == 0:
            break
        elif opcao == 1:
            inicio = input("Digite o mês e ano inicial (formato YYYY-MM): ")
            fim = input("Digite o mês e ano final (formato YYYY-MM): ")
            tipo = int(input("Escolha o tipo de dados (1: todos, 2: precipitação, 3: temperatura, 4: umidade e vento): "))
            visualizar_dados(dados, inicio, fim, tipo)
        elif opcao == 2:
            mes, precipitacao = mes_mais_chuvoso(dados)
            print(f"O mês mais chuvoso foi {mes} com {precipitacao:.2f} mm de precipitação.")
        elif opcao == 3:
            mes = input("Digite o mês (em inglês, por exemplo, 'August'): ")
            medias = media_temp_minima(dados, mes)
            for ano_mes, media in medias.items():
                print(f"{ano_mes}: {media:.2f}°C")
        elif opcao == 4:
            mes = input("Digite o mês (em inglês, por exemplo, 'August'): ")
            medias = media_temp_minima(dados, mes)
            grafico_temp_minima(medias)
        elif opcao == 5:
            mes = input("Digite o mês (em inglês, por exemplo, 'August'): ")
            medias = media_temp_minima(dados, mes)
            media_geral = media_geral_temp_minima(medias)
            print(f"A média geral da temperatura mínima em {mes} nos últimos 11 anos é {media_geral:.2f}°C")
        else:
            print("Opção inválida! Tente novamente.")
