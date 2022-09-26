# imagecodecs.py

# Copyright (c) 2008-2022, Christoph Gohlke
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
# 3. Neither the name of the copyright holder nor the names of its
#    contributors may be used to endorse or promote products derived from
#    this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

r"""Image transformation, compression, and decompression codecs.

Imagecodecs is a Python library that provides block-oriented, in-memory buffer
transformation, compression, and decompression functions for use in Tifffile,
Czifile, Zarr, and other scientific image input/output packages.

Decode and/or encode functions are implemented for Zlib (DEFLATE), GZIP,
ZStandard (ZSTD), Blosc, Brotli, Snappy, LZMA, BZ2, LZ4, LZ4F, LZ4HC, LZW,
LZF, PGLZ (PostgreSQL LZ), RCOMP (Rice), ZFP, AEC, LERC, NPY, PNG, APNG,
GIF, TIFF, WebP, QOI, JPEG 8-bit, JPEG 12-bit, Lossless JPEG (LJPEG, SOF3),
JPEG 2000 (JP2, J2K), JPEG LS, JPEG XR (WDP, HD Photo), JPEG XL, MOZJPEG,
AVIF, HEIF, RGBE (HDR), Jetraw, PackBits, Packed Integers, Delta, XOR Delta,
Floating Point Predictor, Bitorder reversal, Byteshuffle, Bitshuffle,
CMS (color space transformations), and Float24 (24-bit floating point).

:Author: `Christoph Gohlke <https://www.cgohlke.com>`_
:License: BSD 3-Clause
:Version: 2022.9.26
:DOI: 10.5281/zenodo.6915978

Installation
------------

Install the imagecodecs package from the Python Package Index::

    python -m pip install -U imagecodecs

Wheels for macOS may not be available for the latest releases.

Imagecodecs is also available in other package repositories such as
`Anaconda <https://anaconda.org/conda-forge/imagecodecs>`_,
`MSYS2 <https://packages.msys2.org/base/mingw-w64-python-imagecodecs>`_, and
`MacPorts <https://ports.macports.org/port/py-imagecodecs/summary>`_.

See `Requirements`_ and `Notes`_ for building from source.

Requirements
------------

This release has been tested with the following requirements and dependencies
(other versions may work):

- `CPython 3.8.10, 3.9.13, 3.10.7, 3.11.0rc2 <https://www.python.org>`_
  (AMD64 platforms only, 32-bit versions are deprecated)
- `Numpy 1.22.4 <https://pypi.org/project/numpy>`_

Build requirements:

- `Cython 0.29.32 <https://github.com/cython/cython>`_
- `bitshuffle 0.4.2 <https://github.com/kiyo-masui/bitshuffle>`_
- `brotli 1.0.9 <https://github.com/google/brotli>`_
- `brunsli 0.1 <https://github.com/google/brunsli>`_
- `bzip2 1.0.8 <https://gitlab.com/bzip2/bzip2>`_
- `c-blosc 1.21.1 <https://github.com/Blosc/c-blosc>`_
- `c-blosc2 2.4.1 <https://github.com/Blosc/c-blosc2>`_
- `cfitsio 3.49 <https://heasarc.gsfc.nasa.gov/fitsio/>`_
- `charls 2.3.4 <https://github.com/team-charls/charls>`_
- `giflib 5.2.1 <http://giflib.sourceforge.net/>`_
- `jetraw 22.02.16.1 <https://github.com/Jetraw/Jetraw>`_
- `jxrlib 1.1 <https://packages.debian.org/source/sid/jxrlib>`_
- `lcms 2.13.1 <https://github.com/mm2/Little-CMS>`_
- `lerc 4.0.0 <https://github.com/Esri/lerc>`_
- `libaec 1.0.6 <https://gitlab.dkrz.de/k202009/libaec>`_
- `libavif 0.10.1 <https://github.com/AOMediaCodec/libavif>`_
  (`aom 3.4.0 <https://aomedia.googlesource.com/aom>`_,
  `dav1d 1.0.0 <https://github.com/videolan/dav1d>`_,
  `rav1e 0.5.1 <https://github.com/xiph/rav1e>`_)
- `libdeflate 1.14 <https://github.com/ebiggers/libdeflate>`_
- `libheif 1.12.0 <https://github.com/strukturag/libheif>`_
  (`libde265 1.0.8 <https://github.com/strukturag/libde265>`_)
- `libjpeg-turbo 2.1.4 <https://github.com/libjpeg-turbo/libjpeg-turbo>`_
- `libjxl 0.7.0 <https://github.com/libjxl/libjxl>`_
- `liblzf 3.6 <http://oldhome.schmorp.de/marc/liblzf.html>`_
- `liblzma 5.2.5 <https://github.com/xz-mirror/xz>`_
- `libpng 1.6.37 <https://github.com/glennrp/libpng>`_
- `libpng-apng 1.6.37 <https://sourceforge.net/projects/libpng-apng/>`_
- `libspng 0.7.2 <https://github.com/randy408/libspng>`_
- `libtiff 4.4.0 <https://gitlab.com/libtiff/libtiff>`_
- `libwebp 1.2.3 <https://github.com/webmproject/libwebp>`_
- `lz4 1.9.4 <https://github.com/lz4/lz4>`_
- `mozjpeg 4.1.1 <https://github.com/mozilla/mozjpeg>`_
- `openjpeg 2.5.0 <https://github.com/uclouvain/openjpeg>`_
- `qoi 75e7f30 <https://github.com/phoboslab/qoi>`_
- `rgbe.c 5/26/95 <https://www.graphics.cornell.edu/~bjw/rgbe/rgbe.c>`_
- `snappy 1.1.9 <https://github.com/google/snappy>`_
- `zfp 1.0.0 <https://github.com/LLNL/zfp>`_
- `zlib 1.2.12 <https://github.com/madler/zlib>`_
- `zlib-ng 2.0.6 <https://github.com/zlib-ng/zlib-ng>`_
- `zopfli-1.0.3 <https://github.com/google/zopfli>`_
- `zstd 1.5.2 <https://github.com/facebook/zstd>`_

Test requirements:

- `tifffile 2022.8.8 <https://pypi.org/project/tifffile>`_
- `czifile 2019.7.2 <https://pypi.org/project/czifile>`_
- `python-blosc 1.10.6 <https://github.com/Blosc/python-blosc>`_
- `python-blosc2-0.3.2 <https://github.com/Blosc/python-blosc2>`_
- `python-brotli 1.0.9 <https://github.com/google/brotli/tree/master/python>`_
- `python-lz4 4.0.2 <https://github.com/python-lz4/python-lz4>`_
- `python-lzf 0.2.4 <https://github.com/teepark/python-lzf>`_
- `python-snappy 0.6.1 <https://github.com/andrix/python-snappy>`_
- `python-zstd 1.5.3 <https://github.com/sergey-dryabzhinsky/python-zstd>`_
- `bitshuffle 0.4.2 <https://github.com/kiyo-masui/bitshuffle>`_
- `numcodecs 0.10.2 <https://github.com/zarr-developers/numcodecs>`_
- `zarr 2.13.1 <https://github.com/zarr-developers/zarr-python>`_
- `zopflipy 1.7 <https://github.com/hattya/zopflipy>`_

Revisions
---------

2022.9.26

- Pass 6357 tests.
- Support JPEG XL multi-channel (planar grayscale only) and multi-frame.
- Require libjxl 0.7 (breaking).
- Switch to Blosc2 API and require c-blosc 2.4 (breaking).
- Return LogLuv encoded TIFF as float32.
- Add RGBE codec via rgbe.c.

2022.8.8

- Drop support for libjpeg.
- Fix encoding JPEG in RGB color space.
- Require ZFP 1.0.

2022.7.31

- Add option to decode WebP as RGBA.
- Add option to specify WebP compression method.
- Use exact lossless WebP encoding.

2022.7.27

- Add LZW encoder.
- Add QOI codec via qoi.h (#37).
- Add HEIF codec via libheif (source only; #33).
- Add JETRAW codec via Jetraw demo (source only).
- Add ByteShuffle codec, a generic version of FloatPred.
- Replace imcd_floatpred by imcd_byteshuffle (breaking).
- Use bool type in imcd (breaking).

2022.2.22

- Fix jpeg numcodecs with tables (#28).
- Add APNG codec via libpng-apng patch.
- Add lossless and decodingspeed parameters to jpegxl_encode (#30).
- Add option to read JPEG XL animations.
- Add dummy numthreads parameter to codec functions.
- Set default numthreads to 1 (disable multi-threading).
- Drop support for Python 3.7 and numpy < 1.19 (NEP29).

2021.11.20

- Fix testing on pypy and Python 3.10.

2021.11.11

- Require libjxl 0.6.x.
- Add CMS codec via Little CMS library for color space transformations (WIP).
- Add MOZJPEG codec via mozjpeg library (Windows only).
- Add SPNG codec via libspng library.
- Rename avif_encode maxthreads parameter to numthreads (breaking).
- Accept n-dimensional output in non-image numcodecs decoders.
- Support masks in LERC codec.
- Support multi-threading and planar format in JPEG2K codec.
- Support multi-resolution, MCT, bitspersample, and 32-bit in jpeg2k encoder.
- Change jpeg2k_encode level parameter to fixed quality psnr (breaking).
- Change jpegxl_encode effort parameter default to minimum 3.
- Change JPEG encoders to use YCbCr for RGB images by default.
- Replace lerc_encode planarconfig with planar parameter (breaking).
- Add option to specify omp numthreads and chunksize in ZFP codec.
- Set default numthreads to 0.
- Fix Blosc default typesize.
- Fix segfault in jpegxl_encode.
- Replace many constants with enums (breaking).

2021.8.26

- Add BLOSC2 codec via c-blosc2 library.
- Require LERC 3 and libjxl 0.5.
- Do not exceed literal-only size in PackBits encoder.
- Raise ImcdError if output is insufficient in PackBits codecs (breaking).
- Raise ImcdError if input is corrupt in PackBits decoder (breaking).
- Fix delta codec for non-native byteorder.

2021.7.30

- ...

Refer to the CHANGES file for older revisions.

Notes
-----

This library is largely work in progress.

The API is not stable yet and might change between revisions.

Works on little-endian platforms only.

The ``tiff``, ``packints``, and ``jpegsof3`` codecs are currently decode-only.

The ``heif`` and ``jetraw`` codecs are distributed as source code only due to
license and possible patent usage issues.

The latest `Microsoft Visual C++ Redistributable for Visual Studio 2015-2022
<https://docs.microsoft.com/en-US/cpp/windows/latest-supported-vc-redist>`_
is required on Windows.

Refer to the imagecodecs/licenses folder for 3rd-party library licenses.

This software is based in part on the work of the Independent JPEG Group.

This software includes a modified version of `dcm2niix's jpg_0XC3.cpp
<https://github.com/rordenlab/dcm2niix/blob/master/console/jpg_0XC3.cpp>`_.

This software includes a modified version of `PostgreSQL's pg_lzcompress.c
<https://github.com/postgres/postgres/blob/REL_13_STABLE/src/common/
pg_lzcompress.c>`_.

This software includes a modified version of `bitshuffle
<https://github.com/kiyo-masui/bitshuffle>`_.

This software includes a modified version of `liblj92
<https://bitbucket.org/baldand/mlrawviewer/src/master/liblj92/>`_.

This software includes `qoi.h <https://github.com/phoboslab/qoi/>`_.

This software includes a modified version of `rgbe.c
<https://www.graphics.cornell.edu/~bjw/rgbe/rgbe.c>`_.

Build instructions and wheels for manylinux and macOS courtesy of
`Grzegorz Bokota <https://github.com/Czaki/imagecodecs_build>`_.

Update pip and setuptools to the latest version before installing imagecodecs::

    python -m pip install -U pip setuptools wheel Cython

Install the requirements for building imagecodecs from source code on
latest Ubuntu Linux distributions:

    ``sudo apt-get install build-essential python3-dev cython3
    python3-setuptools python3-pip python3-wheel python3-numpy python3-zarr
    python3-pytest python3-blosc python3-brotli python3-snappy python3-lz4
    libz-dev libblosc-dev liblzma-dev liblz4-dev libzstd-dev libpng-dev
    libwebp-dev libbz2-dev libopenjp2-7-dev libjpeg-dev libjxr-dev
    liblcms2-dev libcharls-dev libaec-dev libbrotli-dev libsnappy-dev
    libzopfli-dev libgif-dev libtiff-dev libdeflate-dev libavif-dev
    libheif-dev libcfitsio-dev``

Use the ``--lite`` build option to only build extensions without 3rd-party
dependencies. Use the ``--skip-extension`` build options to skip building
specific extensions, e.g.:

    ``python -m pip install imagecodecs --global-option="build_ext"
    --global-option="--skip-bitshuffle"``

The ``apng``, ``avif``, ``jetraw``, ``jpeg12``, ``jpegls``, ``jpegxl``,
``lerc``, ``lz4f``, ``mozjpeg``, ``zfp``, and ``zlibng`` extensions are
disabled by default when building from source.

To modify other build settings such as library names and compiler arguments,
provide a ``imagecodecs_distributor_setup.customize_build`` function, which
is imported and executed during setup. See ``setup.py`` for examples.

Other Python packages and C libraries providing imaging or compression codecs:
`Python zlib <https://docs.python.org/3/library/zlib.html>`_,
`Python bz2 <https://docs.python.org/3/library/bz2.html>`_,
`Python lzma <https://docs.python.org/3/library/lzma.html>`_,
`backports.lzma <https://github.com/peterjc/backports.lzma>`_,
`python-lzo <https://bitbucket.org/james_taylor/python-lzo-static>`_,
`python-lzw <https://github.com/joeatwork/python-lzw>`_,
`python-lerc <https://pypi.org/project/lerc/>`_,
`packbits <https://github.com/psd-tools/packbits>`_,
`isa-l.igzip <https://github.com/intel/isa-l>`_,
`fpzip <https://github.com/seung-lab/fpzip>`_,
`libmng <https://sourceforge.net/projects/libmng/>`_,
`OpenEXR <https://github.com/AcademySoftwareFoundation/openexr>`_
(EXR, PIZ, PXR24, B44, DWA),
`pyJetraw <https://github.com/Jetraw/pyJetraw>`_,
`tinyexr <https://github.com/syoyo/tinyexr>`_,
`pytinyexr <https://github.com/syoyo/pytinyexr>`_,
`libjpeg <https://github.com/thorfdbg/libjpeg>`_ (GPL),
`pylibjpeg <https://github.com/pydicom/pylibjpeg>`_,
`pylibjpeg-libjpeg <https://github.com/pydicom/pylibjpeg-libjpeg>`_ (GPL),
`pylibjpeg-openjpeg <https://github.com/pydicom/pylibjpeg-openjpeg>`_,
`pylibjpeg-rle <https://github.com/pydicom/pylibjpeg-rle>`_,
`glymur <https://github.com/quintusdias/glymur>`_,
`pyheif <https://github.com/carsales/pyheif>`_,
`pyrus-cramjam <https://github.com/milesgranger/pyrus-cramjam>`_,
`QuickLZ <http://www.quicklz.com/>`_ (GPL),
`LZO <http://www.oberhumer.com/opensource/lzo/>`_ (GPL),
`nvJPEG <https://developer.nvidia.com/nvjpeg>`_,
`nvJPEG2K <https://developer.nvidia.com/nvjpeg>`_,
`PyTurboJPEG <https://github.com/lilohuang/PyTurboJPEG>`_,
`CCSDS123 <https://github.com/drowzie/CCSDS123-Issue-2>`_,
`LPC-Rice <https://sourceforge.net/projects/lpcrice/>`_,
`MAFISC
<https://wr.informatik.uni-hamburg.de/research/projects/icomex/mafisc>`_.

Examples
--------

Import the JPEG2K codec:

>>> from imagecodecs import (
...     jpeg2k_encode, jpeg2k_decode, jpeg2k_check, jpeg2k_version, JPEG2K
... )

Check that the JPEG2K codec is available in the imagecodecs build:

>>> bool(JPEG2K)
True

Print the version of the JPEG2K codec's underlying OpenJPEG library:

>>> jpeg2k_version()
'openjpeg 2.5.0'

Encode a numpy array in lossless JP2 format:

>>> array = numpy.random.randint(100, 200, (256, 256, 3), numpy.uint8)
>>> encoded = jpeg2k_encode(array, level=0)
>>> encoded[:12]
b'\x00\x00\x00\x0cjP  \r\n\x87\n'

Check that the encoded bytes likely contain a JPEG 2000 stream:

>>> jpeg2k_check(encoded)
True

Decode the JP2 encoded bytes to a numpy array:

>>> decoded = jpeg2k_decode(encoded)
>>> numpy.array_equal(decoded, array)
True

Decode the JP2 encoded bytes to an existing numpy array:

>>> out = numpy.empty_like(array)
>>> _ = jpeg2k_decode(encoded, out=out)
>>> numpy.array_equal(out, array)
True

Not all codecs are fully implemented, raising exceptions at runtime:

>>> from imagecodecs import tiff_encode
>>> tiff_encode(array)
Traceback (most recent call last):
 ...
NotImplementedError: tiff_encode

Write the numpy array to a JP2 file:

>>> from imagecodecs import imwrite, imread
>>> imwrite('_test.jp2', array)

Read the image from the JP2 file as numpy array:

>>> image = imread('_test.jp2')
>>> numpy.array_equal(image, array)
True

Create a JPEG 2000 compressed Zarr array:

>>> import zarr
>>> import numcodecs
>>> from imagecodecs.numcodecs import Jpeg2k
>>> numcodecs.register_codec(Jpeg2k)
>>> zarr.zeros(
...     (512, 512, 3), chunks=(256, 256, 3), dtype='u1', compressor=Jpeg2k()
... )
<zarr.core.Array (512, 512, 3) uint8>

Access image data in a sequence of JP2 files via tifffile.FileSequence and
dask.array:

>>> import tifffile
>>> import dask.array
>>> def jp2_read(filename):
...     with open(filename, 'rb') as fh:
...         data = fh.read()
...     return jpeg2k_decode(data)
>>> with tifffile.FileSequence(jp2_read, '*.jp2') as ims:
...     with ims.aszarr() as store:
...         dask.array.from_zarr(store)
dask.array<from-zarr, shape=(1, 256, 256, 3)...chunksize=(1, 256, 256, 3)...

View the image in the JP2 file from the command line::

    $ python -m imagecodecs _test.jp2

"""

