#!/usr/bin/python3
'''
Applied PEP8 (pycodestyle)

Author:       Ahmet Gungor
Date  :       15.12.2019
Description : Solution is developed by Ahmet Gungor with mathematical weight approach.

This problem was asked by Spotify.

You have access to ranked lists of songs for various users.
Each song is represented as an integer, and more preferred songs appear earlier in each list.
For example, the list [4, 1, 7] indicates that a user likes song 4 the best, followed by songs 1 and 7.
Given a set of these ranked lists, interleave them to create a playlist that satisfies everyone's priorities.
For example, suppose your input is {[1, 7, 3], [2, 1, 6, 7, 9], [3, 9, 5]}.
In this case a satisfactory playlist could be [2, 1, 6, 7, 3, 9, 5].

P.S. = (TODO Needs to add compare for same weights according to sort of each music lists. e.g. 3 and 7)
'''

from collections import Counter
import operator


class Playlist():
    def __init__(self, input):
        self.input = input
        print(f"\nPure song input list = {self.input}\n")

        self.longest_val_count = len(max(self.input, key=len))
        print(f"The longest song list count is = {self.longest_val_count}\n")

    def song_frequency_filter(self):
        self.flat_input = [item for elem in self.input for item in elem]
        print(f"Nested list is changed as flat = {self.flat_input}\n")

        self.dict_input_count = dict(Counter(self.flat_input))
        print(f"Count of each songs in music lists = {self.dict_input_count}\n")

    def calculate_weight(self):
        self.total_weights_of_songs = dict()

        for personal_list in self.input:
            print(f"Music list = {personal_list}")
            print("-"*35)
            for i in range(len(personal_list) - 1, -1, -1):  # Reverse loop to prevent unnecessary loop with X at prefix.

                calculation = (float((len(personal_list) - i) / self.longest_val_count) / float(self.dict_input_count[personal_list[i]]))
                calculation = '{:.3f}'.format(round(calculation, 3))
                print(f"Weight for {personal_list[i]} is {calculation}")

                if personal_list[i] in self.total_weights_of_songs:
                    self.total_weights_of_songs[personal_list[i]] = '{:.3f}'.format(float(self.total_weights_of_songs[personal_list[i]]) + float(calculation))
                else:
                    self.total_weights_of_songs[personal_list[i]] = calculation
            print("\n")

        self.total_weights_of_songs = dict(sorted(self.total_weights_of_songs.items(), key=operator.itemgetter(1), reverse=True))
        print(f"Total weights for each song = {self.total_weights_of_songs}\n")
        print(f"\nOptimum Playlist Result = {tuple(self.total_weights_of_songs.keys())}\n")

        # TODO: Needs to add compare for same weights according to sort of each music lists. e.g. 3 and 7


if __name__ == "__main__":
    input = [[1, 7, 3], [2, 1, 6, 7, 9], [3, 9, 5]]

    instance = Playlist(input)
    instance.song_frequency_filter()
    instance.calculate_weight()
