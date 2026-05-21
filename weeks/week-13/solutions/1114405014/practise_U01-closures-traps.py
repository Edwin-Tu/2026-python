def add_to_cart(item, cart=[]):
    cart.append(item)
    return cart

def add_to_cart_safe(item, cart=None):
    if cart is None:
        cart = []
    cart.append(item)
    return cart

def make_counter(start=0):
    count = start

    def counter():
        nonlocal count
        count += 1
        return count

    return counter

def make_visit_tracker():
    visited = set()

    def visit(node):
        nonlocal visited
        if node in visited:
            return False
        visited.add(node)
        return True

    return visit
