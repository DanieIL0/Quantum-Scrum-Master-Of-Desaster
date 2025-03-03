#!/usr/bin/env python3
"""Launch the quantum‑scrum simulation."""

from quantum_scrum.scrum import Sprint

if __name__ == "__main__":
    Sprint(dev_count=5).run_forever()
