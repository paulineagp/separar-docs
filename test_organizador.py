import os
import shutil
import pytest
import tempfile
from unittest.mock import patch, MagicMock
from main import organizar_arquivos


def test_criacao_pastas_principais():
    with tempfile.TemporaryDirectory() as temp_dir:
        organizar_arquivos(temp_dir)
        
        assert os.path.exists(os.path.join(temp_dir, 'arquivos pdf'))
        assert os.path.exists(os.path.join(temp_dir, 'arquivos jpg'))
        assert os.path.exists(os.path.join(temp_dir, 'arquivos txt'))


def test_nao_cria_pastas_duplicadas():
    with tempfile.TemporaryDirectory() as temp_dir:
        os.makedirs(os.path.join(temp_dir, 'arquivos pdf'))
        os.makedirs(os.path.join(temp_dir, 'arquivos jpg'))
        os.makedirs(os.path.join(temp_dir, 'arquivos txt'))
        try:
            organizar_arquivos(temp_dir)
            assert True  
        except:
            assert False 


def test_organiza_arquivos_por_tipo():
    with tempfile.TemporaryDirectory() as temp_dir:
        subpasta = os.path.join(temp_dir, 'teste')
        os.makedirs(subpasta)
        open(os.path.join(subpasta, 'arquivo1.pdf'), 'w').close()
        open(os.path.join(subpasta, 'arquivo2.jpg'), 'w').close()
        open(os.path.join(subpasta, 'arquivo3.txt'), 'w').close()
        organizar_arquivos(temp_dir)
        pdf_path = os.path.join(temp_dir, 'arquivos pdf', 'teste', 'arquivo1.pdf')
        jpg_path = os.path.join(temp_dir, 'arquivos jpg', 'teste', 'arquivo2.jpg')
        txt_path = os.path.join(temp_dir, 'arquivos txt', 'teste', 'arquivo3.txt')
        
        assert os.path.exists(pdf_path)
        assert os.path.exists(jpg_path)
        assert os.path.exists(txt_path)


def test_ignora_pastas_principais():
    with tempfile.TemporaryDirectory() as temp_dir:
        os.makedirs(os.path.join(temp_dir, 'arquivos pdf'))
        os.makedirs(os.path.join(temp_dir, 'arquivos jpg'))
        os.makedirs(os.path.join(temp_dir, 'arquivos txt'))
        subpasta = os.path.join(temp_dir, 'normal')
        os.makedirs(subpasta)
        open(os.path.join(subpasta, 'teste.pdf'), 'w').close()
        organizar_arquivos(temp_dir)
        pdf_path = os.path.join(temp_dir, 'arquivos pdf', 'arquivos pdf')
        
        assert not os.path.exists(pdf_path)  


def test_lida_com_pasta_vazia():
    with tempfile.TemporaryDirectory() as temp_dir:
        subpasta = os.path.join(temp_dir, 'vazia')
        os.makedirs(subpasta)
        try:
            organizar_arquivos(temp_dir)
            assert True 
        except:
            assert False  
            