#!/usr/bin/env python3

import sys
from argparse import ArgumentParser
import os
import os.path
import pyparsing as pp
import hashlib
import json
import pprint

def lexical_analysis(src):
    string = pp.Regex('[a-zA-Z0-9_{}"=+\-*/\.:; ａ-ｚＡ-Ｚぁ-ゔゞァ-・ヽヾ゛゜ー一-龯]+')

    blank = pp.LineStart() + pp.LineEnd()

    start = '['
    end = ']' + pp.LineEnd()

    graph_tag = pp.LineStart() + '@'
    graph = graph_tag + start + string + end

    view_tag = pp.LineStart() + '#'
    view = view_tag + start + string + end

    server_process_tag = pp.LineStart() + '$'
    server_process = server_process_tag + start + string + end

    client_process_tag = pp.LineStart() + '%'
    client_process = client_process_tag + start + string + end

    view_transition_identifier = pp.LineStart() + '-->'
    view_transition = view_transition_identifier + string

    process_transition_identifier = pp.LineStart() + '==>'
    process_transition = process_transition_identifier + string

    state_machine = pp.OneOrMore(graph | view | server_process | client_process | view_transition | process_transition | string | blank)

    return state_machine.parseString(src)

def syntactic_analysis(src):
    prev = False
    next_views_count = 0
    count = 0
    d = {'graph': {'title': ''}, 'views': {}, 'server_processes': {}, 'client_processes': {}}
    for elem in src:
        if elem[0] == '@' and elem[1] == '[' and elem[3] == ']':
            d['graph'][elem[2]] = ''
            prev = elem

        elif elem[0] == '#' and elem[1] == '[' and elem[3] == ']':
            d['views'][elem[2]] = {}
            d['views'][elem[2]]['path'] = ''
            d['views'][elem[2]]['next_views'] = {}
            d['views'][elem[2]]['next_server_processes'] = {}
            d['views'][elem[2]]['next_server_processes']['action'] = {}
            d['views'][elem[2]]['next_server_processes']['process'] = {}
            d['views'][elem[2]]['next_client_processes'] = {}
            d['views'][elem[2]]['next_client_processes']['action'] = {}
            d['views'][elem[2]]['next_client_processes']['process'] = {}
            prev = elem
            next_views_count = 0
            count = 0

        elif elem[0] == '$' and elem[1] == '[' and elem[3] == ']':
            d['server_processes'][elem[2]] = {}
            d['server_processes'][elem[2]]['next_server_processes'] = {}
            d['server_processes'][elem[2]]['next_server_processes']['action'] = {}
            d['server_processes'][elem[2]]['next_server_processes']['process'] = {}
            prev = elem
            count = 0

        elif elem[0] == '%' and elem[1] == '[' and elem[3] == ']':
            d['client_processes'][elem[2]] = {}
            d['client_processes'][elem[2]]['next_client_processes'] = {}
            d['client_processes'][elem[2]]['next_client_processes']['action'] = {}
            d['client_processes'][elem[2]]['next_client_processes']['process'] = {}
            prev = elem
            count = 0

        elif prev and prev[0] == '@':
            d['graph'][prev[2]] = elem[0].strip()

        elif prev and prev[0] == '#' and elem[0] != '-->' and elem[0].startswith('/'):
            d['views'][prev[2]]['path'] = elem[0]

        elif prev and prev[0] == '#' and elem[0] == '-->':
            d['views'][prev[2]]['next_views'][next_views_count] = elem[1].strip()
            next_views_count = next_views_count + 1

        elif prev and prev[0] == '#' and elem[0] != '==>':
            d['views'][prev[2]]['next_server_processes']['action'][count] = elem[0].strip()

        elif prev and prev[0] == '#' and elem[0] == '==>':
            d['views'][prev[2]]['next_server_processes']['process'][count] = elem[1].strip()
            count = count + 1

        elif prev and prev[0] == '$' and elem[0] != '==>':
            d['server_processes'][prev[2]]['next_server_processes']['action'][count] = elem[0].strip()

        elif prev and prev[0] == '$' and elem[0] == '==>':
            d['server_processes'][prev[2]]['next_server_processes']['process'][count] = elem[1].strip()
            count = count + 1

        elif prev and prev[0] == '%' and elem[0] != '==>':
            d['client_processes'][prev[2]]['next_client_processes']['action'][count] = elem[0].strip()

        elif prev and prev[0] == '%' and elem[0] == '==>':
            d['client_processes'][prev[2]]['next_client_processes']['process'][count] = elem[1].strip()
            count = count + 1

    return d

