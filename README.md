# Climate Analysis Project

## Descrição

Este projeto foi desenvolvido para a disciplina de **Lógica de Programação** da **PUCRS** e realizado por **Larissa Albuquerque**. O objetivo do projeto é realizar a análise de dados climáticos, como temperatura máxima, mínima, precipitação e outros indicadores meteorológicos. O projeto é dividido em duas fases:

- **Fase 1**: Entrada manual de dados climáticos mensais para gerar estatísticas anuais.
- **Fase 2**: Análise de dados climáticos carregados a partir de um arquivo CSV, com funcionalidades para visualização de dados, cálculo de médias e geração de gráficos.

## Funcionalidades

### Fase 1:
- Entrada manual da temperatura máxima de cada mês.
- Cálculo da temperatura média anual.
- Identificação do mês mais quente e menos quente.
- Contagem de meses escaldantes (temperatura superior a 33°C).

### Fase 2:
- Carregamento de dados de um arquivo CSV com informações climáticas.
- Visualização de dados por intervalo de tempo.
- Cálculo do mês mais chuvoso.
- Cálculo da média da temperatura mínima para um mês específico nos últimos 11 anos.
- Geração de gráficos da média da temperatura mínima em determinado período.

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/climate-analysis.git

2. Navegue até o diretório do projeto:
   ```bash
   cd climate-analysis

3. Instale as dependências necessárias:
   ```bash
   pip install -r requirements.txt

4. Certifique-se de que o arquivo dados_climaticos.csv esteja no diretório correto (dentro da pasta climate-data-analysis).

## Uso

1. Fase 1: Execute o arquivo manual_input_phase_1.py para inserir os dados manualmente e visualizar as estatísticas.
   ```bash
   python temperature-input-analysis/manual_input_phase_1.py

2. Fase 2: Execute o arquivo csv_analysis_phase_2.py para analisar os dados a partir de um arquivo CSV.
   ```bash
   python climate-data-analysis/csv_analysis_phase_2.py

## Menu de Opções

Ao executar o arquivo `csv_analysis_phase_2.py`, você terá as seguintes opções no menu:

1. **Visualizar intervalo de dados**: 
   Permite visualizar dados como precipitação, temperatura máxima e mínima, umidade e velocidade do vento em um intervalo de datas especificado pelo usuário.

   - **Input**: Mês e ano inicial e final no formato `YYYY-MM`.
   - **Tipo de dados**: 
     - `1`: Todos os dados (Precipitação, Temp_Max, Temp_Min, Umidade, Vento)
     - `2`: Precipitação
     - `3`: Temperatura máxima e mínima
     - `4`: Umidade e vento

2. **Mês mais chuvoso**: 
   Exibe qual foi o mês com a maior quantidade de precipitação.

3. **Média da temperatura mínima de um mês específico nos últimos 11 anos**: 
   Calcula e exibe a média da temperatura mínima para um mês específico (em inglês) entre 2006 e 2016.

4. **Gráfico da média da temperatura mínima de um mês específico nos últimos 11 anos**: 
   Gera um gráfico de barras com a média da temperatura mínima para um mês específico (em inglês) entre 2006 e 2016.

5. **Média geral da temperatura mínima de um mês específico nos últimos 11 anos**: 
   Calcula a média geral da temperatura mínima para o mês especificado (em inglês) entre 2006 e 2016.

0. **Sair**: 
   Encerra o programa.

## Exemplo de Dados (CSV)

O arquivo `dados_climaticos.csv` deve seguir o seguinte formato:

| data       | precip | maxima | minima | um_relativa | vel_vento |
|------------|--------|--------|--------|-------------|-----------|
| 01/01/2020 | 10.5   | 30.2   | 20.1   | 85          | 15        |
| 02/01/2020 | 5.2    | 28.4   | 18.7   | 80          | 10        |
| ...        | ...    | ...    | ...    | ...         | ...       |

## Tecnologias Utilizadas

## Tecnologias Utilizadas

- **Python 3.10+**
- **Bibliotecas**:
  - `csv` para leitura de arquivos CSV.
  - `matplotlib` para geração de gráficos.
  - `datetime` para manipulação de datas.

## Licença

Este projeto está licenciado sob a [MIT License](https://opensource.org/licenses/MIT).
