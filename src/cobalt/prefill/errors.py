"""Shared error types for the prefill engine's data-fetch modules."""


class PrefillFetchError(RuntimeError):
    """External data unavailable — the caller renders FAILED, never guesses."""
