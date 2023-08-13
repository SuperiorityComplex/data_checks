from abc import ABC, abstractmethod
from typing import Iterable, Dict
from data_checks.base.suite_helper_types import SuiteInternal


class SuiteBase(ABC):
    # Default rule context for rules missing fields
    _internal: SuiteInternal  # Internal suite state

    verbose: bool
    name: str
    description: str
    should_schedule_runs: bool  # Whether the suite should just schedule runs and not run them
    check_rule_tags: Dict[
        str, Iterable
    ]  # Tags to be used to filter which rules are run in each check

    @classmethod
    @abstractmethod
    def dataset(cls):
        """
        Get the dataset for the suite
        """
        pass

    @classmethod
    @abstractmethod
    def checks_overrides(cls):
        """
        Overrides for rules in checks
        """
        pass

    @classmethod
    def checks_config(cls):
        """
        Shared fields across checks
        """
        pass

    @classmethod
    def suite_config(cls):
        """
        System configurations for the suite
        """
        pass

    @classmethod
    def checks(cls):
        """
        Checks to be run by the suite
        """
        pass

    ...
