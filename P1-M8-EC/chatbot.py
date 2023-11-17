import re

def main():

    # Função executada quando a intenção de atualização de informações de pagamento for detectada
    def pagamento():
        print(f"Notei que você deseja atualizar suas informações de pagamento. Para isso, você deve ir até a aba entitulada INFORMAÇÕES DE PAGAMENTO.")

    # Função executada quando a intenção de conferir o status do pedido for detectada
    def status():
        print(f"Notei que você deseja conferir o status do seu pedido. Para isso, você deve ir até a aba entitulada PEDIDOS.")

    # Função executada quando o chatbot não for capaz de identificar o comando
    def erro():
        print(f"Não foi possível identificar a informação solicitada. Por favor, tente novamente ou digite 'sair'.")

    # Função que interrompe o loop quando o usuário digita 'sair'
    def sair():
        print("Obrigado!")

    # Dicionário de intenções
    intencoes = {
        r"/\b([Cc]omo)?\b([Pp]reciso)?\b([Qq]uero)?\b([Mm]étodo)?\b(posso|fa(ço|zer))?\b(atualiz(ar|o)|mudar|alterar|modificar)?\b(meu|minha(s)?)?\b(a)?\b(forma(s)?|informaç(õ|o)es)?\b(de)?\b(pagamento)?\b(cart(a|ã)o)?\b(cr(e|é)dito)?\b(desatualizad(o|a|os|as))?\b(proceder)?\b(para)?\b(o)?\b(que)?": "pagamento",
        r"/\b([Oo]nde|[Cc]omo|[Cc]onsultar|[Qq]uero|[Vv](er|isualizar))?\b(ve(e|jo)|fa(er|ço))?\b(saber)?\b([sS]tatus)?\b([Rr]astr(eio|ear))?\b([Oo]nde)?\b(está)?\b(para)?\b((d)?o)?\b(m(eu|inha|inhas|eus))?\b(pedido)?\b(entrega)?\b(de)?(\W)?": "status",
    }

    # Dicionário de ações
    acoes = {
        "atualizar a forma de pagamento": pagamento,
        "conferir status do pedido": status,
    }

    # Comando para input de usuário
    comando = input("Olá! De qual informação você precisa? ")

    # Loop que itera sobre as intenções e verifica se há match com o padrão
    for key, value in intencoes.items():
        if comando == 'sair':
            sair()
        padrao = re.compile(key, re.IGNORECASE)
        grupo_captura = padrao.findall(comando)
        if grupo_captura:
            print(f"Detectei que você deseja obter informações para {valor}.")
            intencao_identificada = grupo_captura[0]
            acoes[value](intencao_identificada)
            break
    else:
        erro()

if __name__ == "__main__":
    main()