# AGENTS.md

## p0 Compiler Project (260311compiler)

### Build & Run
```bash
gcc -o compiler compiler.c && ./compiler <source.p0>
```

### p0 Language
- Test files: `p0/*.p0`
- Supports: `func`, `if`, `while`, arithmetic (`+`, `-`, `*`, `/`), comparisons (`==`, `<`, `>`), `return`
- Semicolons are optional after assignments and returns
- Comments: `// ...` and `/* ... */`

### Architecture
- `compiler.c`: Single-file compiler with Lexer, Parser, IR emitter, and VM
- IR output shows quadruples (op, arg1, arg2, result) during compilation
- VM executes in `vm()` and prints final variable values

### Language Spec
- **Type system**: Strong (integers only)
- **Compilation**: Compiles to stack-based bytecode
- **Execution**: Virtual machine (stack-based)
- **Memory management**: Manual (no GC)