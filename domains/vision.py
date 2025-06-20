import numpy as np
class VisionDomain:
    def generate(self, config):
        # Example: generate synthetic images (arrays)
        num_samples = config.get('num_samples', 10)
        img_shape = config.get('img_shape', (28, 28, 1))
        data = [np.random.randint(0, 256, img_shape, dtype=np.uint8) for _ in range(num_samples)]
        return data

# Allow import as dataset_generator.domains.vision
__all__ = ['VisionDomain']
