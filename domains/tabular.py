import pandas as pd
import numpy as np
class TabularDomain:
    def generate(self, config):
        # Example: generate synthetic tabular data
        num_samples = config.get('num_samples', 10)
        columns = config.get('columns', ['A', 'B', 'C'])
        data = {col: np.random.randn(num_samples) for col in columns}
        df = pd.DataFrame(data)
        return df

# Allow import as dataset_generator.domains.tabular
__all__ = ['TabularDomain']
