import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import json
import pandas as pd
from tqdm import tqdm
from collections import defaultdict
from utils.feature_utils import extract_features
import matplotlib.pyplot as plt
import argparse

def load_transactions(json_path):
    with open(json_path, 'r') as f:
        data = json.load(f)

    grouped = defaultdict(list)
    for txn in data:
        wallet = txn.get('userWallet')
        if wallet:
            # Extract amount from actionData
            txn['amount'] = float(txn.get('actionData', {}).get('amount', 0)) / 1e6  # for USDC (6 decimals)
            grouped[wallet].append({
                'action': txn['action'],
                'amount': txn['amount'],
                'timestamp': txn.get('timestamp', 0)
            })
    return grouped

def main(input_path, output_path):
    raw_data = load_transactions(input_path)

    # Flatten and organize
    wallet_features = []
    for wallet_address, txns in tqdm(raw_data.items()):
        features = extract_features(wallet_address, txns)
        wallet_features.append(features)

    df = pd.DataFrame(wallet_features)

    # Clip score between 0 and 1000
    df['score'] = df['score'].clip(0, 1000)
    df.to_csv(output_path, index=False)
    print(f"[✔] Wallet scores saved to {output_path}")

    # Optional: Score distribution plot
    df['score'].plot.hist(bins=10, rwidth=0.8, title='Wallet Credit Score Distribution')
    plt.xlabel('Score')
    plt.savefig('score_distribution.png')
    print("[📊] Histogram saved as score_distribution.png")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', default='data/user_transactions.json', help='Path to input JSON file')
    parser.add_argument('--output', default='wallet_scores.csv', help='Path to output CSV file')
    args = parser.parse_args()

    main(args.input, args.output)
