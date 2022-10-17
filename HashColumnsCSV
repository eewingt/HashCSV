import csv
import hashlib
import hmac
import base64

IN_PATH = r'C:\Users\username\Downloads\testHash.csv'
OUT_PATH = r'C:\Users\username\Downloads\test_Hash.csv'
ENCODING = 'utf8'
HASH_COLUMNS = dict(Column5='md5')


def main():
    with open(IN_PATH, 'rt', encoding=ENCODING, newline='') as in_file, \
            open(OUT_PATH, 'wt', encoding=ENCODING, newline='') as out_file:
        reader = csv.DictReader(in_file)
        writer = csv.DictWriter(out_file, reader.fieldnames)
        writer.writeheader()
        for row in reader:
            for column, method in HASH_COLUMNS.items():
                data = row[column].encode(ENCODING)
                digest = hashlib.new(method, data).hexdigest()
                row[column] = '0x' + digest.upper()
            writer.writerow(row)

if __name__ == '__main__':
    main()
