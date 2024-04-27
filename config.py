from configparser import ConfigParser


def config(filename='database.ini', section='postgresql'):

    parses = ConfigParser()
    parses.read(filename)
    db = {}
    if parses.has_section(section):
        params = parses.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} is not found in the {1} file.'.format(section, filename))
    return db
