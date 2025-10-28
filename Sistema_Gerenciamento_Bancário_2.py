from datetime import datetime
import json
import os

Class Cliente:

Class PessoaFisica(Cliente):

Class ContaCorrente(Conta):

Class Historico: 

Class Transacao(ABC):

Class Saque(Transacao):

Class Deposito(Transacao):



# Listas para armazenar os dados (como um banco de dados simples)
clientes = []
contas = []
ARQUIVO_BANCO = "banco_banco.json"

def salvar_dados(): # Salva os dados no arquivo JSON
    dados = {
        "clientes": clientes,
        "contas": contas
    }
    try:
        with open(ARQUIVO_DADOS, "w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, ensure_ascii=False, indent=2)
        print("✅ Dados salvos com sucesso!")
    except Exception as e:
        print(f"❌ Erro ao salvar: {e}")

def carregar_dados(): # Carrega os dados do arquivo JSON
    global clientes, contas
    
    try:
        if os.path.exists(ARQUIVO_DADOS):
            with open(ARQUIVO_DADOS, "r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)
                clientes[:] = dados.get("clientes", [])
                contas[:] = dados.get("contas", [])
            print("📂 Dados carregados!")
        else:
            print("📝 Criando novo banco de dados...")
            salvar_dados()
    except Exception as e:
        print(f"⚠️ Erro ao carregar dados: {e}")
        print("Criando banco limpo...")
        clientes.clear()
        contas.clear()
        salvar_dados()

def obter_texto(mensagem, obrigatorio=True): # Função auxiliar para obter texto do usuário
    while True:
        texto = input(mensagem).strip()
        if texto or not obrigatorio:
            return texto.title() if texto else ""
        print("❌ Este campo é obrigatório!")

def obter_numero(mensagem, tipo=int): # Função auxiliar para obter números do usuário
    while True:
        try:
            valor = input(mensagem).strip()
            return tipo(valor)
        except ValueError:
            print("❌ Digite apenas números!")

def cadastrar_cliente(): # Cadastra um novo cliente
    print("\n=== 👤 CADASTRO DE CLIENTE ===")
    
    # Dados básicos
    nome = obter_texto("Nome completo: ")
    
    # CPF simplificado (apenas verificação básica)
    while True:
        cpf = input("CPF (apenas números): ").strip()
        if len(cpf) == 11 and cpf.isdigit():
            # Verifica se CPF já existe
            if any(cliente["cpf"] == cpf for cliente in clientes):
                print("❌ CPF já cadastrado!")
                continue
            break
        print("❌ CPF deve ter 11 dígitos!")
    
    # Data de nascimento simplificada
    data_nascimento = obter_texto("Data de nascimento (dd/mm/aaaa): ")
    
    # Endereço simplificado
    endereco = obter_texto("Endereço completo: ")
    
    # Criar cliente
    cliente = {
        "nome": nome,
        "cpf": cpf,
        "data_nascimento": data_nascimento,
        "endereco": endereco
    }
    
    clientes.append(cliente)
    print(f"✅ Cliente {nome} cadastrado com sucesso!")
    salvar_dados()

def buscar_cliente_por_cpf(cpf): # Busca cliente pelo CPF
    for cliente in clientes:
        if cliente["cpf"] == cpf:
            return cliente
    return None

def criar_conta(): # cria uma nova conta para um cliente
    print("\n=== 🏦 CRIAR CONTA ===")
    
    cpf = input("CPF do cliente: ").strip()
    cliente = buscar_cliente_por_cpf(cpf)
    
    if not cliente:
        print("❌ Cliente não encontrado! Cadastre primeiro.")
        return
    
    # Gerar número da conta automaticamente
    numero_conta = len(contas) + 1
    
    conta = {
        "numero": numero_conta,
        "agencia": "0001",
        "cliente": cliente,
        "saldo": 0.0,
        "historico": []
    }
    
    contas.append(conta)
    print(f"✅ Conta criada!")
    print(f"🏦 Agência: 0001 | Conta: {numero_conta}")
    print(f"👤 Titular: {cliente['nome']}")
    salvar_dados()

def buscar_conta(numero): # Busca conta pelo número
    for conta in contas:
        if conta["numero"] == numero:
            return conta
    return None

def depositar(): # Realiza depósito em uma conta
    print("\n=== 💰 DEPÓSITO ===")
    
    numero_conta = obter_numero("Número da conta: ")
    conta = buscar_conta(numero_conta)
    
    if not conta:
        print("❌ Conta não encontrada!")
        return
    
    valor = obter_numero("Valor do depósito: R$ ", float)
    
    if valor <= 0:
        print("❌ Valor deve ser positivo!")
        return
    
    # Realizar depósito
    conta["saldo"] += valor
    
    # Registrar no histórico
    transacao = {
        "tipo": "DEPÓSITO",
        "valor": valor,
        "data": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        "descricao": "Depósito em conta"
    }
    conta["historico"].append(transacao)
    
    print(f"✅ Depósito realizado!")
    print(f"💰 Novo saldo: R$ {conta['saldo']:.2f}")
    salvar_dados()
    
def sacar(): # Realiza saque de uma conta
    print("\n=== 💸 SAQUE ===")
    
    numero_conta = obter_numero("Número da conta: ")
    conta = buscar_conta(numero_conta)
    
    if not conta:
        print("❌ Conta não encontrada!")
        return
    
    valor = obter_numero("Valor do saque: R$ ", float)
    
    if valor <= 0:
        print("❌ Valor deve ser positivo!")
        return
    
    if valor > conta["saldo"]:
        print(f"❌ Saldo insuficiente! Saldo atual: R$ {conta['saldo']:.2f}")
        return
    
    # Realizar saque
    conta["saldo"] -= valor
    
    # Registrar no histórico
    transacao = {
        "tipo": "SAQUE",
        "valor": -valor,
        "data": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        "descricao": "Saque em conta"
    }
    conta["historico"].append(transacao)
    
    print(f"✅ Saque realizado!")
    print(f"💰 Saldo atual: R$ {conta['saldo']:.2f}")
    salvar_dados()

def exibir_extrato(): # Exibe o extrato de uma conta
    print("\n=== 📄 EXTRATO ===")
    
    numero_conta = obter_numero("Número da conta: ")
    conta = buscar_conta(numero_conta)
    
    if not conta:
        print("❌ Conta não encontrada!")
        return
    
    cliente = conta["cliente"]
    print(f"\n�� BANCO REAL MADRUGA")
    print(f"👤 Cliente: {cliente['nome']}")
    print(f"🏦 Agência: {conta['agencia']} | Conta: {conta['numero']}")
    print("-" * 50)
    
    if not conta["historico"]:
        print("Nenhuma movimentação encontrada.")
    else:
        for transacao in conta["historico"]:
            data = transacao["data"]
            tipo = transacao["tipo"]
            valor = abs(transacao["valor"])
            sinal = "+" if transacao["valor"] > 0 else "-"
            
            print(f"{data} | {tipo} | {sinal}R$ {valor:.2f}")
    
    print("-" * 50)
    print(f"💰 SALDO ATUAL: R$ {conta['saldo']:.2f}")
    print("-" * 50)

def listar_contas(): # Lista todas as contas"""
    print("\n=== 📋 LISTA DE CONTAS ===")
    
    if not contas:
        print("Nenhuma conta cadastrada.")
        return
    
    for conta in contas:
        cliente = conta["cliente"]
        print(f"🏦 Conta: {conta['numero']} | Agência: {conta['agencia']}")
        print(f"👤 Titular: {cliente['nome']}")
        print(f"💰 Saldo: R$ {conta['saldo']:.2f}")
        print("-" * 30)

def menu_principal(): # Exibe o menu principal
    carregar_dados()
    
    while True:
        print("\n" + "="*50)
        print("🏦 BANCO REAL MADRUGA - SISTEMA SIMPLIFICADO")
        print("="*50)
        print("1️⃣  - Cadastrar Cliente")
        print("2️⃣  - Criar Conta")
        print("3️⃣  - Depositar")
        print("4️⃣  - Sacar")
        print("5️⃣  - Extrato")
        print("6️⃣  - Listar Contas")
        print("0️⃣  - Sair")
        print("="*50)
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            cadastrar_cliente()
        elif opcao == "2":
            criar_conta()
        elif opcao == "3":
            depositar()
        elif opcao == "4":
            sacar()
        elif opcao == "5":
            exibir_extrato()
        elif opcao == "6":
            listar_contas()
        elif opcao == "0":
            print("👋 Obrigado por usar o Banco Real Madruga!")
            break
        else:
            print("❌ Opção inválida!")

# Executar o programa
if __name__ == "__main__":
    menu_principal()
