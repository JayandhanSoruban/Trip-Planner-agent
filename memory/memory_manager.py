class MemoryManager:
    def __init__(self):
        self.memory = {}

    def save(self, key, value):
        self.memory[key] = value

    def get(self, key, default=None):
        return self.memory.get(key, default)


    def dump(self):
        return self.memory
