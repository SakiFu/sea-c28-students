def safe_input():
    try:
        raw_input()
    except (EOFError, KeyboardInterrupt):
        return None
