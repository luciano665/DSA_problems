class TimeMap:

    def __init__(self):
        self.keyStore = {} # key: [val, time]
        

    def set(self, key: str, value: str, timestamp: int) -> None:

        # We will use a 2D array for storing all new entries timestamp-val pairs as list

        if key not in self.keyStore:
            # init new hashmap for new key and values
            self.keyStore[key] = []

        # Store [value, list] into [] -> [[]]
        self.keyStore[key].append([value, timestamp])
        
        

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        # Get list of values of currentkey
        values = self.keyStore.get(key, [])
        # Init pointers
        l = 0 
        r = len(values) - 1

        while l <= r:

            m = (l+r) // 2

            if values[m][1] <= timestamp:
                res = values[m][0]
                # Shrink to next timestamp
                l = m + 1
            else:
                r = m - 1

        return res

        
