# General References
- [XML and XPath](https://www.w3schools.com/xml/xml_xpath.asp) from w3schools
- [A Minimal Introduction to XPath](https://pages.lip6.fr/Jean-Francois.Perrot/XML-Int/Session2/XPath/)
- [Test XML command line with xmllint](https://softwaretester.info/test-xml-command-line-with-xmllint/)

# XML Tools
## xmllint
This is in the `libxml2-utils` package on Debian and Ubuntu

See [Baeldung page](https://www.baeldung.com/linux/xmllint) and [Extracting XML data with curl and xmllint](https://www.joshmcarthur.com/til/2018/06/19/extracting-xml-data-with-curl-and-xmllint.html)

## xmlstarlet

Available as Debian package or [homebrew](https://formulae.brew.sh/formula/xmlstarlet)

For example to list all the elements

```
mfranz@cros-x360:~/tmp/xml$ xmlstarlet el config.xml  | head
clickhouse
clickhouse/logger
clickhouse/logger/level
clickhouse/logger/log
clickhouse/logger/errorlog
clickhouse/logger/size
clickhouse/logger/count
```
