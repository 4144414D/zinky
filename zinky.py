"""
GitHub:https://github.com/4144414D/zinky
Email:adam@nucode.co.uk

Usage:
  zinky <files>... [--not-safe --track-changes]
  zinky --help

Options:
  -h, --help               Show this screen.
  -v, --version            Show the version.
  -n, --not-safe           Parse xml. Can be exploited by malicious XML. 
  -t, --track-changes      Parse track changes timeline.
"""
VERSION="BETA 0.0.1"
from docopt import docopt
import zipfile
import re
import os
import xml.dom.minidom as xml
import time
from datetime import datetime

def find_track_changes(raw_data):
    data = ""
    for line in raw_data:
        data = data + line
    track_changes = re.findall('date="(.*?)"', data)
    return track_changes

def read_core_docProps(docprops,zipinfo,not_safe):
    data = ""
    for line in docprops:
        data = data + line
    dates = re.findall('<dcterms:(.*?) xsi:type="dcterms:W3CDTF">(.*?)</', data)
    print "DATES FOUND"
    for date in dates:
        print str(date[0]) + ":",
        print date[1]
    print 
    print "ZIP DETAILS"
    print_details(zipinfo)
    if not_safe:
        print "\nXML"
        print xml.parseString(data).toprettyxml()

def find_content_xml(path):
    f = open(path,'rb')
    f.seek(30)
    data = f.read(19)
    print "[Content_Types].xml POSITION"
    print "---------------------------------------------"
    if data == "[Content_Types].xml":
        print "It looks to be in the right place"
    else:
        print "It isn't found at offset 0x1D... this is hinky!"
    print
    f.close()
        
def test_document(path,safe,track_changes):
    if os.path.isfile(os.path.abspath(path)):
        print "============================================="
        print path
        print
        find_content_xml(path)
        with zipfile.ZipFile(path, 'r') as zip:
            if track_changes:
                print "TRACK CHANGES"
                print "---------------------------------------------"
                for file in all_file_info:
                    results = find_track_changes(zip.open(file.filename))
                    if results:
                        print file.filename
                        for item in results:
                            print item
                        print
            print "docProps/core.xml"
            print "---------------------------------------------"
            try:
                read_core_docProps(zip.open('docProps/core.xml'),zip.getinfo('docProps/core.xml'),safe)
            except KeyError:
                print "ERROR! Cannot find docProps/core.xml. We would expect to see this is a post 2007 office document"
            #list all details
            all_file_info = zip.infolist()

            for file in all_file_info:
                if file.filename != 'docProps/core.xml':
                    print file.filename
                    print "---------------------------------------------"
                    print_details(file)
                print
    else:
        print "WARNING!",
        print path,
        print "does not exist"

def format_zip_date(date):
    return time.strftime("%Y-%m-%dT%H:%M:%S", date + (0, 0, 0,))#convert zip date to something human

def print_details(zipinfo):
    print 'date_time: ' + format_zip_date(zipinfo.date_time)
    print 'compress_type: ' + str(zipinfo.compress_type)
    print 'comment: ' + str(zipinfo.comment)
    print 'extra: ' + str(zipinfo.extra)
    print 'create_system: ' + str(zipinfo.create_system)
    print 'create_version: ' + str(zipinfo.create_version)
    print 'extract_version: ' + str(zipinfo.extract_version)
    print 'reserved: ' + str(zipinfo.reserved)
    print 'flag_bits: ' + str(zipinfo.flag_bits)
    print 'volume: ' + str(zipinfo.volume)
    print 'internal_attr: ' + str(zipinfo.internal_attr)
    print 'external_attr: ' + str(zipinfo.external_attr)
    print 'header_offset: ' + str(zipinfo.header_offset)
    print 'CRC: ' + str(zipinfo.CRC)
    print 'compress_size: ' + str(zipinfo.compress_size)
    print 'file_size: ' + str(zipinfo.file_size)

if __name__ == '__main__':
    arguments = docopt(__doc__, version=VERSION)
    for file in arguments['<files>']:
        test_document(file,arguments['--not-safe'],arguments['--track-changes'])