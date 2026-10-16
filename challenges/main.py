def replace_first(items, new_value):
    if not items:
      return ()

    return (new_value,) + items[1:]