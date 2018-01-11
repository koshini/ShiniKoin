from logging_helper import setup_logger
from datetime import datetime
import hashlib


def main():
    setup_logger()

    # Create the blockchain and add the genesis block
    blockchain = [create_genesis_block()]
    previous_block = blockchain[0]

    num_of_blocks = 20

    # Add blocks to the chain
    for i in range(0, num_of_blocks):
        new_block = next_block(previous_block)
        blockchain.append(new_block)
        previous_block = new_block
        print("Block " + str(new_block.index))

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def hash_block(self):
        sha = hashlib.sha256()
        sha.update((str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash)).encode('utf-8'))
        return sha.hexdigest()

def create_genesis_block():
    # Create the first block with index zero and arbitrary previous hash
    return Block(0, datetime.now(), "Genesis Block", "0")

def next_block(last_block):
    this_index = last_block.index + 1
    this_timestamp = datetime.now()
    this_data = "Hey! I'm block " + str(this_index)
    this_hash = last_block.hash
    return Block(this_index, this_timestamp, this_data, this_hash)

if __name__ == "__main__":
    main()
