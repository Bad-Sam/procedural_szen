from cmath import exp, pi
from complex_draw import draw_circle, draw_cross
from PIL import Image, ImageDraw

# Draw pattern 2 from a starting radius, shrinking coefficient, rotation angle,
# and a number of iterations, with the recurrence approach
# \param draw ImageDraw drawing context
# \param R Radius of the first outer circle
# \param q Shrinking coefficient applied to the radius of consecutive circles
# \param a Angle between the consecutive circles' radius lines
# \param N Number of circles/iterations to go through
# \param show_convergence Whether to put a cross on the point of convergence of the pattern
def Szen2_recurrence(draw : ImageDraw, R : float, q : float, a : float, N : int, show_convergence : bool = False):
    # Safety checks
    assert (N > 2), "N must be superior to 2"
    assert (q > 0 and q < 1), "q must be between 0 and 1 excluded"

    # Since we don't flip the image, the direct rotation is with
    # a negative sign
    a = -a

    # Induction variables
    # w1 and R1
    center = R + 500j
    radius = R    
    e = 1

    # Constant part pre-computed to simplify calculations in the loop 
    constant_part   = ((q ** -1) - 1)
    factor          = exp(1j * a)

    # Draw the first outer circle
    draw_circle(draw, center, R)

    # Find the center and radius of the next circles, and draw them
    for n in range(1, N):
        # Update the induction variables
        e       *= factor
        radius  *= q

        # Find the next center affix
        center  -= radius * constant_part * e

        draw_circle(draw, center, radius)

        if show_convergence:
            draw_cross(draw, center, color="#0000FF")

    if show_convergence:
        draw_cross(draw, (R + 500j) - (R * q * factor * constant_part) / (1 - q * factor))


# ====== Main ======
# Initialize drawing context
image = Image.new("RGB", (1000, 1000), color="#FFFFFF")
draw = ImageDraw.Draw(image)

Szen2_recurrence(draw, R=500, q=.85, a=pi / 4, N=6)

# With convergence point pin-pointed
# Szen2_recurrence(draw, R=500, q=.85, a=pi / 4, N=6, show_convergence=True)

image.show()
image.save("out.png")