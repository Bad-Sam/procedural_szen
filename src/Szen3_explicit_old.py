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
    w1          = R + 500j
    eia         = exp(1j * a)
    const_part  = R * ((q ** -1) - 1) / (N - 2)

    # Induction variables
    radius  = R
    eina    = eia
    qn      = q * q
    qeia    = q * eia
    q2eia   = q * qeia
    denom   = 1 / (1 - qeia)
    denom2  = denom * denom

    denom *= N
    denom2 *= 2

    # Save the first circle's computation (simpler this way)
    draw_circle(draw, w1, R)

    for n in range(2, N + 1):
        # Update the induction variable
        eina    *= eia
        radius  *= q
        qnx1     = qn * q
        
        wn      = w1 + const_part * ((q2eia - n * qn * eina + qnx1 * eina * (n * eia - 1)) * denom2 - (qeia - qn * eina) * denom)
        
        draw_circle(draw, wn, radius)

        qn      = qnx1


# ====== Main ======
# Initialize drawing context
image = Image.new("RGB", (1000, 1000), color="#FFFFFF")
draw = ImageDraw.Draw(image)

Szen3_explicit(draw, R=500, q=.8, a=pi / 6, N=6)

image.show()
# image.save("out.png")
