this is a small experiment to understand how services like crackstation achieve fast hash lookups

instead of computing hashes on the fly this project precomputes hashes from a small wordlist
and stores them in a dictionary hash -> plaintext for instant lookup

this implementation uses Python dictionaries (hashmaps) which works well for small datasets
However it does not scale large wordlists would require too much memory

a more realistic approach would use a database to store precomputed hashes
allowing efficient lookup while handling much larger datasets

this is purely a learning project