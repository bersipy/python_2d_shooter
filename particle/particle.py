import numpy as np
import random

class Particle:
    def __init__(self, position, velocity, color, size, lifespan):
        self.position = np.array(position, dtype=np.float32)
        self.velocity = np.array(velocity, dtype=np.float32)
        self.color = np.array(color, dtype=np.float32)
        self.size = size
        self.lifespan = lifespan  # Time in seconds

    def update(self, delta_time):
        # Update position based on velocity
        self.position += self.velocity * delta_time
        # Reduce lifespan
        self.lifespan -= delta_time
        # Optionally: Fade particle color as it ages
        self.color[3] = max(0, self.lifespan / 2.0)  # Make the particle fade out

    def is_alive(self):
        return self.lifespan > 0
