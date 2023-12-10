# Language.py - Strategy Configuration Parser

**language.py** is a Python script designed to parse YAML configuration files used to define trading strategies. This script provides a structured way to read and validate strategy configurations, making it easier to work with trading algorithms and their parameters.

## Key Functionalities

- **Strategy Class**: Represents a trading strategy with attributes such as name, version, type, author, and more. It validates strategy attributes and converts them to the appropriate data types.

- **Market Class**: Represents market-related information for a strategy, including the connector and trading pairs. It ensures consistent formatting and validation of market data.

- **Parameter Class**: Represents configurable parameters for a strategy, including name, type, description, and default values. It handles dynamic reconfiguration and user prompts for parameter changes.

- **ExchangeConfig Class**: Represents API key and secret information for connecting to cryptocurrency exchanges.

- **YAML Parsing**: Provides a `load_yaml` function to read and parse YAML files, handling potential errors. It parses the YAML data to create instances of the Strategy, Market, and Parameter classes.

- **Command-Line Interface**: Accepts a command-line argument specifying the path to the strategy YAML file. It displays parsed strategy information and validates the configuration.

**language.py** serves as a valuable tool for traders and developers to define, validate, and work with trading strategies in a structured and organized manner. It enhances the reliability and consistency of strategy configurations for cryptocurrency trading.

---

# Validate.py - Strategy Validation Script

**validate.py** is a Python script designed to validate trading strategy configurations defined in YAML files. It imports the `parse_strategy` function from the `language.py` module to parse and validate strategy configurations.

## Key Functionalities

1. **YAML File Loading**: The script loads a specified YAML file containing a trading strategy configuration. It handles potential errors such as file not found or YAML parsing issues.

2. **Validation of Strategy**: It validates the structure and content of the strategy configuration, ensuring that all required fields are present and correctly formatted. These required fields include `name`, `version`, `type`, `author`, `author_email`, `description`, `labels`, and `markets`. Additionally, it verifies that the `type` of the strategy is one of the recognized types ('StrategyBase', 'Script', 'PMM', 'LM').

3. **Validation of Markets**: If the strategy configuration includes market-related information, the script validates each market's `connector` and trading `pairs`. It checks that the `connector` is one of the valid options ('binance', 'kucoin', 'ascent_ex', 'gate_io') and ensures that `pairs` are defined.

4. **Validation of Parameters**: The script checks the parameters defined within the strategy configuration. It validates the presence and format of required fields such as `name`, `type`, `description`, `prompt_msg`, `default`, `keyword`, `dynamic_reconfigure`, and `prompt_on_new`. It also verifies that the `type` of each parameter is one of the recognized types ('int', 'float', 'str', 'bool', 'list', 'dict').

5. **Display Validation Results**: After parsing and validating the strategy, markets, and parameters, the script prints validation messages for each component, indicating whether they are valid or if any issues are found.

6. **Command-Line Interface**: The script is designed to be run from the command line and accepts a single command-line argument, which is the path to the strategy YAML file that needs to be validated.

**validate.py** provides a valuable tool for traders and developers to ensure the correctness and consistency of trading strategy configurations. It helps identify and rectify issues in strategy definitions, ultimately enhancing the reliability of trading algorithms.


# Generator.py - Generator Script 

## Overview
The `generator.py` script is a fundamental component of the DSL (Domain-Specific Language) pipeline for Hummingbot strategies. Its primary purpose is to automate the process of generating executable trading strategy scripts from YAML configuration files.

## Functionality
1. **Validation**: The script initiates the process by validating the YAML strategy configuration file. This is accomplished by calling the `validate_and_save_strategy` function from `validator.py`. If the strategy fails validation, the script aborts, ensuring that only valid strategies are processed.

2. **Loading Strategy Data**: After successful validation, the script proceeds to read the strategy data from the YAML file. This includes various strategy parameters, market settings, and other pertinent information.

3. **Template Rendering**: To dynamically generate a trading strategy script based on the loaded strategy data, the script employs Jinja2 templating. It populates a predefined template (`strategy_template.j2`) with the specific details of the strategy.

4. **Output**: The final rendered script is both displayed in the console and saved to a file. The filename is derived from the original YAML file but is appended with `_script.py` to indicate its executable nature.

5. **Flexibility**: This approach offers a high degree of flexibility and customization in strategy creation. Any changes to the strategy can be made by editing the YAML configuration file, eliminating the need to directly modify complex Python code.

## Usage
Run the script by specifying the path to the YAML strategy file:

```bash
python generator.py /path/to/strategy.yaml
```

## Output

The generated script is saved in the `output_strategies` directory with a filename corresponding to the original YAML file. This naming convention ensures easy tracking and management of different strategies.

