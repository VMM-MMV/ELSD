from Tokenizer import *

class Parser:
    def parse(self, string: str) -> dict:
        self._string: str = string
        self._tokenizer: Tokenizer = Tokenizer(string)

        self._lookahead: dict | None = self._tokenizer.getNextToken()

        return self.Program()
    
    def Program(self) -> dict:
        return {
            "type": "Program",
            "body": self.Obesesity()
        }
    
    def Obesesity(self) -> dict:
        name: str = self._eat("MAIN_STRUCT")
        self._eat("{")
        declarations: list = self.StatementList()
        self._eat("}")

        return {
            "type": "MAIN_STRUCT",
            "name": name,
            "declarations": declarations
        }
    
    # StatementList : Statement | StatementList Statement
    def StatementList(self):
        statementList = []
        
        while self._lookahead != None:
            if self._lookahead["type"] == "}":
                break
            statementList.append(self.Statement())
        
        return statementList

    # Statement : ExpressionStatement
    def Statement(self):
        if self._lookahead["type"] == "DECLARATOR":
            return self.VariableDeclaration()

        # return self.ExpressionStatement()
    
    # ExpressionStatement : Expression ','
    def ExpressionStatement(self) -> dict:
        expression = self.Expression()
        self._eat(",")
        return {
            "type": "ExpressionStatement",
            "expression": expression
        }
    
    def VariableDeclaration(self) -> dict:
        declaration = self.VariableDeclarator()
        self._eat(",")
        return {
            "type": "VariableDeclaration",
            "declarations": declaration
        }
    
    def VariableDeclarator(self) -> dict:
        declarator_token = self._eat("DECLARATOR")
        self._eat("DECLARATOR_OPERATOR")
        literal = self.Expression()
        return {
            "type": "VariableDeclarator",
            "id": declarator_token["value"],
            "init": literal
        }
    
    # Expression : Literal ;
    def Expression(self):
        return self.BinaryExpression()
    
    def BinaryExpression(self):
        left = self.MultiplicativeExpression()

        while self._lookahead["type"] == "ADDITIVE_OPERATOR":
            operator = self._eat("ADDITIVE_OPERATOR")

            right = self.MultiplicativeExpression()

            left = {
                "type": "BinaryExpression",
                "left": left,
                "operator": operator,
                "right": right
            }

        while self._lookahead["type"] == "EQUAL_OPERATOR":
            operator = self._eat("EQUAL_OPERATOR")

            right = self.BinaryExpression()

            left = {
                "type": "BinaryExpression",
                "left": left,
                "operator": operator,
                "right": right
            }

        return left
    
    def MultiplicativeExpression(self):
        left = self.PrimaryExpression()

        while self._lookahead["type"] == "MULTIPLICATIVE_OPERATOR":
            operator = self._eat("MULTIPLICATIVE_OPERATOR")

            right = self.PrimaryExpression()

            left = {
                "type": "BinaryExpression",
                "left": left,
                "operator": operator,
                "right": right
            }
        return left
    
    def PrimaryExpression(self):
        match self._lookahead["type"]:
            case "(": return self.ParanthesizedExpression()
            case _: return self.Literal()

    def ParanthesizedExpression(self):
        self._eat("(")
        expression = self.Expression()
        self._eat(")")
        return expression
        
    # Literal : NumericLiteral | StringLiteral
    def Literal(self):
        match self._lookahead["type"]:
            case "STRING": return self.StringLiteral()
            case "NUMBER": return self.NumericLiteral()

    def NumericLiteral(self) -> dict:
        token = self._eat("NUMBER")
        return {
            "type": "NumericLiteral",
            "value": int(token["value"])
        }
    
    def StringLiteral(self) -> dict:
        token = self._eat("STRING")
        return {
            "type": "StringLiteral",
            "value": token["value"]
        }
    
    def _eat(self, tokenType):
        token = self._lookahead

        if token == None:
            raise SyntaxError(f"Unexpected end of input, expected {tokenType}.") 
    
        if token["type"] != tokenType:
            print(self._string[self._tokenizer._coursor], self._tokenizer._coursor, self._lookahead)
            val = token["value"]
            raise SyntaxError(f"Unexpected token {val}, expected {tokenType}.")
        
        self._lookahead = self._tokenizer.getNextToken()

        return token