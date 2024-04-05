import re

Tokens: list[list[str]] = [
    [r"\A\s+", "WHITESPACE"],
    [r"\A," , ","],
    [r"\A[(]", "("],
    [r"\A[)]", ")"],
    [r"\A[{]", "{"],
    [r"\A[}]", "}"],
    [r"\A\bCreate Template\b", "INIT_STRUCT"],
    [r"\A\bname\b", "STRUCT_NAME"],
    [r"\A\bparams\b", "STRUCT_PARAMS"],
    [r"\A\btarget\b", "STRUCT_TARGET"],
    [r"\A\bdeclare\b", "NEW_STRUCT"],
    [r'\A\w+\.\w+', "METHOD_CALL"],
    [r'\A"""([\s\S]*?)"""', "BCOMMENT"],
    [r"\A\#.*$", "COMMENT"],
    [r'\A:(?!:)', "DECLARATOR_OPERATOR"],
    [r'\A=(?!=)', "DECLARATOR_OPERATOR"],
    [r"\A[^\s\W\d]+", "VARIABLE"],
    [r'\A[+\-]', "ADDITIVE_OPERATOR"],
    [r'\A[*\/]', "MULTIPLICATIVE_OPERATOR"],
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
            match = re.findall(regex, curr_string, flags=re.MULTILINE)
            
            if len(match) == 0:
                continue

            self._coursor += len(match[0])

            if literal_type in ["WHITESPACE", "BCOMMENT","COMMENT"]:
                if literal_type == "BCOMMENT":
                    self._coursor += 6

                return self.getNextToken()
            
            return {
                "type": literal_type,
                "value": match[0]
            }
        
        return None