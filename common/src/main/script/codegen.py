#!/usr/bin/python

'''Translate templates into collections source code'''

import argparse
import os.path


def convert_template(template_dir, output_dir, primitive, obj):
    map_types = ["Collections", "ObjectMap", "ObjectHashMap"]
    key_name = primitive.capitalize()
    keyNumberMethod = primitive + "Value"
    if primitive == "long":
        hashCodeFn = "(int) (key ^ (key >>> 32))"
    else:
        hashCodeFn = "(int) key"

    for map_type in map_types:
        template_fname = os.path.join(template_dir,
                                      "K" + map_type + ".template")
        output_fname = os.path.join(output_dir, key_name + map_type + ".java")
        with open(template_fname, "r") as fp:
            code = fp.read()

        with open(output_fname, "w") as fp:
            fp.write(code.replace("@K@", key_name)
                     .replace("@k@", primitive)
                     .replace("@O@", obj)
                     .replace("@KEY_NUMBER_METHOD@", keyNumberMethod)
                     .replace("@HASH_CODE@", hashCodeFn))


def translate(template_dir, output_dir):
    key_primitives = ["byte", "char", "short", "int", "long"]
    key_objects = ["Byte", "Character", "Short", "Integer", "Long"]
    for primitive, obj in zip(key_primitives, key_objects):
        convert_template(template_dir, output_dir, primitive, obj)


def main():
    parser = argparse.ArgumentParser(
        description = __doc__,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    template_dir = os.path.join(os.path.dirname(__file__),
                                '../templates/io/netty/util/collection')
    parser.add_argument(
        '--output', required=True,
        help='Directory that stored generated java files')
    args = parser.parse_args()
    translate(template_dir, args.output)


if __name__ == '__main__':
    main()
