from complex_draw import draw_circle
from PIL import Image, ImageDraw

# Draw pattern 1 from a starting radius, shrinking coefficient,
# and a number of iterations, with the recurrence approach
# \param draw ImageDraw drawing context
# \param R Radius of the first outer circle
# \param q Shrinking coefficient applied to the radius of consecutive circles
# \param N Number of circles/iterations to go through
def Szen1_recurrence(draw : ImageDraw, R : float, q : float, N : int):
    # Safety checks
    assert (N > 2), "N must be superior to 2"
    assert (q > 0 and q < 1), "q must be between 0 and 1 excluded"

    # w1 and R1
    center = radius = R

    # Constant part pre-computed to simplify calculations in the loop 
    constant_part = ((q ** -1) - 1) / (N - 2)

    # Draw the first outer circle
    draw_circle(draw, center + 500j, R)

    # Find the center and radius of the next circles, and draw them
    for n in range(1, N):
        radius *= q
        center += radius * constant_part * (2 * n - N)

        draw_circle(draw, center + 500j, radius)


# ====== Main ======
# Initialize drawing context
image = Image.new("RGB", (1000, 1000), color="#FFFFFF")
draw = ImageDraw.Draw(image)

Szen1_recurrence(draw, R=500, q=.75, N=6)

image.show()
# image.save("out.png")