__version__ = '2022.9.26'

import os
import sys
import io
import importlib

import numpy

# names of public attributes by module
# will be updated with standard attributes
_API = {
    None: [
        'version',
        'imread',
        'imwrite',
        'imagefileext',
        'DelayedImportError',
        ('none', 'numpy', 'jpeg'),
    ],
    'imcd': [
        'imcd_version',
        'numpy_abi_version',
        'cython_version',
        (
            'bitorder',
            'byteshuffle',
            'delta',
            # 'ccittrle',
            'float24',
            'floatpred',
            'lzw',
            'packbits',
            'packints',
            'xor',
        ),
    ],
    'aec': [],
    'apng': [],
    'avif': [],
    # 'exr': [],
    'bitshuffle': [],
    'blosc': [],
    'blosc2': [],
    'brotli': [],
    'brunsli': [],
    'bz2': [],
    'cms': ['cms_transform', 'cms_profile'],
    'deflate': ['deflate_crc32', 'deflate_adler32', ('deflate', 'gzip')],
    'gif': [],
    'heif': [],
    'jetraw': ['jetraw_init'],
    'jpeg2k': [],
    'jpeg8': [],
    'jpeg12': [],
    'jpegls': [],
    'jpegsof3': [],
    'jpegxl': [],
    'jpegxr': [],
    'lerc': [],
    'ljpeg': [],
    'lz4': [],
    'lz4f': [],
    'lzf': [],
    'lzma': [],
    'mozjpeg': [],
    # 'nvjpeg': [],  # CUDA
    # 'nvjpeg2k': [],  # CUDA
    'pglz': [],
    'qoi': [],
    'png': [],
    'rgbe': [],
    'rcomp': [],
    'snappy': [],
    'spng': [],
    # 'szip': [],
    'tiff': [],
    'webp': [],
    'zfp': [],
    'zlib': ['zlib_crc32', 'zlib_adler32'],
    'zlibng': ['zlibng_crc32', 'zlibng_adler32'],
    'zopfli': [],
    'zstd': [],
    # 'module': ['attribute1', 'attribute2', ('codec1', 'code2')]
}

