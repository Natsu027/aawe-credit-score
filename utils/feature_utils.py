def extract_features(wallet_address, transactions):
    deposit_amount = 0
    borrow_amount = 0
    repay_amount = 0
    redeem_amount = 0
    liquidations = 0

    deposit_count = borrow_count = repay_count = redeem_count = liquidation_count = 0
    timestamps = []

    for txn in transactions:
        action = txn.get('action', '').lower()
        amount = float(txn.get('amount', 0))
        timestamp = int(txn.get('timestamp', 0))
        timestamps.append(timestamp)

        if action == 'deposit':
            deposit_amount += amount
            deposit_count += 1
        elif action == 'borrow':
            borrow_amount += amount
            borrow_count += 1
        elif action == 'repay':
            repay_amount += amount
            repay_count += 1
        elif action == 'redeemunderlying':
            redeem_amount += amount
            redeem_count += 1
        elif action == 'liquidationcall':
            liquidations += 1
            liquidation_count += 1

    num_txns = len(transactions)
    liquidation_ratio = liquidation_count / (borrow_count + 1e-6)
    repayment_ratio = min(repay_amount / (borrow_amount + 1e-6), 1)
    deposit_redeem_ratio = min(redeem_amount / (deposit_amount + 1e-6), 1)

    # Time features
    if len(timestamps) > 1:
        timestamps.sort()
        lifetime_days = (max(timestamps) - min(timestamps)) / 86400
    else:
        lifetime_days = 0

    activity_score = min(num_txns / 100, 1)  # Scaled

    # Score formula
    score = (
        300 * (1 - liquidation_ratio)
        + 200 * repayment_ratio
        + 100 * deposit_redeem_ratio
        + 200 * activity_score
        + 100 * (deposit_count / (borrow_count + 1))
        + 100 * (repay_count / (borrow_count + 1))
    )

    return {
        'wallet': wallet_address,
        'deposit_count': deposit_count,
        'borrow_count': borrow_count,
        'repay_count': repay_count,
        'redeem_count': redeem_count,
        'liquidation_count': liquidation_count,
        'deposit_amount': deposit_amount,
        'borrow_amount': borrow_amount,
        'repay_amount': repay_amount,
        'redeem_amount': redeem_amount,
        'repayment_ratio': repayment_ratio,
        'liquidation_ratio': liquidation_ratio,
        'activity_score': activity_score,
        'lifetime_days': lifetime_days,
        'score': round(score, 2),
    }
