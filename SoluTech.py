# ==========================================
# SISTEMA DE CONTROLE DE CAIXAS
# ==========================================

import json
import os

ARQUIVO_CAIXAS = "caixas.json"
ARQUIVO_PRODUTOS = "produtos.json"

# ==========================================
# BANCO DE DADOS DOS PRODUTOS
# ==========================================

produtos = {
    "1001": {
        "nome": "Arroz",
        "lote": "AR123",
        "validade": "10/2027"
    },
    "1002": {
        "nome": "Feijão",
        "lote": "FE456",
        "validade": "08/2027"
    },
    "1003": {
        "nome": "Macarrão",
        "lote": "MA789",
        "validade": "12/2027"
    }
}

# Banco de dados das caixas
caixas = {}


# ==========================================
# SALVAR E CARREGAR DADOS
# ==========================================

def salvar_caixas():
    with open(ARQUIVO_CAIXAS, "w", encoding="utf-8") as arquivo:
        json.dump(caixas, arquivo, ensure_ascii=False, indent=4)


def carregar_caixas():
    global caixas

    if os.path.exists(ARQUIVO_CAIXAS):
        try:
            with open(ARQUIVO_CAIXAS, "r", encoding="utf-8") as arquivo:
                caixas = json.load(arquivo)
        except (json.JSONDecodeError, OSError):
            caixas = {}


def salvar_produtos():
    with open(ARQUIVO_PRODUTOS, "w", encoding="utf-8") as arquivo:
        json.dump(produtos, arquivo, ensure_ascii=False, indent=4)


def carregar_produtos():
    global produtos

    if os.path.exists(ARQUIVO_PRODUTOS):
        try:
            with open(ARQUIVO_PRODUTOS, "r", encoding="utf-8") as arquivo:
                produtos = json.load(arquivo)
        except (json.JSONDecodeError, OSError):
            print("Erro ao carregar produtos. Usando os produtos iniciais.")


# ==========================================
# 1. CADASTRAR CAIXA
# ==========================================

def criar_caixa():
    print("\n===== CADASTRO DA CAIXA =====")

    codigo_caixa = input("Bipe o código da caixa: ").strip()

    if not codigo_caixa:
        print("Código da caixa inválido!")
        return

    if codigo_caixa in caixas:
        print("Essa caixa já está cadastrada.")
        return

    caixas[codigo_caixa] = []

    print("Caixa", codigo_caixa, "criada!")

    while True:
        codigo_produto = input(
            "\nBipe o código do produto (0 para finalizar): "
        ).strip()

        if codigo_produto == "0":
            break

        if codigo_produto not in produtos:
            print("Produto não cadastrado!")
            continue

        try:
            quantidade = int(input("Digite a quantidade: "))

            if quantidade <= 0:
                print("A quantidade deve ser maior que zero!")
                continue

        except ValueError:
            print("Digite uma quantidade válida!")
            continue

        produto = produtos[codigo_produto]

        item = {
            "codigo": codigo_produto,
            "nome": produto["nome"],
            "quantidade": quantidade,
            "lote": produto["lote"],
            "validade": produto["validade"]
        }

        caixas[codigo_caixa].append(item)

        print(produto["nome"], "adicionado à caixa!")

    salvar_caixas()
    print("\nCaixa cadastrada e salva com sucesso!")


# ==========================================
# 2. CONSULTAR CAIXAS E MATERIAIS
# ==========================================

def consultar_caixas():
    print("\n===== CONSULTA DE CAIXAS =====")

    if not caixas:
        print("Nenhuma caixa cadastrada.")
        return

    for codigo_caixa, itens in caixas.items():
        print("\nCódigo da caixa:", codigo_caixa)
        print("-" * 35)

        if not itens:
            print("Nenhum produto nesta caixa.")
            continue

        for item in itens:
            print("Código do produto:", item["codigo"])
            print("Nome:", item["nome"])
            print("Quantidade:", item["quantidade"])
            print("Lote:", item["lote"])
            print("Validade:", item["validade"])
            print("-" * 35)


# ==========================================
# 3. EXCLUIR CAIXA
# ==========================================

def excluir_caixa():
    print("\n===== EXCLUIR CAIXA =====")

    if not caixas:
        print("Não existem caixas cadastradas.")
        return

    codigo_caixa = input(
        "Digite ou bipe o código da caixa: "
    ).strip()

    if codigo_caixa not in caixas:
        print("Caixa não encontrada!")
        return

    confirmar = input(
        "Deseja realmente excluir esta caixa? (s/n): "
    ).strip().lower()

    if confirmar == "s":
        del caixas[codigo_caixa]
        salvar_caixas()
        print("Caixa excluída com sucesso!")
    else:
        print("Exclusão cancelada.")


# ==========================================
# 4. CADASTRAR PRODUTO
# ==========================================

def cadastrar_produto():
    print("\n===== CADASTRO DE PRODUTO =====")

    codigo = input("Bipe o código do produto: ").strip()

    if not codigo:
        print("Código inválido!")
        return

    if codigo in produtos:
        print("Esse produto já está cadastrado!")
        return

    nome = input("Nome do produto: ").strip()
    lote = input("Lote do produto: ").strip()
    validade = input("Validade (MM/AAAA): ").strip()

    if not nome or not lote or not validade:
        print("Todos os campos são obrigatórios!")
        return

    produtos[codigo] = {
        "nome": nome,
        "lote": lote,
        "validade": validade
    }

    salvar_produtos()

    print("\nProduto cadastrado com sucesso!")
    print("Código:", codigo)
    print("Nome:", nome)
    print("Lote:", lote)
    print("Validade:", validade)


# ==========================================
# MENU PRINCIPAL
# ==========================================

def menu():
    carregar_caixas()
    carregar_produtos()

    while True:
        print("\n===================================")
        print("   SISTEMA DE CONTROLE DE CAIXAS")
        print("===================================")
        print("1 - Cadastrar caixa")
        print("2 - Consultar caixas e materiais")
        print("3 - Excluir caixa")
        print("4 - Cadastrar produto")
        print("0 - Sair")
        print("===================================")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            criar_caixa()

        elif opcao == "2":
            consultar_caixas()

        elif opcao == "3":
            excluir_caixa()

        elif opcao == "4":
            cadastrar_produto()

        elif opcao == "0":
            print("Saindo do sistema. Até mais!")
            break

        else:
            print("Opção inválida! Tente novamente.")


# ==========================================
# INICIAR O SISTEMA
# ==========================================

if __name__ == "__main__":
    menu()
