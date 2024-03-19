import re




Tokens: list[list[str]] = [
    [r"\A\s+", "WHITESPACE"],
    [r"\A;" , ";"],
    [r'\A"""([\s\S]*?)"""', "BCOMMENT"],
    [r"\A\#.*$", "COMMENT"],
    [r"\A\bpregnancies\b", "DECLARATOR"],
    [r"\A\bdiagnosis\b", 'DECLARATOR'],
    [r"\A\btreatment\b", 'DECLARATOR'],
    [r"\A\bglucose\b", 'DECLARATOR'],
    [r"\A\bbloodPressure\b", 'DECLARATOR'],
    [r"\A\bskinThickness\b", 'DECLARATOR'],
    [r"\A\binsulin\b", 'DECLARATOR'],
    [r"\A\bbmi\b", 'DECLARATOR'],
    [r"\A\bdiabetesPedigreeFunction\b", 'DECLARATOR'],
    [r"\A\bage\b", 'DECLARATOR'],
    [r"\A\boutcome\b", 'DECLARATOR'],
    [r'\A=(?!=)', "DECLARATOR_OPERATOR"],
    [r"\A\d+", "NUMBER"],
    [r'\A"[^"]*"', "STRING"],
    [r"\A'[^'']*'", "STRING"]
    # [r'^\"(?:[^"\\]|\\.)*"', "STRING"],
    # [r"^\'(?:[^'\\]|\\.)*'", "STRING"],
]



class Tokenizer:
    def __init__(self, string: str) -> None:
        self._string: str = string
        self._coursor: int = 0
    
    def hasMoreTokens(self) -> bool:
        return self._coursor < len(self._string)
    
    def getNextToken(self) -> dict | None:
        if not self.hasMoreTokens():
            return None
        
        curr_string: str = self._string[self._coursor:]

        for regex, literal_type in Tokens:
            match: list = re.findall(regex, curr_string, flags=re.MULTILINE)
            
            if len(match) == 0:
                continue

            self._coursor += len(match[0])

            if literal_type in ["WHITESPACE", "BCOMMENT","COMMENT", "NEWLINE"]:
                if literal_type == "BCOMMENT":
                    self._coursor += 6

                return self.getNextToken()
            
            return {
                "type": literal_type,
                "value": match[0]
            }
        
        return None