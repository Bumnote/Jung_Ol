L1 = set(list(map(int, input().split())))
L2 = set(list(map(int, input().split())))
L3 = set(list(map(int, input().split())))

Intersection = L1.intersection(L2)
Intersection = Intersection.intersection(L3)
print("Intersection:", Intersection)

Union = L1.union(L2)
Union = Union.union(L3)
print("Union:", Union)
