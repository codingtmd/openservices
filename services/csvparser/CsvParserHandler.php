<?php
/*Add your server side implenmentation below */
class CsvParserHandler implements \openservices\CsvParserIf
{
    public function parse($content, $delimiter)
    {
        return str_getcsv($val);
    }
}
