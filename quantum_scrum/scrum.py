"""
Sprint simulation: spawn stories, assign to devs, run probabilistic stand‑ups.
"""

import queue
import random
import threading
import time

from .backlog import Story, add, all_stories
from .circuits import new_story_circuit
from .devs import Dev
from .quantum import measure_once, random_noise


class Sprint:
    def __init__(self, dev_count=4, rng=None):
        self.rng = rng or random.Random()
        self.inbox = queue.Queue()
        self.donebox = queue.Queue()
        self.devs = [Dev(self.inbox, self.donebox, self.rng) for _ in range(dev_count)]
        self.counter = 0
        self._lock = threading.Lock()

    def _spawn_story(self):
        self.counter += 1
        qc = new_story_circuit()
        story = Story(self.counter, f"Story #{self.counter}", qc)
        add(story)
        self.inbox.put(story)

    def _daily_standup(self):
        print("\n📡  Daily Stand‑Up collapses wave‑functions\n")
        while not self.donebox.empty():
            dev_id, story = self.donebox.get()
            state = measure_once(story.circuit)
            msg = f"· Dev {dev_id}   {story.title:<12} → {state:<7}  |  {story.log[-1]}"
            print(msg)
        time.sleep(random_noise())

    def _retro(self):
        print("\n Sprint Retro: Lessons un‑learned")
        for s in all_stories()[-5:]:
            print(f"- {s.title}: {len(s.log)} quantum pivots")
        print("Backlog size =", len(all_stories()))
        time.sleep(random_noise()*2)

    def run_forever(self):
        try:
            while True:
                if self.rng.random() < 0.65:
                    self._spawn_story()
                if self.rng.random() < 0.2:
                    self._daily_standup()
                if self.rng.random() < 0.05:
                    self._retro()
                time.sleep(random_noise())
        except KeyboardInterrupt:
            print("\n️  Sprint aborted by reality\n")
            for _ in self.devs:
                self.inbox.put(None)
