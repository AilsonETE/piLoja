from flask import request, jsonify, make_response
from app import app, db
from sqlalchemy.exc import IntegrityError
from app.models.modelos import Usuario, Empresa, Venda, Pagina, Promocao,FAQ, Noticia, Categoria, Layout


from datetime import datetime


#Leticia

# Listar todos os usuarios
@app.route('/usuarios', methods=['GET'])
def get_usuaarios():
    usuarios = Usuario.query.all()
    
    lista_usuarios = []
    for usuario in usuarios:
        lista_usuarios.append({
            'id': usuario.id,
            'nome': usuario.nome,
            'email': usuario.email,
            'senha': usuario.senha
        })
    return jsonify(lista_usuarios)

# Obter uma venda por ID
@app.route('/usuarios/<int:usuario_id>', methods=['GET'])
def get_usuario(usuario_id):
    usuario = Usuario.query.get(usuario_id)
    if usuario is None:
        return jsonify({'error': 'Usuário não encontrado'}), 404
    return jsonify({
        'id': usuario.id,
        'nome': usuario.nome,
        'email': usuario.email,
        'senha': usuario.senha
    })

# Criar uma novo usuario
@app.route('/usuarios', methods=['POST'])
def create_usuario():
    usuario = request.json  
   
    novo_usuario = Usuario(nome=usuario['nome'], email=usuario['email'], senha=usuario['senha'])
    db.session.add(novo_usuario)
    db.session.commit()
    return jsonify({'message': 'Usuário criado com sucesso'}), 201



# Atualizar uma venda
@app.route('/usuarios/<int:usuario_id>', methods=['PUT'])
def update_usuario(usuario_id):
    usuario = Usuario.query.get(usuario_id)
    if usuario is None:
        return jsonify({'error': 'Usuário não encontrado'}), 404
    usuario = request.json
    usuario.nome = usuario['nome']
    usuario.email = usuario['email']
    usuario.senha = usuario['senha']
    db.session.commit()
    return jsonify({'message': 'Usuário atualizado com sucesso'})

# Excluir uma venda
@app.route('/usuarios/<int:usuario_id>', methods=['DELETE'])
def delete_usuario(usuario_id):
    usuario = Usuario.query.get(usuario_id)
    if usuario is None:
        return jsonify({'error': 'Usuário não encontrada'}), 404
    db.session.delete(usuario)
    db.session.commit()
    return jsonify({'message': 'Usuário excluído com sucesso'})

#end leticia

#Brenno
# Obter informações de layout por ID
@app.route('/layouts/<int:layout_id>', methods=['GET'])
def get_layout(layout_id):
    layout = Layout.query.get(layout_id)
    if layout is None:
        return jsonify({'error': 'Layout não encontrado'}), 404

    informacoes_layout = {
        'nome': layout.nome,
        'cor_de_fundo': layout.cor_de_fundo,
        'menu_institucional': layout.menu_institucional,
        'menu_servicos': layout.menu_servicos,
        'menu_produtos': layout.menu_produtos,
        'imagem': layout.imagem,
        'logo': layout.logo,
        'posicao_do_menu': layout.posicao_do_menu
    }

    return jsonify(informacoes_layout)

# Atualizar informações de layout por ID
@app.route('/layouts/<int:layout_id>', methods=['PUT'])
def update_layout(layout_id):
    layout = Layout.query.get(layout_id)
    if layout is None:
        return jsonify({'error': 'Layout não encontrado'}), 404

    data = request.json
    layout.nome = data['nome']
    layout.cor_de_fundo = data['cor_de_fundo']
    layout.menu_institucional = data['menu_institucional']
    layout.menu_servicos = data['menu_servicos']
    layout.menu_produtos = data['menu_produtos']
    layout.imagem = data['imagem']
    layout.logo = data['logo']
    layout.posicao_do_menu = data['posicao_do_menu']

    db.session.commit()

# Excluir layout por ID
@app.route('/layouts/<int:layout_id>', methods=['DELETE'])
def delete_layout(layout_id):
    layout = Layout.query.get(layout_id)
    if layout is None:
        return jsonify({'error': 'Layout não encontrado'}), 404

    db.session.delete(layout)
    db.session.commit()

    return jsonify({'message': 'Layout excluído com sucesso'})



#End Brenno


