s1 = [('be.v.01'),
      ('angstrom.n.01'),
      ('function.n.01'),
      ('trial.n.02')]

s2 = [('use.n.01'),
      ('function.n.01'),
      ('see.n.01'),
      ('code.n.01'),
      ('inch.n.01'),
      ('be.v.01'),
      ('correct.v.01')]


def score(s1, s2):
    score = 0
    for x, y in zip(s1.split('.'), s2.split('.')):
        if x == y:
            score += 1
    return score


closest = []  # list of [target,best_match]

for sysnet1 in s1:
    max_score = 0
    best = None
    for sysnet2 in s2:
        cur_score = score(sysnet1, sysnet2)
        if cur_score > max_score:
            max_score = cur_score
            best = sysnet2
    closest.append([sysnet1, best])


print(s2[0])