# map extra to existing attributes
# e.g. keep deprecated names for older versions of tifffile and czifile
_COMPATIBILITY = {
    'JPEG': 'JPEG8',
    'jpeg_check': 'jpeg8_check',
    'jpeg_version': 'jpeg8_version',
    'zopfli_check': 'zlib_check',
    'zopfli_decode': 'zlib_decode',
    'j2k_encode': 'jpeg2k_encode',
    'j2k_decode': 'jpeg2k_decode',
    'jxr_encode': 'jpegxr_encode',
    'jxr_decode': 'jpegxr_decode',
}

# map attribute names to module names
_ATTRIBUTES = {}

# map of codec names to module names
_CODECS = {}


def _add_codec(module, codec=None, attributes=None):
    """Register codec in global _API, _ATTRIBUTES, and _CODECS."""
    if codec is None:
        codec = module
    if attributes is None:
        attributes = (
            f'{codec}_encode',
            f'{codec}_decode',
            f'{codec}_check',
            f'{codec}_version',
            f'{codec.capitalize()}Error',
            f'{codec.upper()}',
        )
    if module in _API:
        _API[module].extend(attributes)
    else:
        _API[module] = attributes
    _ATTRIBUTES.update({attr: module for attr in _API[module]})
    _CODECS[codec] = module


