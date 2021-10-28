import ksignal

example = ksignal.ksignal()

def demof1(a, b):
    print("First function: " + str(a + b))

def demof2(a, b):
    print("Second function: " + str(a * b))

def demof3(a, b):
    print("Third function: " + str(a) + str(b))

connections = example.connect([demof1, demof2]) #connecting multiple at once

print("\nFiring first time")
example.fire(3, 4) #run currently connected functions

example.disconnect(connections[1]) #disconnect existing connection
f3connection = example.connect(demof3) #connect new function by itself

print("\nFiring second time")
example.fire(4, 2) #run currently connected functions

example.disconnect([connections[0], f3connection]) #disconnecting multiple at once
example.connect(demof2) #connect new function by itself

print("\nFiring third time")
example.fire(12, 2) #run currently connected functions

print("\nFiring fourth time")
example.disconnect_all() #disconnect all functions
example.fire() #run all functions (currently none)