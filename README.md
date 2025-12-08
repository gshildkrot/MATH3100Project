# Black-Scholes Option Pricing Simulation

## Project Summary
This project simulates the price of a stock using **Geometric Brownian Motion (GBM)** to determine the fair value of a Call Option. We validated our Python simulation by comparing its results to the analytical Black-Scholes formula, achieving near-perfect accuracy.

## Simulation Results

### 1. Low Volatility (Stable Market)
*Parameters: Volatility ($\sigma$) = 10%*
In a stable market, the stock price paths stay tightly clustered around the trend. The option is cheaper because there is less chance of a massive payout.

![[Low Volatility Chart](https://github.com/gshildkrot/MATH3100Project/blob/main/LowVol.png)]

---

### 2. High Volatility (Risky Market)
*Parameters: Volatility ($\sigma$) = 80%*
In a highly volatile market, the price swings wildly. The option is much more expensive because there is a higher chance the stock could skyrocket (even if it could also crash).

![High Volatility Chart](https://github.com/gshildkrot/MATH3100Project/blob/main/HighVol.png)

---

### 3. Real World Example: Amazon (AMZN)
*Parameters: Price = $227, Volatility ($\sigma$) = 36.72% (Current Market Data), Skrike Price (K) = 230*
We simulated 10,000 paths for Amazon stock over the next year to price an "At-the-Money" Call Option.

![AMZN Chart](https://github.com/gshildkrot/MATH3100Project/blob/main/AMZN.png)

---

## How to Run It
1. Install dependencies: `pip install numpy matplotlib scipy`
2. Run the code: `python black_scholes_simulation.py`
