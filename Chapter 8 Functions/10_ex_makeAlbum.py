# -*- coding: utf-8 -*-


def make_album(name, album, num_track=''):
    albums = {"Author": name, "Album": album}
    if num_track:
        albums["Number of tracks"] = num_track
    return albums


album1 = make_album("Prodigy", "The fat")
print(album1)

album2 = make_album("Keiko Matsui", "1990 - No borders")
print(album2)

album3 = make_album("Bomfunk MC's", "In stereo", num_track=21)
print(album3)