#Henrique
#Listar todas as páginas
@app.route('/paginas', methods=['GET'])
def listar_paginas():
    pagina = Pagina.query.all()
   
    lista_pagina = []
    for pagina in pagina:
        lista_pagina.append({
            'id': pagina.id,
            'nome': pagina.nome,
            'conteudo': pagina.conteudo,
            'descricao': pagina.descricao
        })
    return jsonify(lista_pagina)

#Obter uma página por ID
@app.route('/paginas/<int:pagina_id>', methods=['GET'])
def get_pagina(pagina_id):
    pagina = Pagina.query.get(pagina_id)
    if pagina is None:
        return jsonify({'error': 'Página não encontrada'}), 404
    
    return jsonify({
            'id': pagina.id,
            'nome': pagina.nome,
            'conteudo': pagina.conteudo,
            'descricao': pagina.descricao
    })

 #Criar uma nova página
@app.route('/paginas', methods=['POST'])
def create_pagina():
    pagina = request.json
    _nome = pagina['nome']
    _conteudo = pagina['conteudo']
    _descricao = pagina['descricao']
  
    nova_pagina = Pagina(nome=_nome, conteudo=_conteudo, descricao=_descricao )
    
    db.session.add(nova_pagina)
    db.session.commit()
    return jsonify({'message': 'Página criada com sucesso'}), 201



# Atualizar uma pagina
@app.route('/paginas/<int:pagina_id>', methods=['PUT'])
def update_pagina(pagina_id):
    pagina = Pagina.query.get(pagina_id)
    
    if pagina is None:
        return jsonify({'error': 'Página não encontrada'}), 404
    
    dados_pagina = request.json
    pagina.nome = dados_pagina.get('nome', pagina.nome)
    pagina.conteudo = dados_pagina.get('conteudo', pagina.conteudo)
    pagina.descricao = dados_pagina.get('descricao', pagina.descricao)

    db.session.commit()
    
    return jsonify({'message': 'Página atualizada com sucesso'})

 #Excluir uma página
@app.route('/paginas/<int:pagina_id>', methods=['DELETE'])
def delete_pagina(pagina_id):
    pagina = Pagina.query.get(pagina_id)
    
    if pagina is None:
        return jsonify({'error': 'Página não encontrada'}), 404
    
    db.session.delete(pagina)
    db.session.commit()

    return jsonify({'message': 'Página excluída com sucesso'})


#end Henrique

#Sinara
# Criar uma nova noticias
@app.route('/noticias', methods=['POST'])
def create_noticia():
    data = request.json
    
    data_str = data['data']    
    data_noticia = datetime.strptime(data_str, '%d/%m/%Y').date()
    
    nova_noticia = Noticia(data=data_noticia, autor=data['autor'], titulo=data['titulo'], conteudo=data['conteudo'])
    db.session.add(nova_noticia)
    db.session.commit()
    return jsonify({'message': 'Noticias criada com sucesso'}), 201

# Listar todas as noticias
@app.route('/noticias', methods=['GET'])
def get_noticias():
    noticias = Noticia.query.all()
    lista_noticia = []
    for noticia in noticias:
        lista_noticia.append ({
            'id': noticia.id,
            'titulo': noticia.titulo,
            'autor': noticia.autor,
            'data': noticia.data_noticia.strftime('%d/%m/%Y'),
        })
    return jsonify(lista_noticia)
#end Sinara

#listar todas as perguntas
@app.route('/faqs', methods=['GET'])
def get_faq():
    faq = FAQ.query.all()

    lista_faqs= []
    for faq in faq:
        lista_faqs.append({
            'id': faq.id,
            'titulo': faq.titulo,
            'descricao': faq.descricao,
            'data': faq.data.strftime('%d/%m/%Y'),
        })
    return jsonify(lista_faqs)

@app.route('/faqs', methods=['POST'])
def create_faq():
    data = request.json
    data_faq_str = data['data']
    
    data_faq = datetime.strptime(data_faq_str, '%d/%m/%Y').date()

    nova_faq =FAQ(titulo=data['titulo'],
                  descricao=data['descricao'],
                  data=data_faq
                  )
    db.session.add(nova_faq)
    db.session.commit()
    return jsonify({'message': 'pergunta criada com sucesso'}),201

# atualizar um pergunta
from datetime import datetime

