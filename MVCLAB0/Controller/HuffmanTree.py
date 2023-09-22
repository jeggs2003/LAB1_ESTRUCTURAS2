import heapq
from collections import defaultdict
from Controller.HuffmanNode import HuffmanNode

class HuffmanTree:
    def __init__(self, text):
        self.root = self.build_huffman_tree(text)
        self.codes = {}
        self.generate_huffman_codes(self.root, "", self.codes)

    def build_huffman_tree(self, text):
        char_freq = defaultdict(int)
        for char in text:
            char_freq[char] += 1

        nodes = [HuffmanNode(char, freq) for char, freq in char_freq.items()]
        heapq.heapify(nodes)

        while len(nodes) > 1:
            left_node = heapq.heappop(nodes)
            right_node = heapq.heappop(nodes)
            parent_node = HuffmanNode(None, left_node.freq + right_node.freq)
            parent_node.left = left_node
            parent_node.right = right_node
            heapq.heappush(nodes, parent_node)

        return nodes[0]

    def generate_huffman_codes(self, node, current_code, codes):
        if node is None:
            return

        if node.char is not None:
            codes[node.char] = current_code
            return

        self.generate_huffman_codes(node.left, current_code + '0', codes)
        self.generate_huffman_codes(node.right, current_code + '1', codes)

    def text_to_binary_huffman(self, text):
        binary_text = ""
        for char in text:
            binary_text += self.codes[char]
        return binary_text

    def binary_to_text_huffman(self, binary_text):
        text = ""
        current_node = self.root
        for bit in binary_text:
            if bit == '0':
                current_node = current_node.left
            else:
                current_node = current_node.right

            if current_node.char is not None:
                text += current_node.char
                current_node = self.root

        return text