from linked_list import LinkedList

class Hashtable:

    def __init__(self, size=1024):
        self._size = size
        self._buckets = size * [None]

    def _hash(self, key):

        sum = 0

        for ch in key:
            sum += ord(ch)

        primed = sum * 19

        index = primed % self._size

        return index


    def set(self, key, value):
        hashed_key_index = self._hash(key) # silent same as listen => 167

        if not self._buckets[hashed_key_index]:
            self._buckets[hashed_key_index] = LinkedList()

        self._buckets[hashed_key_index].add((key, value)) # what about listen vs silent?

        # listen : to me
        # silent : so quiet
        # both hash to 167
        # self._buckets[167] contains ("to me") -> ("so quiet")
        # how to "get" listen vs silent


    def get(self, requesting_key):

        hashed_key_index = self._hash(requesting_key) # silent same as listen => 167

        bucket = self._buckets[hashed_key_index]

        current = bucket.head

        while current:

            # if all we had was value
            # to me, so quiet

            #inspect each item in the bucket
            # if correct item found return
            pair = current.data # (key, value)
            stored_key = pair[0]
            stored_value = pair[1]

            if stored_key == requesting_key:
                return stored_value


            current = current.next





