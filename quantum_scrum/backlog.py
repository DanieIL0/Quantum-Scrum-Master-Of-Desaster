"""
Backlog management: never delete, only create.
"""

from dataclasses import dataclass, field
from typing import List


@dataclass
class Story:
    id: int
    title: str
    circuit: "QuantumCircuit"
    log: List[str] = field(default_factory=list)


_backlog: List[Story] = []


def add(story: Story) -> None:
    _backlog.append(story)


def random_story(rng):
    return rng.choice(_backlog) if _backlog else None


def all_stories() -> List[Story]:
    return _backlog
