# language: pt
  Funcionalidade: Essa funcionalidade ira adicionar um item no carrinho

    Cenario: Adicionar um colar ao carrinho
      Dado que acesso a loja virtual Nox Joias
      Quando selecionado o produto "Colar Medalha Menino/Menina 5463"
      E selecionado o genero "Menina"
      E clicar no botão "Comprar"
      Então o valor total do carrinho de compras deve ser R$ "125",00