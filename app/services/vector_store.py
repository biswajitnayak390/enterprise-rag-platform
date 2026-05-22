import math
from collections import Counter


class InMemoryVectorStore:
    def tokenize(self, text: str):
        return [
            token.lower().strip(".,!?()[]{}")
            for token in text.split()
            if len(token.strip()) > 2
        ]

    def vectorize(self, text: str):
        return Counter(self.tokenize(text))

    def cosine_similarity(self, first_text: str, second_text: str) -> float:
        first_vector = self.vectorize(first_text)
        second_vector = self.vectorize(second_text)

        common_tokens = set(first_vector.keys()) & set(second_vector.keys())
        numerator = sum(
            first_vector[token] * second_vector[token]
            for token in common_tokens
        )

        first_norm = math.sqrt(
            sum(value * value for value in first_vector.values())
        )
        second_norm = math.sqrt(
            sum(value * value for value in second_vector.values())
        )

        if first_norm == 0 or second_norm == 0:
            return 0.0

        return numerator / (first_norm * second_norm)
