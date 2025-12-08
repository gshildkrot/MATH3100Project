# Black-Scholes Option Pricing Simulation

## Project Summary
This project simulates the price of a stock using **Geometric Brownian Motion (GBM)** to determine the fair value of a **European** Call Option. We validated our Python simulation by comparing its results to the analytical Black-Scholes formula, achieving high accuracy, would approach 100% accuracy as the number of simulations increases.

## Simulation Results

### 1. Low Volatility (Stable Market)
*Parameters: Price = $100, Volatility (σ) = 10%, Strike Price = $100*

In a stable market, the stock price paths stay tightly clustered around the trend. The option is cheaper than a higher volatility option because there is less chance of a massive payout, even if there is a high chance of small growth.

![Low Volatility Chart](https://github.com/gshildkrot/MATH3100Project/blob/main/LowVol.png?raw=true)

**Running the simulation 10,000 times to estimate a fair option price and comparing it with the real value from the formula:**

```text
Estimated Option Price: $30.31
True Black-Scholes Price: $30.31
Percent Error: 0.01%
```

---

### 2. High Volatility (Risky Market)
*Parameters: Price = $100, Volatility (σ) = 80%, Strike Price = $100*

In a highly volatile market, the price swings wildly. The option is more expensive because there is a higher chance the stock could skyrocket (even if it could also crash).

![High Volatility Chart](https://github.com/gshildkrot/MATH3100Project/blob/main/HighVol.png?raw=true)

**Running the simulation 10,000 times to estimate a fair option price and comparing it with the real value from the formula:**

```text
Estimated Option Price: $43.69
True Black-Scholes Price: $44.00
Percent Error: 0.71%
```
---

### 3. Real World Example: Amazon (AMZN)
*Parameters: Price = $227, Volatility (σ) = 36.72% (Current Market Data), Strike Price (K) = $230*

This is a real-world example of this simulation (no longer using dummy variables). In this case, the option is expensive, as the stock is expensive but also has a relatively high chance of growing rapidly.

![AMZN Chart](https://github.com/gshildkrot/MATH3100Project/blob/main/AMZN.png?raw=true)

```text
Estimated Option Price: $73.15
True Black-Scholes Price: $73.08
Percent Error: 0.09%
```

---

## How to Run It
1. Install dependencies: `pip install numpy matplotlib scipy`
2. Run the code: `python black_scholes_simulation.py`
