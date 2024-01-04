RG Image Transform V1.2: Technique for Creating an IRG (EIR-Style) Image from a Single Full-Spectrum Digital Image
This image is posted for this discussion group:

www.flickr.com/groups/55027594@N00/discuss/72157601045395...

 

Please see this related figure first:

www.flickr.com/photos/jw_wong/4959503473/

 

 

This is a screen capture of a custom software that creates an IRG colour infrared image from a yellow-filtered full-spectrum image.

 

The mathematical model used is as follows:

 

Y = IR channel

X1 = Red channel

X2 = Green channel

X3 = Blue channel

Z1 = full-spectrum Red channel (Red + Infrared)

Z2 = full-spectrum Green channel (Green + Infrared)

Z3 = full-spectrum Blue channel (Blue + Infrared)

 

A regular colour image is represented by: (R,G,B) = (X1,X2,X3)

A IRG colour infrared image is represented by: (R,G,B) = (Y,X1,X2)

In a regular full-spectrum image, the channels are mapped: (R,G,B) = (Z1,Z2,Z3)

 

The full-spectrum channels are modeled by the following equations:

Z1 = (1 - (1 - X1) ^ gammaRx) * fracRx + (1 - (1 - Y) ^ gammaRy) * fracRY

Z2 = (1 - (1 - X2) ^ gammaGx) * fracGx + (1 - (1 - Y) ^ gammaGy) * fracGY

Z3 = (1 - (1 - X3) ^ gammaBx) * fracBx + (1 - (1 - Y) ^ gammaBy) * fracBY

 

Constants

fracRx - fraction of Red component in full-spectrum Red channel

fracRy - fraction of Infrared component in full-spectrum Red channel

fracGx - fraction of Green component in full-spectrum Green channel

fracGy - fraction of Infrared component in full-spectrum Green channel

fracBx - fraction of Blue component in full-spectrum Blue channel

fracBy - fraction of Infrared component in full-spectrum Blue channel

 

gammaRx - gamma correction of Red component in full-spectrum Red channel

gammaRy - gamma correction of Infrared component in full-spectrum Red channel

gammaGx - gamma correction of Green component in full-spectrum Green channel

gammaGy - gamma correction of Infrared component in full-spectrum Green channel

gammaBx - gamma correction of Blue component in full-spectrum Blue channel

gammaBy - gamma correction of Infrared component in full-spectrum Blue channel

 

Constraints:

0 <= X1, X2, X3, Y, Z1, Z2, Z3, fracRx, fracRy, fracGx, fracGy, fracBx, fracBy <= 1

fracRx + fracRy <= 1

fracGx + fracGy <= 1

fracBx + fracBy <= 1

0.1 <= gammaRx, gammaRy, gammaGx, gammaGy, gammaBx, gammaBy <= 10

 

Taking a full-spectrum image through a yellow filter is modeled by setting fracBx = 0, thus eliminating X3 from the equation for Z3, then

Z3 = (1 - (1 - Y) ^ gammaBy) * fracBY

 

By rearranging the equations for Z1, Z2, Z3, it is now possible to derive Y, X1, X2 as follows:

Y = 1 - (1 - Z3 / fracBy) ^ (1 / gammaBy)

X1 = 1 - (1 - ((Z1 - (fracRy * (1 - (1 - Y) ^ gammaRy))) / fracRx)) ^ (1 / gammaRx)

X2 = 1 - (1 - ((Z2 - (fracGy * (1 - (1 - Y) ^ gammaGy))) / fracGx)) ^ (1 / gammaGx)

 

These are the formulae used in the IRG Tranform software pictured above. By applying the values of "frac"and "gamma" used in creating the simulated yellow-filtered full-spectrum image, the values of Y, X1, X2 are extracted, thus allowing the creation of the IRG image.

 

In an actual "real" full-spectrum image, the values of "frac" and "gamma" are unknown and must be detemined by "trial and error" or careful calibration.
