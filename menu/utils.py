def build_tree(menu_items, current_path):
    items_by_id = {item.id: item for item in menu_items}
    tree = []

    for item in menu_items:
        item.temp_children = []
        item.is_active = False
        item.is_open = False

    active_item = None
    for item in menu_items:
        if item.get_url() == current_path:
            item.is_active = True
            active_item = item
            break

    for item in menu_items:
        if item.parent_id:
            parent = items_by_id.get(item.parent_id)
            if parent:
                parent.temp_children.append(item)
        else:
            tree.append(item)

    def mark_open(item):
        while item:
            item.is_open = True
            item = items_by_id.get(item.parent_id)

    if active_item:
        mark_open(active_item)

        for child in active_item.temp_children:
            child.is_open = True

    return tree
