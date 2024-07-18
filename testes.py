from loja import *

comprador = Comprador(1, "Otávio", "oscandido10@gmail.com", "pass@2023")
vendedor_ = vendedor(2, "Kellyson", "kellyson.medeiros.pdf@gmail.com", "abc123")

print(comprador.get_id())
print(comprador.get_nome())
print(comprador.get_email())

garrafa = Produto(1, "Garrafa Pet", "Uma garrafa para carregar líquidos", 1.8)

vendedor_.adicionar_produto(garrafa)
vendedor_.repor_estoque(garrafa, 10)

print(vendedor_.get_produtos())
print(vendedor_.get_produtos()[0].get_estoque())

comprador.adicionar_produto_ao_carrinho(garrafa, 3)

print(comprador.get_carrinho())

venda = Venda(1, vendedor_, comprador, comprador.get_carrinho())

print(venda.gerar_comprovante())



