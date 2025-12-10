# Black-Scholes Option Pricing Simulation

## Project Summary
This project simulates the price of a stock using **Geometric Brownian Motion (GBM)** to determine the fair value of a **European** Call Option. We validated our Python simulation by comparing its results to the analytical Black-Scholes formula, achieving high accuracy, would approach 100% accuracy as the number of simulations increases.

## Simulation Results

### 1. Low Volatility (Stable Market)
*Price = $100, Volatility (σ) = 10%, Strike Price = $100, Time to Expiration (T) = 1 Year*

In a stable market, the stock price paths stay tightly clustered around the trend. The option is cheaper than a higher volatility option because there is less chance of a massive payout, even if there is a high chance of small growth.

![Low Volatility Chart](https://github.com/gshildkrot/MATH3100Project/blob/main/LowVol.png?raw=true)

**Running the simulation 10,000 times to estimate a fair option price and comparing it with the value from Black Shoals Formula:**

```text
Estimated Option Price: $5.98
True Black-Scholes Price: $5.94
Percent Error: 0.58%
```

---

### 2. High Volatility (Risky Market)
*Price = $100, Volatility (σ) = 80%, Strike Price = $100, Time to Expiration (T) = 1 Year*

The increase in price is due to the option's positive convexity. Because an option holder's loss is capped (you can't lose more than the premium) but the potential profit is theoretically unlimited, high volatility is beneficial. Extreme price swings increase the likelihood of massive payouts on the upside, while the downside remains fixed at zero.

![High Volatility Chart](https://github.com/gshildkrot/MATH3100Project/blob/main/HighVol.png?raw=true)

**Running the simulation 10,000 times to estimate a fair option price and comparing it with the value from Black Shoals Formula:**

```text
Estimated Option Price: $31.55
True Black-Scholes Price: $32.34
Percent Error: 2.43%
```

---

### 3. Real World LOW Volatility Example: Coca-Cola (KO)
*Price = $70, Volatility (σ) = 19.94% (Current Market Data), Strike Price (K) = $70, Time to Expiration (T) = 1 Year*

With volatility at just 20%, the price paths are tightly clustered. The option is cheap because the probability of a massive breakout is very low.
![KO Chart](https://github.com/gshildkrot/MATH3100Project/blob/main/KO.png?raw=true)

**Running the simulation 10,000 times to estimate a fair option price and comparing it with the value from Black Shoals Formula:**

```text
Estimated Option Price: $6.77
True Black-Scholes Price: $6.79
Percent Error: 0.29%
```

---

### 4. Real World In-Between Volatility Example: Amazon (AMZN)
*Price = $228, Volatility (σ) = 36.59% (Current Market Data), Strike Price (K) = $230, Time to Expiration (T) = 1 Year*

With volatility around 40%, the simulation shows some wild price swings, while the majority of the paths stay close together. The option premium has a high price still because there still are some cases where the stock grows dramatically, and the loss is capped. 
![AMZN Chart](https://github.com/gshildkrot/MATH3100Project/blob/main/AMZN.png?raw=true)

**Running the simulation 10,000 times to estimate a fair option price and comparing it with the value from Black Shoals Formula:**

```text
Estimated Option Price: $36.45
True Black-Scholes Price: $35.82
Percent Error: 1.75%
```
---

### 5. Real World HIGH Volatility Example: Strategy (MSTR)
*Price = $183, Volatility (σ) = 80.16% (Current Market Data), Strike Price (K) = $185, Time to Expiration (T) = 1 Year*

With volatility around 80%, the simulation shows wild price swings. The option premium is expensive because the Positive Convexity of the option captures all the upside potential while capping the downside risk.
![MSTR Chart](https://github.com/gshildkrot/MATH3100Project/blob/main/MSTR.png?raw=true)

**Running the simulation 10,000 times to estimate a fair option price and comparing it with the value from Black Shoals Formula:**

```text
Estimated Option Price: $59.86
True Black-Scholes Price: $58.59
Percent Error: 2.18%
```

---

## How to Run It
1. Install dependencies: `pip install numpy matplotlib scipy`
2. Run the code: `python black_scholes_simulation.py`










