# Trading Algorithm

## Project Overview

DancingRedSeahorse is a simple algorithmic trading strategy designed to backtest SPY (S&P 500 ETF) trades on the QuantConnect platform. This algorithm aims to buy SPY when it’s not invested and sell it when its price fluctuates by a certain percentage.

## Project Structure

### Key Components
- **AlgorithmImports**: Includes necessary libraries and classes from QuantConnect’s algorithm framework.
- **DancingRedSeahorse Class**: Implements the trading logic, including initialization and execution during backtesting.

### Main Logic
- **initialize()**: 
    - Sets up the backtesting environment by specifying start and end dates, initial cash, and the asset (SPY) to be traded.
    - Configures data normalization and brokerage model (Interactive Brokers).
    - Defines helper variables to track entry prices and manage trading periods.

- **on_data(data)**: 
    - This method is triggered when new market data (in this case, SPY) is available.
    - If not invested, it checks whether it’s time to enter a trade (every 31 days).
    - Buys SPY when conditions are met and sells it when the price moves 10% above or below the entry price.
    - Logs all buying and selling actions.

### Parameters
- **SPY (S&P 500 ETF)**: The security traded in this algorithm.
- **Data Normalization**: Set to raw price data (no adjustment for dividends or splits).
- **Brokerage Model**: Interactive Brokers margin account is used.
- **Holding Period**: The algorithm checks for new entries every 31 days.
- **Price Fluctuation Exit**: The algorithm exits positions if the price changes by ±10% from the entry price.

## Setup Instructions

To use this algorithm:
1. Clone the repository or copy the code into your QuantConnect project.
2. Set up your QuantConnect environment and API keys.
3. Run the backtest by specifying the desired start and end dates.

## Example Logs
```bash
BUY SPY @ 420.5
SELL SPY @ 462.55
```

## License

This project is licensed under the MIT License - feel free to use and modify the code as needed.
