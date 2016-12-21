# import sys
import argparse


def convert(filename, numbers, separator=";", newfilename=None):
    with open(filename) as f:
        lines = f.readlines()

        total_lines = len(lines)
        print "Number %d" % total_lines
        if len(lines) % int(numbers):
            print "Error!"
            return 1

        buckets = []
        current_line_index = 0
        current_bucket_index = 0

        while current_line_index < total_lines:
            if current_line_index % int(numbers) == 0:
                current_bucket_index = current_bucket_index + 1
                buckets.append([])
                print "Next %d bucket created" % current_bucket_index

            buckets[current_bucket_index - 1].append(
                lines[current_line_index].replace('\n', ''))
            current_line_index = current_line_index + 1
            print "Current line number %d" % current_line_index

        print buckets
        output_file = filename + ".csv" if not newfilename else newfilename

        # hack to create file
        with open(output_file, "w") as f:
            print "Created new file %s" % output_file

        with open(output_file, "w") as f:
            for bucket in buckets:
                f.write(separator.join(bucket))
                f.write('\n')
    pass

####
# It is useful if you have file with values on each new line
# and you want to have it converted to csv file
# where lines will be transformed to elements separated
# by semicolon.
# For that purpose you have to have file with lines equal to
# any number multiplied by parameter `number`.
# For example, a.txt file has:
# a
# b
# c
# d
#
# if you call script $ python convert_cert.py --file a.txt --number 2
# it will produce new file a.txt.csv
# where content will be next:
# a;b
# c;d

if __name__ == '__main__':
    args = argparse.ArgumentParser(
        "This util takes an input file and converts it "
        "to csv.\n Each line out of `number` lines is "
        "seprate value in csv file.")
    args.add_argument(
        "--file",
        required=True,
        help="File name to parse and convert")
    args.add_argument(
        "--number",
        required=True,
        help="Number of lines for one block")
    parsed_args = args.parse_args()
    print parsed_args

    convert(parsed_args.file, parsed_args.number)
