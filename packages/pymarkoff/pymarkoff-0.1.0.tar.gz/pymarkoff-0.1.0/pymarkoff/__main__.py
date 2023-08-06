#!/usr/bin/env python3

import pprint as pp
import re
import random
import time

class Head():
    """A dummy class used to anchor the beginning of an input chain."""
    def __len__(self):
        return 0

class Markov:

    """Get a lot of input and produce a short output multiple times.
    Input should be lists of strings beginning with an emptystring.
    The emptystring is used as the entry point every time generate() is called."""
    empty = dict()
    start = "\n"

    def __init__(self, seeds, orders=(0,)):
        """Seeds should be an iterable or iterables.
        This is so that entry points can be determined automatically."""
        if 0 not in orders:
            raise ValueError("0 is a required order.")
        self.transitions = self.empty.copy()
        self.orders = orders
        self.feed(seeds)
        self.cur_state = self.start

    def feed(self, seeds, sep=' '):
        """Feed the generator with a list of seeds (iterables).
        I.e. m = pymarkoff.Markov()
        m.feed([['The','quick','brown','fox','jumped','over','the','lazy','dog.']])
        m.generate() => ['The','lazy','dog.']

        """
        for seed in seeds:
            # print(seed)
            seed = [Head()] + seed
            for cur_order in self.orders:
                # for each head + tail
                # Or rather count(tail|head)
                for i in range(len(seed) - cur_order):
                    try:
                        head = tuple(
                            s for s in seed[i:i + cur_order + 1] if len(s) > 0)

                        tail = seed[i + cur_order + 1]
                        self.transitions[head].append(tail
                                                      )
                    except KeyError:
                        self.transitions[head] = [tail]
                    except IndexError:
                        pass

    def generate(self, *, max_length=100, terminators=('.', '?', '!'), sep=' '):
        result = []
        state = Head()
        choice = ''
        i = 0
        while i <= max_length and not state in terminators:
            # check for transitions in the highest allowed order first
            # then check lower orders
            for cur_order in self.orders[::-1]:
                try:
                    # reach back for a sequence of states of length less equal
                    # to the current order.
                    temp_state = tuple(result[-(cur_order + 1):len(result)])
                    choice = random.choice(self.transitions[temp_state])
                    break
                except KeyError as e:
                    # A KeyError happens where there aren't transitions for an
                    # arbitrary higher order state
                    # In which case, carry on and continue to the next lowest order.
                    pass

            state = choice
            result.append(choice)
            i += 1
        return result

    def __str__(self):
        return str(self.transitions)

    def __iter__(self):
        for t in self.transitions.items():
            yield (t[0], sorted(t[1]))


def prepare_str(s):
    """For massaging purposes."""
    return [''] + s.split(" ")


def clean_data(s):
    return s


def filter_by_user(data):
    good = []
    for sentence in data:
        print(sentence)
        res = input("Good? y/n >>>").lower()
        if res == 'y':
            good.append(sentence)
        elif res == 'e':
            break
        else:
            pass
    return good


def main():
    pass
    # with open("good.txt") as g:
    #     good = g.read().split('\n')
    # with open("sample.txt") as f:
    #         # this bit is just massaging the text into usable data
    #     samples = [prepare_str(line) for line in f.read().split(
    #         "\n") + good if len(line) > 0]

    seeds = ["the quick brown fox jumped over the lazy dog".split(' ') + ['.']]
    print(seeds)
    m = Markov(seeds)

    with open("transitions.txt", 'w') as f:
        f.write(pp.pformat(dict(m)))

    # generate some sentences
    results_o = tuple(m.generate(max_length=20) for i in range(10))
    # pp.pprint(results_o)
    # feed those back in
    # This is a method of telling the generator what is "good" input
    # TRAINING it
    # m.feed([ prepare_str(i) for i in results_o])
    results_f = tuple(' '.join(m.generate(max_length=30)) for i in range(25))
    ascending = sorted(results_f, key=lambda s: len(s))
    print("\n".join(results_f))
    print()
    pp.pprint(dict(m))

if __name__ == '__main__':
    main()

    # from itertools import product
# combs = '\n'.join(' '.join([''.join(line) for line in zip(*sol)])
#                   for sol in product(permutations(prefixes), permutations(suffixes)))
# print(combs)
