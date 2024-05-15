N, M = map(int, input().split())
anya = set(int(input()) for _ in range(N))
boris = set(int(input()) for _ in range(M))

common = anya & boris
anya_only = anya - boris
boris_only = boris - anya

print(len(common))
print(*sorted(common))

print(len(anya_only))
print(*sorted(anya_only))

print(len(boris_only))
print(*sorted(boris_only))
