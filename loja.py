
from usuarios import Usuario

class Produto:
    def __init__(self, id, nome, descricao, preco) -> None:
        self.__id = id
        self.__nome = nome
        self.__descricao = descricao
        self.__preco = preco
        self.__estoque = 0

    def get_id(self):
        return self.__id
    
    def get_nome(self):
        return self.__nome
    
    def set_nome(self, nome):
        self.__nome = nome
    
    def get_descricao(self):
        return self.__descricao
    
    def set_descricao(self, descricao):
        self.__descricao = descricao

    def get_preco(self):
        return self.__preco
    
    def set_preco(self, preco):
        self.__preco = preco

    def get_estoque(self):
        return self.__estoque
    
    def set_estoque(self, estoque):
        self.__estoque = estoque

class Pedido:
    def __init__(self, id, produto, quantidade):
        self.__id = id
        self.__produto = produto
        self.__quantidade = quantidade
    
    def consultar_preco(self):
        return self.__produto.get_preco() * self.__quantidade

    def get_id(self):
        return self.__id
    
    def get_produto(self):
        return self.__produto
    
    def get_quantidade(self):
        return self.__quantidade

class vendedor(Usuario):
    def __init__(self, id, nome, email, senha):
        super().__init__(id, nome, email, senha)
        self.__produtos = []
    def adicionar_produto(self, produto):
        self.__produtos.append(produto)
    
    def repor_estoque(self, produto, quantidade):
        produto.set_estoque(produto.get_estoque() + quantidade)

    def get_produtos(self):
        return self.__produtos
    
class Comprador(Usuario):
    def __init__(self, id, nome, email, senha):
        super().__init__(id, nome, email, senha)
        self.__carrinho = []

    def get_carrinho(self):
        return self.__carrinho
    
    def adicionar_produto_ao_carrinho(self, produto):
        self.__carrinho.append(produto)

    def finalizar_compra(self):
        self.__carrinho.clear()