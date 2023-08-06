# Simple-Passgen
: *A very simple script to generate cryptographically random passwords*
Simple-Passgen is a script that uses `os.urandom()` to generate crypotographically suitable 
random characters from the set of characters typable on a standard keyboard (a-z, A-Z, 0-9, and 
punctuation).  For a complete listing refer to an ASCII or Unicode table, as this implementation 
uses precisely ASCII codes 33-126. This generates passwords with 6.554 bits of entropy per 
character.  Some basic statistics are given about the password on each generation depending on 
the length settings chosen.
## Usage
```
shell passgen [phrase length]
```
