# 🏦 Aave V2 Wallet Credit Scoring

This project analyzes Aave V2 user wallet activity (on-chain transaction data) and calculates a **credit score (0–1000)** for each wallet based on key DeFi behavior such as deposits, borrowings, repayments, and liquidations.

It also outputs a CSV report and visualizes the distribution of scores.

---

## 📂 Project Structure

aawe-credit-score/
├── data/
│ └── user_transactions.json # ✅ Input: flat list of transactions
├── scripts/
│ └── score_wallets.py # 🔁 Main script
├── utils/
│ └── feature_utils.py # 🧠 Feature extraction logic
├── wallet_scores.csv # ✅ Output: scores per wallet
├── score_distribution.png # 📊 Histogram of scores
└── README.md


---

## ⚙️ How It Works

### ✅ Input Format (sample):
Flat list of user transactions (from Aave V2 protocol):

```json
[
  {
    "userWallet": "0xabc...",
    "action": "deposit",
    "timestamp": 1629178166,
    "actionData": {
      "amount": "2000000000",        // Amount in base units
      "assetSymbol": "USDC"
    }
  },
  ...
]
Scoring Criteria:
Each wallet is scored based on:

✅ Repayment Ratio

✅ Liquidation Penalty

✅ Deposit vs Redeem Balance

✅ Activity Score

✅ Transaction Lifetime

✅ Borrow-Deposit Behavior Ratio

Final score is scaled and clipped to 0–1000.

How to Run
1. 🔧 Install Dependencies
bash
Copy
Edit
pip install pandas matplotlib tqdm
2. 🏗️ Project Setup
Ensure this folder structure exists:

kotlin
Copy
Edit
aawe-credit-score/
├── scripts/
│   └── score_wallets.py
├── utils/
│   └── feature_utils.py
├── data/
│   └── user_transactions.json
3. ▶️ Run the Scoring Script
bash
Copy
Edit
python scripts/score_wallets.py --input data/user_transactions.json --output wallet_scores.csv
4. 📁 Output Files
wallet_scores.csv: Score breakdown for each wallet

score_distribution.png: Histogram of all scores

🧮 Feature Extraction (in utils/feature_utils.py)
The function extract_features(wallet_address, transactions) computes all key stats, such as:

repayment_ratio

liquidation_ratio

activity_score

deposit_count, borrow_count, etc.

Final score
