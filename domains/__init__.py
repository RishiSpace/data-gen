from .nlp import NLPDomain
from .vision import VisionDomain
from .tabular import TabularDomain

def get_domain_module(domain):
    if domain == 'nlp':
        return NLPDomain()
    elif domain == 'vision':
        return VisionDomain()
    elif domain == 'tabular':
        return TabularDomain()
    else:
        raise ValueError(f"Unknown domain: {domain}")

# Make this importable as a submodule
__all__ = ['nlp', 'vision', 'tabular', 'get_domain_module']
