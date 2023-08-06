=========================
Hearthstone Card Detector
=========================
To use (with caution), simply do::

    >>> from hearthstonecarddetector import image_to_card_id
    >>> from PIL import Image
    >>> with Image.open("test_image_here.ext") as img:
    >>>     # if image is not cropped, perform the crop now
    >>>     img = img.crop(bbox=(x1, y1, x2, y2))
    >>>     card_id = image_to_card_id(img)
    >>>     print(card_id)

It's that simple!

db
^^
The most interesting part of this module is the hashing of all the cards.
The hashes are taken of only a certain crop of the card image, a good portion
of the artwork. This is explained in "crop_explained.png" and you can see
the examples in the tests folder for more help.

Each card was hashed in the four ways provided by the imagehash library. These are
average_hash, dhash, phash, and whash. phash is the default algorithm used in this
module.

Tests and Examples
^^^^^^^^^^^^^^^^^^
Please take a look at the tests directory. You will find several images
that are cropped appropriately, in order to match. The TestDetector.py file
also contains a working code example.

Please examine the file "crop_explained.png" for information about
specific areas to crop. For even more information, you can find the
entire collection of cropped images that were used to create these hashes
online at https://s3.amazonaws.com/draftwithme/hashed_images/ + CARD_ID .png.
For example, the first card is linked at
"https://s3.amazonaws.com/draftwithme/hashed_images/AT_001.png".

Future Work
^^^^^^^^^^^
Ideally, this library should support working with full card images. The problem
was that the bottom half of cards are all too similar, so hashing the full image
ended up with lots of errors. Focusing on the card artwork has provided a lot of
success.

One idea for improvement is to organize the cards by mana (and subsequently by attack / health).
Then, parse each of these individually and compare some region to the region previously hashed and indexed.


License
^^^^^^^
The MIT License (MIT)

Copyright (c) 2016 Tristan Kernan

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and
associated documentation files (the "Software"), to deal in the Software without restriction, including without
limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the
Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial
portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT
LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE
OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.