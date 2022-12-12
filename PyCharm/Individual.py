#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    u = set("abcdefghijklmnopqrstuvwxyz")

    a = {"b", "e", "f", "k", "t"}
    b = {"f", "i", "j", "p", "y"}
    c = {"j", "k", "l", "y"}
    d = {"i", "j", "s", "t", "u", "y", "z"}

    # X = (A ∩ C) ∪ (B ∩ C).
    x = a.intersection(c).union(b.intersection(c))
    print(f'X = {x}')

    not_b = u.difference(b)

    # Y = (A ∩ ¯B) ∪ (D / C).
    y = a.intersection(not_b).union(d.difference(c))
    print(f'Y = {y}')
