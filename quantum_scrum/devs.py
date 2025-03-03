"""
Developer threads that mutate story circuits and write daily nonsense.
"""

import threading
import time

from .backlog import Story
from .circuits import entangle
from .quantum import random_noise

BUZZ = [
    "Refactoring a refactor of the refactor",
    "Waiting for CI‑/CD‑/XYZ pipeline",
    "Fighting a Heisenbug (appears only un‑observed)",
    "Rubber‑ducking with Schrödinger",
    "Ping‑ponging ownership",
    "Cycling the sprint board for exercise",
]


class Dev(threading.Thread):
    _ids = 0

    def __init__(self, inbox, donebox, rng):
        super().__init__(daemon=True)
        self.inbox = inbox
        self.donebox = donebox
        self.rng = rng
        Dev._ids += 1
        self.id = Dev._ids
        self.start()

    def run(self):
        while True:
            story = self.inbox.get()
            if story is None:
                break
            self._futz_with(story)
            self.donebox.put((self.id, story))

    def _futz_with(self, story: Story):
        # back to IN‑PROGRESS
        if self.rng.random() < 0.3:
            story.circuit.h(0)
        # Sometimes entangle with a random story
        if self.rng.random() < 0.25:
            from .backlog import random_story
            other = random_story(self.rng)
            if other and other is not story:
                story.circuit = entangle(story.circuit, other.circuit)
        story.log.append(self.rng.choice(BUZZ))
        time.sleep(random_noise())
