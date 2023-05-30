# Distributed Text Search

This code provides a multithreaded approach for searching a given string in a text file. It utilizes the `threading` module and regular expressions (`re`) in Python to efficiently search for occurrences of a specified string.

The code consists of two main components:

1. `SearchThread` class:
   - Inherits from `threading.Thread`.
   - Represents a thread responsible for searching a chunk of text for the specified string.
   - Contains attributes such as `text` (the text to search in), `string_to_find` (the string to search for), `delta` (the number of "spaces" between letters in the wanted string), `line_offset` (the current line in the text), and `locations` (a list of all locations where the string is found).
   - Overrides the `run()` method to perform the search using regular expressions.

2. `DistributedSearch` function:
   - Accepts arguments such as `textfile` (the path to the text file), `string_to_search` (the string to search for), `n_threads` (the number of threads to use), and `delta` (the spacing between letters in the string).
   - Reads the text file and divides it into chunks.
   - Creates multiple `SearchThread` instances, each responsible for searching a specific chunk of text.
   - Starts the threads and waits for them to complete.
   - Prints the locations of all occurrences of the string.

Usage:
To use this code, call the `DistributedSearch` function with appropriate arguments, such as the path to the text file, the string to search for, the number of threads, and the delta value. The code will perform a distributed search for the specified string in the text file and display the locations where it is found.

```python
DistributedSearch("path/to/textfile.txt", "string_to_search", n_threads, delta)

