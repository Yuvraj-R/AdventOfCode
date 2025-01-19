input_locs = [x for x in open('input.txt').read().split('\n')]
locs = {complex(i, j): input_locs[j][i] for j in range(
    len(input_locs)) for i in range(len(input_locs[0]))}

deltas = {1, -1, 1j, -1j}  # legal deltas for area
all_deltas = {1, -1, 1j, -1j, 1 + 1j, 1 - 1j, -
              1 + 1j, -1 - 1j}  # deltas for finding perimeter
neighs = {l: [l + d for d in deltas if l + d in locs and locs[l + d]
              == locs[l]] for l in locs}  # neighbors for area
outside_neighs = {l: set([l + d for d in deltas if l + d not in neighs[l]])
                  for l in locs}  # neighbors for perimeter


def get_area(z, areas):
    todo = True
    for A in areas:  # make sure we didn't already do this one
        if z in A:
            todo = False
            return False
    if todo:  # flood fill
        area = set([z])
        front = set([z])
        while len(front) > 0:
            front = set([w for x in front for w in neighs[x] if w not in area])
            area = area.union(front)

        return (area)


def get_perimeter(area):
    outs = []
    for a in area:
        outs += outside_neighs[a]
    return (len(outs))


def get_sides(area):
    turns = 0  # record how many turns taken
    # get all spaces one layer away from the area itself, including diagonal moves
    border = set(
        [z + d for z in area for d in all_deltas if z + d not in area])
    ccw = -1j  # rotation to turn counter clockwise
    cw = 1j  # rotation to turn clockwise

    out_done = False
    while len(border) > 0:  # continue while we haven't traced any separate border location
        r = 1 + 0j  # shape is to your right
        d = -1j  # go up
        if out_done == False:  # do the outside border first
            left_pts = [z for z in border if z.real == min(
                [z.real for z in border])]  # find the leftmost points
            # find the bottommost points of those
            down = [z for z in left_pts if z.imag ==
                    max([z.imag for z in left_pts])]
            p = down[0]  # starting point
            # record the pairs of points, and direction of movement seen
            seen = set([(p, d)])
            done = set([p])
            out_done = True
        else:  # deal with a remaining inside border region
            # rightmost inside border points left
            right_pts = [z for z in border if z.real ==
                         max([z.real for z in border])]
            down = [z for z in right_pts if z.imag == max(
                [z.imag for z in right_pts])]  # bottommost of these
            p = down[0]  # starting point
            seen.add((p, d))
            done.add(p)

        while True:
            if p + d in border and p + d + r in area:  # border ahead and shape to the right of the new point
                p += d
            elif (p + d in border and p + d + r not in area and p + r in area) or (p + d in area and p + d + r in border):
                # border ahead and space forward and to the right and area to the right of where we are now
                # or area ahead but forward and right in border
                p += d
                d *= cw  # turn right
                r *= cw
                turns += 1
            elif p + d in area:  # area stragith ahead
                d *= ccw  # turn left
                r *= ccw
                turns += 1
            if (p, d) not in seen:
                seen.add((p, d))
                done.add(p)
            else:
                break
        border = set([z for z in border if z not in done])

    return (turns)


areas = []
total1, total2 = 0, 0
for l in locs.keys():
    # get a new area or False if we already did this one
    a = get_area(l, areas)
    if a:
        areas.append(a)
        total1 += len(a) * get_perimeter(a)
        total2 += len(a) * get_sides(a)

print('Part 1: ', total1)
print('Part 2: ', total2)
