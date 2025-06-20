from domains import get_domain_module
from utils.logger import get_logger
from utils.exporter import export_data
from utils.augment import augment_and_label
import argparse
import json

def main():
    parser = argparse.ArgumentParser(description='Modular Synthetic Data Generator')
    parser.add_argument('--domain', required=True, choices=['nlp', 'vision', 'tabular'], help='Domain type')
    parser.add_argument('--config', required=True, help='Path to config JSON')
    parser.add_argument('--output', required=True, help='Output file path')
    args = parser.parse_args()

    logger = get_logger()
    with open(args.config) as f:
        config = json.load(f)

    domain_module = get_domain_module(args.domain)
    data = domain_module.generate(config)
    data = augment_and_label(data, config)
    export_data(data, args.output, config)
    logger.info(f"Data generated and exported to {args.output}")

if __name__ == '__main__':
    main()
