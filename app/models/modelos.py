from app import db

#cada classe é uma tabela no banco de dados

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    senha = db.Column(db.String(100))
    
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha
class Layout(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(30))
    cor_de_fundo = db.Column(db.String(10))
    menu_institucional = db.Column(db.Boolean)
    menu_servicos = db.Column(db.Boolean)
    menu_produtos = db.Column(db.Boolean)
    imagem = db.Column(db.String(255))
    logo = db.Column(db.String(255))
    posicao_do_menu = db.Column(db.String(20))


    def __init__(self, nome, cor_de_fundo, menu_institucional, menu_servicos, menu_produtos, imagem, logo, posicao_do_menu):
        self.nome = nome
        self.cor_de_fundo = cor_de_fundo
        self.menu_institucional = menu_institucional
        self.menu_servicos = menu_servicos
        self.menu_produtos = menu_produtos
        self.imagem = imagem
        self.logo = logo
        self.posicao_do_menu = posicao_do_menu

class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    preco = db.Column(db.Float)
    descricao = db.Column(db.Text)
    categoria_id = db.Column(db.Integer, db.ForeignKey('categoria.id'))
    imagem = db.Column(db.String(100))

    def __init__(self, nome, preco, descricao, categoria_id, imagem):
        self.nome = nome
        self.preco = preco
        self.descricao = descricao
        self.categoria_id = categoria_id
        self.imagem = imagem

class Categoria(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100))
    descricao = db.Column(db.String(100))
    tipo = db.Column(db.String(20))

    def __init__(self, nome, descricao, tipo):
        self.nome = nome
        self.descricao = descricao
        self.tipo = tipo

class Servico(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    descricao = db.Column(db.String(255))  # Aumentei o tamanho do campo para a descrição
    link_contato = db.Column(db.String(100))
    categoria = db.Column(db.String(100))  # Nome da categoria
    imagem = db.Column(db.String(100))

    def __init__(self, nome, descricao, link_contato, categoria, imagem):
        self.nome = nome
        self.descricao = descricao
        self.link_contato = link_contato
        self.categoria = categoria
        self.imagem = imagem

class Promocao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data_inicial = db.Column(db.Date)
    data_final = db.Column(db.Date)
    ativo = db.Column(db.Boolean)
    produto_id = db.Column(db.Integer, db.ForeignKey('produto.id'))

    def __init__(self, data_inicial, data_final, ativo, produto_id):
        self.data_inicial = data_inicial
        self.data_final = data_final
        self.ativo = ativo
        self.produto_id = produto_id

class Empresa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    cnpj = db.Column(db.String(20))
    endereco = db.Column(db.String(100))
    cep = db.Column(db.String(10))
    cidade = db.Column(db.String(50))
    estado = db.Column(db.String(50))
    telefone = db.Column(db.String(15))
    whats = db.Column(db.String(15))

    def __init__(self, nome, cnpj, endereco, cep, cidade, estado, telefone, whats):
        self.nome = nome
        self.cnpj = cnpj
        self.endereco = endereco
        self.cep = cep
        self.cidade = cidade
        self.estado = estado
        self.telefone = telefone
        self.whats = whats

class Pagina(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100))
    conteudo = db.Column(db.Text)
    descricao = db.Column(db.Text)

    def __init__(self, nome, conteudo, descricao):
        self.nome = nome
        self.conteudo = conteudo
        self.descricao = descricao


class FAQ(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100))
    descricao = db.Column(db.Text)
    data = db.Column(db.Date)

    def __init__(self, titulo, descricao, data):
        self.titulo = titulo
        self.descricao = descricao
        self.data = data

class Noticia(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100))
    conteudo = db.Column(db.Text)
    autor = db.Column(db.Text)
    data = db.Column(db.Date)


    def __init__(self, titulo, conteudo,autor,data):
        self.titulo = titulo
        self.conteudo = conteudo
        self.autor= autor
        self.data = data
class TabelaExemplo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    produto_id = db.Column(db.Integer, db.ForeignKey('produto.id'))

    def __init__(self, nome, produto_id):
        self.nome = nome
        self.produto_id = produto_id

class Venda(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data_venda = db.Column(db.Date)
    valor_total = db.Column(db.Float)
    obs = db.Column(db.String(100))
    obs1 = db.Column(db.String(100))
    
    def __init__(self, data_venda, valor_total, obs):
        self.data_venda = data_venda
        self.valor_total = valor_total
        self.obs = obs
      
