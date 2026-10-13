
# Python **JSON**

JSON is a syntax for storing and exchanging data.

JSON is text, written with JavaScript object notation.

## JSON in Python

Python has a built-in package called `json`, which can be used to work with JSON data.

## Parse JSON - Convert from JSON to Python

If you have a JSON string, you can parse it by using the `json.loads()` method.

## Convert from Python to JSON

If you have a Python object, you can convert it into a JSON string by using the `json.dumps()` method.

# You can convert Python objects of the following types, into JSON strings:


* dict
* list
* tuple
* string
* int
* float
* True
* False
* None

When you convert from Python to JSON, Python objects are converted into the JSON (JavaScript) equivalent:

| Python | JSON   |
| ------ | ------ |
| dict   | Object |
| list   | Array  |
| tuple  | Array  |
| str    | String |
| int    | Number |
| float  | Number |
| True   | true   |
| False  | false  |
| None   | null   |

## Format the Result

The example above prints a JSON string, but it is not very easy to read, with no indentations and line breaks.

The `json.dumps()` method has parameters to make it easier to read the result:

Use the `indent` parameter to define the numbers of indents:

You can also define the separators, default value is (", ", ": "), which means using a comma and a space to separate each object, and a colon and a space to separate keys from values:

## Order the Result

The `json.dumps()` method has parameters to order the keys in the result:

### Example

Use the `sort_keys` parameter to specify if the result should be sorted or not:

**json.dumps(x, indent=**4**, sort_keys=**True**)**
