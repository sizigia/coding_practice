import re

def response(hey_bob):
    """Determine Bob's answer based on:
    
    - Bob answers 'Sure.' if you ask him a question, such as "How are you?".
    - He answers 'Whoa, chill out!' if you YELL AT HIM (in all capitals).
    - He answers 'Calm down, I know what I'm doing!' if you yell a question at him.
    - He says 'Fine. Be that way!' if you address him without actually saying anything.
    - He answers 'Whatever.' to anything else.

    :param hey_bob: string - conversation prompt to get Bob to answer.
    :return: string - Bob's answer
    """
    hey_bob = hey_bob.strip()

    bobs_resp = {
        'R1': 'Sure.',
        'R2': 'Whoa, chill out!',
        'R3': "Calm down, I know what I'm doing!",
        'R4': 'Fine. Be that way!',
        'R5': 'Whatever.'
    }

    prompts = {
        '?': hey_bob.endswith('?'),
        '!': hey_bob.isupper(),
        ' ': hey_bob.isspace()
    }

    if prompts['?'] and not prompts['!']:
            return bobs_resp['R1']
    elif not prompts['?'] and prompts['!']:
        return bobs_resp['R2']
    elif prompts['?'] and prompts['!']:
            return bobs_resp['R3']
    elif not len(hey_bob) or prompts[' ']:
        return bobs_resp['R4']
    else:
        return bobs_resp['R5']