import yaml
from jinja2 import Environment, FileSystemLoader

# Load YAML file
with open('/Users/christos/hummingbot-dsl/hummingbot/strategy/dsl_yaml_strategy/yaml_files/RSI_EthUsdt_Strategy.yaml', 'r') as file:
    yaml_data = yaml.safe_load(file)

# Load Jinja2 template
env = Environment(loader=FileSystemLoader('/Users/christos/hummingbot-dsl/hummingbot/strategy/dsl_yaml_strategy/templates'))
template = env.get_template('demo_v1.j2')

# Render the template with YAML data
rendered_script = template.render(yaml=yaml_data)

# Write the rendered script to a Python file
with open('/Users/christos/hummingbot-dsl/hummingbot/strategy/dsl_yaml_strategy/output_strategies/RSI_EthUsdt_Strategy.py', 'w') as file:
    file.write(rendered_script)
