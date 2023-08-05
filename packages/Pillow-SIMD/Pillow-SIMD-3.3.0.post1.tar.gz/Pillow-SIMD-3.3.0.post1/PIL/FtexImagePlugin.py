"""
A Pillow loader for .ftc and .ftu files (FTEX)
Jerome Leclanche <jerome@leclan.ch>

The contents of this file are hereby released in the public domain (CC0)
Full text of the CC0 license:
  https://creativecommons.org/publicdomain/zero/1.0/

Independence War 2: Edge Of Chaos - Texture File Format - 16 October 2001

The textures used for 3D objects in Independence War 2: Edge Of Chaos are in a
packed custom format called FTEX. This file format uses file extensions FTC and FTU.
* FTC files are compressed textures (using standard texture compression).
* FTU files are not compressed.
Texture File Format
The FTC and FTU texture files both use the same format, called. This
has the following structure:
{header}
{format_directory}
{data}
Where:
{header} = { u32:magic, u32:version, u32:width, u32:height, u32:mipmap_count, u32:format_count }

* The "magic" number is "FTEX".
* "width" and "height" are the dimensions of the texture.
* "mipmap_count" is the number of mipmaps in the texture.
* "format_count" is the number of texture formats (different versions of the same texture) in this file.

{format_directory} = format_count * { u32:format, u32:where }

The format value is 0 for DXT1 compressed textures and 1 for 24-bit RGB uncompressed textures.
The texture data for a format starts at the position "where" in the file.

Each set of texture data in the file has the following structure:
{data} = format_count * { u32:mipmap_size, mipmap_size * { u8 } }
* "mipmap_size" is the number of bytes in that mip level. For compressed textures this is the
size of the texture data compressed with DXT1. For 24 bit uncompressed textures, this is 3 * width * height.
Following this are the image bytes for that mipmap level.

Note: All data is stored in little-Endian (Intel) byte order.
"""

import struct
from io import BytesIO
from PIL import Image, ImageFile
from PIL.DdsImagePlugin import _dxt1


MAGIC = b"FTEX"
FORMAT_DXT1 = 0
FORMAT_UNCOMPRESSED = 1


class FtexImageFile(ImageFile.ImageFile):
    format = "FTEX"
    format_description = "Texture File Format (IW2:EOC)"

    def _open(self):
        magic = struct.unpack("<I", self.fp.read(4))
        version = struct.unpack("<i", self.fp.read(4))
        self.size = struct.unpack("<2i", self.fp.read(8))
        mipmap_count, format_count = struct.unpack("<2i", self.fp.read(8))

        self.mode = "RGB"

        # Only support single-format files. I don't know of any multi-format file.
        assert format_count == 1

        format, where = struct.unpack("<2i", self.fp.read(8))
        self.fp.seek(where)
        mipmap_size, = struct.unpack("<i", self.fp.read(4))

        data = self.fp.read(mipmap_size)

        if format == FORMAT_DXT1:
            data = _dxt1(BytesIO(data), self.width, self.height)
            self.tile = [("raw", (0, 0) + self.size, 0, ('RGBX', 0, 1))]
        elif format == FORMAT_UNCOMPRESSED:
            self.tile = [("raw", (0, 0) + self.size, 0, ('RGB', 0, 1))]
        else:
            raise ValueError("Invalid texture compression format: %r" % (format))

        self.fp.close()
        self.fp = BytesIO(data)

    def load_seek(self, pos):
        pass


def _validate(prefix):
    return prefix[:4] == MAGIC


Image.register_open(FtexImageFile.format, FtexImageFile, _validate)
Image.register_extension(FtexImageFile.format, ".ftc")
Image.register_extension(FtexImageFile.format, ".ftu")
