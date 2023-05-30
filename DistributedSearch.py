import threading
import re


class SearchThread(threading.Thread):
    """
    class that inheriting from threading.Thread
    arguments:
    text - textfile to search in
    string_to_find in the text
    delta - num of "spaces" between letters in wanted string
    line_offset - current line in the text
    locations - list of all locations string as found
    """
    def __init__(self, text, string_to_find, delta, line):
        super().__init__()
        self.text = text
        self.string_to_find = string_to_find
        self.delta = delta
        self.line_offset = line
        self.locations = []

    def re_line(self):
        """
        :return: the line of the current thread
        """
        return self.line_offset

    def run(self):
        """
        overrides of run: looking for matches of the string to find in the chunk: splits to lines using regex.
        """
        lines = self.text.split("\n")
        for i in range(len(lines)):
            delta_line = lines[i]
            delta_line = "".join(delta_line)
            pat = list(self.string_to_find)
            points = "." * self.delta
            pat = points.join(pat)
            for match in re.finditer(pat, delta_line):
                self.locations.append([self.line_offset, match.start()])
            self.line_offset += 1


def DistributedSearch(textfile, string_to_search, n_threads, delta):
    # Read the text file
    with open(textfile, 'r') as f:
        text = f.read()

    # Divide the text into chunks
    if n_threads > text.count("\n"):
        n_threads = text.count("\n")
    chunk_size = text.count("\n") // n_threads
    lines = text.split("\n")
    chunks = [lines[i:i + chunk_size] for i in range(0, text.count("\n"), chunk_size)]

    # Create a list of threads and start them
    threads = []
    line = 0
    # going through all chunks one by one
    for chunk in chunks:
        chunk = "\n".join(chunk)
        # creating new thread
        thread = SearchThread(chunk, string_to_search, delta,line)
        thread.start()
        line = thread.re_line()
        threads.append(thread)

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    # Print the locations of all occurrences of the string
    locations = [location for thread in threads for location in thread.locations]
    if locations:
        for location in locations:
            print(location)
    else:
        print("not found.")

import unittest
class TestAssignment(unittest.TestCase):

    def test_threads(self):
        DistributedSearch(r"C:\Users\1\Desktop\alice_in_wonderland.txt", "A", 50, 5000000)
