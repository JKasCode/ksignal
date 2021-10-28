<style>
    .code {
        font-family: menlo;
        color: rgb(200, 200, 200);
        font-size: 90%;
    }
    .code2 {
        font-family: menlo-italic;
        color: rgb(200, 240, 50);
    }
    .code3 {
        color: rgb(240, 100, 50);
    }
    .code4 {
       font-family: menlo-bold;
       color: rgb(150, 150, 200); 
    }
</style>

<h1 align="center">
    <b>ksignal</b>
</h1>

<h3 align="center">
    <em>Fast, compact and easy to use signal class to run multiple functions at once</em>
</h3>

<br>
<h2>
    <b>Usage</b>
</h2>

1. Insert the `ksignal.py` file into your Python project
2. `import` the module into your code where you will use it
3. Create a new `ksignal` object and add it to a variable with `ksignal.ksignal()`

<br>
<h2>
    <b>API</b>
</h2>

<h3>
    <span class="code">
        <span class="code4">ksignal</span>.connect( 
        <span class="code2">variant</span> 
        <span class="code3">function</span> 
    )</span>
    <br>
    <span class="code" style="font-size: 80%;"> -> returns 
        <span class="code2">variant</span>
        <span class="code3">connection index</span> 
    </span>
</h3>

Connect one or more functions to the ksignal class, returning the new connection index/s.<br>
<span class="code"><span class="code2">variant </span><span class="code3">function</span></span>
can be a single function or a list with functions. If a list is given, a list will be returned with the connection indices, otherwise a single integer will be returned.
<br><br>

<h3>
    <span class="code">
        <span class="code4">ksignal</span>.disconnect( 
        <span class="code2">variant</span> 
        <span class="code3">index</span> 
    )</span>
    <br>
    <span class="code" style="font-size: 80%;"> -> returns None</span>
</h3>

Disconnects the stored function of the given index/s. Index/s is given in the return value of 
<span class="code"><span class="code4">ksignal</span>.connect</span><br>
A single integer or a list of integers can be given to disconnect multiple connections at once.
<br><br>

<h3>
    <span class="code">
        <span class="code4">ksignal</span>.disconnect_all()</span>
    <br>
    <span class="code" style="font-size: 80%;"> -> returns None</span>
</h3>

Disconnects all connected functions and resets the stored function list.
<br><br>

<h3>
    <span class="code">
        <span class="code4">ksignal</span>.get_connected()</span>
    <br>
    <span class="code" style="font-size: 80%;"> -> returns 
        <span class="code2">list</span>
        <span class="code3">connections</span> 
    </span>
</h3>

Returns all connected functions in a list. Any <span class="code">None</span> values are connections that were disconnected.
Same list can also be accessed with the <span class="code"><span class="code4">ksignal</span>.functions</span> value.
<br><br>

<h3>
    <span class="code">
        <span class="code4">ksignal</span>.fire( 
        <span class="code2">tuple</span> 
        <span class="code3">arguments</span> 
    )</span>
    <br>
    <span class="code" style="font-size: 80%;"> -> returns None</span>
</h3>

Runs all the currently connected functions with the given arguments.
<br><br>

<h2>
    <b>Example</b>
</h2>
Run the `example.py` file included with this repo using Python 3.