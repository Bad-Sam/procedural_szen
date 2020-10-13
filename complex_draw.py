import cmath
from PIL import ImageDraw

# Draw a circle of radius
def draw_circle(draw : ImageDraw, center : complex, radius : float, color : str = "#000000"):
    # Define the bounds of the circle
    bounds = [(center.real - radius, center.imag - radius)]
    bounds.append((center.real + radius, center.imag + radius))

    draw.ellipse(bounds, outline=color)