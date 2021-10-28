<div align="center">
    <h1><b>ksignal</b></h1>
    <h3><em>Fast, compact and easy to use signal class to run multiple functions at once</em></h3>
    <img alt="GitHub release (latest by date)" src="https://img.shields.io/github/v/release/JKasCode/ksignal">
    <img alt="GitHub all releases" src="https://img.shields.io/github/downloads/JKasCode/ksignal/total">
</div>
<br>

## **Usage**

1. Insert the `ksignal.py` file into your Python project
2. `import` the module into your code where you will use it
3. Create a new `ksignal` object and add it to a variable with `ksignal.ksignal()`
<br><br>

## **API**

### `ksignal.connect( variant function )`<br>` -> returns variant`
Connect one or more functions to the ksignal class, returning the new connection index/s.<br>
`variant function` can be a single function or a list with functions. If a list is given, a list will be returned with the connection indices, otherwise a single integer will be returned.
<br><br>

### `ksignal.disconnect( variant index )`<br>` -> returns None`
Disconnects the stored function of the given index/s. Index/s is given in the return value of `ksignal.connect`<br>
A single integer or a list of integers can be given to disconnect multiple connections at once.
<br><br>


### `ksignal.disconnect_all()`<br>` -> returns None`
Disconnects all connected functions and resets the stored function list.
<br><br>

### `ksignal.get_connected()`<br>` -> returns list connections`
Returns all connected functions in a list. Any `None` values are connections that were disconnected.
Same list can also be accessed with the `ksignal.functions` value.
<br><br>

### `ksignal.fire( tuple arguments )`<br>` -> returns None`
Runs all the currently connected functions with the given arguments.
<br><br>

## **Example**
Run the `example.py` file included with this repo using Python 3.