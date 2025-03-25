#Jonas Fairchild, tracing

"""
What is tracing?
    It allows you to see what is happening with your functions. To do it, use: python -m trace --trace [relative path]. You can use:
    --trace (displays function lines as they are executed)
    --count (displays the number of times each function is executed)
    --listfuncs (lists the functions you have)
    --trackcalls (shows relationship between functions)

What are some ways we can debug by tracing?
    Make a function that lets us see how our functions are interacting and running

How do you access the debugger in VS Code?
    F5 or you can run a debug on the left side or you can scroll down under the play button to debug python file

What is testing?
    Testing is when you go through your code and try to break it so that you can find problems and fix them. The best testers are other people because they didn't write your code.

What are boundary conditions?
    User inputs that are not outside bounds, but close enough that it might cause problems (extreme highs and lows, most likely to be wrong).

How do you handle when users give strange inputs?
    You can use try/except, conditionals, loops, recurstion, etc.

"""

import trace
import sys

tracer = trace.Trace(count=False, trace=True)
def trace_calls(frame, event, arg):
    if event == 'call':
        print(f"Calling function: {frame.f_code.co_name}")
    elif event == 'line':
        print(f"Executing line: {frame.f_lineno} in {frame.f_code.co_name}")
    elif event == 'return':
        print(f"{frame.f_code.co_name} returned {arg}")
    elif event == 'exception':
        print(f"Exception in {frame.f_code.co_name}: {arg}")
    return trace_calls

sys.settrace(trace_calls)

"""
call - when the function is called
line - when a new line is executed
return - when the function returns a value
exception - when an exception is raised
"""

def sub(x, y):
    print(x - y)

def add(x, y):
    print(sub(x, y))
    return x + y

print(add(5, 4))