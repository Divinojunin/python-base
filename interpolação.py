"""Um boot para enviar email para várias pessoas de uma vez só"""

__version__ = "0.0.1"
__author__ = "Divino"
__license__ ="Unlicense"

#Um email formatado para enviar para pessoas
email_tmpl = """
        Olá, %(nome)s
        Tem interesse em comprar %(produto)s?
        Este produto é ótimo para resolver 
        %(texto)s
        Clique agora em %(link)s
        Apenas %(quantidade)d disponível!
        Preço promocional %(preco).2f
        """
#Uma lista vazia
clientes = []
#quantidade de nomes que o usuário irá passar
quantidades = int(input("Quantos nomes gostaria de ter: "))

#Um for para percorrer a quantidade escolhida pelo o usuário 
for i in range(quantidades):
    #Um input para o usuário colocar o nome das pessoas
    nome = input(f"Qual é o nome da {i+1}ª pessoa: ")
    #Adicionando o nomes das pessoas na lista vazia
    clientes.append(nome)

#Um for para mandar a mensagem para cada nome da lista 
for cliente in clientes:
    print(
        email_tmpl 
    %   {
            "nome": cliente,
            "produto": "Celular",
            "texto":"Para o seu dia-a-dia",
            "link": "https:celular.com.br",
            "quantidade": 5,
            "preco": 1500.00
        }
)