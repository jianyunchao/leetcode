from collections import deque
class LFUCache:

    def __init__(self, capacity: int):
        self.key_to_val = dict()
        self.key_to_freq = dict()
        self.freq_to_keys = dict()
        self.min_freq = 0
        self.cap = capacity
        pass

    def get(self, key: int) -> int:
        if key not in self.key_to_val:
            return -1

        self.increase_freq(key)
        return self.key_to_val.get(key)

    def put(self, key: int, value: int) -> None:
        if self.cap <= 0:
            return

        if key in self.key_to_val:
            self.key_to_val[key] = value
            self.increase_freq(key)
            return

        if self.cap <= len(self.key_to_val):
            self.remove_min_freq_key()

        self.key_to_val[key] = value
        self.key_to_freq[key] = 1
        self.freq_to_keys.setdefault(1, deque())
        self.freq_to_keys.get(1).append(key)
        self.min_freq = 1

    def increase_freq(self, key):
        freq = self.key_to_freq.get(key)
        self.key_to_freq[key] = freq + 1
        self.freq_to_keys[key].pop(key)
        a = deque()
        a.remove()
        self.freq_to_keys.setdefault(freq + 1, deque())
        self.freq_to_keys[freq + 1].append(key)

        if not self.freq_to_keys[key]:
            del self.freq_to_keys[key]
            if freq == self.min_freq:
                self.min_freq += 1

    def remove_min_freq_key(self):
        key_list = self.freq_to_keys.get(self.min_freq)
        delete_key = key_list.popleft()
        if not key_list:
            del self.freq_to_keys[self.min_freq]

        del self.key_to_val[delete_key]
        del self.key_to_freq[delete_key]


if __name__ == '__main__':
    lfu = LFUCache(2)
    lfu.put(1, 1)
    lfu.put(2, 2)
    lfu.get(1)
    lfu.put(3, 3)
    lfu.get(2)
    lfu.get(3)
    lfu.put(4, 4)
    lfu.get(1)
    lfu.get(3)
    lfu.get(4)
