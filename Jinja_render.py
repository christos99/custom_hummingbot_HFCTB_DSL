import os
import yaml
from jinja2 import Environment, FileSystemLoader

try:
    # Load YAML file
    yaml_file_path = '/path/to/RSI_EthUsdt_Strategy.yaml'
    with open(yaml_file_path, 'r') as file:
        yaml_data = yaml.safe_load(file)

    # Load Jinja2 template
    template_dir = '/path/to/templates'
    env = Environment(loader=FileSystemLoader(template_dir))
    template = env.get_template('demo_v1.j2')

    # Render the template with YAML data
    rendered_script = template.render(yaml=yaml_data)

    # Write the rendered script to a Python file
    output_file_path = '/path/to/output/RSI_EthUsdt_Strategy.py'
    with open(output_file_path, 'w') as file:
        file.write(rendered_script)

    print(f"Strategy script successfully written to {output_file_path}")
except Exception as e:
    print(f"An error occurred: {e}")
