stock_prices = {}
with open("stock_prices.csv","r") as f:
    for line in f:
        tokens = line.split(',')
        day = tokens[0]
        price = float(tokens[1])
        stock_prices[day] = price


print(stock_prices)
print(stock_prices['march 9']) #retreving


class HashTable:  
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]
        
    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX
    
    def get(self, index):
        h = self.get_hash(index)
        return self.arr[h]
    
    def add(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val    
        
    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None


t = HashTable()
t.add("march 6", 310) #adding
t.add("march 7", 420)
print(t.arr)
t.add("dec 30", 88)
print(t.get("dec 30")) #reteiving

del t["march 6"]    #deleting
print(t.arr)
