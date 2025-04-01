import time
start_time = time.time()

a = ((2,), (2,), (2,))
for i in a:
    print(list(i))
print(len(a))
for i in range(3):
    print(i)

end_time = time.time()
print("\ntime:", end_time - start_time)
