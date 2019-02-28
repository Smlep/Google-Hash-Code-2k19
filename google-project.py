#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 18:32:02 2019

@author: Vincoux
"""

import sys


class Photo:
    def __init__(self, line, id):
        line_split = line.split(' ')
        self.id = id
        self.vertical = line_split[0] == 'V'
        self.tags = []
        for tag_str in line_split[2:]:
            self.tags.append(tag_str)

    def __str__(self):
        res = str(self.id)
        if self.vertical:
            res += ' Vertical '
        else:
            res += ' Horizontal '
        for tag in self.tags:
            res += tag + ' '
        return res


class Slide:
    def __init__(self, photo1, photo2=None):
        self.photos = []
        if not photo2:
            if photo1.vertical:
                print('Only one vertical photo', file=sys.stderr)
            else:
                self.photos.append(photo1)
        else:
            if not photo1.vertical or not photo2.vertical:
                print("The two photos aren't vertical", file=sys.stderr)
            else:
                self.photos.append(photo1)
                self.photos.append(photo2)

    def get_tags(self):
        if len(self.photos) == 2:
            return list(set(self.photos[0].tags + self.photos[1].tags))
        return self.photos[0]

    def __str__(self):
        res = str(self.photos[0].id)
        if len(self.photos) == 2:
            res += ' ' + str(self.photos[1].id)
        return res


def process_file(filename, out):
    photos = []
    file = open(filename, "r")
    lines = file.readlines()
    for i in range(1, len(lines)):
        photos.append(Photo(lines[i], i - 1))

    verticals = []

    slides = []
    for photo in photos:
        if photo.vertical:
            verticals.append(photo)
        else:
            slides.append(Slide(photo))

    out = open(out, 'w')
    out.write(str(len(slides)) + '\n')
    for slide in slides:
        out.write(str(slide) + '\n')
    out.close()


process_file('in/a_example.txt', 'out/a_example_out.txt')
process_file('in/b_lovely_landscapes.txt', 'out/b_lovely_landscapes_out.txt')
process_file('in/c_memorable_moments.txt', 'out/c_memorable_moments_out.txt')
process_file('in/d_pet_pictures.txt', 'out/d_pet_pictures_out.txt')
process_file('in/e_shiny_selfies.txt', 'out/e_shiny_selfies_out.txt')
