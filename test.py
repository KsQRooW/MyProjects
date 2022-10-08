import pyperclip

while 1:
    pyperclip.waitForNewPaste()
    a = pyperclip.paste()
    a = a.replace('\n', ' ')
    a = a.replace('\r', ' ')
    a = a.replace('\t', ' ')
    pyperclip.copy(a)
...
...
