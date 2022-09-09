import secrets

def private_key(p):
    p_key = secrets.choice(range(1, p))
    return p_key


def public_key(p, g, private):
    return (g ** private) % p


def secret(p, public, private):
    return (public ** private) % p
