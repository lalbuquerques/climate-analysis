#1. Define as variáveis necessárias para o cálculo.
somaMes = 0
somaTemperatura = 0
maiorTemperatura = -float('inf')
menorTemperatura = float('inf')
mesesEscaldantes = 0
mesMaisEscaldante = 0
mesMenosQuente = 0
meses_inseridos = set()  # Conjunto para rastrear meses já inseridos.
#2. Define um dicionário que relaciona o número com o mês de referência.
temperaturas = {
    1: 'Janeiro',
    2: 'Fevereiro',
    3: 'Março',
    4: 'Abril',
    5: 'Maio',
    6: 'Junho',
    7: 'Julho',
    8: 'Agosto',
    9: 'Setembro',
    10: 'Outubro',
    11: 'Novembro',
    12: 'Dezembro'
}
#3. Solicita e valida os dados de entrada(mês do ano e temperatura do mês).
while somaMes < 12:
    try:
        mes = int(input('Digite o mês no intervalo [1;12]: '))
        if mes < 1 or mes > 12:
            print('Mês inválido. Digite um valor entre 1 e 12.')
            continue
        if mes in meses_inseridos:
            print(f'Mês {temperaturas[mes]} já foi inserido. Por favor, escolha outro mês.')
            continue
        temperatura = float(input('Digite a temperatura máxima em celsius nesse mês: '))
        if temperatura < -60 or temperatura > 50:
            print('Temperatura inválida. Digite um valor entre -60 e 50.')
            continue
        # Com mês e temperatura válidos, incrementa a variável somaMes, somaTemperatura e o conjunto meses_inseridos.
        somaMes += 1
        somaTemperatura += temperatura
        meses_inseridos.add(mes)
        print(f'Temperatura do mês de {temperaturas[mes]}: {temperatura}')
        #5. Verifica se a temperatura é escaldante e incrementa a variável mesesEscaldantes.
        if temperatura > 33:
            mesesEscaldantes += 1
        #6. Verifica se a temperatura é a maior do ano e atualiza a variável mesMaisEscaldante.
        if temperatura > maiorTemperatura:
            maiorTemperatura = temperatura
            mesMaisEscaldante = mes
        #7. Verifica se a temperatura é a menor do ano e atualiza a variável mesMenosQuente.
        if temperatura <= menorTemperatura:
            menorTemperatura = temperatura
            mesMenosQuente = mes
    except ValueError:
        print('Entrada inválida. Por favor, digite valores numéricos válidos.')
#8. Calcula a temperatura média máxima anual.
temperaturaMediaMaxAnual = somaTemperatura/somaMes
#9. Exibe os resultados.
print(f'Temperatura média máxima anual: {temperaturaMediaMaxAnual:.1f} graus')
print(f'Quantidade de meses escaldantes: {mesesEscaldantes}')
print(f'Mês mais escaldante do ano: {temperaturas[mesMaisEscaldante]}: {maiorTemperatura} graus')
print(f'Mês menos quente do ano: {temperaturas[mesMenosQuente]}: {menorTemperatura} graus')