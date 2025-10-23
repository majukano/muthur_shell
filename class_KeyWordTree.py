class KeyWordTree:
    def __init__(self):
        self.data = {}

    def add(self, *path):
        """Flexibles Hinzufügen: add('a', 'ab', 'aba') oder add(['a', 'ab', 'aba'])"""
        if len(path) == 1 and isinstance(path[0], (list, tuple)):
            path = path[0]

        current = self.data
        for key in path:
            if key not in current:
                current[key] = {}
            current = current[key]

    def search(self, *path):
        """Flexibles Suchen"""
        if len(path) == 1 and isinstance(path[0], (list, tuple)):
            path = path[0]

        current = self.data
        for key in path:
            if key not in current:
                return []
            current = current[key]
        #return True, sorted(current.keys())
        return sorted(current.keys())

    def exists(self, *path):
        """Prüft nur Existenz"""
        keywords = self.search(*path)
        exist = True
        if not keywords:
           exist = False 
        return exist

# # Sehr einfache Verwendung:
# store = FlexibleKeywordStore()

# # Verschiedene Wege zum Hinzufügen
# store.add('a', 'aa', 'aaa')
# store.add(['a', 'ab', 'aba'])
# store.add(['a', 'ab', 'abb'])

# # Verschiedene Wege zum Suchen
# print(store.search('a'))           # (True, ['aa', 'ab'])
# print(store.search(['a', 'ab']))   # (True, ['aba', 'abb'])
# print(store.exists('a', 'ab'))     # True

if __name__ == "__main__":

    a = KeyWordTree()
    a.add('a', 'aa', 'aaa', 'aaaa')
    print(a.exists(['a','aa']))
    print(a.search(['a','aa']))
#    a.add('a', 'aa', 'aab')
    print(a.exists(['b','bb']))
    print(a.search(['b','bb']))

