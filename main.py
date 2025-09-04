import os
import shutil


def organizar_arquivos(separar_arquivos):
    pasta_pdf = os.path.join(separar_arquivos, 'arquivos pdf')
    pasta_jpg = os.path.join(separar_arquivos, 'arquivos jpg')
    pasta_txt = os.path.join(separar_arquivos, 'arquivos txt')

    os.makedirs(pasta_pdf, exist_ok=True)
    os.makedirs(pasta_jpg, exist_ok=True)
    os.makedirs(pasta_txt, exist_ok=True)

    for nome_pasta in os.listdir(separar_arquivos):
        caminho_pasta_original = os.path.join(separar_arquivos, nome_pasta)

        if os.path.isdir(caminho_pasta_original) and nome_pasta not in ['arquivos pdf', 'arquivos jpg', 'arquivos txt']:
            caminho_pasta_pdf = os.path.join(pasta_pdf, nome_pasta)
            caminho_pasta_jpg = os.path.join(pasta_jpg, nome_pasta)
            caminho_pasta_txt = os.path.join(pasta_txt, nome_pasta)

            os.makedirs(caminho_pasta_pdf, exist_ok=True)
            os.makedirs(caminho_pasta_jpg, exist_ok=True)
            os.makedirs(caminho_pasta_txt, exist_ok=True)

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
                    elif extensao == 'txt':
                        shutil.move(
                            caminho_arquivo,
                            os.path.join(caminho_pasta_txt, arquivo)
                        )


organizar_arquivos("C:\\Users\\Pedro\\Documents\\GitHub\\cidades")

print("Arquivos separados em pastas com sucesso!")
