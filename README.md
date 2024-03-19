Grammar:
```
<Program> ::= "MAIN_STRUCT" "{" <StatementList> "}"

<StatementList> ::= <Statement> | <Statement> <StatementList> | ε

<Statement> ::= <VariableDeclaration>

<VariableDeclaration> ::= <VariableDeclarator> ","

<VariableDeclarator> ::= "DECLARATOR" "DECLARATOR_OPERATOR" <Expression>

<Expression> ::= <BinaryExpression>

<BinaryExpression> ::= <MultiplicativeExpression> | <MultiplicativeExpression> "ADDITIVE_OPERATOR" <MultiplicativeExpression>

<MultiplicativeExpression> ::= <PrimaryExpression> | <PrimaryExpression> "MULTIPLICATIVE_OPERATOR" <PrimaryExpression>

<PrimaryExpression> ::= <ParanthesizedExpression> | <Literal>

<ParanthesizedExpression> ::= "(" <Expression> ")"

<Literal> ::= <StringLiteral> | <NumericLiteral>

<NumericLiteral> ::= "NUMBER"

<StringLiteral> ::= "STRING"
```
