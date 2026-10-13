# Python **RegEx**

A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.

RegEx can be used to check if a string contains the specified search pattern.

## RegEx Module

Python has a built-in package called `re`, which can be used to work with Regular Expressions.

Import the `re` module:

## RegEx Functions

The `re` module offers a set of functions that allows us to search a string for a match:

| Function                                                            | Description                                                                                                                     |
| ------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| [findall](https://www.w3schools.com/python/python_regex.asp#findall) | Returns a list containing all matches                                                                                           |
| [search](https://www.w3schools.com/python/python_regex.asp#search)   | Returns a[Match object](https://www.w3schools.com/python/python_regex.asp#matchobject)if there is a match anywhere in the string |
| [split](https://www.w3schools.com/python/python_regex.asp#split)     | Returns a list where the string has been split at each match                                                                    |
| [sub](https://www.w3schools.com/python/python_regex.asp#sub)         | Replaces one or many matches with a string                                                                                      |



## Flags

You can add flags to the pattern when using regular expressions.

| Flag          | Shorthand | Description                                                                                                        | Try it |
| ------------- | --------- | ------------------------------------------------------------------------------------------------------------------ | ------ |
| re.ASCII      | re.A      | Returns only ASCII matches                                                                                         |        |
| re.DEBUG      |           | Returns debug information                                                                                          |        |
| re.DOTALL     | re.S      | Makes the . character match all characters (including newline character)                                           |        |
| re.IGNORECASE | re.I      | Case-insensitive matching                                                                                          |        |
| re.MULTILINE  | re.M      | Returns matches at the start/end of each line                                                                      |        |
| re.NOFLAG     |           | Specifies that no flag is set for this pattern                                                                     |        |
| re.UNICODE    | re.U      | Returns Unicode matches. This is default from Python 3. For Python 2: use this flag to return only Unicode matches |        |
| re.VERBOSE    | re.X      | Allows whitespaces and comments inside patterns. Makes the pattern more readable                                   |        |



Metacharacters are characters with a special meaning:

Character	Description	Example	Try it
[]	A set of characters	"[a-m]"
\	Signals a special sequence (can also be used to escape special characters)	"\d"
.	Any character (except newline character)	"he..o"
^	Starts with	"^hello"
$	Ends with	"planet$"

* Zero or more occurrences	"he.*o"

+ One or more occurrences	"he.+o"
  ?	Zero or one occurrences	"he.?o"
  {}	Exactly the specified number of occurrences	"he.{2}o"
  |	Either or	"falls|stays"
  ()	Capture and group
+ 

## Special Sequences

A special sequence is a `\` followed by one of the characters in the list below, and has a special meaning:

| Character | Description                                                                                                                                                                                                | Example          | Try it |
| --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- | ------ |
| \A        | Returns a match if the specified characters are at the beginning of the string                                                                                                                             | "\AThe"          |        |
| \b        | Returns a match where the specified characters are at the beginning or at the end of a word(the "r" in the beginning is making sure that the string is being treated as a "raw string")                    | r"\bain"r"ain\b" |        |
| \B        | Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word(the "r" in the beginning is making sure that the string is being treated as a "raw string") | r"\Bain"r"ain\B" |        |
| \d        | Returns a match where the string contains digits (numbers from 0-9)                                                                                                                                        | "\d"             |        |
| \D        | Returns a match where the string DOES NOT contain digits                                                                                                                                                   | "\D"             |        |
| \s        | Returns a match where the string contains a white space character                                                                                                                                          | "\s"             |        |
| \S        | Returns a match where the string DOES NOT contain a white space character                                                                                                                                  | "\S"             |        |
| \w        | Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)                                                                    | "\w"             |        |
| \W        | Returns a match where the string DOES NOT contain any word characters                                                                                                                                      | "\W"             |        |
| \Z        | Returns a match if the specified characters are at the end of the string                                                                                                                                   | "Spain\Z"        |        |

---

## Sets

A set is a set of characters inside a pair of square brackets `[]` with a special meaning:

| Set        | Description                                                                                                                                   | Try it |
| ---------- | --------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| [arn]      | Returns a match where one of the specified characters (`a`,`r`, or`n`) is present                                                       |        |
| [a-n]      | Returns a match for any lower case character, alphabetically between`a`and`n`                                                             |        |
| [^arn]     | Returns a match for any character EXCEPT`a`,`r`, and`n`                                                                                 |        |
| [0123]     | Returns a match where any of the specified digits (`0`,`1`,`2`, or`3`) are present                                                    |        |
| [0-9]      | Returns a match for any digit between`0`and`9`                                                                                            |        |
| [0-5][0-9] | Returns a match for any two-digit numbers from`00`and`59`                                                                                 |        |
| [a-zA-Z]   | Returns a match for any character alphabetically between`a`and`z`, lower case OR upper case                                               |        |
| [+]        | In sets,`+`,`*`,`.`,`\|`,`()`,`$`,`{}`has no special meaning, so`[+]`means: return a match for any`+`character in the string |        |

## The search() Function

The `search()` function searches the string for a match, and returns a [Match object](https://www.w3schools.com/python/python_regex.asp#matchobject) if there is a match.

If there is more than one match, only the first occurrence of the match will be returned:

Python counts positions starting from  **0** .

* `T` is position 0
* `h` is position 1
* `e` is position 2
* **The ****first space** right after "The" is position 3.

## The split() Function

The `split()` function returns a list where the string has been split at each match:

# you can control the number of occurrences by specifying the `maxsplit` parameter:

## The sub() Function

The `sub()` function replaces the matches with the text of your choice:

## Match Object

A Match Object is an object containing information about the search and the result.

## The Match object has properties and methods used to retrieve information about the search, and the result:

`.span()` returns a tuple containing the start-, and end positions of the match.
`.string` returns the string passed into the function
`.group()` returns the part of the string where there was a match

Print the part of the string where there was a match.

The regular expression looks for any words that starts with an upper case "S":