def _register_codecs():
    """Parse _API and register all codecs."""
    for module, attributes in _API.items():
        for attr in attributes.copy():
            if isinstance(attr, tuple):
                attributes.remove(attr)
                for codec in attr:
                    _add_codec(module, codec)
                break
        else:
            _add_codec(module)


def _load_all():
    """Add all registered attributes to package namespace."""
    for name in __dir__():
        __getattr__(name)


def __dir__():
    """Return list of attribute names accessible on module."""
    return sorted(list(_ATTRIBUTES) + list(_COMPATIBILITY))


def __getattr__(name):
    """Return module attribute after loading it from extension.

    Load attribute's extension and add its attributes to the package namespace.

    """
    name_ = name
    name = _COMPATIBILITY.get(name, name)

    if name not in _ATTRIBUTES:
        raise AttributeError(f"module 'imagecodecs' has no attribute {name!r}")

    module_ = _ATTRIBUTES[name]
    if module_ is None:
        return None

    try:
        module = importlib.import_module('._' + module_, 'imagecodecs')
    except ImportError:
        module = None
    except AttributeError:
        # AttributeError: type object 'imagecodecs._module.array' has no
        # attribute '__reduce_cython__'
        # work around Cython raises AttributeError e.g. when the _shared
        # module failed to import due to an incompatible numpy version
        from . import _shared  # noqa

        module = None

    for n in _API[module_]:
        if n in _COMPATIBILITY:
            continue
        attr = getattr(module, n, None)
        if attr is None:
            attr = _stub(n, module)
        setattr(imagecodecs, n, attr)

    attr = getattr(imagecodecs, name)
    if name != name_:
        setattr(imagecodecs, name_, attr)
    return attr


