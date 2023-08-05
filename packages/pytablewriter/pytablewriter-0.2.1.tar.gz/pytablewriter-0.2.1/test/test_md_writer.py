# encoding: utf-8

"""
.. codeauthor:: Tsuyoshi Hombashi <gogogo.vm@gmail.com>
"""

from __future__ import absolute_import
import collections

import pytablewriter
import pytest

from .data import header_list
from .data import value_matrix
from .data import value_matrix_with_none
from .data import mix_header_list
from .data import mix_value_matrix


Data = collections.namedtuple("Data", "table indent header value expected")

normal_test_data_list = [
    Data(
        table="",
        indent=0,
        header=header_list,
        value=value_matrix,
        expected=""" a |  b  | c |dd | e  
--:|----:|---|--:|----
  1|123.1|a  |1.0|1   
  2|  2.2|bb |2.2|2.2 
  3|  3.3|ccc|3.0|cccc
"""
    ),
    Data(
        table="tablename",
        indent=0,
        header=header_list,
        value=value_matrix,
        expected="""# tablename
 a |  b  | c |dd | e  
--:|----:|---|--:|----
  1|123.1|a  |1.0|1   
  2|  2.2|bb |2.2|2.2 
  3|  3.3|ccc|3.0|cccc
"""
    ),
    Data(
        table="tablename",
        indent=1,
        header=header_list,
        value=value_matrix,
        expected="""## tablename
 a |  b  | c |dd | e  
--:|----:|---|--:|----
  1|123.1|a  |1.0|1   
  2|  2.2|bb |2.2|2.2 
  3|  3.3|ccc|3.0|cccc
"""
    ),
    Data(
        table="",
        indent=0,
        header=header_list,
        value=value_matrix_with_none,
        expected=""" a | b | c |dd | e  
--:|--:|---|--:|----
  1|   |a  |1.0|    
   |2.2|   |2.2|2.2 
  3|3.3|ccc|   |cccc
   |   |   |   |    
"""
    ),
    Data(
        table="",
        indent=0,
        header=mix_header_list,
        value=mix_value_matrix,
        expected=""" i | f  | c  | if |ifc|bool |inf|nan|mix_num|          time          
--:|---:|----|---:|---|-----|---|---|------:|------------------------
  1|1.10|aa  | 1.0|1  |True |inf|nan|    1.0|2017-01-01T00:00:00     
  2|2.20|bbb | 2.2|2.2|False|inf|nan|    inf|2017-01-02T03:04:05+0900
  3|3.33|cccc|-3.0|ccc|True |inf|nan|    nan|2017-01-01T00:00:00     
"""
    ),
]

exception_test_data_list = [
    Data(
        table="",
        indent=0,
        header=[],
        value=[],
        expected=pytablewriter.EmptyHeaderError
    ),
    Data(
        table="",
        indent=0,
        header=[],
        value=value_matrix,
        expected=pytablewriter.EmptyHeaderError
    ),
    Data(
        table="",
        indent=0,
        header=None,
        value=value_matrix,
        expected=pytablewriter.EmptyHeaderError
    ),
    Data(
        table="",
        indent=0,
        header=header_list,
        value=[],
        expected=pytablewriter.EmptyValueError
    ),
    Data(
        table="",
        indent=0,
        header=header_list,
        value=None,
        expected=pytablewriter.EmptyValueError
    ),
]

table_writer_class = pytablewriter.MarkdownTableWriter


class Test_MarkdownTableWriter_write_new_line:

    def test_normal(self, capsys):
        writer = table_writer_class()
        writer.write_null_line()

        out, err = capsys.readouterr()
        assert out == "\n"


class Test_MarkdownTableWriter_write_table:

    @pytest.mark.parametrize(
        ["table", "indent", "header", "value", "expected"],
        [
            [data.table, data.indent, data.header, data.value, data.expected]
            for data in normal_test_data_list
        ]
    )
    def test_normal(self, capsys, table, indent, header, value, expected):
        writer = table_writer_class()
        writer.table_name = table
        writer.set_indent_level(indent)
        writer.header_list = header
        writer.value_matrix = value
        writer.write_table()

        out, err = capsys.readouterr()
        assert out == expected

    @pytest.mark.parametrize(
        ["table", "indent", "header", "value", "expected"],
        [
            [data.table, data.indent, data.header, data.value, data.expected]
            for data in exception_test_data_list
        ]
    )
    def test_exception(self, capsys, table, indent, header, value, expected):
        writer = table_writer_class()
        writer.table_name = table
        writer.set_indent_level(indent)
        writer.header_list = header
        writer.value_matrix = value

        with pytest.raises(expected):
            writer.write_table()
