from pathlib import Path

programa = "BlocoNotas.txt"
open(programa, "a", encoding="utf-8")


def adicionar_nota():
    nota = input("Digite uma nota: ").strip()
    if nota:
        with open(programa, "a", encoding="utf-8") as file:
            f.write(nota + "\n")
        print("Nota adicionada!")
    else:
        print("Não foi adicionada qualquer nota.")


def mostrar_notas():
    with open(programa, "r", encoding="utf-8") as file:
        conteudo = f.read().strip()

    print("\n***As minhas notas***")
    if conteudo:
        print(conteudo)
    else:
        print("Sem conteúdo.")
    print("-----------------------\n")


def apagar_notas():
    with open(programa, "w", encoding="utf-8"):
        pass
    print("Todas as notas foram apagadas.")


def pesquisar_notas():
    palavra = input("Digite a palavra-chave para pesquisa: ").strip()

    if not palavra:
        print("Pesquisa inválida.")
        return

    with open(programa, "r", encoding="utf-8") as f:
        linhas = f.readlines()

    resultados = []
    for linha in linhas:
        if palavra.lower() in linha.lower():
            resultados.append(linha.strip())

    print(f"\n--- Resultados da pesquisa por '{palavra}' ---")
    if resultados:
        for r in resultados:
            print(f"- {r}")
    else:
        print("Nenhuma nota encontrada com essa palavra-chave.")
    print("----------------------------------------------\n")


def menu():
    while True:
        print("\n=== Bloco de Notas ===")
        print("1. Adicionar nota")
        print("2. Mostrar notas")
        print("3. Apagar todas as notas")
        print("4. Pesquisar notas")
        print("5. Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            adicionar_nota()
        elif opcao == "2":
            mostrar_notas()
        elif opcao == "3":
            apagar_notas()
        elif opcao == "4":
            pesquisar_notas()
        elif opcao == "5":
            print("A sair... Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()