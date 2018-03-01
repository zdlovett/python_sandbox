import pyautogui as gui


print(f"Screen size is {gui.size()}")


#mouse movement testing
s = gui.size()
tl = (s[0] // 4, s[1] // 4)
tr = (s[0] * 3 // 4, s[1] // 4)
bl = (s[0] // 4, s[1] * 3 // 4)
br = (s[0] * 3 // 4, s[1] * 3 // 4)

positions = [tl, tr, br, bl, tl]

for p in positions:
    gui.moveTo(p[0], p[1])


#keyboard button testing
line = "hello, this is a test of what the autogui typewriter outputs"
output = [c for c in line]
gui.typewrite(output)


#mouse click testing
gui.rightClick()
gui.moveRel(0,  - 100)
gui.click()

