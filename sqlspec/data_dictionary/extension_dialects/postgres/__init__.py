"""Postgres extension dialects"""

from sqlspec.data_dictionary.extension_dialects.postgres.paradedb import ParadeDB
from sqlspec.data_dictionary.extension_dialects.postgres.pgvector import PGVector

__all__ = ("PGVector", "ParadeDB")
