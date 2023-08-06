"""
Copyright 2016 William La Cava

This file is part of the FEW library.

The FEW library is free software: you can redistribute it and/or
modify it under the terms of the GNU General Public License as published by the
Free Software Foundation, either version 3 of the License, or (at your option)
any later version.

The FEW library is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with
the FEW library. If not, see http://www.gnu.org/licenses/.

"""
import numpy as np
import copy

def tournament(individuals,tourn_size, num_selections=None):
    """conducts tournament selection of size tourn_size"""
    winners = []
    if num_selections is None:
        num_selections = len(individuals)

    for i in np.arange(num_selections):
        # sample pool with replacement
        pool_i = np.random.choice(len(individuals),size=tourn_size)
        pool = []
        for i in pool_i:
            pool.append(np.mean(individuals[i].fitness))

        winners.append(copy.deepcopy(individuals[pool_i[np.argmin(pool)]]))

    return winners

def lexicase(individuals, num_selections=None, survival = False):
    """conducts lexicase selection for de-aggregated fitness vectors"""
    if num_selections is None:
        num_selections = len(individuals)
    winners = []

    for i in np.arange(num_selections):

        candidates = individuals
        # print("individuals[0].fitness",individuals[0].fitness)
        cases = list(np.arange(len(individuals[0].fitness_vec)))
        np.random.shuffle(cases)

        while len(cases) > 0 and len(candidates) > 1:

            best_val_for_case = min(map(lambda x: x.fitness_vec[cases[0]], individuals))
            # filter individuals without an elite fitness on this case
            candidates = list(filter(lambda x: x.fitness_vec[cases[0]] == best_val_for_case, individuals))
            cases.pop(0)

        if len(candidates) == 0:
            print("out of candidates!")
            winners.append(np.random.choice(individuals))
        else:
            choice = np.random.randint(len(candidates))
            winners.append(copy.deepcopy(candidates[choice]))
            if survival: # filter out winners from remaining selection pool
                 individuals = list(filter(lambda x: x.stack != candidates[choice].stack, individuals))

    return winners

def epsilon_lexicase(individuals, num_selections=None, survival = False):
    """conducts epsilon lexicase selection for de-aggregated fitness vectors"""
    if num_selections is None:
        num_selections = len(individuals)

    winners = []
    mad_for_case = []
    best_val_for_case = []
    # calculate epsilon thresholds based on median absolute deviation (MAD)
    for i in np.arange(len(individuals[0].fitness_vec)):
        mad_for_case.append(mad(np.asarray(list(map(lambda x: x.fitness_vec[i], individuals)))))
        # best_val_for_case.append(min(map(lambda x: x.fitness_vec[i], individuals)))

    for i in np.arange(num_selections):

        candidates = individuals
        cases = list(range(len(individuals[0].fitness_vec)))
        np.random.shuffle(cases)

        while len(cases) > 0 and len(candidates) > 1:

            best_val_for_case = min(map(lambda x: x.fitness_vec[cases[0]], individuals))

            if not np.isinf(best_val_for_case):
                # filter individuals without an elite+epsilon fitness on this case
                candidates = list(filter(lambda x: x.fitness_vec[cases[0]] <= best_val_for_case+mad_for_case[cases[0]], individuals))

            cases.pop(0)
        if len(candidates) == 0: # should not happen
            print("out of candidates!")
            winners.append(np.random.choice(individuals))
        else:
            choice = np.random.randint(len(candidates))
            winners.append(copy.deepcopy(candidates[choice]))
            if survival: # filter out winners from remaining selection pool
                 individuals = list(filter(lambda x: x.stack != candidates[choice].stack, individuals))

    return winners


def mad(x, axis=None):
    """median absolute deviation statistic"""
    return np.median(np.abs(x - np.median(x, axis)), axis)
