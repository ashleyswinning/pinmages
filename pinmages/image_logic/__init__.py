from . import cairosvg

def get_png_bytestring(svg_data, width=None, height=None):
    return cairosvg.svg2png(
        svg_data,
        parent_width=width,
        parent_height=height
    )
