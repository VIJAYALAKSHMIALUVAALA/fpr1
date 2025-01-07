# Blockchain Project
## Folder Structure
blockchain_project/
├── app/
│   ├── blockchain.py
│   ├── encryption.py
│   ├── node.py
├── example_requests/
│   ├── add_transaction.json
│   ├── connect_nodes.json
├── run_node.sh
├── requirements.txt
├── README.md

## Setup Instructions
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run a node:
   ```bash
   ./run_node.sh 5000
   ```

## API Endpoints
- `/mine_block`: Mines a new block.
- `/add_transaction`: Adds a transaction (POST).
- `/connect_node`: Connects nodes (POST).
- `/replace_chain`: Replaces the chain with the longest valid chain.
- `/get_chain`: Retrieves the blockchain.