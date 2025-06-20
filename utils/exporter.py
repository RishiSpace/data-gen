import pandas as pd
import numpy as np
import os

def export_data(data, output_path, config):
    fmt = config.get('format', 'csv')
    if isinstance(data, pd.DataFrame):
        if fmt == 'csv':
            data.to_csv(output_path, index=False)
        elif fmt == 'parquet':
            data.to_parquet(output_path)
        else:
            raise ValueError(f"Unsupported format: {fmt}")
    elif isinstance(data, list):
        with open(output_path, 'w') as f:
            for item in data:
                f.write(str(item) + '\n')
    elif isinstance(data, np.ndarray):
        np.save(output_path, data)
    else:
        raise ValueError("Unknown data type for export")

# Allow import as dataset_generator.utils.exporter
__all__ = ['export_data']
