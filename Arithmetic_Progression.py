# Try if you can survive lists of MASSIVE numbers (which means time limit should be considered)
# find([3, 9, 1, 11, 13, 5]) # => 7

def find(seq):
    sorted_seq = sorted(seq)
    if sorted_seq[1] - sorted_seq[0] == sorted_seq[-1] - sorted_seq[-2]:
        difference = sorted_seq[1] - sorted_seq[0]
        for x in range(len(sorted_seq) - 1):
            if sorted_seq[x + 1] - sorted_seq[x] != difference:
                return sorted_seq[x] + difference
