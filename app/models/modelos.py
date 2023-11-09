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
    nome = db.Column(db.String(100))
    endereco = db.Column(db.String(100))

    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco

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
    id = db.Column(db.Integer, primary_key=True)
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
    descricao = db.Column(db.String(100))
    categoria_id = db.Column(db.Integer, db.ForeignKey('categoria.id'))
    imagem = db.Column(db.String(100))

    def __init__(self, nome, descricao, categoria_id, imagem):
        self.nome = nome
        self.descricao = descricao
        self.categoria_id = categoria_id
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
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    conteudo = db.Column(db.Text)

    def __init__(self, nome, conteudo):
        self.nome = nome
        self.conteudo = conteudo

class FAQ(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100))
    descricao = db.Column(db.Text)

    def __init__(self, titulo, descricao):
        self.titulo = titulo
        self.descricao = descricao

class Noticia(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100))
    conteudo = db.Column(db.Text)

    def __init__(self, titulo, conteudo):
        self.titulo = titulo
        self.conteudo = conteudo

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
      