def generate(in_file, out_path, image_type, src, fontname=None):
    dot_file = hashlib.md5(bytes(json.dumps(src), 'utf-8')).hexdigest()
    out_file = os.path.basename(in_file.replace('.txt', '.' + image_type))
    f_out = open(dot_file, 'w', encoding='utf-8')
    f_out.write('digraph sample {')
    fontsetting = "fontname=\"" + fontname + "\"" if fontname else ""
    f_out.write('graph [label="' + src['graph']['title'] + '",labelloc=t,fontsize=18,' + fontsetting + '];')
    f_out.write('node ['+fontsetting+'];')
    f_out.write('edge ['+fontsetting+'];')
    for key, value in src['views'].items():
        f_out.write('"' + key + '"' + '[peripheries=2,label="' + key + ' ' + value['path'] + '"];')
    for key, value in src['views'].items():
        for key2, value2 in value['next_views'].items():
            f_out.write('"' + key + '"' + '->' + '"' + value2 + '"' + '[style=dashed];')
    for key, value in src['server_processes'].items():
        f_out.write('"' + key + '"' + '[style=filled];')
    for key, value in src['views'].items():
        for key2, value2 in value.items():
            if key2 != 'path' and key2 != 'next_views':
                for key3, value3 in value2['process'].items():
                    if key3 in value2['action']:
                        f_out.write('"' + key + '"' + '->' + '"' + value3 + '"' + '[label="' + value2['action'][key3] + '"];')
                    else:
                        f_out.write('"' + key + '"' + '->' + '"' + value3 + '";')
    for key, value in src['server_processes'].items():
        for key2, value2 in value.items():
            for key3, value3 in value2['process'].items():
                if key3 in value2['action']:
                    f_out.write('"' + key + '"' + '->' + '"' + value3 + '"' + '[label="' + value2['action'][key3] + '"];')
                else:
                    f_out.write('"' + key + '"' + '->' + '"' + value3 + '";')
    for key, value in src['client_processes'].items():
        for key2, value2 in value.items():
            for key3, value3 in value2['process'].items():
                if key3 in value2['action']:
                    f_out.write('"' + key + '"' + '->' + '"' + value3 + '"' + '[label="' + value2['action'][key3] + '"];')
                else:
                    f_out.write('"' + key + '"' + '->' + '"' + value3 + '";')
    f_out.write('}')
    f_out.flush()
    f_out.close()

    command1 = 'dot -T' + image_type + ' -o ' + out_path + '/' + out_file + ' ' + dot_file
    os.system(command1)

    os.remove(dot_file)

def compile(in_file, out_path, image_type, fontname=None):
    f_in = open(in_file, 'r', encoding='utf-8')
    lines = []
    for line in f_in.readlines():
        replaced_line = str(line.replace('\n',''))
        if len(replaced_line) != 0:
            result1 = lexical_analysis(replaced_line)
            lines.append(result1)
    result2 = syntactic_analysis(lines)
    generate(in_file, out_path, image_type, result2, fontname=fontname)

def main():
    parser = ArgumentParser(description='Pyagram: Diagram generator')
    parser.add_argument('-i', '--input', help='Input filename')
    parser.add_argument('-o', '--outpath', help='Output file path', default='.')
    parser.add_argument('-t', '--imagetype', help='Output image type')
    parser.add_argument('-f', '--font', help='Fontname for labels')
    _args = parser.parse_args()
    if not _args.imagetype in ['gif', 'png', 'svg']:
        raise ValueError('Output image type must be gif, png or svg.')
    if not os.path.exists(_args.outpath):
        raise ValueError('Output file path must exist.')
    compile(_args.input, _args.outpath, _args.imagetype, fontname=_args.font)

if __name__ == '__main__':
    main()
