import pprint
def toPattern(wd):
    # Returns a string of the pattern form of the given word.
    # e.g. '0.1.2.3.0.4.5.6' for 'DEVMECHA'
    wd = wd.upper()
    n = 0
    Num = {}
    wdP = []

    for c in wd:
        if c not in Num:
            Num[c] = str(n)
            n += 1
        wdP.append(Num[c])
    return '.'.join(wdP)


def main():
    Ps = {}
    fo = open('dictionary.txt')
    wds = fo.read().split('\n')
    fo.close()

    for wd in wds:
        # Get the pattern for each string in wordList:
        p = toPattern(wd)

        if p not in Ps:
            Ps[p] = [wd]
        else:
            Ps[p].append(wd)

    # This is code that writes code. The wordPatterns.py file contains
    # one very, very large assignment statement:
    fo = open('wPs.py', 'w')
    fo.write('Ps = ')
    fo.write(pprint.pformat(Ps))
    fo.close()


if __name__ == '__main__':
    main()