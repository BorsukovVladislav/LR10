#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":

    punc_marks = set(".?,!:;`'  ")

    s_1 = set(input("Введите первую строку: ").lower())
    s_2 = set(input("Введите вторую строку: ").lower())

    inter = s_1.intersection(s_2)

    clear_inter = inter.difference(punc_marks)

    print(f"Общие символы: {clear_inter}")
