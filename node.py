from flask import Flask, jsonify, request
from blockchain import Blockchain
from encryption import encrypt, decrypt
from uuid import uuid4

app = Flask(__name__)
node_address = str(uuid4()).replace('-', '')
blockchain = Blockchain()

@app.route('/mine_block', methods=['GET'])
def mine_block():
    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)
    blockchain.add_transaction(sender=node_address, receiver='Miner_Reward', amount=1)
    block = blockchain.create_block(proof, previous_hash)
    response = {'message': 'Block mined successfully!', 'block': block}
    return jsonify(response), 200

@app.route('/add_transaction', methods=['POST'])
def add_transaction():
    data = request.get_json()
    required_fields = ['sender', 'receiver', 'amount']
    if not all(field in data for field in required_fields):
        return 'Some fields are missing', 400
    index = blockchain.add_transaction(data['sender'], data['receiver'], data['amount'])
    response = {'message': f'Transaction will be added to Block {index}'}
    return jsonify(response), 201

@app.route('/connect_node', methods=['POST'])
def connect_node():
    data = request.get_json()
    nodes = data.get('nodes')
    if nodes is None:
        return "No nodes to connect", 400
    for node in nodes:
        blockchain.add_node(node)
    response = {'message': 'Nodes connected successfully.', 'total_nodes': list(blockchain.nodes)}
    return jsonify(response), 201

@app.route('/replace_chain', methods=['GET'])
def replace_chain():
    is_chain_replaced = blockchain.replace_chain()
    if is_chain_replaced:
        response = {'message': 'The chain was replaced.', 'new_chain': blockchain.chain}
    else:
        response = {'message': 'The chain is the largest.', 'chain': blockchain.chain}
    return jsonify(response), 200

@app.route('/get_chain', methods=['GET'])
def get_chain():
    response = {'chain': blockchain.chain, 'length': len(blockchain.chain)}
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)