Printing Barcodes
-----------------
:Last Reviewed: 2016-07-31

Most ESC/POS-printers implement barcode-printing.
The barcode-commandset is implemented in the barcode-method.
For a list of compatible barcodes you should check the manual of your printer.
As a rule of thumb: even older Epson-models support most 1D-barcodes.
To be sure just try some implementations and have a look at the notices below.

bla
~~~~~~~~
.. py:currentmodule:: escpos.escpos
.. autoclass:: escpos.escpos.Escpos

   .. automethod:: barcode
