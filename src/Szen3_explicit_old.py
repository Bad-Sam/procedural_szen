from cmath import exp, pi
from complex_draw import draw_circle, draw_cross
from PIL import Image, ImageDraw  

# Draw pattern 2 from a starting radius, shrinking coefficient,
# and a number of iterations, with the explicit approach
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
    # a negative angle
    a = -a

    # Constant parts pre-computed to simplify calculations in the loop
    w1              = R + 500j
    eia             = exp(1j * a)
    ei2a            = eia * eia
    qeia            = q * eia
    q_1_eia         = (q ** -1)
    left_coef       = R * (q_1_eia - 1) / (N - 2)
    q_1_eia         -= eia
    inner_left_coef = 1 - qeia * (1 + eia)
    denom           = 1 / (1 - qeia)
    denom2          = denom * denom
    denom           *= N
    denom2          *= 2 * q

    # Induction variables
    radius  = R
    eina    = eia
    qn      = q

    # Save the first circle's computation (simpler this way)
    draw_circle(draw, w1, R)

    for n in range(2, N + 1):
        # Update the induction variable
        eina    *= eia
        radius  *= q
        qn      *= q
        
        wn      = w1 + left_coef * (denom2 * (inner_left_coef - qn * (n * eina * q_1_eia - ei2a)) - denom * (qeia - qn * eina))
        
        draw_circle(draw, wn, radius)


# ====== Main ======
# Initialize drawing context
image = Image.new("RGB", (1000, 1000), color="#FFFFFF")
draw = ImageDraw.Draw(image)

Szen3_explicit(draw, R=500, q=.8, a=pi / 6, N=6)

image.show()
# image.save("out.png")
