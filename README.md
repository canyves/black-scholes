# Black-Scholes Option Pricing Model

This repository contains a Python implementation of the Black-Scholes formula, a fundamental model used in finance to determine the theoretical price of European-style options.

## Introduction to the Black-Scholes Formula

The Black-Scholes model provides a formula for calculating the price of European call and put options. It's based on the following assumptions:
- The stock price follows a geometric Brownian motion with constant drift and volatility.
- The risk-free rate and volatility are constant.
- The markets are frictionless (no transaction costs or taxes, and the ability to short-sell without restriction).

The formula for a European call option is:

$$
C(S, t) = S_0 N(d_1) - K e^{-r(T-t)} N(d_2)
$$

And for a European put option:

$$
P(S, t) = K e^{-r(T-t)} N(-d_2) - S_0 N(-d_1)
$$

Where:
- \( C(S, t) \) and \( P(S, t) \) are the call and put option prices respectively.
- \( S \) is the current stock price.
- \( K \) is the strike price of the option.
- \( T \) is the time to maturity (in years).
- \( r \) is the risk-free interest rate.
- \( N(\cdot) \) is the cumulative distribution function of the standard normal distribution.
- \( d_1 = \frac{\ln(\frac{S}{K}) + (r + \frac{\sigma^2}{2})T}{\sigma\sqrt{T}} \)
- \( d_2 = d_1 - \sigma\sqrt{T} \)
- \( \sigma \) is the volatility of the stock’s returns.

## Implementation in Python

The repository includes a Python script (`black_scholes.py`) that implements the Black-Scholes formula. The script uses the `scipy.stats` module for calculating the cumulative normal distribution function.

## Usage

To run the script, you need Python installed on your machine along with the `scipy` package.

The script can be executed from the command line with parameters. Here's an example command:

```bash
python black_scholes.py --stock_price 100 --strike_price 110 --time_to_expiration 1 --risk_free_rate 0.05 --volatility 0.2 --option_type call
````
