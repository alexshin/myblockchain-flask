import hashlib
import json
from time import time


class Blockchain:

    def __init__(self, difficulty_sequence='000'):
        self.chain = []
        self.current_transactions = []

        # Add the first (genesis) block
        self.create_new_block(proof=1000, previous_hash=1)

    def create_new_block(self, proof, previous_hash=None):
        """
        Generates a new block and adds its to the chain
        :param proof: <int> The proof given by the PoW algorithm
        :param previous_hash: (optional) <str> Hash of previous Block
        :return: <dict> New block
        """

        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.get_hash(self.chain[-1])
        }

        # Clear list of current transactions
        self.current_transactions = []

        self.chain.append(block)

        return block

    def add_new_transaction(self, sender, recipient, amount):
        """
        Adds a new transaction to the list of transactions to go into the next mined block
        :param sender: <str> Address of sender
        :param recipient: <str> Address of recipient
        :param amount: <int> Amount of coins
        :return: <int> The index of block where transaction will be stored
        """
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        })

        return self.last_block['index'] + 1

    @staticmethod
    def get_hash(block):
        """
        Hashes a block using SHA-256 hash algorithm
        :param block: <dict> Block
        :return: <str> Hash string
        """
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hex_digest()

    @property
    def last_block(self):
        """
        Returns the last block of the chain
        :return: <str> The last block of the chain
        """
        return self.chain[-1]

    # Proof-of-Work implementation

    @staticmethod
    def valid_proof(last_proof, proof):
        """
        Validates valid of proof
        :param last_proof: <int>
        :param proof: <int>
        :return: <boolean>
        """
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()

        return guess_hash[:4] == '0000'

    def do_proof_of_work(self, last_proof):
        """
        Does work while mining is not finished
        :param last_proof: <int>
        :return: <int>
        """
        proof = 0
        while self.valid_proof(last_proof=last_proof, proof=proof) is False:
            proof = proof + 1

        return proof
