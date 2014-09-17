zinky
=====

Use the zip details of post 2007 office documents to find hinky files.

Installing
----------
1) Download and install python2.7 https://www.python.org/download

2) Download and install docopt https://github.com/docopt/docopt

Example Output
----------

Below is an example output from zinky. It shows a few indications that the document may have been faked:

1) The `[Content_Types].xml` file is normally found as the first entry in a zip created by Microsoft products. When documents have been modified and zipped with other software this isn't always the case, and therefore may be hinky.

2) The embedded dates within `docProps/core.xml` don't match the zip date for the file. The document properties seem to show that the document was modified in 2000 but the zip date is 2014-09-16T13:24:24. This should be either 1980-01-01T00:00:00 or the actual date the file was written. The fact it is different again suggests that the file is hinky. 

3) The folders within the zip have dates later then the document properties. These should be 1980-01-01T00:00:00 or the actual date the file was written. The fact they aren’t suggests the zip has been written to disk and re-zipped after some modifications. 

4) The internal_attr and external_attr for the contents are none-zero. Files written by Microsoft products typically set these values to 0. 

5) The flag_bits are not equal to 6, which is normally expected when files are written Microsoft products. 

6) The create_version and the extract_version are all identical. Typically when a file is written by Microsoft products the create_version for folders and xml files is 45 and the extract_version is 20. For embedded jpeg files this would normally be a create_version of 45 and an extract_version of 10. 

7) The compress_type is the same for all files. Normally when files are written by Microsoft products the compress_type will vary depending on the content that is being compressed. For example xml files are typically compress_type 8 and thumbnail jpeg files are compress_type 0 

