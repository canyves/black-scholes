import argparse
import scipy.stats as si
import math

def black_scholes(S, K, T, r, sigma, option_type='call'):
    """
    Calculate the Black-Scholes option price.

    Parameters:
    S : float
        Current stock price
    K : float
        Option strike price
    T : float
        Time to expiration in years
    r : float
        Risk-free interest rate (annual)
    sigma : float
        Volatility of the stock (annual)
    option_type : str, optional
        Type of the option - 'call' or 'put' (default is 'call')
    
    Returns:
    float
        Price of the option
    """    
    # Calculating d1 and d2
    d1 = (math.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)

    if option_type == 'call':
        # Calculating call option price
        call_price = S * si.norm.cdf(d1, 0.0, 1.0) - K * math.exp(-r * T) * si.norm.cdf(d2, 0.0, 1.0)
        return call_price
    elif option_type == 'put':
        # Calculating put option price
        put_price = K * math.exp(-r * T) * si.norm.cdf(-d2, 0.0, 1.0) - S * si.norm.cdf(-d1, 0.0, 1.0)
        return put_price
    else:
        raise ValueError("Invalid option type. Use 'call' or 'put'.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Black-Scholes Option Pricing')
    parser.add_argument('--stock_price', type=float, required=True, help='Current stock price')
    parser.add_argument('--strike_price', type=float, required=True, help='Option strike price')
    parser.add_argument('--time_to_expiration', type=float, required=True, help='Time to expiration in years')
    parser.add_argument('--risk_free_rate', type=float, required=True, help='Risk-free interest rate (annual)')
    parser.add_argument('--volatility', type=float, required=True, help='Volatility of the stock (annual)')
    parser.add_argument('--option_type', type=str, default='call', choices=['call', 'put'], help="Type of the option ('call' or 'put')")

    args = parser.parse_args()

    price = black_scholes(args.stock_price, args.strike_price, args.time_to_expiration, args.risk_free_rate, args.volatility, args.option_type)
    print(f"The {args.option_type} option price is: {price}")
    
