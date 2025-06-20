import random
class NLPDomain:
    def generate(self, config):
        # Example: generate synthetic sentences
        num_samples = config.get('num_samples', 10)
        base_sentences = config.get('base_sentences', [
            'The quick brown fox jumps over the lazy dog.',
            'AI is transforming the world.',
            'Data science is fun!'
        ])
        data = [random.choice(base_sentences) for _ in range(num_samples)]
        return data

# Allow import as dataset_generator.domains.nlp
__all__ = ['NLPDomain']