```
=============================================
example.pptx

[Content_Types].xml POSITION
---------------------------------------------
It isn't found at offset 0x1D... this is hinky!

docProps/core.xml
---------------------------------------------
DATES FOUND
created: 2000-09-16T12:22:45Z
modified: 2000-09-16T12:22:51Z

ZIP DETAILS
date_time: 2014-09-16T13:24:24
compress_type: 8
comment: 
extra: 
create_system: 0
create_version: 20
extract_version: 20
reserved: 0
flag_bits: 0
volume: 0
internal_attr: 1
external_attr: 32
header_offset: 569
CRC: 3484317341
compress_size: 329
file_size: 657

XML
<?xml version="1.0" ?>
<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcmitype="http://purl.org/dc/dcmitype/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
	<dc:title>EXAMPLE</dc:title>
	<dc:creator>Adam</dc:creator>
	<cp:lastModifiedBy>Adam</cp:lastModifiedBy>
	<cp:revision>1</cp:revision>
	<dcterms:created xsi:type="dcterms:W3CDTF">2000-09-16T12:22:45Z</dcterms:created>
	<dcterms:modified xsi:type="dcterms:W3CDTF">2000-09-16T12:22:51Z</dcterms:modified>
</cp:coreProperties>

docProps/app.xml
---------------------------------------------
date_time: 1980-01-01T00:00:00
compress_type: 8
comment: 
extra: 
create_system: 0
create_version: 20
extract_version: 20
reserved: 0
flag_bits: 0
volume: 0
internal_attr: 1
external_attr: 0
header_offset: 0
CRC: 3442205237
compress_size: 523
file_size: 1298


docProps/thumbnail.jpeg
---------------------------------------------
date_time: 1980-01-01T00:00:00
compress_type: 8
comment: 
extra: 
create_system: 0
create_version: 20
extract_version: 20
reserved: 0
flag_bits: 0
volume: 0
internal_attr: 0
external_attr: 0
header_offset: 945
CRC: 3853572735
compress_size: 1229
file_size: 1910

ppt/_rels/
---------------------------------------------
date_time: 2014-09-16T13:24:08
compress_type: 0
comment: 
extra: 
create_system: 0
create_version: 20
extract_version: 20
reserved: 0
flag_bits: 0
volume: 0
internal_attr: 0
external_attr: 16
header_offset: 2227
CRC: 0
compress_size: 0
file_size: 0

ppt/_rels/presentation.xml.rels
---------------------------------------------
date_time: 1980-01-01T00:00:00
compress_type: 8
comment: 
extra: 
create_system: 0
create_version: 20
extract_version: 20
reserved: 0
flag_bits: 0
volume: 0
internal_attr: 1
external_attr: 0
header_offset: 2267
CRC: 120925723
compress_size: 261
file_size: 976

ppt/presentation.xml
---------------------------------------------
date_time: 1980-01-01T00:00:00
compress_type: 8
comment: 
extra: 
create_system: 0
create_version: 20
extract_version: 20
reserved: 0
flag_bits: 0
volume: 0
internal_attr: 1
external_attr: 0
header_offset: 2589
CRC: 880638401
compress_size: 544
file_size: 3212

ppt/presProps.xml
---------------------------------------------
date_time: 1980-01-01T00:00:00
compress_type: 8
comment: 
extra: 
create_system: 0
create_version: 20
extract_version: 20
reserved: 0
flag_bits: 0
volume: 0
internal_attr: 1
external_attr: 0
header_offset: 3183
CRC: 454101784
compress_size: 387
file_size: 816

ppt/slideLayouts/
---------------------------------------------
date_time: 2014-09-16T13:24:08
compress_type: 0
comment: 
extra: 
create_system: 0
create_version: 20
extract_version: 20
reserved: 0
flag_bits: 0
volume: 0
internal_attr: 0
external_attr: 16
header_offset: 3617
CRC: 0
compress_size: 0
file_size: 0

ppt/slideLayouts/_rels/
---------------------------------------------
date_time: 2014-09-16T13:24:08
compress_type: 0
comment: 
extra: 
create_system: 0
create_version: 20
extract_version: 20
reserved: 0
flag_bits: 0
volume: 0
internal_attr: 0
external_attr: 16
header_offset: 3664
CRC: 0
compress_size: 0
file_size: 0

ppt/slideLayouts/_rels/slideLayout1.xml.rels
---------------------------------------------
date_time: 1980-01-01T00:00:00
compress_type: 8
comment: 
extra: 
create_system: 0
create_version: 20
extract_version: 20
reserved: 0
flag_bits: 0
volume: 0
internal_attr: 1
external_attr: 0
header_offset: 3717
CRC: 4052931029
compress_size: 182
file_size: 311

ppt/slideLayouts/_rels/slideLayout10.xml.rels
---------------------------------------------
date_time: 1980-01-01T00:00:00
compress_type: 8
comment: 
extra: 
create_system: 0
create_version: 20
extract_version: 20
reserved: 0
flag_bits: 0
volume: 0
internal_attr: 1
external_attr: 0
header_offset: 3973
CRC: 4052931029
compress_size: 182
file_size: 311

ppt/slideLayouts/_rels/slideLayout11.xml.rels
---------------------------------------------
date_time: 1980-01-01T00:00:00
compress_type: 8
comment: 
extra: 
create_system: 0
create_version: 20
extract_version: 20
reserved: 0
flag_bits: 0
volume: 0
internal_attr: 1
external_attr: 0
header_offset: 4230
CRC: 4052931029
compress_size: 182
file_size: 311

ppt/slideLayouts/_rels/slideLayout2.xml.rels
---------------------------------------------
date_time: 1980-01-01T00:00:00
compress_type: 8
comment: 
extra: 
create_system: 0
create_version: 20
extract_version: 20
reserved: 0
flag_bits: 0
volume: 0
internal_attr: 1
external_attr: 0
header_offset: 4487
CRC: 4052931029
compress_size: 182
file_size: 311

ppt/slideLayouts/_rels/slideLayout3.xml.rels
---------------------------------------------
date_time: 1980-01-01T00:00:00
compress_type: 8
comment: 
extra: 
create_system: 0
create_version: 20
extract_version: 20
reserved: 0
flag_bits: 0
volume: 0
internal_attr: 1
external_attr: 0
header_offset: 4743
CRC: 4052931029
compress_size: 182
file_size: 311

ppt/slideLayouts/_rels/slideLayout4.xml.rels
---------------------------------------------
date_time: 1980-01-01T00:00:00
compress_type: 8
comment: 
extra: 
create_system: 0
create_version: 20
extract_version: 20
reserved: 0
flag_bits: 0
volume: 0
internal_attr: 1
external_attr: 0
header_offset: 4999
CRC: 4052931029
compress_size: 182
file_size: 311

ppt/slideLayouts/_rels/slideLayout5.xml.rels
---------------------------------------------
date_time: 1980-01-01T00:00:00
compress_type: 8
comment: 
extra: 
create_system: 0
create_version: 20
extract_version: 20
reserved: 0
flag_bits: 0
volume: 0
internal_attr: 1
external_attr: 0
header_offset: 5255
CRC: 4052931029
compress_size: 182
file_size: 311

ppt/slideLayouts/_rels/slideLayout6.xml.rels
---------------------------------------------
date_time: 1980-01-01T00:00:00
compress_type: 8
comment: 
extra: 
create_system: 0
create_version: 20
extract_version: 20
reserved: 0
flag_bits: 0
volume: 0
internal_attr: 1
external_attr: 0
header_offset: 5511
CRC: 4052931029
compress_size: 182
file_size: 311

ppt/slideLayouts/_rels/slideLayout7.xml.rels
---------------------------------------------
date_time: 1980-01-01T00:00:00
compress_type: 8
comment: 
extra: 
create_system: 0
create_version: 20
extract_version: 20
reserved: 0
flag_bits: 0
volume: 0
internal_attr: 1
external_attr: 0
header_offset: 5767
CRC: 4052931029
compress_size: 182
file_size: 311

ppt/slideLayouts/_rels/slideLayout8.xml.rels
---------------------------------------------
date_time: 1980-01-01T00:00:00
compress_type: 8
comment: 
extra: 
create_system: 0
create_version: 20
extract_version: 20
reserved: 0
flag_bits: 0
volume: 0
internal_attr: 1
external_attr: 0
header_offset: 6023
CRC: 4052931029
compress_size: 182
file_size: 311

ppt/slideLayouts/_rels/slideLayout9.xml.rels
---------------------------------------------
date_time: 1980-01-01T00:00:00
compress_type: 8
comment: 
extra: 
create_system: 0
create_version: 20
extract_version: 20
reserved: 0
flag_bits: 0
volume: 0
internal_attr: 1
external_attr: 0
header_offset: 6279
CRC: 4052931029
compress_size: 182
file_size: 311

ppt/slideLayouts/slideLayout1.xml
---------------------------------------------
date_time: 1980-01-01T00:00:00
compress_type: 8
comment: 
extra: 
create_system: 0
create_version: 20
extract_version: 20
reserved: 0
flag_bits: 0
volume: 0
internal_attr: 1
external_attr: 0
header_offset: 6535
CRC: 4289559771
compress_size: 1052
file_size: 3675

ppt/slideLayouts/slideLayout10.xml
---------------------------------------------
date_time: 1980-01-01T00:00:00
compress_type: 8
comment: 
extra: 
create_system: 0
create_version: 20
extract_version: 20
reserved: 0
flag_bits: 0
volume: 0
internal_attr: 1
external_attr: 0
header_offset: 7650
CRC: 3788319286
compress_size: 917
file_size: 3025

ppt/slideLayouts/slideLayout11.xml
---------------------------------------------
date_time: 1980-01-01T00:00:00
compress_type: 8
comment: 
extra: 
create_system: 0
create_version: 20
extract_version: 20
reserved: 0
flag_bits: 0
volume: 0
internal_attr: 1
external_attr: 0
header_offset: 8631
CRC: 1170458131
compress_size: 967
file_size: 3249

ppt/slideLayouts/slideLayout2.xml
---------------------------------------------
date_time: 1980-01-01T00:00:00
compress_type: 8
comment: 
extra: 
create_system: 0
create_version: 20
extract_version: 20
reserved: 0
flag_bits: 0
volume: 0
internal_attr: 1
external_attr: 0
header_offset: 9662
CRC: 4105386210
compress_size: 887
file_size: 2970

ppt/slideLayouts/slideLayout3.xml
---------------------------------------------
date_time: 1980-01-01T00:00:00
compress_type: 8
comment: 
extra: 
create_system: 0
create_version: 20
extract_version: 20
reserved: 0
flag_bits: 0
volume: 0
internal_attr: 1
external_attr: 0
header_offset: 10612
CRC: 3496461149
compress_size: 1117
file_size: 4411

ppt/slideLayouts/slideLayout4.xml
---------------------------------------------
date_time: 1980-01-01T00:00:00
compress_type: 8
comment: 
extra: 
create_system: 0
create_version: 20
extract_version: 20
reserved: 0
flag_bits: 0
volume: 0
internal_attr: 1
external_attr: 0
header_offset: 11792
CRC: 1213180690
compress_size: 964
file_size: 3900

ppt/slideLayouts/slideLayout5.xml
---------------------------------------------
date_time: 1980-01-01T00:00:00
compress_type: 8
comment: 
extra: 
create_system: 0
create_version: 20
extract_version: 20
reserved: 0
flag_bits: 0
volume: 0
internal_attr: 1
external_attr: 0
header_offset: 12819
CRC: 3247376944
compress_size: 1236
file_size: 6455

ppt/slideLayouts/slideLayout6.xml
---------------------------------------------
date_time: 1980-01-01T00:00:00
compress_type: 8
comment: 
extra: 
create_system: 0
create_version: 20
extract_version: 20
reserved: 0
flag_bits: 0
volume: 0
internal_attr: 1
external_attr: 0
header_offset: 14118
CRC: 3901197185
compress_size: 794
file_size: 2237

ppt/slideLayouts/slideLayout7.xml
---------------------------------------------
date_time: 1980-01-01T00:00:00
compress_type: 8
comment: 
extra: 
create_system: 0
create_version: 20
extract_version: 20
reserved: 0
flag_bits: 0
volume: 0
internal_attr: 1
external_attr: 0
header_offset: 14975
CRC: 3986940608
compress_size: 746
file_size: 1899

ppt/slideLayouts/slideLayout8.xml
---------------------------------------------
date_time: 1980-01-01T00:00:00
compress_type: 8
comment: 
extra: 
create_system: 0
create_version: 20
extract_version: 20
reserved: 0
flag_bits: 0
volume: 0
internal_attr: 1
external_attr: 0
header_offset: 15784
CRC: 1405569586
compress_size: 1207
file_size: 4797

ppt/slideLayouts/slideLayout9.xml
---------------------------------------------
date_time: 1980-01-01T00:00:00
compress_type: 8
comment: 
extra: 
create_system: 0
create_version: 20
extract_version: 20
reserved: 0
flag_bits: 0
volume: 0
internal_attr: 1
external_attr: 0
header_offset: 17054
CRC: 2276846232
compress_size: 1156
file_size: 4650

ppt/slideMasters/
---------------------------------------------
date_time: 2014-09-16T13:24:08
compress_type: 0
comment: 
extra: 
create_system: 0
create_version: 20
extract_version: 20
reserved: 0
flag_bits: 0
volume: 0
internal_attr: 0
external_attr: 16
header_offset: 18273
CRC: 0
compress_size: 0
file_size: 0

ppt/slideMasters/_rels/
---------------------------------------------
date_time: 2014-09-16T13:24:08
compress_type: 0
comment: 
extra: 
create_system: 0
create_version: 20
extract_version: 20
reserved: 0
flag_bits: 0
volume: 0
internal_attr: 0
external_attr: 16
header_offset: 18320
CRC: 0
compress_size: 0
file_size: 0

ppt/slideMasters/_rels/slideMaster1.xml.rels
---------------------------------------------
date_time: 1980-01-01T00:00:00
compress_type: 8
comment: 
extra: 
create_system: 0
create_version: 20
extract_version: 20
reserved: 0
flag_bits: 0
volume: 0
internal_attr: 1
external_attr: 0
header_offset: 18373
CRC: 559915625
compress_size: 271
file_size: 1991

ppt/slideMasters/slideMaster1.xml
---------------------------------------------
date_time: 1980-01-01T00:00:00
compress_type: 8
comment: 
extra: 
create_system: 0
create_version: 20
extract_version: 20
reserved: 0
flag_bits: 0
volume: 0
internal_attr: 1
external_attr: 0
header_offset: 18718
CRC: 511201415
compress_size: 1811
file_size: 12924

ppt/slides/
---------------------------------------------
date_time: 2014-09-16T13:24:08
compress_type: 0
comment: 
extra: 
create_system: 0
create_version: 20
extract_version: 20
reserved: 0
flag_bits: 0
volume: 0
internal_attr: 0
external_attr: 16
header_offset: 20592
CRC: 0
compress_size: 0
file_size: 0

ppt/slides/_rels/
---------------------------------------------
date_time: 2014-09-16T13:24:08
compress_type: 0
comment: 
extra: 
create_system: 0
create_version: 20
extract_version: 20
reserved: 0
flag_bits: 0
volume: 0
internal_attr: 0
external_attr: 16
header_offset: 20633
CRC: 0
compress_size: 0
file_size: 0

ppt/slides/_rels/slide1.xml.rels
---------------------------------------------
date_time: 1980-01-01T00:00:00
compress_type: 8
comment: 
extra: 
create_system: 0
create_version: 20
extract_version: 20
reserved: 0
flag_bits: 0
volume: 0
internal_attr: 1
external_attr: 0
header_offset: 20680
CRC: 3022216291
compress_size: 185
file_size: 311

ppt/slides/slide1.xml
---------------------------------------------
date_time: 1980-01-01T00:00:00
compress_type: 8
comment: 
extra: 
create_system: 0
create_version: 20
extract_version: 20
reserved: 0
flag_bits: 0
volume: 0
internal_attr: 1
external_attr: 0
header_offset: 20927
CRC: 3110847393
compress_size: 567
file_size: 1329

ppt/tableStyles.xml
---------------------------------------------
date_time: 1980-01-01T00:00:00
compress_type: 8
comment: 
extra: 
create_system: 0
create_version: 20
extract_version: 20
reserved: 0
flag_bits: 0
volume: 0
internal_attr: 1
external_attr: 0
header_offset: 21545
CRC: 2408447448
compress_size: 165
file_size: 182

ppt/theme/
---------------------------------------------
date_time: 2014-09-16T13:24:08
compress_type: 0
comment: 
extra: 
create_system: 0
create_version: 20
extract_version: 20
reserved: 0
flag_bits: 0
volume: 0
internal_attr: 0
external_attr: 16
header_offset: 21759
CRC: 0
compress_size: 0
file_size: 0

ppt/theme/theme1.xml
---------------------------------------------
date_time: 1980-01-01T00:00:00
compress_type: 8
comment: 
extra: 
create_system: 0
create_version: 20
extract_version: 20
reserved: 0
flag_bits: 0
volume: 0
internal_attr: 1
external_attr: 0
header_offset: 21799
CRC: 4028356832
compress_size: 1535
file_size: 6807

ppt/viewProps.xml
---------------------------------------------
date_time: 1980-01-01T00:00:00
compress_type: 8
comment: 
extra: 
create_system: 0
create_version: 20
extract_version: 20
reserved: 0
flag_bits: 0
volume: 0
internal_attr: 1
external_attr: 0
header_offset: 23384
CRC: 1359162733
compress_size: 380
file_size: 810

[Content_Types].xml
---------------------------------------------
date_time: 1980-01-01T00:00:00
compress_type: 8
comment: 
extra: 
create_system: 0
create_version: 20
extract_version: 20
reserved: 0
flag_bits: 0
volume: 0
internal_attr: 1
external_attr: 0
header_offset: 23811
CRC: 4112043231
compress_size: 425
file_size: 3142

_rels/.rels
---------------------------------------------
date_time: 1980-01-01T00:00:00
compress_type: 8
comment: 
extra: 
create_system: 0
create_version: 20
extract_version: 20
reserved: 0
flag_bits: 0
volume: 0
internal_attr: 1
external_attr: 0
header_offset: 24285
CRC: 2708797544
compress_size: 252
file_size: 738
```