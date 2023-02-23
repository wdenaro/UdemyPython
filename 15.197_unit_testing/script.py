def do_stuff(num=0):

    try:
        if num:
            return int(num) + 5
        else:
            return 'parameter must be a number'

    except ValueError as err:
        return err

    except TypeError as err:
        return err
