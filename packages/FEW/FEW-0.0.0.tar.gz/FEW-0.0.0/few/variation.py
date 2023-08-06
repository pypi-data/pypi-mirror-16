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
from .population import make_program, ind
from itertools import accumulate

# from few.tests.test_population import is_valid_program

def cross(p_i,p_j, max_depth = 3):
    """subtree-like swap crossover between programs p_i and p_j."""
    # grab subtree of p_i
    x_i_end = np.random.randint(0,len(p_i))

    x_i_begin = x_i_end
    arity_sum = p_i[x_i_end][1]
    # print("x_i_end:",x_i_end)
    while (arity_sum > 0):
        if x_i_begin == 0:
            print("arity_sum:",arity_sum,"x_i_begin:",x_i_begin,"x_i_end:",x_i_end)
        x_i_begin -= 1
        arity_sum += p_i[x_i_begin][1]-1

    # grab subtree of p_j
    x_j_end = np.random.randint(len(p_j))
    x_j_begin = x_j_end
    arity_sum = p_j[x_j_end][1]

    while (arity_sum > 0):
        if x_j_begin == 0:
            print("arity_sum:",arity_sum,"x_j_begin:",x_j_begin,"x_j_end:",x_j_end)
            print("p_j:",p_j)
        x_j_begin -= 1
        arity_sum += p_j[x_j_begin][1]-1

    #swap subtrees
    tmpi = p_i[:]
    tmpj = p_j[:]
    tmpi[x_i_begin:x_i_end+1:],tmpj[x_j_begin:x_j_end+1:] = tmpj[x_j_begin:x_j_end+1:],tmpi[x_i_begin:x_i_end+1:]

    if not is_valid_program(p_i) or not is_valid_program(p_j):

        print("parent 1:",p_i,"x_i_begin:",x_i_begin,"x_i_end:",x_i_end)
        print("parent 2:",p_j,"x_j_begin:",x_j_begin,"x_j_end:",x_j_end)
        print("child 1:",tmpi)
        print("child 2:",tmpj)
        raise ValueError('Crossover produced an invalid program.')

    # size check, then assignment
    if len(tmpi) <= 2**max_depth-1:
        p_i[:] = tmpi
    if len(tmpj) <= 2**max_depth-1:
        p_j[:] = tmpj



def mutate(p_i,func_set,term_set):
    """point mutation on individual p_i"""
    # point mutation
    x = np.random.randint(len(p_i))
    arity = p_i[x][1]
    wholeset = func_set+term_set
    reps = [n for n in func_set+term_set if n[1]==arity]
    tmp = reps[np.random.randint(len(reps))]

    p_i[x] = tmp
    assert is_valid_program(p_i)

def is_valid_program(p):
    """checks whether program p makes a syntactically valid tree.

    checks that the accumulated program length is always greater than the
    accumulated arities, indicating that the appropriate number of arguments is
    alway present for functions. It then checks that the sum of arties +1
    exactly equals the length of the stack, indicating that there are no
    missing arguments.
    """
    # print("p:",p)
    arities = list(a[1] for a in p)
    accu_arities = list(accumulate(arities))
    accu_len = list(np.arange(len(p))+1)
    check = list(a < b for a,b in zip(accu_arities,accu_len))
    # print("accu_arities:",accu_arities)
    # print("accu_len:",accu_len)
    # print("accu_arities < accu_len:",accu_arities<accu_len)
    return all(check) and sum(a[1] for a in p) +1 == len(p) and len(p)>0