class DelayedImportError(ImportError):
    """Delayed ImportError."""

    def __init__(self, name):
        """Initialize instance from attribute name."""
        msg = f"could not import name {name!r} from 'imagecodecs'"
        super().__init__(msg)


def _stub(name, module):
    """Return stub function or class."""
    if name.endswith('_version'):
        if module is None:

            def stub_version():
                """Stub for imagecodecs.codec_version function."""
                return f"{name[:-8]} n/a"

        else:

            def stub_version():
                """Stub for imagecodecs.codec_version function."""
                return f"{name[:-8]} unknow"

        return stub_version

    if name.endswith('_check'):

        def stub_check(arg):
            """Stub for imagecodecs.codec_check function."""
            return False

        return stub_check

    if name.endswith('_decode'):

        def stub_decode(*args, **kwargs):
            """Stub for imagecodecs.codec_decode function."""
            raise DelayedImportError(name)

        return stub_decode

    if name.endswith('_encode'):

        def stub_encode(*args, **kwargs):
            """Stub for imagecodecs.codec_encode function."""
            raise DelayedImportError(name)

        return stub_encode

    if name.islower():

        def stub_function(*args, **kwargs):
            """Stub for imagecodecs.codec_function."""
            raise DelayedImportError(name)

        return stub_function

    if name.endswith('Error'):

        class StubError(RuntimeError):
            """Stub for imagecodecs.CodecError class."""

            def __init__(self, *args, **kwargs):
                raise DelayedImportError(name)

        return StubError

    class StubType(type):
        def __getattr__(cls, arg):
            raise DelayedImportError(name)

        if module is None:

            def __bool__(cls):
                return False

    if name.isupper():

        class STUB(metaclass=StubType):
            """Stub for imagecodecs.CODEC constants."""

        return STUB

    class Stub(metaclass=StubType):
        """Stub for imagecodecs.Codec class."""

    return Stub


