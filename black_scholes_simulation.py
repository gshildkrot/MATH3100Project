import numpy as np
import matplotlib.pyplot as plt

# Assume that the options are EUROPEAN 

# PARAMETERS
S0 = 100        # Current Price ($)
K = 100         # Strike Price ($)
T = 1.0         # Time to maturity (1 Year)
r = 0.05        # Interest rate (5%)
sigma = 0.2     # Volatility (20%)
steps = 252     # Trading days in a year
dt = T / steps  # Time step size

# DRAWING THE PATHS
num_paths = 10
all_paths = []

for i in range(num_paths):
    path = [S0]
    current_price = S0
    
    for day in range(steps):
        Z = np.random.normal(0, 1)
        
        # Calculate the change in price using the GBM formula
        drift = (r - 0.5 * sigma**2) * dt
        shock = sigma * np.sqrt(dt) * Z
        
        # Update the price
        current_price = current_price * np.exp(drift + shock)
        path.append(current_price)
        
    all_paths.append(path)

# PLOT THE PATHS
plt.figure(figsize=(10, 6))
for path in all_paths:
    plt.plot(path)

plt.title("Stock Price Simulation (GBM)")
plt.xlabel("Days")
plt.ylabel("Price ($)")
plt.axhline(y=K, color='r', linestyle='--', label='Strike Price')
plt.legend()
plt.show()

# PRICING THE OPTION
num_sims = 10000
payoffs = []

for i in range(num_sims):
    Z = np.random.normal(0, 1)
    drift_total = (r - 0.5 * sigma**2) * T
    shock_total = sigma * np.sqrt(T) * Z
    
    final_price = S0 * np.exp(drift_total + shock_total)
    payoff = max(final_price - K, 0)
    payoffs.append(payoff)

average_payoff = np.mean(payoffs)
option_price = average_payoff * np.exp(-r * T)

print(f"Estimated Option Price: ${option_price:.2f}")

# CHECK ANSWER
from scipy.stats import norm

d1 = (np.log(S0/K) + (r + 0.5*sigma**2)*T) / (sigma*np.sqrt(T))
d2 = d1 - sigma*np.sqrt(T)
true_price = S0 * norm.cdf(d1) - K * np.exp(-r*T) * norm.cdf(d2)


print(f"True Black-Scholes Price: ${true_price:.2f}")
print(f"Percent Error: {abs(true_price - option_price) / true_price * 100:.2f}%")
