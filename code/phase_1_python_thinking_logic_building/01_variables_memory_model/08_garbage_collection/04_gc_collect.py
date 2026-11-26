"""
Topic: Garbage Collection

Concept:
Manually trigger garbage collection.
"""

import gc


print("Before Collection")

collected_objects = gc.collect()


print()

print("Objects Collected:")
print(collected_objects)