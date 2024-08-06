# brainfunc
An implementation of an extended brainfuck interpreter in python. This extended version of brainfuck, called brainfunc, supports use of functions. Function are defined using the `(` and `)` operators and called with the `*` command.

## Brainfunc specification:

| Command          | Meaning                                                                     |
| :--------------- | :-------------------------------------------------------------------------- |
| `>`              | `Increment the data pointer (to point to the next cell to the right).`      |
| `<`              | `Decrement the data pointer (to point to the next cell to the left).`       |
| `+`              | `Increment (increase by one) the byte at the data pointer.`                 |
| `-`              | `Decrement (decrease by one) the byte at the data pointer.`                 |
| `[`              | `If the byte at the data pointer is zero, then instead of moving the instruction pointer forward to the next command, jump it forward to the command after the matching ] command.`                                      |
| `]`              | `If the byte at the data pointer is nonzero, then instead of moving the instruction pointer forward to the next command, jump it back to the command after the matching [ command.` |
| `(`, `)`         | `Define a function inside (). Nested function definitions like (()) are not supported.` |
| `*`              | `Call the function that has number == value of the byte at the data pointer.`|

All other characters that are not commands are ignored.

The function are numbered following the order in which they were defined.
For instance, for the code input `(+++)(->>[-<+>]<<)++<++++<+*`, we define two functions and then execute the sequence `++<++++<+*`, which sets the values 2 and 4 in the bytes at positions 0 and -1, then sets the value 1 at byte-position -2 and calls the function of index 1 (the second function: `(->>[-<+>]<<)`) by executing the `*` command. This code does the summation of the numbers 2 and 4.

## Example:
```
( Try to figure out how this works :)
(->-<+<+<+<+++*[<++++*>++*>>>+<<<+++*])
(-->>[-<<+>>]<[->+<<+>]<[->+<])
(--->>>>[-<<<<+<+>>>>>]<<<<<[->>>>>+<<<<<]>>>>[-<<<-<+>>>>]<<<<[->>>>+<<<<]>)
(---->[-]<)
+++++++++++++++<+*
```