def _extensions():
    """Return sorted list of extension names."""
    return sorted(e for e in _API if e is not None)


def version(astype=None, _versions_=[]):
    """Return version information about all codecs and dependencies."""
    if not _versions_:
        _versions_.extend(
            (
                f'imagecodecs {__version__}',
                imagecodecs.cython_version(),
                imagecodecs.numpy_version(),
                imagecodecs.numpy_abi_version(),
                imagecodecs.imcd_version(),
            )
        )
        _versions_.extend(
            sorted(
                {
                    getattr(imagecodecs, v)()
                    for v in _ATTRIBUTES
                    if v.endswith('_version')
                    and v
                    not in (
                        'imcd_version',
                        'numpy_abi_version',
                        'numpy_version',
                        'cython_version',
                        'none_version',
                    )
                }
            )
        )

    if astype is None or astype is str:
        return ', '.join(ver.replace(' ', '-') for ver in _versions_)
    if astype is dict:
        return dict(ver.split(' ') for ver in _versions_)
    return tuple(_versions_)


def imread(fileobj, codec=None, memmap=True, return_codec=False, **kwargs):
    """Return image data from file as numpy array."""
    import mmap

    codecs = []
    if codec is None:
        # find codec based on file extension
        if isinstance(fileobj, (str, os.PathLike)):
            ext = os.path.splitext(os.fspath(fileobj))[-1][1:].lower()
        else:
            ext = None
        if ext in _imcodecs():
            codec = _imcodecs()[ext]
            if codec == 'jpeg':
                codecs.extend(('jpeg8', 'jpeg12', 'jpegsof3', 'ljpeg'))
            else:
                codecs.append(codec)
        # try other imaging codecs
        codecs.extend(
            c
            for c in (
                'tiff',
                'apng',
                'png',
                'gif',
                'webp',
                'jpeg8',
                'jpeg12',
                'jpegsof3',
                'jpeg2k',
                'jpegls',
                'jpegxr',
                'jpegxl',
                'avif',
                'heif',
                'ljpeg',
                # 'brunsli',
                # 'exr',
                'zfp',
                'lerc',
                'rgbe',
                'numpy',
            )
            if c not in codecs
        )
    else:
        # use provided codecs
        if not isinstance(codec, (list, tuple)):
            codec = [codec]
        for c in codec:
            if isinstance(c, str):
                c = c.lower()
                c = _imcodecs().get(c, c)
            codecs.append(c)

    offset = None
    close = False
    if isinstance(fileobj, mmap.mmap):
        data = fileobj
        offset = data.tell()
    elif hasattr(fileobj, 'read'):
        # binary stream: open file, BytesIO
        data = fileobj.read()
    elif isinstance(fileobj, (str, os.PathLike)):
        # TODO: support urllib.request.urlopen ?
        # file name
        with open(os.fspath(fileobj), 'rb') as fh:
            if memmap:
                offset = 0
                close = True
                data = mmap.mmap(fh.fileno(), 0, access=mmap.ACCESS_READ)
            else:
                data = fh.read()
    else:
        # binary data
        data = fileobj

    exceptions = []
    image = None
    for codec in codecs:
        if callable(codec):
            func = codec
        else:
            try:
                func = getattr(imagecodecs, codec + '_decode')
            except Exception as exc:
                exceptions.append(f'{repr(codec).upper()}: {exc}')
                continue
        try:
            image = func(data, **kwargs)
            if image.dtype == 'object':
                image = None
                raise ValueError('failed')
            break
        except DelayedImportError:
            pass
        except Exception as exc:
            # raise
            exceptions.append(f'{func.__name__.upper()}: {exc}')
        if offset is not None:
            data.seek(offset)

    if close:
        data.close()

    if image is None:
        raise ValueError('\n'.join(exceptions))

    if return_codec:
        return image, func
    return image


