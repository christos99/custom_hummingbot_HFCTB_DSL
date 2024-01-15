# Strategy Configuration DSL

## Overview
This repository hosts the `strategy.tx`, a TextX grammar file for defining comprehensive trading strategies. It utilizes a Domain-Specific Language (DSL) for creating detailed and flexible trading strategies.

## File Description

### `strategy.tx`
- **Main Grammar File**: Integrates various components of a trading strategy.
- **Imports**: Includes `indicator` and `tradeParameters` for extended functionality.
- **Sections**:
  - `StrategyInfo`: Authorship and metadata about the strategy.
  - `MarketConfig`: Configuration for market-related parameters.
  - `Candles`: Definitions for candlestick patterns in trading.
  - `Indicators`: Technical indicators for strategy, imported from `indicator`.
  - `Conditions`: Conditions under which trades should be executed.
  - `Orders`: Order types and related actions.

### `indicator.tx`
- Defines a variety of technical indicators used in trading strategies.
- Includes indicators such as RSI, MACD, Bollinger Bands, SMA, EMA, and customizable indicators.

### `tradeParameters.tx`
- Specifies the trading parameters for different strategies like directional, PMM (Pure Market Making), and custom parameters.
- Details each parameter with attributes like name, value, description, and default settings.

### Modular Structure
- **Modularity**: Facilitates easy updates and maintenance.
- **Reusability**: Shared components are reused across different strategy definitions.

## Usage
To define a trading strategy:
1. Create a new text file following the grammar specified in `strategy.tx`.
2. Define each section with relevant details as per your strategy requirements.

Refer to each section's specific syntax and rules in `strategy.tx` for accurate strategy modeling.

## Extensions
- Customize and extend the strategy by adding new rules or modifying existing ones in the grammar files.
- Additional modules can be integrated by following the import pattern demonstrated in `strategy.tx`.

For detailed grammar syntax and rules, see the contents of `strategy.tx`, `indicator.tx`, and `tradeParameters.tx`.
