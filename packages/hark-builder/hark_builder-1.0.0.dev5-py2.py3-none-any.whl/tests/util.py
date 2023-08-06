try:
    from unittest.mock import patch, MagicMock
except ImportError:
    from mock import patch, MagicMock


__all__ = [
    'patch',
    'MagicMock'
]
