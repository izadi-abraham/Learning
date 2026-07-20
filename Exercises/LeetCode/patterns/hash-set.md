# Hash Set

## Use when

- Detect duplicates
- Fast lookup
- Track visited items

## Complexity

Lookup: O(1) average

Insert: O(1) average

## Problems

- [0217 Contains Duplicate](../problems/0217-contains-duplicate.md)

## Related patterns

Hash Map

## Real-world examples

- Prevent duplicate usernames
- Detect repeated requests
- Cache visited pages

## Questions

- What is the difference between an Array, an Object, a Map, and a Set in JavaScript?

In Array the lookup would be O(n) but in an Object the lookup would be O(1). Map is just a modern JavaScript tool to create Maps and avoid JS quirks like the Object's key
can not be a number or an Object's prototype chain's surprises. Set is again another tool that helps you build an object of unique members, fast lookup. On both Map and Set
there are some handy methods that you can use and they are very efficient. Like map.set(key, value) or map.get(key). set.has(value) or set.add(value).

## Arrays

- Ordered collection.
- O(1) access by index.
- O(n) search by value.

## Object

- Stores key/value pairs.
- Average O(1) lookup.
- keys are strings (Symbols); numeric keys are converted to strings.
- Commonly used as a simple hash map.

## Map

- Hash map data structure built into JavaScript.
- Average O(1) lookup.
- Preserves insertion order
- Keys can be any type
- Avoids prototype-chain issues
- Useful methods: set(), get(), has(), delete()

## Set

- Collection of unique values.
- Duplicate values are ignored.
- Average O(1) lookup.
- Average O(1) insertion.
- Useful methods: add(), has(), delete()
