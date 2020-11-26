usuario = []
lugar = []
custo = []
id = []
continuar = 's'
alterar = 's'
mudar = 's'
excluir = 's'
print("\n\t Bem vindo a nossa agencia de viagens")

print("\tVamos realizar uma reserva ?\n")

while continuar == 's' or continuar == 'S':
    nome = input("Digite seu nome: ")
    usuario.append(nome)

    destino = input("Insira o destino de sua viagem: ")
    lugar.append(destino)

    gasto = int(input("Digite o valor de deposito para despesas: "))
    custo.append(gasto)

    identificacao = int(input("Insira uma senha para sua identificação : "))
    id.append(identificacao)

    continuar = input("\nDeseja realizar outro cadastro ? PRECIONE 'S' para continuar : ")


print("\n\tReserva cadastrada!\n \t Confirme seus dados! ")
for i in range(len(usuario)):

    print(" Nome: %s\n Destino: %s\n Disponivel para despesas U$ %s \n" % (usuario[i], lugar[i], custo[i]))


mudar = input("\nDeseja alterar o destino ? Digite 'S' para alterar: ")

if mudar == 's' or mudar == 'S':

    numero = int(input("\nDigite seu numero de identificação para  alterar o destino: "))
    lugar.pop(id.index(numero))

    novodestino = input("\nDigite seu novo destino: ")
    lugar.insert(id.index(numero),novodestino)

print("\n\tReserva cadastrada!\n")

for i in range(len(usuario)):
    print("\n Nome: %s\n Destino: %s\n Disponivel para despesas U$ %s \n" % (usuario[i], lugar[i], custo[i]))

excluirCadastro = input("Deseja excluir algum cadastro 'S' ou 'N' ")

if excluirCadastro == 's' or excluirCadastro == "S":
        delete = int (input("Digite sua senha para exluir a reserva : "))

        lugar.pop(id.index(delete))

        print("reserva excluida com sucesso")


print("\n\tReserva cadastrada!\n")

for i in range(len(usuario)):
         print("\n Nome: %s\n Destino: %s\n Disponivel para despesas U$ %s \n" % (usuario[i], lugar[i], custo[i]))
