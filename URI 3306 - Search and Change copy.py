def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

class SegmentTree:
    def __init__(self, n):
        self.tree = [0] * (4 * n)
        
    def build(self, arr, v, tl, tr):
        if tl == tr:
            self.tree[v] = arr[tl]
        else:
            tm = (tl + tr) // 2
            self.build(arr, 2*v, tl, tm)
            self.build(arr, 2*v+1, tm+1, tr)
            self.tree[v] = gcd(self.tree[2*v], self.tree[2*v+1])
            
    def query(self, v, tl, tr, l, r):
        if l > r:
            return 0
        if l == tl and r == tr:
            return self.tree[v]
        tm = (tl + tr) // 2
        return gcd(self.query(2*v, tl, tm, l, min(r, tm)),
                   self.query(2*v+1, tm+1, tr, max(l, tm+1), r))
        
    def update(self, v, tl, tr, l, r, val):
        if l > r:
            return
        if l == tl and r == tr:
            self.tree[v] += val
        else:
            tm = (tl + tr) // 2
            self.update(2*v, tl, tm, l, min(r, tm), val)
            self.update(2*v+1, tm+1, tr, max(l, tm+1), r, val)
            self.tree[v] = gcd(self.tree[2*v], self.tree[2*v+1])
        

while True:
    try:
        n, q = map(int, input().split())
        arr = list(map(int, input().split()))
        tree = SegmentTree(n)
        tree.build(arr, 1, 0, n-1)
        for i in range(q):
            query = input().split()
            if query[0] == '1':
                a, b, v = map(int, query[1:])
                tree.update(1, 0, n-1, a-1, b-1, v)
            elif query[0] == '2':
                a, b = map(int, query[1:])
                print(tree.query(1, 0, n-1, a-1, b-1))
    except:
        break
