# How to read commands

## Key Words

- Required Argument
- Optional Argument

## Examples

Here is an example of a command that will copy a file contents into a new file:

```bash
cp <original-file> <new-file>
```

When you see words in the "< >" symbols, it means you are meant to replace it with an argument. It's a **required argument**

Here is an example of a command that will list the contents of a folder:

```bash
ls [path]
```

When you see words in "[ ]" symbols, it means you *can* replace it with an argument, but you don't *need* to put an argument there. It's an **optional argument**

## You try!

Use this command, but with the correct required argument:

```bash
mkdir Code Code/ComputerClass-<your-name>
```

What do you think this did?
<details>
<summary>Answer</summary>
If I ran it, it would make two new directories:

    Code/
    ├─ ComputerClass-Rosie/

</details>