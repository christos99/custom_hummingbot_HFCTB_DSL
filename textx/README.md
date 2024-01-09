# Trading Strategy Configuration Grammar

## Overview
This repository contains TextX grammar definitions to configure complex trading strategies. It uses a Domain-Specific Language (DSL) for ease and flexibility, allowing the definition of strategies, parameters, indicators, and more.

## Files and Structure

### `grammar.tx`
- Central file defining the core structure of a trading strategy.
- Includes strategy information, market configuration, candles, conditions, orders.
- Uses imports to integrate `tradeParameters` and `indicators`.

### `tradeParameters.tx`
- Modular file, imported by `grammar.tx`.
- Specifies trading parameters with options for directional, PMM (Pure Market Making), and custom parameters.
- Details each parameter including name, value, description, and default setting.

### `indicators.tx`
- Another modular file, imported by `grammar.tx`.
- Describes technical indicators like RSI, MACD, Bollinger Bands, SMA, EMA, plus custom indicators.
- Details indicator-specific properties such as length, thresholds, and smoothing.

## Usage
- Define trading strategies by creating a model file following the syntax and structure outlined in `grammar.tx`.
- `grammar.tx` integrates and extends the rules from `tradeParameters.tx` and `indicators.tx`.

## Customization
- Users can mix predefined parameter sets or define custom configurations to create comprehensive trading strategies.

Refer to the detailed documentation within each file for more information on using these grammar files to define trading strategies.