@app.route('/faqs/<int:faq_id>', methods=['PUT'])
def update_faq(faq_id):
    faq = FAQ.query.get(faq_id)
    if faq is None:
        return jsonify({'Error': 'Pergunta não encontrada'}), 404

    data = request.json
    faq.titulo = data.get('titulo', faq.titulo)  
    faq.descricao = data.get('descricao', faq.descricao) 

    if 'data' in data:
        try:
            date_obj = datetime.strptime(data['data'], '%d/%m/%Y').date()
            faq.data = date_obj
        except ValueError:
            return jsonify({'Error': 'Formato de data inválido. Use o formato dd/mm/aaaa'}), 400

    db.session.commit()
    return jsonify({'message': 'Atualização feita com sucesso'})

    
#Excluir uma pergunta
@app.route('/faqs/<int:faq_id>', methods=['DELETE'])
def delete_faq(faq_id):
    faq = FAQ.query.get(faq_id)
    if faq is None:
        return jsonify({'Error': 'Pergunta não encontrada'}),404
    db.session.delete(faq)
    db.session.commit()
    return jsonify({'message': 'Pergunta excluida com sucesso'})

#Josuel
# Listar todas as promocao
@app.route('/promocoes', methods=['GET'] )
def list_promocoes():
    promocoes = Promocao.query.all()
    lista_promocao = []
    for pagina in promocoes:
        lista_promocao.append({
            'id': promocoes.id,
            'data_inicial': promocoes.data_inicial,
            'data_final': promocoes.data_final,
            'ativo': promocoes.ativo,
            'produto_id': promocoes.produto_id 
        })
    return jsonify(lista_promocao)
   
    
 # Rota para criar uma nova promoção
@app.route('/promocoes', methods=['POST'])
def criar_promocao():
    dados = request.json

    nova_promocao = Promocao(
        data_inicial=datetime.strptime(dados['data_inicial'], '%d/%m/%Y').date(),
        data_final=datetime.strptime(dados['data_final'], '%d/%m/%Y').date(),
        ativo=dados['ativo'],
        produto_id=dados['produto_id']
    )

    db.session.add(nova_promocao)
    db.session.commit()

    return jsonify({'mensagem': 'Promoção criada com sucesso'}), 201


# Rota para editar uma promocao 
@app.route('/promocoes/<int:promocao_id>', methods=['PUT'])
def editar_promocao(promocao_id):
    dados = request.get_json()
    promocao = dados.query.get(promocao_id)

    if promocao:
        promocao.data_inicial = dados['data_inicial']
        promocao.data_final = dados['data_final']
        promocao.ativo = dados['ativo']
        promocao.produto_id = dados['produto_id']

        db.session.commit()

        return jsonify({'mensagem': 'Promoção editada com sucesso!'})
    else:
        return jsonify({'erro': 'Promoção não encontrada'}), 404


    
   # Rota para excluir uma promoção existente
@app.route('/promocoes/<int:promocao_id>', methods=['DELETE'])
def excluir_promocao(promocao_id):
    promocao = Promocao.query.get(promocao_id)

    if promocao:
        db.session.delete(promocao)
        db.session.commit()

        return jsonify({'mensagem': 'Promoção excluída com sucesso!'})
    else:
        return jsonify({'erro': 'Promoção não encontrada'}), 404




#empresa leo
# Listar empresa
@app.route('/empresa', methods=['GET'])
def get_empresas():
    empresas = Empresa.query.all()
    
    lista_empresas = []
    for empresa in empresas:
        lista_empresas.append({
            'id': empresa.id,
            'nome': empresa.nome
            
        })
    return jsonify(lista_empresas)

# Obter uma empresa por ID
@app.route('/empresas/<int:empresa_id>', methods=['GET'])
def get_empresa(empresa_id):
    empresa = Empresa.query.get(empresa_id)
    if empresa is None:
        return jsonify({'error': 'Empresa não encontrada'}), 404
    return jsonify({
        'id': empresa.id,
        'data_empresa': empresa.data_empresa.strftime('%d/%m/%Y'),
        'valor_total': empresa.valor_total,
        'obs': empresa.obs
    })

# Criar uma nova empresa

@app.route('/empresa', methods=['POST'])
def create_empresa():
    data = request.json
   
    
    nova_empresa = Empresa(data_empresa=data_empresa, valor_total=data['valor_total'], obs=data['obs'])
    db.session.add(nova_empresa)
    db.session.commit()
    return jsonify({'message': 'Empresa criada com sucesso'}), 201


