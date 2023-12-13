import os
import yaml
import jinja2

try:
    # Load YAML file
    yaml_file_path = '/Users/christos/custom_hummingbot_DSL/yaml_files/dynamic_indicator.yaml'
    with open(yaml_file_path, 'r') as file:
        yaml_data = yaml.safe_load(file)

    # Load Jinja2 template
    template_dir = '/Users/christos/custom_hummingbot_DSL/templates'
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir))
    template = env.get_template('base_template.j2')

    # Render the template with YAML data
    rendered_script = template.render(**yaml_data)
    

    # Write the rendered script to a Python file
    output_file_path = '/Users/christos/custom_hummingbot_DSL/output_strategies/directional_strategy_rsi.py'
    with open(output_file_path, 'w') as file:
        file.write(rendered_script)

    print(f"Strategy script successfully written to {output_file_path}")
except Exception as e:
    print(f"An error occurred: {e}")    
