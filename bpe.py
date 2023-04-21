from collections import defaultdict
import pandas as pd


valid_char = "abcdefghijklmnopqrstuvwxyz0123456789 \n-&/'\":,.()!%?+"
symbols = set(" \n-:,.()!?")
char_to_token = {c: i for i, c in enumerate(valid_char)}
char_to_token["@"] = len(valid_char)


class BytePairEncoding:
    def __init__(self):
        self.rules = []
        self.token_to_text = [c for c in valid_char] + ["<|name|>"]
        self._encoding = {}

    def fit(self, corpus: pd.DataFrame, size=100, threshold=3):
        count = defaultdict(int)
        current_encoding = {}
        for _, row in corpus.iterrows():
            text = row["detailed_description"].replace(row["name"], "@").lower()
            for word in self._tokenize_into_words(text):
                count[word] += 1
        for word in count:
            current_encoding[word] = [char_to_token[c] for c in word]
        while len(self.token_to_text) < size:
            (pair, freq) = self._find_most_freq_pair(count, current_encoding)
            # Do not compress if below threshold.
            if freq < threshold:
                break
            # Create the new token.
            new_token = len(self.token_to_text)
            self.token_to_text.append(self.token_to_text[pair[0]] + self.token_to_text[pair[1]])
            rule = (pair[0], pair[1], new_token)
            self.rules.append(rule)
            # Merge the encodings.
            for word, encoded in current_encoding.items():
                current_encoding[word] = self._do_merge(encoded, rule)
        for word in current_encoding:
            self._populate_count(word)
        return self

    def transform_count(self, data: pd.Series) -> pd.Series:
        text = data["detailed_description"].replace(data["name"], "@").lower()
        x = pd.Series([0] * len(self.token_to_text))
        for word in self._tokenize_into_words(text):
            if word not in self._encoding:
                self._populate_count(word)
            x += self._encoding[word]
        return x

    def _tokenize_into_words(self, text: str) -> list[str]:
        words = []
        i = -1
        start = 0
        while i < len(text)-1:
            i += 1
            c = text[i]
            if start == i:
                continue
            if (text[i-1] in symbols) == (c in symbols):
                continue
            words.append(text[start:i])
            start = i
        if start < len(text):
            words.append(text[start:])
        return words

    def _find_most_freq_pair(self, words: dict[str, int], current_encoding: dict[str, list[int]]) -> tuple[tuple[int, int], int]:
        pairs = defaultdict(int)
        for word, count in words.items():
            encoded = current_encoding[word]
            for i in range(len(encoded) - 1):
                pairs[(encoded[i], encoded[i+1])] += count
        max_pair = max(pairs, key=pairs.get)
        freq = pairs[max_pair]
        return (max_pair, freq)

    def _populate_count(self, word: str):
        word_encoded = [char_to_token[c] for c in word]
        for rule in self.rules:
            word_encoded = self._do_merge(word_encoded, rule)
        count = [0] * len(self.token_to_text)
        for t in word_encoded:
            count[t] += 1
        self._encoding[word] = pd.Series(count)

    def _do_merge(self, word: list[int], rule: tuple[int, int, int]):
        read_head = 0
        write_head = 0
        while read_head < len(word):
            if read_head+1 < len(word) and word[read_head] == rule[0] and word[read_head+1] == rule[1]:
                word[write_head] = rule[2]
                read_head += 2
                write_head += 1
                continue
            word[write_head] = word[read_head]
            read_head += 1
            write_head += 1
        return word[:write_head]
