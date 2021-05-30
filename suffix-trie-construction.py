"""
    Write a SuffixTrie class for a Suffix-Trie-like data structure.
    The class should have a root property set to be the root node of the trie and should support:
  
    Creating the trie from a string; this will be done by calling the
    populateSuffixTrieFrom method upon class instantiation, which
    should populate the root of the class.
  
    Searching for strings in the trie.

    Note that every string added to the trie should end with the special endSymbol character: "*".

    If you're unfamiliar with Suffix Tries, we recommend watching the Conceptual Overview section of this 
    question's video explanation before starting to code.

    Example (for creation):
        string = "babc"

        Output:
            The structure below is the root of the trie.
            {
            "c": {"*": true},
            "b": {
                "c": {"*": true},
                "a": {"b": {"c": {"*": true}}},
            },
            "a": {"b": {"c": {"*": true}}},
            }

    Example (for searching in the suffix trie above):
        string = "abc"

        Output: True
"""
# Do not edit the class below except for the
# populateSuffixTrieFrom and contains methods.
# Feel free to add new properties and methods
# to the class.
class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

    def populateSuffixTrieFrom(self, string):
        for i in range(len(string)):
			char = string[i]
			
            if char not in self.root:
                self.root[char] = {}
                
            trie_elem = self.root[char]

            for j in range(i + 1, len(string)):
                inner_char = string[j]
				
				if inner_char not in trie_elem:
					trie_elem[inner_char] = {}
					
				trie_elem = trie_elem[inner_char]

            trie_elem[self.endSymbol] = True

        return self.root
	
	def contains(self, string):
		trie_elem = self.root
		for char in string:
			if char not in trie_elem:
                return False
			trie_elem = trie_elem[char]
			
		return self.endSymbol in trie_elem