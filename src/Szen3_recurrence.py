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
def Szen3_recurrence(draw : ImageDraw, R : float, q : float, a : float, N : int):
    # Safety checks
    assert (N > 2), "N must be superior to 2"
    assert (q > 0 and q < 1), "q must be between 0 and 1 excluded"

    # Since we don't flip the image, the direct rotation is with
    # a negative angle
    a = -a

    # Induction variables
    # w1 and R1
    center = R + 500j
    radius = R
    e = 1

    # Constant part pre-computed to simplify calculations in the loop 
    constant_part   = ((q ** -1) - 1) / (N - 2)
    factor          = exp(1j * a)

    # Draw the first outer circle
    draw_circle(draw, center, R)

    # Find the center and radius of the next circles, and draw them
    for n in range(1, N):
        e *= factor
        radius *= q
        center += radius * e * constant_part * (2 * n - N)

        draw_circle(draw, center, radius)


# ====== Main ======
# Initialize drawing context
image = Image.new("RGB", (1000, 1000), color="#FFFFFF")
draw = ImageDraw.Draw(image)

Szen3_recurrence(draw, R=500, q=.8, a=pi / 6, N=6)

image.show()
# image.save("out.png")