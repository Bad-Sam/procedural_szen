from cmath import exp, pi
from complex_draw import draw_circle
from PIL import Image, ImageDraw  

# Draw pattern 3 from a starting radius, shrinking coefficient,
# an angle, and a number of iterations, with the explicit approach
# \param draw ImageDraw drawing context
# \param R Radius of the first outer circle
# \param R Radius of the first outer circle
# \param q Shrinking coefficient applied to the radius of consecutive circles
# \param a Angle between the consecutive circles' radius lines
# \param N Number of circles/iterations to go through
def Szen3_explicit(draw : ImageDraw, R : float, q : float, a : float, N : int):
    # Safety checks
    assert (N > 2), "N must be superior to 2"
    assert (q > 0 and q < 1), "q must be between 0 and 1 excluded"
    
    # Since we don't flip the image, the direct rotation is with
    # a negative sign
    a = -a

    # Constant parts pre-computed to simplify calculations in the loop
    w1              = R + 500j
    qeia            = q * exp(1j * a)
    Nqeia_2         = qeia * qeia
    const_num       = 2 - N
    left_coef       = R * ((q ** -1) - 1) / (-const_num * ((1 - qeia) ** 2))
    qeia_const_num  = qeia * const_num
    right_const     = N + 2

    # Induction variables
    qeia_n          = qeia
    qeia_nx1        = Nqeia_2
    radius          = R

    Nqeia_2         *= N

    draw_circle(draw, w1, radius)

    for n in range(2, N + 1):
        # Update the induction variables
        nx2         = 2 * n
        qeia_n      = qeia_nx1
        qeia_nx1    = qeia_n * qeia
        radius      *= q

        # Find the next center affix
        wn = w1 + left_coef * (qeia_const_num + Nqeia_2 + qeia_n * (N - nx2) + qeia_nx1 * (nx2 - right_const))

        draw_circle(draw, wn, radius)


# ====== Main ======
# Initialize drawing context
image = Image.new("RGB", (1000, 1000), color="#FFFFFF")
draw = ImageDraw.Draw(image)

Szen3_explicit(draw, R=500, q=.8, a=pi / 6, N=6)

image.show()
# image.save("out.png")
