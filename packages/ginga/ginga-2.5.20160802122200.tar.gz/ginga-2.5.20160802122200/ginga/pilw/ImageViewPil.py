#
# ImageViewPil.py -- a backend for Ginga using Python Imaging Library
#
# This is open-source software licensed under a BSD license.
# Please see the file LICENSE.txt for details.

import numpy
from io import BytesIO

from PIL import Image
from . import PilHelp
from .CanvasRenderPil import CanvasRenderer

from ginga import ImageView


class ImageViewPilError(ImageView.ImageViewError):
    pass

class ImageViewPil(ImageView.ImageViewBase):

    def __init__(self, logger=None, rgbmap=None, settings=None):
        ImageView.ImageViewBase.__init__(self, logger=logger,
                                         rgbmap=rgbmap,
                                         settings=settings)

        self.surface = None
        self._rgb_order = 'RGBA'

        self.renderer = CanvasRenderer(self)

        self.message = None

        # cursors
        self.cursor = {}

        self.t_.setDefaults(show_pan_position=False,
                            onscreen_ff='Sans Serif')

    def get_surface(self):
        return self.surface

    def render_image(self, rgbobj, dst_x, dst_y):
        """Render the image represented by (rgbobj) at dst_x, dst_y
        in the pixel space.
        """
        if self.surface is None:
            return
        canvas = self.surface
        self.logger.debug("redraw surface")

        # get window contents as a buffer and paste it into the PIL surface
        rgb_arr = self.getwin_array(order=self._rgb_order)
        p_image = Image.fromarray(rgb_arr)

        if p_image.size != canvas.size:
            # window size must have changed out from underneath us!
            width, height = self.get_window_size()
            canvas = Image.new("RGB", (width, height), color=0)
            assert p_image.size == canvas.size, \
                   ImageViewPilError("Rendered image does not match window size")
            self.surface = canvas

        canvas.paste(p_image)

        cr = PilHelp.PilContext(canvas)

        # Draw a cross in the center of the window in debug mode
        if self.t_['show_pan_position']:
            ctr_x, ctr_y = self.get_center()
            pen = cr.get_pen('red')
            cr.line((ctr_x - 10, ctr_y), (ctr_x + 10, ctr_y), pen)
            cr.line((ctr_x, ctr_y - 10), (ctr_x, ctr_y + 10), pen)

        # render self.message
        if self.message:
            font = cr.get_font(self.t_['onscreen_ff'], 24.0, self.img_fg)
            wd, ht = cr.text_extents(self.message, font)
            imgwin_wd, imgwin_ht = self.get_window_size()
            y = ((imgwin_ht // 3) * 2) - (ht // 2)
            x = (imgwin_wd // 2) - (wd // 2)
            pen = cr.get_pen('white')
            cr.text((x, y), self.message, font, pen)

    def configure_surface(self, width, height):
        # create PIL surface the size of the window
        # NOTE: pillow needs an RGB image in order to draw with alpha
        # blending, not RGBA
        #self.surface = Image.new(self._rgb_order, (width, height), color=0)
        self.surface = Image.new("RGB", (width, height), color=0)

        # inform the base class about the actual window size
        self.configure(width, height)

    def get_rgb_image_as_buffer(self, output=None, format='png', quality=90):
        if self.surface is None:
            raise ImageViewPilError("No PIL surface defined")

        obuf = output
        if obuf is None:
            obuf = BytesIO()

        # TODO: could these have changed between the time that self.surface
        # was last updated?
        wd, ht = self.get_window_size()

        # Get PIL surface
        p_image = self.get_surface()

        p_image.save(obuf, format=format, quality=quality)
        if output is not None:
            return None
        return obuf.getvalue()

    def get_image_as_array(self):
        if self.surface is None:
            raise ImageViewPilError("No PIL surface defined")

        # TODO: could these have changed between the time that self.surface
        # was last updated?
        wd, ht = self.get_window_size()

        # Get PIL surface
        p_image = self.get_surface()
        arr8 = numpy.array(p_image, dtype=numpy.uint8)
        arr8 = arr8.reshape((ht, wd, 3))
        return arr8

    def get_image_as_buffer(self, output=None):
        obuf = output
        if obuf is None:
            obuf = BytesIO()

        arr8 = self.get_image_as_array()
        obuf.write(arr8.tostring(order='C'))

        if not (output is None):
            return None
        return obuf.getvalue()

    def get_rgb_image_as_bytes(self, format='png', quality=90):
        buf = self.get_rgb_image_as_buffer(format=format, quality=quality)
        return buf

    def save_rgb_image_as_file(self, filepath, format='png', quality=90):
        if not have_PIL:
            raise ImageViewPilError("Please install PIL to use this method")
        if self.surface is None:
            raise ImageViewPilError("No PIL surface defined")

        with open(filepath, 'w') as out_f:
            self.get_rgb_image_as_buffer(output=out_f, format=format,
                                          quality=quality)
        self.logger.debug("wrote %s file '%s'" % (format, filepath))

    def update_image(self):
        # subclass implements this method to actually update a widget
        # from the PIL surface
        self.logger.warning("Subclass should override this method")
        return False

    def set_cursor(self, cursor):
        # subclass implements this method to actually set a defined
        # cursor on a widget
        self.logger.warning("Subclass should override this method")

    def reschedule_redraw(self, time_sec):
        # subclass implements this method to call delayed_redraw() after
        # time_sec
        self.delayed_redraw()

    def define_cursor(self, ctype, cursor):
        self.cursor[ctype] = cursor

    def get_cursor(self, ctype):
        return self.cursor[ctype]

    def switch_cursor(self, ctype):
        self.set_cursor(self.cursor[ctype])

    def get_rgb_order(self):
        return self._rgb_order

    def onscreen_message(self, text, delay=None):
        # subclass implements this method using a timer
        self.logger.warning("Subclass should override this method")

    def show_pan_mark(self, tf):
        self.t_.set(show_pan_position=tf)
        self.redraw(whence=3)


#END