# Atualizar uma empresa
@app.route('/empresas/<int:empresa_id>', methods=['PUT'])
def update_empresa(empresa_id):
    empresa = Empresa.query.get(empresa_id)
    if empresa is None:
        return jsonify({'error': 'Empresa não encontrada'}), 404
    data = request.json
    empresa.data_empresa = data['data_empresa']
    empresa.valor_total = data['valor_total']
    empresa.obs = data['obs']
    db.session.commit()
    return jsonify({'message': 'Empresa atualizada com sucesso'})

# Excluir uma empresa
@app.route('/empresas/<int:empresa_id>', methods=['DELETE'])
def delete_empresa(empresa_id):
    empresa = Empresa.query.get(empresa_id)
    if empresa is None:
        return jsonify({'error': 'Empresa não encontrada'}), 404
    db.session.delete(empresa)
    db.session.commit()
    return jsonify({'message': 'Empresa excluída com sucesso'})



# Listar todas as vendas
@app.route('/vendas', methods=['GET'])
def get_vendas():
    vendas = Venda.query.all()
    
    lista_vendas = []
    for venda in vendas:
        lista_vendas.append({
            'id': venda.id,
            'data_venda': venda.data_venda.strftime('%d/%m/%Y'),
            'valor_total': venda.valor_total,
            'obs': venda.obs
        })
    return jsonify(lista_vendas)

# Obter uma venda por ID
@app.route('/vendas/<int:venda_id>', methods=['GET'])
def get_venda(venda_id):
    venda = Venda.query.get(venda_id)
    if venda is None:
        return jsonify({'error': 'Venda não encontrada'}), 404
    return jsonify({
        'id': venda.id,
        'data_venda': venda.data_venda.strftime('%d/%m/%Y'),
        'valor_total': venda.valor_total,
        'obs': venda.obs
    })

# Criar uma nova venda
@app.route('/vendas', methods=['POST'])
def create_venda():
    data = request.json
    data_venda_str = data['data_venda']
  
    data_venda = datetime.strptime(data_venda_str, '%d/%m/%Y').date()
    
    nova_venda = Venda(data_venda=data_venda, valor_total=data['valor_total'], obs=data['obs'])
    db.session.add(nova_venda)
    db.session.commit()
    return jsonify({'message': 'Venda criada com sucesso'}), 201



# Atualizar uma venda
@app.route('/vendas/<int:venda_id>', methods=['PUT'])
def update_venda(venda_id):
    venda = Venda.query.get(venda_id)
    if venda is None:
        return jsonify({'error': 'Venda não encontrada'}), 404
    data = request.json
    venda.data_venda = data['data_venda']
    venda.valor_total = data['valor_total']
    venda.obs = data['obs']
    db.session.commit()
    return jsonify({'message': 'Venda atualizada com sucesso'})

# Excluir uma venda
@app.route('/vendas/<int:venda_id>', methods=['DELETE'])
def delete_venda(venda_id):
    venda = Venda.query.get(venda_id)
    if venda is None:
        return jsonify({'error': 'Venda não encontrada'}), 404
    db.session.delete(venda)
    db.session.commit()
    return jsonify({'message': 'Venda excluída com sucesso'})

# Listar todas as categorias
@app.route('/categoria', methods=['GET'])
def get_categorias():
    categorias = Categoria.query.all()
    
    lista_categorias = []
    for c in categorias:
        lista_categorias.append({
            'id': c.id,
            'nome': c.nome,
            'descricao': c.descricao,
            'tipo': c.tipo,
        })
    return jsonify(lista_categorias)

@app.route('/categoria', methods=['POST'])
def create_categoria():
    data = request.json
    _nome = data['nome']
    _descricao = data['descricao']
    _tipo = data['tipo']    
    categoria = Categoria(nome=_nome, descricao=_descricao, tipo=_tipo)
    db.session.add(categoria)
    db.session.commit()
    return jsonify({'status': 201, 'message': 'Categoria criada com sucesso'}), 201


# Excluir uma categoria
@app.route('/categoria/<int:categoria_id>', methods=['DELETE'])
def delete_categoria(categoria_id):
    categoria = Categoria.query.get(categoria_id)
    if categoria is None:
        return jsonify({'error': 'Categoria não encontrada'}), 404
    db.session.delete(categoria)
    db.session.commit()
    return jsonify({'message': 'Categoria excluída com sucesso'})
