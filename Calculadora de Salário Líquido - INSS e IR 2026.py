salario_bruto = float(input("Digite o seu salario bruto: R$ "))
print(f"Salario bruto informado: R$ {salario_bruto}")

if salario_bruto > 8475.55:
    teto_inss = 8475.55
else:
    teto_inss = salario_bruto

primeira_faixa = 0.0
segunda_faixa = 0.0
terceira_faixa = 0.0
quarta_faixa = 0.0

if teto_inss <= 1621.00:
    primeira_faixa = teto_inss * 0.075
else:
    primeira_faixa = 1621.00 * 0.075

if teto_inss > 1621.00:
    if teto_inss <= 2902.84:
        segunda_faixa = (teto_inss - 1621.00) * 0.09
    else:
        segunda_faixa = (2902.84 - 1621.00) * 0.09

if teto_inss > 2902.84:
    if teto_inss <= 4354.27:
        terceira_faixa = (teto_inss - 2902.84) * 0.12
    else:
        terceira_faixa = (4354.27 - 2902.84) * 0.12

if teto_inss > 4354.27:
    quarta_faixa = (teto_inss - 4354.27) * 0.14

desconto_inss = primeira_faixa + segunda_faixa + terceira_faixa + quarta_faixa
print(f"Desconto INSS: R$ {desconto_inss}")

base_calculo_ir = salario_bruto - desconto_inss
print(f"Base de calculo do IR (salario bruto - INSS): R$ {base_calculo_ir}")

if base_calculo_ir <= 2259.20:
    imposto_pela_tabela = 0.0
elif base_calculo_ir <= 2826.65:
    imposto_pela_tabela = (base_calculo_ir * 0.075) - 169.44
elif base_calculo_ir <= 3751.05:
    imposto_pela_tabela = (base_calculo_ir * 0.15) - 381.44
elif base_calculo_ir <= 4664.68:
    imposto_pela_tabela = (base_calculo_ir * 0.225) - 662.77
else:
    imposto_pela_tabela = (base_calculo_ir * 0.275) - 896.00

if base_calculo_ir <= 5000.00:
    imposto_de_renda = 0.0
elif base_calculo_ir <= 7350.00:
    reducao = imposto_pela_tabela * ((7350.00 - base_calculo_ir) / 2350.00)
    imposto_de_renda = imposto_pela_tabela - reducao
else:
    imposto_de_renda = imposto_pela_tabela

if imposto_de_renda < 0:
    imposto_de_renda = 0.0

print(f"Desconto Imposto de Renda: R$ {imposto_de_renda}")

salario_liquido = salario_bruto - desconto_inss - imposto_de_renda
print(f"Salario Liquido: R$ {salario_liquido}")