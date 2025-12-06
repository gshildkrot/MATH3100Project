# Black-Scholes Project

## Overview
This project simulates stock prices and calculates the value of a Call Option using the Black-Scholes model. We use Python to run a simulate thousands of simulations and compare the result to the actual formula.

## What the Code Does
1.  **Generates Stock Paths:** We use Geometric Brownian Motion (GBM) to simulate how a stock price moves over 1 year.
2.  **Visualizes Risk:** It plots 10 different random paths to show how volatility affects price.
3.  **Prices the Option:** It runs 10,000 simulations to find the fair price of a European Call Option.
4.  **Checks Accuracy:** It compares our simulation result with the true Black-Scholes formula to calculate the error.

## How to Experiment with Results
You can change the stock market conditions by editing the **PARAMETERS** section at the top of the Python file.

## How to Run It
You need Python installed on your computer along with a few standard libraries.

1.  **Install the requirements:**
    ```bash
    pip install numpy matplotlib scipy
    ```

2.  **Run the simulation:**
    (Make sure your file is named `main.py` or change the name below)
    ```bash
    python main.py
    ```

## Example Output
When you run the code, a graph will pop up showing the random stock paths. In the console, you will see:

```text
Estimated Option Price: $10.42
True Black-Scholes Price: $10.45