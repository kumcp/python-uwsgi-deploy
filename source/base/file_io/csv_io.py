
import csv
from ..data_transpose.dict_transpose import (
    filter_dict_by_keys,
    get_value_list,
    transform_list_dict)


def read_data_csv_line_list(csv_file, **kwargs):
    """Read data from a csv file to a line list

    CSV:
    item1-1,item1-2,item1-3
    item2-1,item2-2,item2-3
    item3-1,item3-2,item3-3

    ->
    [
        "item1-1,item1-2,item1-3",
        "item2-1,item2-2,item2-3",
        "item3-1,item3-2,item3-3"
    ]

    Arguments:
        csv_file {string} -- path to csv file

    Raises:
        error -- if there are problems reading or file

    Returns:
        list -- string list of csv file
    """

    try:
        with open(csv_file, 'r', encoding="utf-8") as f:
            reader = csv.reader(f, **kwargs)
            data_list = list(reader)
    except IOError as error:
        raise error
    return data_list


def read_data_csv_dict_list(csv_file):
    """Read data csv as header is the key and each line is an dictionary

    CSV:
    header1,header2,header3
    item2-1,item2-2,item2-3
    item3-1,item3-2,item3-3

    ->
    [
        {
            "header1" : "item2-1",
            "header2" : "item2-1",
            "header3" : "item2-3"
        },
        {
            "header1" : "item3-1",
            "header2" : "item3-1",
            "header3" : "item3-3"
        }
    ]

    Arguments:
        csv_file {string} -- csv file path

    Raises:
        Exception -- error

    Returns:
        dict -- A dictionary follow format

    """

    line_list = read_data_csv_line_list(csv_file, delimiter=",")

    if (len(line_list) < 1):
        raise ValueError("csv file does not contain headers")

    headers = line_list[0]

    return [transform_list_dict(headers, line)
            for index, line in enumerate(line_list) if index > 0]


def read_csv_dict_horizontal(csv_file, **kwargs):
    """Read data csv as each row has the first item is the key
    and the rest item is a list belong to this key in dict

    CSV:
    group1,item1-1,item1-2
    group2,item2-1,item2-2,item2-3,item2-4
    group3,item3-1,item3-2,item3-3

    ->
    {
        "group1": ["item1-1", "item1-2"],
        "group2": ["item2-1", "item2-2", "item2-3", "item2-4"],
        "group3": ["item3-1", "item3-2", "item3-3"],
    }

    Arguments:
        csv_file {string} -- csv file path

    Returns:
        dict -- A dictionary follow format
    """

    line_list = read_data_csv_line_list(csv_file, **kwargs)

    result = {}

    for item_line in line_list:
        if len(item_line) < 1:
            continue

        if item_line[0].strip() == '':
            continue

        result[item_line[0].strip()] = item_line[1:]

    return result


def write_data_csv_line_list(label_list, data_list, output_csv_file, **extra):
    """Write data from data_list to output_csv_file
    Only write the item in label_list

    Arguments:
        label_list {list} -- list string label header
        data_list {list} -- list line need writing to csv file
        output_csv_file {string} -- output csv file

    Raises:
        identifier -- [description]
    """

    try:
        with open(output_csv_file, 'w', encoding="utf-8") as f:
            writer = csv.writer(f, **extra)
            writer.writerow(label_list)

            for line in data_list:
                writer.writerow(line)

    except IOError as error:
        raise error


def write_data_csv_dict_list(label_list, data_list, output_csv_file, **extra):
    """Write data from data_dict_list to output_csv_file
    Only write the item in label_list

    data_list = [
        {col1: 1, col2: 2, col3: 3},
        {col1: 4, col2: 5, col3: 6},
        {col1: 1, col2: 2},
    ]

    => will be written as:
    ```
    col1,col2,col3
    1,2,3
    4,5,6
    1,2,
    ```

    Arguments:
        label_list {list} -- list string label header
        data_list {list} -- list dictionary contain label
        output_csv_file {string} -- output csv file

    Raises:
        identifier -- [description]
    """

    def extract(row): return get_value_list(row, label_list)

    data_dict_filter_list = [extract(item) for item in data_list]

    return write_data_csv_line_list(label_list, data_dict_filter_list,
                                    output_csv_file, **extra)


# Maping default function
read_data_csv = read_data_csv_line_list
write_data_csv = write_data_csv_dict_list
