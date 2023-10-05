import heapq
from collections import defaultdict
from Controller.HuffmanNode import HuffmanNode

class HuffmanTree:
    def __init__(self, texto):
        self.root = self.ConstruccionHuffman(texto)
        self.codes = {}
        self.CodigosHuffman(self.root, "", self.codes)

    def ConstruccionHuffman(self, texto):
        char_freq = defaultdict(int)
        for char in texto:
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

    def CodigosHuffman(self, node, current_code, codes):
        if node is None:
            return

        if node.char is not None:
            codes[node.char] = current_code
            return

        self.CodigosHuffman(node.left, current_code + '0', codes)
        self.CodigosHuffman(node.right, current_code + '1', codes)

    def Texto_Binario(self, texto):
        codigo_bin = ""
        for char in texto:
            codigo_bin += self.codes[char]
        return codigo_bin

    def Binario_Texto(self, codigo_bin):
        texto = ""
        current_node = self.root
        for bit in codigo_bin:
            if bit == '0':
                current_node = current_node.left
            else:
                current_node = current_node.right

            if current_node.char is not None:
                texto += current_node.char
                current_node = self.root

        return texto