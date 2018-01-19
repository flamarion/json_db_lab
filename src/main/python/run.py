#!/usr/bin/env python

from json_cabuloso import JsonCabuloso
import argparse


def main(args):
    op = JsonCabuloso(args.file)

    if args.add and args.dry_run:
        op.add(args.add[0], args.add[1])
        print("Key, Value pair added successfully")
        print(op.retrieveAll())
    elif args.add:
        op.add(args.add[0], args.add[1])
        print("Key, Value pair added successfully")
        op.save()
    elif args.delete and args.dry_run:
        if op.delete(args.delete[0]):
            op.delete(args.delete[0])
            print("Key pair deleted successfully")
            print(op.retrieveAll())
        else:
            print("Key {key} not found for deletion".format(key=args.change[0]))
    elif args.delete:
        try:
            op.delete(args.delete[0])
            op.save()
            print("Key pair deleted successfully")
            print(op.retrieveAll())
        except KeyError:
            print("Key not found for deletion")
    elif args.change and args.dry_run:
        try:
            op.retrieveAll()[args.change[0]]
        except KeyError:
            raise
        else:
            op.change(args.change[0], args.change[1])
            print(op.retrieveAll())
    elif args.change:
        try:
            op.retrieveAll()[args.change[0]]
        except KeyError:
            raise
        else:
            op.change(args.change[0], args.change[1])
            op.save()
            print(op.retrieveAll())
    elif args.query:
        print(op.query(args.query[0]))
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
    parser.add_argument('--dry-run', help='Does not change the file', action='store_true')
    args = parser.parse_args()
    main(args)
