import re

def main():
    
    # Função executada quando a localização for detectada
    def localizacao(local_identificado):
        if local_identificado in local:
            print(f"Vou te levar até o local indicado: {local[local_identificado]}.")
        else:
            print("Local não encontrado.")


    # Função executada quando o comando não for reconhecido
    def comando_alternativo():
        print(f"Desculpe, não entendi o seu comando. Indique o local para onde deseja ir.")

    # Dicionário que armazena os locais de interesse
    local = {
        "secretaria": (0.0, 0.0, 1.0),
        "laboratório": (0.0, 0.0, 2.0),
        "biblioteca": (0.0, 0.0, 3.0),
    }

    # Dicionário que armazena as intenções e os padrões que as identificam
    intencoes = {
        r"\b[Mm]e\W*lev[ea]\W*at[eé]\W*(secretaria|laboratório|biblioteca)\b": "localizacao",
        r"\b[Mm]e\W*leve\W*para\W+(a)?\W*(secretaria|laboratório|biblioteca)\b": "localizacao",
        r"\b[Qq]uero\W+ir\W*(para)?\s*(secretaria|laboratório|biblioteca)\b": "localizacao",
        r"\b[vV][aá](i)?\W*(para|at[eé])\W*(a)?\s*(secretaria|laboratório|biblioteca)\b": "localizacao",
        r"\b([Ss]e)?\W*(dirija|dirija-se)\W*(a|ao|à)?\s*(secretaria|laboratório|biblioteca)\b": "localizacao",
    }

    # Dicionário que armazena as ações que devem ser executadas quando uma intenção é detectada
    acoes = {
        "localizacao": localizacao,
        "comando_alternativo": comando_alternativo,
    }

    # Comando que será interpretado pelo chatbot
    comando = input("Digite seu comando: ")

    # Itera sobre as intenções e verifica se há match com o padrão
    for chave, valor in intencoes.items():
        padrao = re.compile(chave, re.IGNORECASE)
        grupo_captura = padrao.findall(comando) # Verifica se há match com o padrão
        if grupo_captura:
            print(f"Detectei a intenção: {valor}.")
            local_identificado = grupo_captura[0] if grupo_captura else ""
            acoes[valor](local_identificado)
            break
    else:
        acoes["comando_alternativo"]()    

if __name__ == "__main__":
    main()