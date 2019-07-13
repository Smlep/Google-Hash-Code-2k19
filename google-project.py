#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 18:32:02 2019

@author: Vincoux
"""

import sys
import random

local_compute = True


class Photo:
    def __init__(self, line, id):
        line_split = line[:-1].split(' ')
        self.id = id
        self.vertical = line_split[0] == 'V'
        self.tags = []
        for tag_str in line_split[2:]:
            self.tags.append(tag_str)

    def get_tags_length(self, other):
        return len(set(self.tags + other.tags))

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
        return self.photos[0].tags

    def __sub__(self, other):
        core = 0
        t1 = self.get_tags()
        t2 = other.get_tags()
        for tag in t1:
            if tag in t2:
                core += 1
        return min(core, len(t1) - core, len(t2) - core)

    def __str__(self):
        res = str(self.photos[0].id)
        if len(self.photos) == 2:
            res += ' ' + str(self.photos[1].id)
        return res


def verticals_to_slides(verticals):
    if not len(verticals):
        return []
    result = []
    moy = 0
    for i in range(1, len(verticals)):
        moy += verticals[0].get_tags_length(verticals[i])
    moy /= len(verticals)
    while (len(verticals) > 1):
        closest = 1000
        index = 1
        for i in range(1, min(len(verticals), 40)):
            current = verticals[0].get_tags_length(verticals[i])
            if (moy == current):
                result.append(Slide(verticals[0], verticals[i]))
                verticals.pop(i)
                verticals.pop(0)
                break
            if (abs(moy - current) < closest):
                closest = abs(moy - current)
                index = i
        result.append(Slide(verticals[0], verticals[index]))
        verticals.pop(index)
        verticals.pop(0)
    return result


def get_slides(photos):
    verticals = []

    slides = []
    for photo in photos:
        if photo.vertical:
            verticals.append(photo)
        else:
            slides.append(Slide(photo))

    vertical_slides = verticals_to_slides(verticals)

    return slides + vertical_slides


def dumb_sort(slides):
    for i in range(len(slides) - 1):
        print('sorting ' + str(i) + '/' + str(len(slides)))
        best_index = 0
        best_compare = 0
        for j in range(i + 1, len(slides)):
            compare = slides[i] - slides[j]
            if compare > best_compare:
                best_compare = compare
                best_index = j
        tmp = slides[i + 1]
        slides[i + 1] = slides[best_index]
        slides[best_index] = tmp


def process_file(filename, out):
    photos = []
    file = open(filename, "r")
    lines = file.readlines()
    for i in range(1, len(lines)):
        photos.append(Photo(lines[i], i - 1))

    slides = get_slides(photos)

    # graph = Graph(slides)
    # print(graph.longest())

    # slides.sort(key=lambda s: len(s.get_tags()))

    #dumb_sort(slides)

    score = 0
    save_slides = None
    for i in range(10):
        random.shuffle(slides)
        score_ = simulate_score(slides)
        if score_ > score:
            save_slides = slides
            score = score_
        print(score_)


    if local_compute:
        print('score for ' + filename + ': ' + str(simulate_score(save_slides)))

    out = open(out, 'w')
    out.write(str(len(save_slides)) + '\n')
    for slide in save_slides:
        out.write(str(slide) + '\n')
    out.close()


def simulate_score(slides):
    score = 0
    for i in range(len(slides) - 1):
        score += (slides[i] - slides[i + 1])
    return score


process_file('in/a_example.txt', 'out/a_example_out.txt')
process_file('in/b_lovely_landscapes.txt', 'out/b_lovely_landscapes_out.txt')
process_file('in/c_memorable_moments.txt', 'out/c_memorable_moments_out.txt')
process_file('in/d_pet_pictures.txt', 'out/d_pet_pictures_out.txt')
process_file('in/e_shiny_selfies.txt', 'out/e_shiny_selfies_out.txt')
