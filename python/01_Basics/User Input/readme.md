## User Input

Python allows for user input.

That means we are able to ask the user for input.

The following example asks for your name, and when you enter a name, it gets printed on the screen:

## Syntax

input( *prompt* )

## Parameter Values


| Parameter | Description                                                |
| ----------- | ------------------------------------------------------------ |
| *prompt*  | A String, representing a default message before the input. |


## Using prompt

In the example above, the user had to input their name on a new line. The Python `input` function has a `prompt` parameter, which acts as a message you can put in front of the user input, on the same line:

## Input Number

The input from the user is treated as a string. Even if, in the example above, you can input a number, the Python interpreter will still treat it as a string.

You can convert the input into a number with the `float` function:

## Syntax

float( *value* )

## Parameter Values


| Parameter | Description                                                             |
| ----------- | ------------------------------------------------------------------------- |
| *value*   | A number or a string that can be converted into a floating point number |

## Validate Input

It is a good practice to validate any input from the user. In the example above, an error will occur if the user inputs something other than a number.

To avoid getting an error, we can test the input, and if it is not a number, the user could get a message like "Wrong input, please try again", and allowed to make a new input:
