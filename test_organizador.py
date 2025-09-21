import os
import shutil
import pytest
import tempfile
from unittest.mock import patch, MagicMock
from main.py import organizar_arquivos


def test_criacao_pastas_principais():
    """Testa se as pastas principais são criadas corretamente"""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Chama a função
        organizar_arquivos(temp_dir)
        
        # Verifica se as pastas foram criadas
        assert os.path.exists(os.path.join(temp_dir, 'arquivos pdf'))
        assert os.path.exists(os.path.join(temp_dir, 'arquivos jpg'))
        assert os.path.exists(os.path.join(temp_dir, 'arquivos txt'))


def test_nao_cria_pastas_duplicadas():
    """Testa que a função não cria pastas duplicadas"""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Cria as pastas primeiro
        os.makedirs(os.path.join(temp_dir, 'arquivos pdf'))
        os.makedirs(os.path.join(temp_dir, 'arquivos jpg'))
        os.makedirs(os.path.join(temp_dir, 'arquivos txt'))
        
        # Chama a função (não deve lançar exceção)
        try:
            organizar_arquivos(temp_dir)
            assert True  # Passou sem erro
        except:
            assert False  # Falhou


def test_organiza_arquivos_por_tipo():
    """Testa se os arquivos são movidos para as pastas corretas"""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Cria uma subpasta com arquivos de teste
        subpasta = os.path.join(temp_dir, 'teste')
        os.makedirs(subpasta)
        
        # Cria arquivos de teste
        open(os.path.join(subpasta, 'arquivo1.pdf'), 'w').close()
        open(os.path.join(subpasta, 'arquivo2.jpg'), 'w').close()
        open(os.path.join(subpasta, 'arquivo3.txt'), 'w').close()
        
        # Executa a função
        organizar_arquivos(temp_dir)
        
        # Verifica se os arquivos foram movidos
        pdf_path = os.path.join(temp_dir, 'arquivos pdf', 'teste', 'arquivo1.pdf')
        jpg_path = os.path.join(temp_dir, 'arquivos jpg', 'teste', 'arquivo2.jpg')
        txt_path = os.path.join(temp_dir, 'arquivos txt', 'teste', 'arquivo3.txt')
        
        assert os.path.exists(pdf_path)
        assert os.path.exists(jpg_path)
        assert os.path.exists(txt_path)


def test_ignora_pastas_principais():
    """Testa que a função ignora as pastas principais durante a varredura"""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Cria as pastas principais primeiro
        os.makedirs(os.path.join(temp_dir, 'arquivos pdf'))
        os.makedirs(os.path.join(temp_dir, 'arquivos jpg'))
        os.makedirs(os.path.join(temp_dir, 'arquivos txt'))
        
        # Cria uma subpasta normal
        subpasta = os.path.join(temp_dir, 'normal')
        os.makedirs(subpasta)
        open(os.path.join(subpasta, 'teste.pdf'), 'w').close()
        
        # Executa a função
        organizar_arquivos(temp_dir)
        
        # Verifica que a pasta principal não foi processada como subpasta
        pdf_path = os.path.join(temp_dir, 'arquivos pdf', 'arquivos pdf')
        assert not os.path.exists(pdf_path)  # Não deve existir esta pasta


def test_lida_com_pasta_vazia():
    """Testa que a função lida corretamente com pastas vazias"""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Cria uma subpasta vazia
        subpasta = os.path.join(temp_dir, 'vazia')
        os.makedirs(subpasta)
        
        # Executa a função (não deve lançar exceção)
        try:
            organizar_arquivos(temp_dir)
            assert True  # Passou sem erro
        except:
            assert False  # Falhou
            