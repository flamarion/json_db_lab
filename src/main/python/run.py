#!/usr/bin/env python

from json_cabuloso import JsonCabuloso
import argparse

def main(args):

    op = JsonCabuloso(args.file)

    if args.add:
        try:
            op.add(args.add[0], args.add[1])
            op.save()
            print("Key added successfully")
            print(op.retrieveAll())
        except:
            print('Key already exists')
    elif args.delete:
        try:
            op.delete(args.delete[0])
            op.save()
            print("Key deleted successfully")
            print(op.retrieveAll())
        except:
            print("Key not found")
    elif args.change:
        try:
            op.change(args.change[0], args.change[1])
            op.save()
            print("Key value changed successfuly")
            print(op.retrieveAll())
        except:
            print("Key not found")
    elif args.query:
        try:
            print(op.query(args.query[0]))
        except:
            print("Key not found")
    elif args.query_all:
        print(op.retrieveAll())
    else:
        return False


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Json Cabuloso", prog='run.py')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-a', '--add', nargs=2, metavar=('key', 'value'), help="Add key, value pair")
    group.add_argument('-d', '--delete', nargs=1, metavar='Key', help="Delete key, value pair based on key")
    group.add_argument('-c', '--change', nargs=2, metavar=('key', 'newvalue'), help="Change value of a key")
    group.add_argument('-q', '--query', nargs=1, metavar='key', help="Query value of a key")
    group.add_argument('-qa', '--query-all', help="Query all key,value pairs", action="store_true")
    parser.add_argument('file', help=('File to perform the operations'))
    args = parser.parse_args()
    # print(args)
    main(args)
