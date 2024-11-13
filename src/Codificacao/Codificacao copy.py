def zenit_polar_replace(text):
    # Aplicar a codificação ZENIT POLAR utilizando o método replace
    replacements = [('z', 'p'), ('e', 'o'), ('n', 'l'), ('i', 'a'), ('t', 'r'),
                    ('Z', 'P'), ('E', 'O'), ('N', 'L'), ('I', 'A'), ('T', 'R')]
    for old, new in replacements:
        text = text.replace(old, new)
    return text


def main():
    # Entrada da frase e aplicação da codificação
    frase = "O pato pateta Pintou o caneco Surrou a galinha Bateu no marreco"
    frase = frase.title() # Primeira letra de cada palavra em maiúscula

    print(zenit_polar_replace(frase))
    exit()
    # Dividir a frase em palavras
    palavras = frase.split()

    # Processar cada palavra na lista usando ZENIT POLAR
    palavras_codificada = [zenit_polar_replace(palavra) for palavra in palavras]

    # Juntar todas as palavras codificadas em uma frase

    frase_codificada = " ".join(palavras_codificada)
    print("Original: ", frase)
    print("Codificada: ", frase_codificada)


if __name__ == "__main__":
    main()