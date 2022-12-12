#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    glasn = set("аеёийоуыэюя")

    s = input("Введите строку: ").lower()

    count = 0
    for i in s:
        if i in glasn:
            count += 1

    print(f"Количество гласных: {count}")
