def heading(header="A", lvl_head=1):
    if lvl_head < 1:
        return f"# {header}"
    if lvl_head > 6:
        return f"###### {header}"
    else:
        but_how = "#" * lvl_head
        return f"{but_how} {header}"
