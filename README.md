# Python Hands-on

## Python Execution Architecture & Bytecode

![Python Bytecode and VM](assets/python-bytecode-vm.png)

### Notes:
- **Compile to bytecode:** Low level & platform independent.
- **Python Virtual Machine (VM):** Executes the compiled bytecode.
- **Performance:** Bytecode runs faster.
- **`.pyc`:** Compiled Python (frozen binaries).
- **`__pycache__`:** Manages bytecode based on source changes and Python version.
  - Works only for imported files.
  - Not generated for top-level executed scripts.

# Python Virtual Machine  

Code loops to iterate bytecode 
Runtime Engine 
Also know as python Interpreter 

Byte Code is not a Machine code 

Python specific interpretation 
cpython ( standard implementation ) , jython ( java platform ) , Iron python ( .NET platform ) , stackless ( lightweight threads ) , pypy ( just in time compilation ) 