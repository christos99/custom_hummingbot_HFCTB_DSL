# Custom Hummingbot Strategy Generator

## Overview
This tool generates custom trading strategies for Hummingbot by transforming domain-specific language (DSL) specifications into executable Python code. It uses a TextX metamodel to parse `.strategy` files and then renders these into Python scripts through Jinja2 templates.

## Prerequisites
- Python 3.6 or higher
- TextX
- Jinja2

You can install the required Python packages using:

```bash
pip install textx jinja2
```

## Project Structure

- `/textx/strategy.tx`: This file defines the grammar of the custom DSL used for defining trading strategies.
- `/textx_files/*.strategy`: These are the strategy specification files written according to the custom DSL grammar.
- `/templates/base_template.j2`: A Jinja2 template that defines the structure of the final Python script.
- `/output_strategies/`: The directory where the generated Python scripts will be saved.

## Usage

1. Define your strategy in a `.strategy` file using the DSL defined in `strategy.tx`.
2. Place your `.strategy` file in the `/textx_files/` directory.
3. Ensure the Jinja2 template in `/templates/` is set up to correctly format the Python script based on the DSL model.
4. Run the script to generate the Python trading strategy:
   ```python
   python generate_strategy.py
   ```

5. The script will parse the `.strategy` file, render the template, and save the resulting Python file in `/output_strategies/`.

## Error Handling

If there are errors during the generation process, the script will output an error message detailing what went wrong. Ensure that the `.strategy` file matches the grammar specified in `strategy.tx` and that the Jinja2 template is correctly set up to handle the model.

## Customization

To customize the generation process, you can modify the `strategy.tx` grammar file to fit your DSL needs, or update the Jinja2 template to change the output Python script's structure.
```

This README provides a comprehensive guide on the usage and structure of your project, which should be helpful for both users and developers.