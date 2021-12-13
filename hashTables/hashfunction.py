# In order to look up values by key, we need a way to convert keys into valid indices
# A function that performs this task is called a hash function

# What makes a good hash?
# 1. Fase (i.e. constant time)
# 2. Don't cluster outputs at specific indices. but distributes uniformly
# 3. Deterministic (same input yields same output)