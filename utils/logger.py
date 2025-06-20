import logging

def get_logger():
    logging.basicConfig(level=logging.INFO)
    return logging.getLogger('dataset-generator')

# Allow import as dataset_generator.utils.logger
__all__ = ['get_logger']
