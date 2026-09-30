import pytest

from dominio.item import Item

def test_item_valido():
    assert Item("água", 6).descricao() == "água: R$ 6"
    
def test_item_com_preco_negativo_levanta_erro():
    with pytest.raises(ValueError):
        Item("erro", -1)


