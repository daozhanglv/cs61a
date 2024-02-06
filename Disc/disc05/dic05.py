def height(t):
    if is_leaf(t):
        return 0
    result = []
    for b in branches(t):
        result += [sum([1] + [height(b)])]
    return max(result)

def max_path_sum(t):
    if is_leaf(t):
        return label(t)
    result = []
    for b in branches(t):
        result += [sum([label(t)] + [max_path_sum(b)])]
    return max(result)

def square(x):
    return x * x

def square_tree(t):
    new_label = square(label(t))
    if is_leaf(t):
        return tree(new_label)
    return tree(new_label, [square_tree(b) for b in branches(t)])    
    
def find_path(tree, x):
    if label(tree)==x:
        return [label(tree)]
    for b in branches(tree):
        path = find_path(b,x)
        if path:
            return [label(tree)] + path

def prune_binary(t, nums):
    if is_leaf(t):
        if label(t) in nums:
            return t
        return None
    else:
        next_valid_nums = [n[1:] for n in nums if n[0] == label(t)]
        new_branches = []
        for b in branches(t):
            pruned_branch = prune_binary(b, next_valid_nums)
            if pruned_branch is not None:
                new_branches = new_branches + [pruned_branch]
        if not new_branches:
            return None
        return tree(label(t), new_branches)

def print_tree(t, indent=0):
    """Print a representation of this tree in which each label is
    indented by two spaces times its depth from the root.

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> print_tree(fib_tree(4))
    3
      1
        0
        1
      2
        1
        1
          0
          1
    """
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)



# ADT tree
def tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)