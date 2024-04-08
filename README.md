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

