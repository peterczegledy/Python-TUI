A text based user interface that's easy to use those who want to recreate the old style user interfaces. This is an improved version of my [older project](https://github.com/peterczegledy/Python_TUI), with more features and fixes.

## Features

### Controls

### Multiple border styles:

One of the improvements from my [older project](https://github.com/peterczegledy/Python_TUI), is that you can costumise the borders.

| Type        | Single      | Single thick        | Double       | Double Horizontal                                                      | Double Vertical                                                        | Rounded                                            |
| ----------- | ----------- | ------------------- | ------------ | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | -------------------------------------------------- |
| Code name    | SINGLELIGHT | SINGLEHEAVY         | DOUBLE       | DOUBLEH                                                                | DOUBLEV                                                                | ROUNDED                                            |
| Picture     |             |                     |              |                                                                        |                                                                        |                                                    |
| Description | Single line | Single thicker line | Double lines | All the horizontal lines are double, but the vertical lines are single | All the vertical lines are double, but the horizontal lines are single | Same as the single lines, but with rounded corners |

## Usage

First of all, you have to import the modul.

```python
import python-tui as tui
```

Then you need to define an array for the items. The items in this array will be drawn to the screen.

```python
objects = []
```

The program can be started with the run(objects) function. You have to pass the array which contains all the objects.

```python
tui.run(objects)
```

## Installation

Currently you can't install the modul, because it's still under development.