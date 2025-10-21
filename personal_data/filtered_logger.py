#!/usr/bin/env python3
"""Module for filtering log messages to obfuscate PII fields"""
import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """
    Obfuscates specified fields in a log message.

    Args:
        fields: List of field names to obfuscate
        redaction: String to replace field values with
        message: The log line to filter
        separator: Character separating fields

    Returns:
        The log message
    """
    pattern = f"({'|'.join(fields)})=[^{separator}]*"
    return re.sub(pattern, rf"\1={redaction}", message)
