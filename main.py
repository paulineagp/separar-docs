import os
import shutil

# criar pasta para cada tipo de extensão


def organizar_arquivos(separar_arquivos):
    pasta_pdf = os.path.join(separar_arquivos, 'pdf')
    pasta_jpg = os.path.join(separar_arquivos, 'jpg')

    os.makedirs(pasta_pdf, exist_ok=True)
    os.makedirs(pasta_jpg, exist_ok=True)

    for nome_pasta in os.listdir(separar_arquivos):
        caminho_pasta_original = os.path.join(separar_arquivos, nome_pasta)

        if os.path.isdir(caminho_pasta_original) and nome_pasta not in ['pdf', 'jpg']:
            caminho_pasta_pdf = os.path.join(pasta_pdf, nome_pasta)
            caminho_pasta_jpg = os.path.join(pasta_jpg, nome_pasta)

            os.makedirs(caminho_pasta_pdf, exist_ok=True)
            os.makedirs(caminho_pasta_jpg, exist_ok=True)

            # separando as extensões
            for arquivo in os.listdir(caminho_pasta_original):
                caminho_arquivo = os.path.join(caminho_pasta_original, arquivo)

                if os.path.isfile(caminho_arquivo):
                    extensao = arquivo.split('.')[-1].lower()

                    if extensao == 'pdf':
                        shutil.move(
                            caminho_arquivo,
                            os.path.join(caminho_pasta_pdf, arquivo)
                        )
                    elif extensao == 'jpg':
                        shutil.move(
                            caminho_arquivo,
                            os.path.join(caminho_pasta_jpg, arquivo)
                        )


organizar_arquivos("C:\\Users\\Pedro\\Documents\\GitHub\\cidades")

print("Pastas organizadas por tipo de arquivo com sucesso!")
