import sys

def downcase_it(txt):
    return txt.lower()

if len(sys.argv) < 2:
    print("none")
else:
    for para in sys.argv[1:]:
        print(downcase_it(para))