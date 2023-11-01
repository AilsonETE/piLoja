from flask import request, jsonify
from app import app, db
from app.models.modelos import Venda

# Listar todas as vendas
@app.route('/vendas', methods=['GET'])
def get_vendas():
    vendas = Venda.query.all()
    lista_vendas = []
    for venda in vendas:
        lista_vendas.append({
            'id': venda.id,
            'data_venda': venda.data_venda.strftime('%Y-%m-%d'),
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
        'data_venda': venda.data_venda.strftime('%Y-%m-%d'),
        'valor_total': venda.valor_total,
        'obs': venda.obs
    })

# Criar uma nova venda
@app.route('/vendas', methods=['POST'])
def create_venda():
    data = request.json
    nova_venda = Venda(data_venda=data['data_venda'], valor_total=data['valor_total'], obs=data['obs'])
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
