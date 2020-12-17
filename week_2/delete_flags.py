import os

test = os.listdir()

for item in test:
    if item.endswith(".png"):
        os.remove(item)
