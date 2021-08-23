cpf = input("Digite o seu CPF no formato xxx.xxx.xxx-xx: ")

while(cpf[3] !=".") or (cpf[7] !=".") or (cpf[11] !="-"):
    cpf = input("O 'CPF' pricisa estar no formato (xxx.xxx.xxx-xx) :")
else:
    print("O 'CPF' está no formato correto")
