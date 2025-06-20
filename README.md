# dataset-generator

A modular synthetic data generator for NLP, vision, and tabular domains. Can be used as a Python module or CLI after pip installation.

## Installation

```bash
pip install .
```

## Usage as a Python module

```python
from dataset_generator.domains import get_domain_module
from dataset_generator.utils.augment import augment_and_label
from dataset_generator.utils.exporter import export_data

config = {"domain": "nlp", "num_samples": 5, "format": "csv"}
domain = get_domain_module(config["domain"])
data = domain.generate(config)
data = augment_and_label(data, config)
export_data(data, "output.csv", config)
```

## CLI Usage

```bash
dataset-generator --domain nlp --config config/schema.json --output output.csv
```

## Web API

```bash
python -m dataset_generator.web.app
```

## Project Structure

- `domains/` - Domain-specific generators (NLP, vision, tabular)
- `utils/` - Augmentation, export, logging utilities
- `web/` - Optional Flask web API
- `config/` - Config schema

## License
MIT