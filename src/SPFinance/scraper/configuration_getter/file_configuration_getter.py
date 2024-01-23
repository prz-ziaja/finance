import yaml
from pathlib import Path

def get_configuration(component_name, configuration_path: str = ""):
    if not configuration_path:
        configPath = Path(__file__).parent / "config.yml"
    else:
        configPath = Path(configuration_path)

    with open(configPath, 'r') as f:
        config = yaml.safe_load(f)

    return config[component_name]