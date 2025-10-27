#Na futurística cidade de Tecnos, a equipe do Laboratório de Inovação está desenvolvendo um robô que processa comandos de texto enviados por usuários. Para garantir clareza nos logs e troca de dados, o robô deve ser capaz de padronizar e aprimorar mensagens usando funções bem definidas, seguindo boas práticas de programação. Seu desafio é ajudar a equipe do laboratório a criar uma função que recebe uma mensagem enviada ao robô e retorna a mesma mensagem: (1) sem espaços extras no início ou fim, (2) com todas as letras minúsculas, e (3) com apenas um único espaço separando as palavras.
#Implemente esta função seguindo boas práticas (clareza, reutilização e modularização) e sem utilizar bibliotecas externas. Certifique-se de que a função trate corretamente mensagens já padronizadas ou compostas apenas de espaços.
#Entrada
#Uma única linha contendo uma mensagem (string) enviada ao robô. A mensagem pode conter letras maiúsculas ou minúsculas, espaços múltiplos entre palavras ou ao redor, e pode estar vazia ou conter apenas espaços.
#Saída
#Uma única linha contendo a mensagem processada: sem espaços extras no início/fim, todas as letras em minúsculo, e com apenas um espaço separando cada palavra. Se a entrada for vazia ou composta apenas por espaços, a saída deve ser uma linha vazia.

def formatar_mensagem(texto):
    # Remove espaços extras do início e do fim da string
    texto = texto.strip()
    
    # Se a string ficou vazia após o strip, retorne a string vazia
    if not texto:
        return ""
    
    # Processar o texto para garantir:
    # - letras minúsculas
    # - apenas um espaço separando as palavras
    texto = texto.lower()
    palavras = texto.split()  # Separa em palavras (remove múltiplos espaços automaticamente)
    mensagem_formatada = " ".join(palavras)  # Une com apenas um espaço
    
    return mensagem_formatada

def menu():
    print("\n Bem Vindo ao Laboratório de Inovação de Tecnos")
    print("1 - Enviar Mensagem ao Robo")
    print("2 - Resposta do Robo")
    print("3 - Cadastrar Projeto")
    print("0 - Sair")
    return input("Escolha uma opção: ")

def main():
    while True:  # Corrigido: adicionado dois pontos
        opcao = menu()
        
        if opcao == "0":  # Corrigido: adicionado dois pontos
            print("Finalizando o sistema.")
            break
        
        if opcao == "1":  # Corrigido: adicionado dois pontos
            print("\n O que deseja saber?")
            print("1 - Status do Projeto")
            print("2 - Responsável do Projeto")
            escolha = input("Digite a opção (1/2): ")
            status = ("Em Andamento", "Concluído", "Cancelado")
            responsavel = ("Ana", "José", "Maria", "João")
            
            if escolha == "1":  # Corrigido: adicionado dois pontos
                print("Status disponíveis:", status)
            elif escolha == "2":
                print("Responsáveis disponíveis:", responsavel)

# Lê a mensagem enviada ao robô via input padrão
entrada = input()  # Tipo de dado esperado: str

# Chama a função formatar_mensagem (implementada)
saida = formatar_mensagem(entrada)

# Exibe a mensagem formatada
print(saida)
