import cmath

from cmath import exp
from PIL import ImageDraw

# Draw a circle of radius
def draw_circle(draw : ImageDraw, center : complex, radius : float, color : str = "#000000"):
    # Define the bounds of the circle
    bounds = [(center.real - radius, center.imag - radius)]
    bounds.append((center.real + radius, center.imag + radius))

    draw.ellipse(bounds, outline=color)

def draw_cross(draw : ImageDraw, center : complex, size : complex = 25 + 25j, angle : float = 0, color : str = "#FF0000"):
    pnt1 =   (size.imag * 0.5 * 1j) * exp(1j * angle) + center
    pnt2 = - (size.imag * 0.5 * 1j) * exp(1j * angle) + center

    draw.line([pnt1.real, pnt1.imag, pnt2.real, pnt2.imag], fill=color, width=1)

    pnt1 =   (size.real * 0.5) * exp(1j * angle) + center    
    pnt2 = - (size.real * 0.5) * exp(1j * angle) + center

    draw.line([pnt1.real, pnt1.imag, pnt2.real, pnt2.imag], fill=color, width=1)