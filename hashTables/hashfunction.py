# In order to look up values by key, we need a way to convert keys into valid indices
# A function that performs this task is called a hash function

# What makes a good hash?
# 1. Fase (i.e. constant time)
# 2. Don't cluster outputs at specific indices. but distributes uniformly
# 3. Deterministic (same input yields same output)

# Big O of Hash Tables
# Insert: O(1)
# Delete: O(1)
# Access: O(1)

# Recap
# Hash tables are collections of key-value pairs
# Hash tables can find values quickly given a key
# Hash tables can add new key-values quickly
# Hash tables store data in a large array, and work by hashing the keys
# A good hash should be fast, distribute keys uniformly, and be deterministic
# Separate chaining and linear probing are two strategies used to deal with two keys that hash the same index