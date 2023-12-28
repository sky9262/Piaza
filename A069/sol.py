from itertools import combinations

def is_pin_inside_triangle(Tstake1, Tstakes2, Tstake3, px, py):
    x1, y1 = Tstake1
    x2, y2 = Tstakes2
    x3, y3 = Tstake3
    def cross_product(v1, v2):
        return v1[0] * v2[1] - v1[1] * v2[0]

    def same_sign(a, b):
        return (a >= 0) == (b >= 0)

    AB = (x2 - x1, y2 - y1)
    BC = (x3 - x2, y3 - y2)
    CA = (x1 - x3, y1 - y3)

    AP = (px - x1, py - y1)
    BP = (px - x2, py - y2)
    CP = (px - x3, py - y3)

    cross_AB_AP = cross_product(AB, AP)
    cross_BC_BP = cross_product(BC, BP)
    cross_CA_CP = cross_product(CA, CP)

    return same_sign(cross_AB_AP, cross_BC_BP) and same_sign(cross_BC_BP, cross_CA_CP)


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