def imwrite(fileobj, data, codec=None, **kwargs):
    """Write numpy array to image file."""
    if codec is None:
        # find codec based on file extension
        if isinstance(fileobj, (str, os.PathLike)):
            ext = os.path.splitext(os.fspath(fileobj))[-1].lower()[1:]
        else:
            raise ValueError('no codec specified')

        codec = _imcodecs().get(ext, ext)
        try:
            codec = getattr(imagecodecs, codec + '_encode')
        except AttributeError as exc:
            raise ValueError(f'invalid codec {codec!r}') from exc

    elif isinstance(codec, str):
        codec = codec.lower()
        codec = _imcodecs().get(codec, codec)
        try:
            codec = getattr(imagecodecs, codec + '_encode')
        except AttributeError as exc:
            raise ValueError(f'invalid codec {codec!r}') from exc

    elif not callable(codec):
        raise ValueError(f'invalid codec {codec!r}')

    data = codec(data, **kwargs)
    if hasattr(fileobj, 'write'):
        # binary stream: open file, BytesIO
        fileobj.write(data)
    else:
        # file name
        with open(str(fileobj), 'wb') as fh:
            fh.write(data)


def _imcodecs(_codecs_={}):
    """Return map of image file extensions to codec names."""
    if not _codecs_:
        codecs = {
            'apng': ('apng',),
            'avif': ('avif', 'avifs'),
            'brunsli': ('brn',),
            # 'exr': ('exr',),
            'gif': ('gif',),
            'heif': (
                'heif',
                'heic',
                'heifs',
                'heics',
                'hif',  # 'avci', 'avcs'
            ),
            'jpeg': ('jpg', 'jpeg', 'jpe', 'jfif', 'jif', 'ljpeg'),
            'jpeg2k': ('j2k', 'jp2', 'j2c', 'jpc', 'jpx', 'jpf'),  # jpm, mj2
            'jpegls': ('jls',),
            'jpegxl': ('jxl',),
            'jpegxr': ('jxr', 'hdp', 'wdp'),
            'lerc': ('lerc1', 'lerc2'),
            'numpy': ('npy', 'npz'),
            'png': ('png',),
            'qoi': ('qoi',),
            'rgbe': ('hdr', 'rgbe', 'pic'),
            'tiff': ('tif', 'tiff', 'ptif', 'ptiff', 'tf8', 'tf2', 'btf'),
            'webp': ('webp',),
            'zfp': ('zfp',),
        }
        _codecs_.update(
            (ext, codec) for codec, exts in codecs.items() for ext in exts
        )
    return _codecs_


def imagefileext():
    """Return list of image file extensions handled by imread and imwrite."""
    return list(_imcodecs().keys())


NONE = True
NoneError = RuntimeError


def none_version():
    """Return empty version string."""
    return ''


def none_check(data):
    """Return True if data likely contains Template data."""


def none_decode(data, *args, **kwargs):
    """Decode NOP."""
    return data


def none_encode(data, *args, **kwargs):
    """Encode NOP."""
    return data


