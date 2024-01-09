# Trading Strategy Configuration Grammar

## Overview
This repository contains the TextX grammar definitions for configuring trading strategies, parameters, and indicators. It allows the definition of complex trading strategies using a Domain-Specific-Language (DSL) crafted for ease of use and flexibility.

## Files

### `grammar.tx`
Defines the core structure for a trading strategy, including authorship, market configuration, parameters for trade, candles, indicators, conditions for trading signals, and order specifications.

### `tradeParameters.tx`
Specifies the trading parameters with options for directional, PMM (Pure Market Making), and custom parameters. Each parameter is detailed with its name, value, description, and default setting.

### `indicators.tx`
Describes various technical indicators used in trading strategies, such as RSI, MACD, Bollinger Bands, SMA, EMA, and custom indicators. It includes properties like length, thresholds, and smoothing factors.

## Grammar Structure
The grammar allows for a flexible composition of trading strategies, where users can mix predefined parameter sets or define their own. Conditions and orders are specified to create a comprehensive strategy.

## Customization
Users can extend the predefined parameters and indicators by adding their custom configurations as needed.

For more information on how to use these grammar files to define your trading strategies, refer to the detailed documentation within each file.
