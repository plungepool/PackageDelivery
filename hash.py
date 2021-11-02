# Hash Map class
""" Portions of code adapted from:
James, Joe. “Python: Creating a HASHMAP Using Lists.” YouTube, https://www.youtube.com/watch?v=9HFbhPscPU0. """


# Class representing a hashmap and its related operations
class HashMap:
    # Initialize hashmap with fixed size
    def __init__(self):
        self.size = 10
        self.map = [None] * self.size

    # Return hash value from key
    # Time complexity of O(n)
    def _get_hash(self, key):
        hash = 0
        for char in str(key):
            hash += ord(char)
        return hash % self.size

    # Add key-value pairs to hashmap
    # Time complexity of O(1), worst case O(n)
    def add(self, key, value):
        key_hash = self._get_hash(key)
        key_value = [key, value]

        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_value])
            return True
        else:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.map[key_hash].append(key_value)
            return True

    # Retrieve/lookup value using package ID as the key
    # Time complexity of O(1), worst case O(n)
    def get(self, key):
        key_hash = self._get_hash(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None