NUMPY = True
NumpyError = RuntimeError


def numpy_version():
    """Return numpy version string."""
    return f'numpy {numpy.__version__}'


def numpy_check(data):
    """Return True if data likely contains NPY or NPZ data."""
    with io.BytesIO(data) as fh:
        data = fh.read(64)
    magic = b'\x93NUMPY'
    return data.startswith(magic) or (data.startswith(b'PK') and magic in data)


def numpy_decode(data, index=0, numthreads=None, out=None, **kwargs):
    """Decode NPY and NPZ."""
    with io.BytesIO(data) as fh:
        try:
            out = numpy.load(fh, **kwargs)
        except ValueError as exc:
            raise ValueError('not a numpy array') from exc
        if hasattr(out, 'files'):
            try:
                index = out.files[index]
            except Exception:
                pass
            out = out[index]
    return out


def numpy_encode(data, level=None, numthreads=None, out=None):
    """Encode NPY and NPZ."""
    with io.BytesIO() as fh:
        if level:
            numpy.savez_compressed(fh, data)
        else:
            numpy.save(fh, data)
        fh.seek(0)
        out = fh.read()
    return out


JpegError = RuntimeError


def jpeg_decode(
    data,
    bitspersample=None,
    tables=None,
    header=None,
    colorspace=None,
    outcolorspace=None,
    shape=None,
    numthreads=None,
    out=None,
):
    """Decode JPEG 8-bit, 12-bit, and SOF3."""
    if header is not None:
        data = header + data + b'\xff\xd9'
    if bitspersample is None:
        try:
            return imagecodecs.jpeg8_decode(
                data,
                tables=tables,
                colorspace=colorspace,
                outcolorspace=outcolorspace,
                shape=shape,
                numthreads=numthreads,
                out=out,
            )
        except Exception as exc:
            msg = str(exc)

            if 'Unsupported JPEG data precision' in msg:
                return imagecodecs.jpeg12_decode(
                    data,
                    tables=tables,
                    colorspace=colorspace,
                    outcolorspace=outcolorspace,
                    shape=shape,
                    numthreads=numthreads,
                    out=out,
                )
            if 'SOF type' in msg:
                try:
                    return imagecodecs.jpegsof3_decode(
                        data, numthreads=numthreads, out=out
                    )
                except Exception:
                    return imagecodecs.ljpeg_decode(
                        data, numthreads=numthreads, out=out
                    )
            # if 'Empty JPEG image' in msg:
            # e.g. Hamamatsu NDPI slides with dimensions > 65500
            # Unsupported marker type
            raise exc
    try:
        if bitspersample == 8:
            return imagecodecs.jpeg8_decode(
                data,
                tables=tables,
                colorspace=colorspace,
                outcolorspace=outcolorspace,
                shape=shape,
                numthreads=numthreads,
                out=out,
            )
        if bitspersample == 12:
            return imagecodecs.jpeg12_decode(
                data,
                tables=tables,
                colorspace=colorspace,
                outcolorspace=outcolorspace,
                shape=shape,
                numthreads=numthreads,
                out=out,
            )
        try:
            return imagecodecs.jpegsof3_decode(
                data, numthreads=numthreads, out=out
            )
        except Exception:
            return imagecodecs.ljpeg_decode(
                data, numthreads=numthreads, out=out
            )
    except Exception as exc:
        msg = str(exc)
        if 'SOF type' in msg:
            try:
                return imagecodecs.jpegsof3_decode(
                    data, numthreads=numthreads, out=out
                )
            except Exception:
                return imagecodecs.ljpeg_decode(
                    data, numthreads=numthreads, out=out
                )
        # if 'Empty JPEG image' in msg:
        raise exc


def jpeg_encode(
    data,
    level=None,
    colorspace=None,
    outcolorspace=None,
    subsampling=None,
    optimize=None,
    smoothing=None,
    lossless=None,
    bitspersample=None,
    numthreads=None,
    out=None,
):
    """Encode JPEG 8-bit or 12-bit."""
    if lossless:
        return imagecodecs.ljpeg_encode(
            data, bitspersample=bitspersample, out=out
        )
    if data.dtype == numpy.uint8:
        func = imagecodecs.jpeg8_encode
    elif data.dtype == numpy.uint16:
        func = imagecodecs.jpeg12_encode
    else:
        raise ValueError(f'invalid data type {data.dtype}')
    return func(
        data,
        level=level,
        colorspace=colorspace,
        outcolorspace=outcolorspace,
        subsampling=subsampling,
        optimize=optimize,
        smoothing=smoothing,
        numthreads=numthreads,
        out=out,
    )


# initialize package
imagecodecs = sys.modules['imagecodecs']

_register_codecs()
