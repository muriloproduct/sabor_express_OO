from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('praça', 'gourmet')
bebida_suco = Bebida('suco de melancia', 5.00, 'grande')
bebida_suco.aplicar_desconto()  # Aplicando desconto de 8%
prato_paozinho = Prato('pãozinho', 2.00, 'o melhor pão da cidade')
prato_paozinho.aplicar_desconto()  # Aplicando desconto de 5%
restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_paozinho)


def main ():
    restaurante_praca.listar_cardapio

if __name__ == "__main__":
    main()

