import os
import jinja2
from textx import metamodel_from_file

try:
    # Define the path to your TextX grammar file
    grammar_file_path = '/path/to/your/grammar.tx'

    # Load TextX grammar and create a metamodel
    metamodel = metamodel_from_file(grammar_file_path)

    # Load TextX file
    textx_file_path = '/Users/christos/custom_hummingbot_DSL/textx_files/dynamic_indicator.textx'
    with open(textx_file_path, 'r') as file:
        model = metamodel.model_from_str(file.read())

    # Assume 'model' now contains the parsed data structure
    # which you want to use in your Jinja2 template

    # Load Jinja2 template
    template_dir = '/Users/christos/custom_hummingbot_DSL/templates'
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir))
    template = env.get_template('base_template.j2')

    # Render the template with the parsed model
    rendered_script = template.render(**model)

    # Write the rendered script to a Python file
    output_file_path = '/Users/christos/custom_hummingbot_DSL/output_strategies/directional_strategy_rsi.py'
    with open(output_file_path, 'w') as file:
        file.write(rendered_script)

    print(f"Strategy script successfully written to {output_file_path}")
except Exception as e:
    print(f"An error occurred: {e}")
