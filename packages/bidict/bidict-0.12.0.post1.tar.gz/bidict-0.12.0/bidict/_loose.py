"""Implements :class:`bidict.loosebidict`."""

from ._common import OVERWRITE
from ._bidict import bidict


class loosebidict(bidict):
    """Mutable bidict with *OVERWRITE* duplication behaviors by default."""

    _on_dup_val = OVERWRITE
    _on_dup_kv = OVERWRITE
