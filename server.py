from flask import Flask, jsonify, request
from uuid import uuid4

from blockchain import Blockchain

app = Flask(__name__)

node_identifier = str(uuid4()).replace('-', '')

blockchain = Blockchain()


@app.route('/mine', methods=['GET'])
def mine():
    return 'We will mine a new block'


@app.route('/transaction', methods=['POST'])
def new_transaction():
    values = request.get_json() or []
    required = ('sender', 'recipient', 'amount')
    if not all(k in values for k in required):
        return 'Missing values', 400

    # Add new transaction
    index = blockchain.add_new_transaction(**values)
    resp = {'msg': f'Transaction will be added to block #{index}'}

    return jsonify(resp), 201


@app.route('/chain', methods=['GET'])
def full_chain():
    resp = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain)
    }

    return jsonify(resp), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
