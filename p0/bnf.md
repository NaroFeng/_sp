## p0 語言 EBNF 語法定義

### 1. 程式結構 (Program Structure)

```ebnf
program       = { function_def | statement } ;
function_def  = "func" identifier "(" [ parameter_list ] ")" "{" { statement } "}" ;
parameter_list = identifier { "," identifier } ;
```

### 2. 陳述句 (Statements)

```ebnf
statement     = if_statement
              | while_statement
              | assignment_statement
              | return_statement ;

if_statement  = "if" "(" expression ")" "{" { statement } "}" ;
while_statement = "while" "(" expression ")" "{" { statement } "}" ;
assignment_statement = identifier "=" expression [ ";" ] ;
return_statement     = "return" expression [ ";" ] ;
```

### 3. 表達式與運算 (Expressions & Arithmetic)

```ebnf
expression    = arith_expr [ ( "==" | "<" | ">" ) arith_expr ] ;
arith_expr    = term { ( "+" | "-" ) term } ;
term          = factor { ( "*" | "/" ) factor } ;
factor        = number
              | identifier [ "(" [ argument_list ] ")" ]
              | "(" expression ")" ;
argument_list = expression { "," expression } ;
```

### 4. 詞法元素 (Lexical Elements)

```ebnf
identifier    = letter { letter | digit | "_" } ;
number        = digit { digit } ;
letter        = "A" | ... | "Z" | "a" | ... | "z" ;
digit         = "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" ;
comment       = "//" { all_characters } newline
              | "/*" { all_characters } "*/" ;
```

### 5. 語言特性

- **強型態**: 是
- **編譯/解譯**: 編譯至位元組碼，虛擬機執行
- **目標檔**: 基於堆疊的位元組碼 (Bytecode)
- **垃圾蒐集**: 否 (使用手動記憶體管理)