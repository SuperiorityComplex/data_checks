from abc import ABC
from typing import Iterable, Dict
from .check import Check
from .suite_helper_types import SuiteInternal


class SuiteBase(ABC):
    # Default rule context for rules missing fields
    _internal: SuiteInternal
    verbose: bool
    name: str
    description: str
    checks: list[Check]  # Checks to be run in the suite
    check_rule_tags: Dict[
        str, Iterable
    ]  # Tags to be used to filter which rules are run in each check
    ...
