# Logo3D Architecture

This document describes the architecture and data flow of the Logo3D interpreter.

## High-Level Architecture

```
┌─────────────────┐
│  Logo3D Program │  (.l3d file)
│   (Source Code) │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  ANTLR4 Lexer   │  (logo3dLexer.py)
│  Tokenization   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  ANTLR4 Parser  │  (logo3dParser.py)
│  Syntax Analysis│
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Abstract       │  Parse Tree / AST
│  Syntax Tree    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Tree Visitor   │  (visitor.py)
│  AST Traversal  │
│  & Execution    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Turtle3D API   │  (turtle3d.py)
│  Graphics Layer │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│    VPython      │  3D Visualization Library
│  3D Rendering   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  3D Graphics    │  Interactive 3D Window
│     Output      │
└─────────────────┘
```

## Component Details

### 1. Lexical Analysis (Lexer)
- **File**: `logo3dLexer.py` (generated from `logo3d.g`)
- **Purpose**: Converts raw text into tokens
- **Input**: Logo3D source code as text
- **Output**: Stream of tokens (keywords, identifiers, operators, etc.)

### 2. Syntax Analysis (Parser)
- **File**: `logo3dParser.py` (generated from `logo3d.g`)
- **Purpose**: Validates syntax and builds parse tree
- **Input**: Token stream from lexer
- **Output**: Abstract Syntax Tree (AST)

### 3. Semantic Analysis & Execution (Visitor)
- **File**: `visitor.py` (inherits from `logo3dVisitor.py`)
- **Purpose**: Traverses AST and executes commands
- **Features**:
  - Variable management and scope handling
  - Procedure definition and invocation
  - Control flow (IF, WHILE, FOR)
  - Expression evaluation
  - Turtle command execution

### 4. Graphics API (Turtle3D)
- **File**: `turtle3d.py`
- **Purpose**: 3D turtle graphics abstraction
- **Features**:
  - Turtle state management (position, orientation, color)
  - Movement commands (forward, backward)
  - Rotation commands (left, right, up, down)
  - Drawing state (show/hide)
  - VPython integration

### 5. Visualization (VPython)
- **Library**: VPython
- **Purpose**: 3D rendering and user interaction
- **Features**:
  - Interactive 3D scene
  - Real-time rendering
  - Camera controls (rotate, zoom, pan)

## Data Structures

### Procedure Storage
```python
class ProcL3D:
    - name: str
    - parameters: list[str]
    - tree: AST node
```

### Turtle State
```python
class Turtle3D:
    - position: vector(x, y, z)
    - alpha: float (horizontal angle)
    - beta: float (vertical angle)
    - color: vector(r, g, b)
    - opacity: float
    - radius: float
```

### Variable Storage
```python
# Dictionary mapping variable names to values
variables = {
    "x": 10.0,
    "y": 5.0,
    "color": 1.0,
    ...
}
```

## Execution Flow

1. **Parse Phase** (Pre-execution)
   - Parse all procedure definitions
   - Store in procedure table
   - No turtle commands executed yet

2. **Execution Phase**
   - Start from specified procedure (default: `main()`)
   - Visitor traverses AST
   - Turtle commands initialize graphics on first use
   - Commands execute in sequence

3. **Graphics Rendering**
   - VPython window opens on first turtle command
   - Real-time rendering as turtle moves
   - Interactive controls available immediately

## Example Execution Trace

For program:
```logo3d
PROC main() IS
    forward(10)
    left(90)
    forward(5)
END
```

Execution trace:
1. Lexer: Tokenize source → `[PROC, IDENT("main"), LP, RP, IS, IDENT("forward"), ...]`
2. Parser: Build AST → `ProcD(name="main", params=[], body=[Forward(10), Left(90), Forward(5)])`
3. Visitor: Store procedure "main" in procedure table
4. Visitor: Execute "main" procedure
5. Visitor: Visit Forward(10) → Initialize Turtle3D → Call turtle.forward(10)
6. Turtle3D: Update position, draw cylinder in VPython
7. Visitor: Visit Left(90) → Call turtle.left(90)
8. Turtle3D: Update angle (alpha)
9. Visitor: Visit Forward(5) → Call turtle.forward(5)
10. Turtle3D: Update position in new direction, draw cylinder
11. VPython: Display interactive 3D scene

## Key Design Patterns

### Visitor Pattern
- Used for AST traversal
- Each node type has corresponding `visit` method
- Separates tree structure from operations

### Facade Pattern
- `Turtle3D` wraps VPython complexity
- Simple API for visitor to use
- Hides low-level 3D math and rendering

### Interpreter Pattern
- Visitor interprets AST nodes
- Each statement type has execution logic
- Maintains runtime state (variables, call stack)

## Error Handling

Errors can occur at multiple stages:

1. **Lexical Errors**: Invalid characters or tokens
2. **Syntax Errors**: Grammar violations (ANTLR reports)
3. **Semantic Errors**: Undefined procedures/variables, type mismatches
4. **Runtime Errors**: Division by zero, infinite loops

The visitor performs semantic checking during execution and reports errors with context.
