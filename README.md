This is a domain specific language(dsl), aka a custom language for medical analysis.

Grammar:
```
<Program>           ::= "Program" "{" <StatementList> "}"

<StatementList>     ::= <Statement> <StatementList>
                      | <Statement>

<Statement>         ::= <InitStruct>
                      | <MethodCall>
                      | <NewStruct>
                      | <VariableDeclaration>

<InitStruct>        ::= "INIT_STRUCT" "{" <StructName> <StructParameters> <StructTarget> <StructData> "}"

<StructName>        ::= "STRUCT_NAME" "DECLARATOR_OPERATOR" <Expression>

<StructParameters>  ::= "STRUCT_PARAMS" "DECLARATOR_OPERATOR" "{" <StatementList> "}"

<StructTarget>      ::= "STRUCT_TARGET" "DECLARATOR_OPERATOR" "{" <VariableDeclaration> "}"

<StructData>        ::= "STRUCT_DATA" "DECLARATOR_OPERATOR" <Expression>

<NewStruct>         ::= "NEW_STRUCT" <Variable> "DECLARATOR_OPERATOR" <Variable> "{" <StatementList> "}"

<MethodCall>        ::= "METHOD_CALL"

<VariableDeclaration> ::= <VariableDeclarator>

<VariableDeclarator> ::= "DECLARATOR" "DECLARATOR_OPERATOR" <Expression>

<Variable>          ::= "VARIABLE"

<Expression>        ::= <BinaryExpression>

<BinaryExpression>  ::= <MultiplicativeExpression> <ADDITIVE_OPERATOR> <MultiplicativeExpression>

<MultiplicativeExpression> ::= <PrimaryExpression> <MULTIPLICATIVE_OPERATOR> <PrimaryExpression>

<PrimaryExpression> ::= <ParanthesizedExpression>
                      | <Literal>
                      | <Variable>

<ParanthesizedExpression> ::= "(" <Expression> ")"

<Literal>           ::= <NumericLiteral>
                      | <StringLiteral>

<NumericLiteral>    ::= "NUMBER"

<StringLiteral>     ::= "STRING"
```
