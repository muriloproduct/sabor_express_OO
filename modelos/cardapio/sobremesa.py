from modelos.cardapio.item_cardapio import ItemCardapio

class Sobremesa(ItemCardapio):
    def __init__(self, nome, preco, tamanho, descricao, tipo):
        super().__init__(nome, preco)
        self._tamanho = tamanho
        self._tipo = tipo
        self._descricao = descricao

    def __str__(self):
        return self._nome
    
    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.15) # Aplicando 15% de desconto

    
