
from csvkitcat.alltext import AllTextUtility
import csv

def count_csv_rows(file, no_headers=False):
    c = csv.reader(file)
    if not no_headers:
        headers = next(c)
    else:
        headers = None

    xc = sum(1 for r in c)
    return xc

class CSVCount(AllTextUtility):
    description = """Returns count of rows, not counting header. Much much MUCH slower than `xsv count` ¯\\_(ツ)_/¯"""

    override_flags = [] # 'L', 'blanks', 'date-format', 'datetime-format']

    def add_arguments(self):
        self.argparser.add_argument('-D', '--out-delimiter', dest='out_delimiter',
                                    help='Delimiting character of the output CSV file.')


    def main(self):
        x = count_csv_rows(self.skip_lines(), no_headers=self.args.no_header_row)
        self.output_file.write("{}\n".format(x))


def launch_new_instance():
    utility = CSVCount()
    utility.run()


if __name__ == '__main__':
    launch_new_instance()