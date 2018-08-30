"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Vibha Alangar, Amanda Stouder,
         their colleagues and Shamus_Sparling.
"""
###############################################################################
# done: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
###############################################################################

###############################################################################
# TODO: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
###############################################################################

import rosegraphics as rg

window = rg.TurtleWindow()

blue_t = rg.SimpleTurtle('turtle')
blue_t.pen = rg.Pen('blue', 10)
blue_t.speed = 20
red_t = rg.SimpleTurtle('turtle')
red_t.pen = rg.Pen('red', 10)
red_t.speed = 20
size1 = 100
size2 = 50

for k in range(9):

    blue_t.draw_circle(size2)
    red_t.draw_square(size1)

    blue_t.pen_up()
    blue_t.right(45)
    blue_t.forward(10)

    red_t.pen_up()
    red_t.right(45)
    red_t.forward(10)

    blue_t.pen_down()
    size2 = size2 - 5

    red_t.pen_down()
    size1 = size1 - 10

window.close_on_mouse_click()

