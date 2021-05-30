"""
    You're looking to move into a new apartment on specific street, and you're
    given a list of contiguous blocks on that street where each block contains an
    apartment that you could move into.

    You also have a list of requirements: a list of buildings that are important
    to you. For instance, you might value having a school and a gym near your
    apartment. The list of blocks that you have contains information at every
    block about all of the buildings that are present and absent at the block in
    question. For instance, for every block, you might know whether a school, a
    pool, an office, and a gym are present.

    In order to optimize your life, you want to pick an apartment block such that
    you minimize the farthest distance you'd have to walk from your apartment to
    reach any of your required buildings.

    Write a function that takes in a list of contiguous blocks on a specific
    street and a list of your required buildings and that returns the location
    (the index) of the block that's most optimal for you.

    If there are multiple most optimal blocks, your function can return the index
    of any one of them.

    Example:
        blocks = [
            {
            "gym": False,
            "school": True,
            "store": False
            },
            {
            "gym": True,
            "school": False,
            "store": False
            },
            {
            "gym": True,
            "school": True,
            "store": False
            },
            {
            "gym": False,
            "school": True,
            "store": False
            },
            {
            "gym": False,
            "school": True,
            "store": True
            }
        ]

        reqs = ["gym", "school", "store"]    

        Output: 3
"""

def apartmentHunting(blocks, reqs):
    reqs_dict = {}
    closest = {}

    for req in reqs:
        closest[req] = len(blocks)
        reqs_dict[req] = []

    for idx,block in enumerate(blocks):
        for req in reqs:
            if block[req]:
                reqs_dict[req].append(0)
                closest[req] = 0

                reached_last_one, i, dist = False, idx - 1, 1
                while not reached_last_one and i >= 0:
                    if reqs_dict[req][i] == 0:
                        reached_last_one = True

                    if reqs_dict[req][i] > dist:
                        reqs_dict[req][i] = dist

                    dist += 1   
                    i -= 1             
            else:
                closest[req] += 1
                reqs_dict[req].append(closest[req])

    return get_best_walk_score(blocks, reqs, reqs_dict)


def get_best_walk_score(blocks, reqs, reqs_dict):
    best_block = [-1, float("inf")]

    for idx, block in enumerate(blocks):
        block_score = []

        for req in reqs:
            block_score.append(reqs_dict[req][idx])

        if max(block_score) < best_block[1]:
            best_block = [idx, max(block_score)]

    return best_block[0]    

print(apartmentHunting(blocks, reqs)) # 3