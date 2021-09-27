
# VI Editing Commands
```
Command    	Description
```
```
i	Insert at cursor (goes into insert mode)
a	Write after cursor (goes into insert mode)
A	Write at the end of line (goes into insert mode)
ESC	Terminate insert mode
u	Undo last change
U	Undo all changes to the entire line
o	Open a new line (goes into insert mode)
dd	Delete line
3dd	Delete 3 lines
D	Delete contents of line after the cursor
C	Delete contents of a line after the cursor and insert new text. Press ESC key to end insertion.
dw	Delete word
4dw	Delete 4 words
cw	Change word
x	Delete character at the cursor
r	Replace character
R	Overwrite characters from cursor onward
s	Substitute one character under cursor continue to insert
S	Substitute entire line and begin to insert at the beginning of the line
~	Change case of individual character
```


Command mode commands
```
:g/X/s//x/g	Global Search and replace (X=search object x=replace object)
:r file	Import a file into the current file
:20 r file	Import a file into the current file after line 20
:w	Write out the file to save changes
:w file	Write the file to named file
:wq	Save the file exit vi
:w!	Force save the file
:q!	Quit vi but don’t save changes
```

Input mode commands
```
a	Insert characters to the right of the cursor
A	Append characters to the current line
i	Insert characters to the left of cursor
I	Insert characters at the beginning of the current line
o	Add a new line after current line
O	Insert a new line above the current line
```
