Caches
- keep copies of data from slow sources (such as a hard-drive) in a fast, local source
- frequently-used data shows the greatest speedup since you don't have to keep going to the slow sources constantly
- `Cache Hit`: when the data you want is in the cache
- `Cache Miss`: when you have to got to the primary (slow) storage to get the data because it is not in the cache

LRU Cache
- `LRU Cache` (Least-Recently Used Cache): since caches are limited in size, the LRU Caches will discard the least-recently used item in the cache when it is full

Building an LRU Cache
- you need to be able to look something up by a key in a cache
- `Hash Table`: data structure that does key look-ups in order, one time
- cache entries should be stored in memory that are connected in a doubly-linked list
  -- makes it easy to moved entries to/from the head/tail `O(1)`

  In short, to create an LRU Cache you need:
    1. hash table: gives quick access to all entries in the cache by allowing key look-ups
    2. doubly-linked list: that has cached entries in order from most-recently (head) used to least-recently used (tail)

Adding Entries to the Cache
  1. Allocate new entry
  2. Move to the head of the list
  3. Add new hash table entry
  4. Hook up prev/next pointers

Getting Entries from the Cache
  1. Look up the entry's key in the hash table to see if it is in there
  2. Move this entry to the head of the list (MRU)
  3. Return pointer to entry

Deleting LRU from the Cache
  1. If cache is overfull, delete the tail (LRU)