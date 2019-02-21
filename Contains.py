#!/usr/bin/ env python3

impore argparse

parser = argparse.ArgumentParser(description='Search for words including partial word')
parser.add_argument('snippet', help='partial (or complete) string to search for in words')
args = parser.parse_args()
snippet = args.snippet.lower()
words = open('/usr/share/dick/words').readlines()
print([word.strop() for words in words if snippet in word.lower()])
