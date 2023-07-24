import json

estoque = {}

def salvar_estoque_arquivo():
    with open('estoque.json', 'w') as arquivo:
        json.dump(estoque, arquivo)

def carregar_estoque_arquivo():
    try:
        with open('estoque.json', 'r') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        print("Erro ao carregar o arquivo de estoque. Criando novo estoque vazio...")
        return {}

def add_produto():
    nome = input('Digite o nome do produto: ')
    preco = None
    quantidade = None

    while preco is None:
        try:
            preco = float(input('Digite o preço do produto: R$'))
            if preco < 0:
                print("O preço deve ser um valor positivo.")
                preco = None
        except ValueError:
            print("Digite um valor numérico válido para o preço.")

    while quantidade is None:
        try:
            quantidade = int(input('Digite a quantidade em estoque: '))
            if quantidade < 0:
                print("A quantidade deve ser um valor positivo.")
                quantidade = None
        except ValueError:
            print("Digite um valor numérico válido para a quantidade.")

    estoque[nome] = {'preço': preco, 'quantidade': quantidade}
    salvar_estoque_arquivo()
    print(f"Produto {nome} adicionado com sucesso!")

def atualizar_produto():
    nome = input('Digite o nome do produto a ser atualizado: ')
    if nome in estoque:
        novo_preco = None
        nova_quantidade = None

        while novo_preco is None:
            try:
                novo_preco = float(input('Digite o novo preço do produto: '))
                if novo_preco < 0:
                    print("O preço deve ser um valor positivo.")
                    novo_preco = None
            except ValueError:
                print("Digite um valor numérico válido para o preço.")

        while nova_quantidade is None:
            try:
                nova_quantidade = int(input('Digite a nova quantidade no estoque: '))
                if nova_quantidade < 0:
                    print("A quantidade deve ser um valor positivo.")
                    nova_quantidade = None
            except ValueError:
                print("Digite um valor numérico válido para a quantidade.")

        estoque[nome]["preço"] = novo_preco
        estoque[nome]["quantidade"] = nova_quantidade
        salvar_estoque_arquivo()
        print(f"Produto {nome} atualizado com sucesso!")
    else:
        print(f"Produto {nome} não localizado no estoque.")

def remover_produto():
    nome = input('Digite o nome do produto a ser removido: ')
    if nome in estoque:
        del estoque[nome]
        salvar_estoque_arquivo()
        print(f"Produto {nome} removido do estoque com sucesso!")
    else:
        print(f"Produto {nome} não encontrado no estoque.")

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
    print('3 => Remover produto')
    print('4 => Visualizar estoque')
    print('5 => Calcular valor do estoque')
    print('6 => Sair do estoque')
    print('=-='*10)

def sair():
    salvar_estoque_arquivo()
    print('\nSAINDO DO SISTEMA...\n')

def executar_opcao(opcao):
    if opcao == 1:
        print('Adicionando produto...')
        add_produto()
    elif opcao == 2:
        print('Atualizando produto...')
        atualizar_produto()
    elif opcao == 3:
        print('Removendo produto...')
        remover_produto()
    elif opcao == 4:
        print('Exibindo o estoque...')
        visualizar_estoque()
    elif opcao == 5:
        print('Calculando valor total do estoque...')
        valor_total = calcular_valor_total()
        print(f'Valor total do estoque: R${valor_total:.2f}')
    elif opcao == 6:
        sair()
        return True
    else:
        print('\nOpção Inválida... Tente novamente!\n')

    return False

def main():
    global estoque
    estoque = carregar_estoque_arquivo()

    usuario = input('\nDigite seu usuário: ')
    print("=-="*10)
    print(f'Bem vindo ao Sistema de estoque, {usuario}!')
    print("=-="*14)

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
