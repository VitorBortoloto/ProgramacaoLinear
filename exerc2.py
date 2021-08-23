def somaImposto(taxaImposto, custo):

    valor_imposto = custo + (custo * taxaImposto / 100)

    return valor_imposto

print ('O valor do produto com imposto é: R$', somaImposto(20, 100))