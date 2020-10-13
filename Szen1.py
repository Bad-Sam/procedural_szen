from complex_draw import draw_circle
from PIL import Image, ImageDraw

# Draw motif1 from a starting radius, and shrinking coefficient, and a number of iterations
def Szen1(draw : ImageDraw, radius : float, shrink_coef : float, iterations : int):
    # w1 and R1
    center = R = radius

    # Constant part pre-computed to simplify calculation in the loop 
    constant_part = ((shrink_coef ** -1) - 1) / (iterations - 2)

    # Draw the first outer circle
    draw_circle(draw, center + 500j, R)

    # Find the center and radius of the next circles, and draw them
    for i in range(1, iterations):
        R *= shrink_coef
        center += R * constant_part * (2 * i - iterations)

        draw_circle(draw, center + 500j, R)


# ====== Main ======
# Initialize drawing context
image = Image.new("RGB", (1000, 1000), color="#FFFFFF")
draw = ImageDraw.Draw(image)

Szen1(draw, radius=500, shrink_coef=.75, iterations=6)

image.show()