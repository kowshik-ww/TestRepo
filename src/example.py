#!/usr/bin/env python3
"""
Example Python file for CodeQL testing.
"""

import os
import sys
from typing import List, Optional


def greet(name: str) -> str:
    """Return a greeting message."""
    return f"Hello, {name}!"


def process_data(data: List[str]) -> List[str]:
    """Process a list of strings."""
    return [item.upper() for item in data if item]


def main() -> None:
    """Main function."""
    print(greet("World"))
    result = process_data(["hello", "world", ""])
    print(result)


if __name__ == "__main__":
    main() 