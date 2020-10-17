from complex_draw import draw_circle
from PIL import Image, ImageDraw

# Draw pattern 1 from a starting radius, shrinking coefficient,
# and a number of iterations, with the explicit approach
# \param draw ImageDraw drawing context
# \param R Radius of the first outer circle
# \param q Shrinking coefficient applied to the radius of consecutive circles
# \param N Number of circles/iterations to go through
def Szen1_explicit(draw : ImageDraw, R : float, q : float, N : int):
    # Safety checks
    assert (N > 2), "N must be superior to 2"
    assert (q > 0 and q < 1), "q must be between 0 and 1 excluded"

    # Induction variables
    qn_1                = q
    radius              = R

    # Constant parts pre-computed to simplify calculations in the loop
    left_operand        = R * ((q ** -1) - 1) / (N - 2)
    right_inner_coef    = 1 / (1 - q)
    left_inner_coef     = 2 * q * right_inner_coef * right_inner_coef
    right_inner_coef    *= N

    # Save the first circle's computation (simpler this way)
    draw_circle(draw, R + 500j, R)

    # The explicit formula used here is slightly different : a "q" factor was
    # taken out to compute left_inner_coef
    for n in range(2, N + 1):
        # Update the induction variables
        radius  *= q
        qn      = qn_1 * q

        # Find the next center coordinates on the reals axis
        wn      = R + left_operand * (left_inner_coef * (1 - n * qn_1 + qn * (n - 1)) - right_inner_coef * (q - qn))
        qn_1    = qn
        
        draw_circle(draw, wn + 500j, radius)


# ====== Main ======
# Initialize drawing context
image = Image.new("RGB", (1000, 1000), color="#FFFFFF")
draw = ImageDraw.Draw(image)

Szen1_explicit(draw, R=500, q=.75, N=6)

image.show()
# image.save("out.png")