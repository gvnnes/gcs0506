"""
Testes para o módulo app.py
"""

from app import soma

def test_soma():
    """Teste para a função soma"""
    assert soma(2, 3) == 5

# Removido test_main() por não ter implementação
