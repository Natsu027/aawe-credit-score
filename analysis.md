
# 📊 Wallet Credit Score Analysis

This report analyzes Aave V2 wallet activity and resulting credit scores (0–1000), computed based on deposit, borrow, repay, redeem, and liquidation behavior.

---

## 📈 Score Distribution by Range

Wallets have been grouped into 100-point score bins:

```
0-99         13
100-199       7
200-299       7
300-399     211
400-499    1319
500-599     588
600-699     281
700-799     392
800-899     262
900-999     417
```

![Score Distribution by Range](score_distribution_binned.png)

---

## ⚠️ Behavior of Wallets with Lower Scores (0–300)

Wallets in this group typically exhibit:

- High liquidation rates per borrow
- Very low or no repayments
- Minimal transaction activity (low number of total txns)
- Short wallet activity duration (in days)
- Poor borrow-to-deposit and repay-to-borrow ratios

### 📉 Summary Statistics (Score ≤ 300)
```
       deposit_count  borrow_count  repay_count  redeem_count  liquidation_count  deposit_amount  borrow_amount  repay_amount  redeem_amount  repayment_ratio  liquidation_ratio  activity_score  lifetime_days   score
count          27.00         27.00        27.00         27.00              27.00    2.700000e+01   2.700000e+01  2.700000e+01   2.700000e+01            27.00              27.00           27.00          27.00   27.00
mean            2.81          2.41         0.44          0.48               2.70    5.009423e+15   4.627855e+14  1.559786e+14   1.891602e+14             0.08               1.39            0.09          37.63  119.39
std             2.50          2.19         0.75          1.05               2.25    2.078604e+16   1.557535e+15  8.082071e+14   8.691917e+14             0.24               0.97            0.07          25.44  102.91
min             0.00          1.00         0.00          0.00               1.00    0.000000e+00   3.000000e-02  0.000000e+00   0.000000e+00             0.00               0.25            0.03           1.35    0.00
25%             1.00          1.00         0.00          0.00               1.00    5.766149e+11   3.950200e+02  0.000000e+00   0.000000e+00             0.00               1.00            0.05          19.42   11.13
50%             2.00          2.00         0.00          0.00               2.00    2.179230e+13   1.800000e+07  0.000000e+00   0.000000e+00             0.00               1.00            0.07          32.38  114.00
75%             3.00          2.00         1.00          0.00               3.50    2.112313e+14   7.500000e+13  8.233000e+01   0.000000e+00             0.00               1.50            0.11          57.67  202.08
max            11.00          9.00         2.00          4.00              11.00    1.078000e+17   7.136000e+15  4.200000e+15   4.500000e+15             1.00               4.00            0.33          96.58  297.33
```

---

## 🌟 Behavior of Wallets with Higher Scores (700–1000)

Wallets in the top score bands show strong creditworthiness:

- Very low or zero liquidation events
- High repayment ratios (close to or at 1.0)
- Balanced or high redeem-to-deposit ratios
- Long wallet lifetime (more days active)
- High transaction volume and healthy borrow/deposit behavior

### 📈 Summary Statistics (Score ≥ 700)
```
       deposit_count  borrow_count  repay_count  redeem_count  liquidation_count  deposit_amount  borrow_amount  repay_amount  redeem_amount  repayment_ratio  liquidation_ratio  activity_score  lifetime_days    score
count        1071.00       1071.00      1071.00       1071.00            1071.00    1.071000e+03   1.071000e+03  1.071000e+03   1.071000e+03          1071.00            1071.00         1071.00        1071.00  1071.00
mean           28.76         12.35        10.50         13.18               0.07    1.922535e+17   1.504670e+17  9.702954e+16   1.315099e+17             0.70               0.00            0.40          45.89   856.72
std            48.57         24.09        22.31         24.04               0.86    2.208482e+18   1.695449e+18  1.517069e+18   2.066894e+18             0.42               0.03            0.36          39.28   110.86
min             0.00          0.00         0.00          0.00               0.00    0.000000e+00   0.000000e+00  0.000000e+00   0.000000e+00             0.00               0.00            0.02           0.00   702.67
25%             4.00          1.00         1.00          2.00               0.00    5.083389e+13   5.014000e+02  2.997900e+02   4.952422e+08             0.22               0.00            0.09           7.86   756.70
50%            10.00          3.00         3.00          5.00               0.00    1.227004e+15   8.000001e+11  1.975528e+05   2.410686e+14             1.00               0.00            0.25          40.04   843.49
75%            32.00         13.00        10.00         13.00               0.00    8.091788e+15   1.350530e+15  8.850274e+14   4.543539e+15             1.00               0.00            0.72          77.97   993.01
max           511.00        200.00       291.00        234.00              26.00    5.283732e+19   3.496460e+19  3.500300e+19   5.287256e+19             1.00               0.50            1.00         153.79  1000.00
```

---

## 📌 Conclusion

This scoring system can serve as a creditworthiness indicator for DeFi wallets. Wallets with higher scores display healthier financial behavior, making them potential candidates for undercollateralized lending or financial incentives. Lower scoring wallets indicate high risk and less responsible borrowing patterns.

Future extensions can include machine learning to further enhance risk assessment and integrate real-time on-chain analytics.
