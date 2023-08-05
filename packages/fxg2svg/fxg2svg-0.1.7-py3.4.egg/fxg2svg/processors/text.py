from lxml import etree
from PIL import Image, ImageFont, ImageDraw
import logging

from ..utils import process_transform, get_attribute
from ..utils.fonts import get_font
from .default import DefaultTagProcessor


def get_recursive_data(element):
    text = element.text or ''
    for e in element:
        text += get_recursive_data(e)
    return text


def process_font(**attrs):
    params = {}
    if 'fontFamily' in attrs:
        params['font-family'] = attrs['fontFamily']
    if 'fontSize' in attrs:
        params['font-size'] = attrs['fontSize']
    if 'fontWeight' in attrs:
        params['font-weight'] = attrs['fontWeight']
    if 'color' in attrs:
        params['fill'] = attrs['color']
    if 'textAlign' in attrs:
        params['text-anchor'] = {
            'left': 'start',
            'center': 'middle',
            'right': 'end',
        }[attrs['textAlign']]
    if 'lineHeight' in attrs:
        params['line-height'] = attrs['lineHeight']
    if 'fontStyle' in attrs:
        params['font-style'] = attrs['fontStyle']
    return params


processors = {}
logger = logging.getLogger(__name__)


def tag_processor(tagname):
    def register_tag_processor(cls):
        processors[tagname] = cls()
        return cls
    return register_tag_processor


@tag_processor('RichText')
class RichTextTagProcessor(DefaultTagProcessor):

    def on_start(self, target):
        target._p_count = -1
        params = {}
        params.update(process_transform(**target.attrs))
        params.update(process_font(**target.attrs))
        target.element = etree.SubElement(
            target.element,
            "text",
            **params
        )

    def on_end(self, target):
        family = target.element.get('font-family')
        size = target.element.get('font-size')
        text = get_recursive_data(target.element)
        if size is not None:
            size = float(size)
            font_object = get_font(family, fontdir=target.fontdir, size=round(size))
        else:
            font_object = get_font(family, fontdir=target.fontdir)
            fw, fh = font_object.getsize(text)
            size = fh
        asc, desc = font_object.getmetrics()
        target.element.attrib['y'] = str(size - desc)
        target.element = target.element.getparent()


@tag_processor('p')
class PTagProcessor(DefaultTagProcessor):

    def on_start(self, target):
        target._p_count += 1
        params = {}
        params.update(process_font(**target.attrs))
        params['x'] = '0'
        dy = max([
            float(get_attribute(target.element, 'line-height') or '0'),
            float(get_attribute(target.element, 'font-size') or '0'),
        ])
        if target._p_count > 0:
            params['dy'] = str(dy)
        target.element = etree.SubElement(
            target.element,
            "tspan",
            **params
        )


@tag_processor('span')
class SpanTagProcessor(PTagProcessor):
    def on_start(self, target):
        params = {}
        params.update(process_font(**target.attrs))
        target.element = etree.SubElement(
            target.element,
            "tspan",
            **params
        )

    def on_data(self, target):
        super(SpanTagProcessor, self).on_data(target)
        typographic_case = target.get_attribute('typographicCase')
        if typographic_case:
            if typographic_case == "uppercase":
                target.element.text = target.text.upper()
            if typographic_case == "lowercase":
                target.element.text = target.text.lower()
