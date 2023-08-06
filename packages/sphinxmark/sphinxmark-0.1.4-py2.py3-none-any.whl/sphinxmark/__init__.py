#!/bin/python3
# coding: utf-8
"""
A Sphinx extension that enables watermarks for HTML output.

https://github.com/kallimachos/sphinxmark
"""

import logging
import os
import shutil

from bottle import TEMPLATE_PATH, template
from PIL import Image, ImageDraw, ImageFont


def setstatic(app):
    """Set the static path, and create static directory if required."""
    staticpath = app.config.html_static_path
    logging.debug('html_static_path: ' + str(app.config.html_static_path))

    if not staticpath:
        logging.debug('html_static_path not set. Using _static/')
        app.config.html_static_path.append('_static')
        staticpath = '_static'
    else:
        staticpath = app.config.html_static_path[0]
        logging.debug("Using '" + staticpath + "' as static path.")

    if not os.path.exists(staticpath):
        logging.debug('Creating ' + staticpath)
        os.makedirs(staticpath)

    staticpath = os.path.abspath(staticpath)

    return(staticpath)


def createimage(text, srcdir, staticpath):
    """Create PNG image from string."""
    width = 400
    height = 300

    img = Image.new('RGBA', (width, height), (255, 255, 255, 0))
    d = ImageDraw.Draw(img)

    # set font
    fontfile = os.path.join(srcdir, 'arial.ttf')
    font = ImageFont.truetype(fontfile, 100)

    # set x y location for text
    xsize, ysize = d.textsize(text, font)
    logging.debug('x = ' + str(xsize) + '\ny = ' + str(ysize))
    x = (width / 2) - (xsize / 2)
    y = 20

    # add text to image
    d.text((x, y), text, font=font, fill=(255, 0, 0), align="center")

    # set opacity
    img.putalpha(40)

    # save image
    imagename = 'textmark_' + text + '.png'
    imagefile = os.path.join(staticpath, imagename)
    logging.debug('imagefile: ' + imagefile)
    img.save(imagefile, 'PNG')
    logging.debug('Image saved to: ' + imagefile)

    return(imagename)


def watermark(app, env):
    """Add watermark."""
    if app.config.watermark_debug is True:
        logging.basicConfig(level=logging.DEBUG)

    app.info('adding watermark...', nonl=True)

    if app.config.watermark_enable is True:
        staticpath = setstatic(app)

        # append source directory to TEMPLATE_PATH so template is found
        srcdir = os.path.abspath(os.path.dirname(__file__))
        TEMPLATE_PATH.append(srcdir)

        if app.config.watermark_image == 'default':
            image = os.path.join(srcdir, 'watermark-draft.png')
            logging.debug('Using default image: ' + image)
            shutil.copy(image, staticpath)
            logging.debug("Copying '" + image + "' to '" + staticpath + "'")

        elif app.config.watermark_image == 'text':
            image = createimage(app.config.watermark_text, srcdir, staticpath)
            logging.debug('Image: ' + image)

        else:
            image = app.config.watermark_image
            logging.debug('Image: ' + image)

        image = os.path.basename(image)
        if os.path.exists(os.path.join(staticpath, image)) is False:
            logging.error("Cannot find '%s'. Place watermark images in '%s'",
                          image, staticpath)

        if app.config.watermark_div == 'default':
            div = 'body'
        else:
            div = app.config.watermark_div

        cssfile = 'watermark.css'
        css = template('watermark', div=div, image=image)
        logging.debug("Template: " + css)

        with open(os.path.join(staticpath, cssfile), 'w') as f:
            f.write(css)
        app.add_stylesheet(cssfile)
        app.info(' done')


def setup(app):
    """Setup for Sphinx ext."""
    logging.basicConfig(format='%(levelname)s:Watermark: %(message)s')
    try:
        app.add_config_value('watermark_enable', False, 'html')
        app.add_config_value('watermark_image', 'default', 'html')
        app.add_config_value('watermark_text', 'default', 'html')
        app.add_config_value('watermark_div', 'default', 'html')
        app.add_config_value('watermark_debug', False, 'html')
        app.connect('env-updated', watermark)
    except:
        logging.error('Failed to add watermark.')
    return {'version': '0.1'}


if __name__ == '__main__':
    pass
