from collections import Counter
import re


class Solution1(object):
    def __init__(self):
        self.COMPONENT_RE = (
            r'('
                r'[A-Z][a-z]?'
                r'|'
                r'\([^(]+\)'
                r'|'
                r'\[[^[]+\]'
                r'|'
                r'\{[^}]+\}'
            r')'
            r'(\d*)'
        )

    def parse_molecule(self, formula):
        counts = Counter()
        for element, count in re.findall(self.COMPONENT_RE, formula):
            count = int(count) if count else 1
            if element[0] in '([{':
                for k, v in self.parse_molecule(element[1:-1]).items():
                    counts[k] += count * v
            else:
                counts[element] += count
        return counts


class Solution(object):
    def parse_group(self, tokens, counts, scale=1):
        _scale = scale
        for t in tokens:
            if t in '])}':
                self.parse_group(tokens, counts, _scale)
            elif t in '([{':
                break
            elif t.isdigit():
                _scale = scale * int(t)
                continue
            elif t.isalpha():
                counts[t] = counts.get(t, 0) + _scale
            _scale = scale
        return counts

    def parse_molecule(self, formula):
        tokens = re.findall(r'[A-Z][a-z]?|[()\[\]{}]|\d+', formula)
        return self.parse_group(iter(reversed(tokens)), {})


if __name__=='__main__':
    s = Solution()
    water = 'H2O'
    print(s.parse_molecule(water))
