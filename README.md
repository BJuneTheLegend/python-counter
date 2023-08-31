# Python Counter

This is a really simple alaways-on-top counter made with Pygame. I made this really quick and dirty for a friend who needed a counter for a game and we couldent find an alternative that worked for us. Only works on Windows.
## Config
You can change the `x` and `y` values to what ever you want on the screen.
```py
>18 user32.SetWindowPos(hwnd, -1, 0, x, y, 0, 0x0001)
```
default is 
```py
>18 user32.SetWindowPos(hwnd, -1, 0, 0, 500, 0, 0x0001)
```

Code should be easy enough to follow to add/change whatever you want.
## Usage

Download proper pip libaries with `pip3 install <package>`
Run with `python3 main.py`

To exit, press `p` and then click the x to close the window. The `p` key stops the keyboard listner.
To increase the counter, press `space`.
To reset the counter press `r`.

--------------------

If someone finds a better alternaive, please let me know! In the mean time, if request is high, I will improve the counter and make the code better and what-not.
Made with ❤️

