from itertools import combinations

def is_pin_inside_triangle(Tstake1, Tstakes2, Tstake3, px, py):
    x1, y1 = Tstake1
    x2, y2 = Tstakes2
    x3, y3 = Tstake3
    def sign(p1, p2, p3):
        return (p1[0] - p3[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p3[1])

    d1 = sign((px, py), (x1, y1), (x2, y2))
    d2 = sign((px, py), (x2, y2), (x3, y3))
    d3 = sign((px, py), (x3, y3), (x1, y1))

    has_neg = (d1 < 0) or (d2 < 0) or (d3 < 0)
    has_pos = (d1 > 0) or (d2 > 0) or (d3 > 0)

    return not (has_neg and has_pos)

def count_internal_pins(pins):
    internal_pins = []

    for comb in combinations(pins, 3):
        trangle_pins = [comb[0], comb[1], comb[2]]
        left_pins = [pin for pin in pins if pin not in trangle_pins]
        true_case = 0
        for i in left_pins:
            px, py = i
            if is_pin_inside_triangle(comb[0], comb[1], comb[2], px, py) == True:
                true_case += 1
        internal_pins.append(true_case)


    return max(internal_pins)

if __name__ == "__main__":
    N = int(input())
    pins = [tuple(map(int, input().split())) for _ in range(N)]
    result = count_internal_pins(pins)
    print(result)
