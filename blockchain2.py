# each block will have its own timestamp
import datetime

# use to hash the blocks
import hashlib

# encode blocks before hashing them
import json

# Flask class (web app), jsonify return messages in Postman
from flask import Flask, jsonify

# Part 1: build a blockchain
class Blockchain:
    
    # previous hash needs to be a string; sha256 can only accept encoded strings
    def __init__(self):
        self.chain = []  
        self.create_block(proof = 1, previous_hash = "0")
        
    # datetime.datetime.now = current time
    def create_block(self, proof, previous_hash):
        block = {'index': len(self.chain) + 1, 
                'timestamp': datetime.datetime.now(), 
                'proof': proof, 
                'previous_hash': previous_hash}    
        
        self.chain.append(block)
        return block
    
    # get the last index of the chain
    def get_previous_block(self):
        return self.chain[-1]
    
    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False
        
        while check_proof is False:
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] == '0000':
                check_proof = True
            else:
                new_proof += 1
                
        return new_proof
    
    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys = True).encode()
        return hashlib.sha256(encoded_block).hexdigest()
    
    def is_chain_valid(self, chain):
        previous_block = chain[0]
        block_index = 1
        while block_index < len(chain):
            block = chain[block_index]
            if block['previous_hash'] != self.hash(previous_block):
                return False
            previous_proof = previous_block("proof")
            proof = block['proof']
            hash_operation = hashlib.sha156(str(proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] != '0000':
                return False
            previous_block = block
            block_index +=1
        return True
        
# Part 2: mining our blockchain

# create web app
app = Flask(__name__)

# create a blockchain
blockchain = Blockchain()

# mine a new block
@app.route('/mine_block', methods=['GET'])
def mine_block():
    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)
    block = blockchain.create_block(proof, previous_hash)
    response = {'message': 'Congratulations, you just mined a block!', 
               'index': block['index'],
               'timeStamp': block['timestamp'], 
               'proof': block['proof'], 
               'previous_hash': block['previous_hash']}
    
    return jsonify(response), 200


# get the full blockchain
@app.route('/get_chain', methods=['GET'])
def get_chain():
    response = {'chain': blockchain.chain,
               'length': len(blockchain.chain)}
    
    return jsonify(response), 200

# run the app
app.run(host = '0.0.0.0', port = 5000)
