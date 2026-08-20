import pytest

from Aula1208.calculadora import calcular_desconto


@pytest.mark.parametrize(
    "preco, percentual, esperado",
    [
        (200.0, 10.0, 180.0),
        (150.0, 20.0, 120.0),
        (99.90, 0.0, 99.90),
        (100.0, 100.0, 0.0),
    ],
)
def test_calcular_desconto_cenarios_validos(preco, percentual, esperado):
    resultado = calcular_desconto(preco, percentual)
    assert resultado == esperado
    
@pytest.mark.parametrize("percentual", [-1.0, 101.0])
def test_percentual_invalido_deve_gerar_erro(percentual):
    with pytest.raises(ValueError, match="percentual"):
        calcular_desconto(100.0, percentual)


def test_preco_negativo_deve_gerar_erro():
    with pytest.raises(ValueError, match="preço"):
        calcular_desconto(-50.0, 10.0)