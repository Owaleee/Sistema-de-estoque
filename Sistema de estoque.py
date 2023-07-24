estoque = {}

def add_produto():
    nome = input('Digite o nome do produto: ')
    preco = float(input('Digite o preço do produto: R$'))
    quantidade = int(input('Digite a quantidade em estoque: '))
    estoque[nome] = {'preço': preco, 'quantidade': quantidade}
    print(f"Produto {nome} adicionado com sucesso!")

def atualizar_produto():
    nome = input('Digite o nome do produto a ser atualizado: ')
    if nome in estoque:
        novo_preco = float(input('Digite o novo preço do produto: '))
        nova_quantidade = int(input('Digite a nova quantidade no estoque: '))
        estoque[nome]["preço"] = novo_preco
        estoque[nome]["quantidade"] = nova_quantidade
        print(f"Produto {nome} atualizado com sucesso!")
    else:
        print(f"Produto {nome} não localizado no estoque.")

def visualizar_estoque():
    if len(estoque) == 0:
        print('Estoque Vazio...')
    else:
        print("\nLista de produtos no estoque...\n")
        for nome, dados in estoque.items():
            preco = dados["preço"]
            quantidade = dados["quantidade"]
            print(f'Nome: {nome}\nPreço: R${preco:.2f}\nQuantidade: {quantidade}\n')

def calcular_valor_total():
    valor_total = 0 
    for produto, dados in estoque.items():
        preco = dados["preço"]
        quantidade = dados['quantidade']
        valor_total += preco * quantidade
    return valor_total

def exibir_menu():
    print('\nSelecione uma opção:')
    print('1 => Adicionar produto')
    print('2 => Atualizar produto')
    print('3 => Visualizar estoque')
    print('4 => Calcular valor do estoque')
    print('5 => Sair do estoque')
    print('=-='*10)

def sair():
    print('\nSAINDO DO SISTEMA...\n')

def executar_opcao(opcao):
    if opcao == 1:
        print('Adicionado produto...')
        add_produto()
    elif opcao == 2:
        print('Atualizando produto...')
        atualizar_produto()
    elif opcao == 3:
        print('Exibindo o estoque...')
        visualizar_estoque()
    elif opcao == 4:
        print ('Calculando valor total do estoque...')
        valor_total = calcular_valor_total()
        print(f'Valor total do estoque: R${valor_total:.2f}')
    elif opcao == 5:
        sair()
        return True
    else:
        print('\nOpção Inválida... Tente novamente!\n')

    return False

def main():
    usuario = input('\nDigite seu usuário: ')
    print("=-="*10)
    print(f'Bem vindo ao Sistema de estoque, {usuario}!')
    print("=-="*10)

    while True:
        exibir_menu()

        try:
            opcao = int(input())
            should_exit = executar_opcao(opcao)

            if should_exit:
                break
        except ValueError:
            print('\nOpção inválida. Digite um número válido.')

    print(f'\nObrigado por utilizar o Sistema de estoque, {usuario}! Volte sempre! ;)\n')

if __name__ == "__main__":
    main()
