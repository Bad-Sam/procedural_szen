from cmath import exp, pi
from complex_draw import draw_circle, draw_cross
from PIL import Image, ImageDraw  

# Draw pattern 2 from a starting radius, shrinking coefficient,
# an angle, and a number of iterations, with the explicit approach
# \param draw ImageDraw drawing context
# \param R Radius of the first outer circle
# \param R Radius of the first outer circle
# \param q Shrinking coefficient applied to the radius of consecutive circles
# \param a Angle between the consecutive circles' radius lines
# \param N Number of circles/iterations to go through
# \param show_convergence Whether to put a cross on the point of convergence of the pattern
def Szen2_explicit(draw : ImageDraw, R : float, q : float, a : float, N : int, show_convergence : bool = False):
    # Safety checks
    assert (N > 2), "N must be superior to 2"
    assert (q > 0 and q < 1), "q must be between 0 and 1 excluded"

    # Since we don't flip the image, the direct rotation is with
    # a negative sign
    a = -a

    # Induction variables
    qeian       = 1
    radius      = R

    # Constant parts pre-computed to simplify calculations in the loop
    w1          = R + 500j
    qeia        = q * exp(1j * a)
    const_part  = R * qeia * ((q ** -1) - 1) / (1 - qeia)

    # Save the first circle's computation (simpler this way)
    draw_circle(draw, R + 500j, R)

    for n in range(2, N + 1):
        # Update the induction variable
        qeian   *= qeia
        radius  *= q
        
        wn      = w1 - const_part * (1 - qeian)
        
        draw_circle(draw, wn, radius)

        if show_convergence:
            draw_cross(draw, wn, color="#0000FF")

    if show_convergence:
        factor = exp(1j * a)
        draw_cross(draw, w1 - (R * q * factor * ((q ** -1) - 1)) / (1 - q * factor))


# ====== Main ======
# Initialize drawing context
image = Image.new("RGB", (1000, 1000), color="#FFFFFF")
draw = ImageDraw.Draw(image)

Szen2_explicit(draw, R=500, q=.85, a=pi / 4, N=6)

# With convergence point pin-pointed
#Szen2_explicit(draw, R=500, q=.85, a=pi / 4, N=6, show_convergence=True)

image.show()
# image.save("out.png")
