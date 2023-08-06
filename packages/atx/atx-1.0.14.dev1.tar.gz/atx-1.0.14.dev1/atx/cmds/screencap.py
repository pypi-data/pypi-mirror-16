#!/usr/bin/env python
# coding: utf-8
#
# Usage: python -matx screen [-s 0.8]
from __future__ import absolute_import

import time
from atx import adbkit


def main(host=None, port=None, serial=None, scale=1.0, out='screenshot.png', method='minicap'):
    """
    If minicap not avaliable then use uiautomator instead

    Disable scale for now.
    Because -s scale is conflict of -s serial
    """
    start = time.time()

    client = adbkit.Client(host=host, port=port)
    device = client.device(serial)
    im = device.screenshot(scale=scale)
    im.save(out)
    print 'Time spend: %.2fs' % (time.time() - start)
    print 'File saved to "%s"' % out


if __name__ == '__main__':
    main()