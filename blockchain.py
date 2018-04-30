
class Blockchain:

    def __init__(self):
        self.chain = []
        self.current_transactions = []

    def create_new_block(self):
        # Generates a new block and adds its to the chain
        pass

    def add_new_transaction(self):
        # Adds a new transaction to the list of transactions
        pass

    @staticmethod
    def get_hash(block):
        # Hashes a block
        pass

    @property
    def last_block(self):
        # Returns the last block of the chain
        return None
