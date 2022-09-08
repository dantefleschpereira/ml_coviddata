def filter(txt, arquivo_inicial, novo_arquivo):
    '''\
    Read a list of names from a file line by line into an output file.
    If a line begins with a particular name, insert a string of text
    after the name before appending the line to the output file.
    '''

    with open(novo_arquivo, 'w') as outfile, open(arquivo_inicial, 'r', encoding='utf-8') as infile:
        for linha in infile:
            if linha.startswith(txt):
                linha.replace(txt, '0')
            outfile.write(linha)


if __name__ == '__main__':
    txt = 'x'
    arquivo_inicial = r'C:\Nucleo_IA\COVID\ML\_apps\anti-inflamatorio1.txt'
    novo_arquivo = r'C:\Nucleo_IA\COVID\ML\_apps\anti-inflamatorio2.txt'
    filter(txt, arquivo_inicial, novo_arquivo)
