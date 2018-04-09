def get_teams_names(env='HIGHT'):
    if env == 'MEDIUM':
        return range(1, 5)
    elif env == 'MINIMAL':
        return range(1, 3)
    elif env == 'HIGHT':
        return range(1, 21)
