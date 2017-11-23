from .models import Collection
import urllib.parse


class CollectionBuilder:

    """ Takes a prefix, a filepath and a separator and creates nested Collection objects"""

    def __init__(self, path, prefix, separator="_"):
        self.path = path
        self.prefix = prefix
        self.separator = separator

    def make_collections(self):
        prefix = self.prefix
        current = 0
        col_names = self.path.split(self.separator)
        cols = []
        for x in range(0, len(col_names)):
            col_object = {}
            current += 1
            title = urllib.parse.quote("/".join(col_names[0:current]), safe="")
            col_object["has_title"] = title
            col_object["has_id"] = "{}/{}".format(prefix, title)
            cols.append(col_object)
        new_cols = []
        parent = 0
        for x in cols:
            parent += 1
            try:
                x['has_child'] = cols[parent]['has_id']
                new_cols.append(x)
            except IndexError:
                new_cols.append(x)
        for x in new_cols:
            temp_col, _ = Collection.objects.get_or_create(
                has_title=x['has_title'],
                has_id=x['has_id']
            )
        for x in new_cols:
            try:
                temp_col = Collection.objects.get(has_id=x['has_child'])
                temp_col.part_of = Collection.objects.get(has_id=x['has_id'])
                temp_col.save()
            except KeyError:
                pass
        return new_cols


def path2cols(path, separator="_"):
    """takes a splittable string and creates nested collections"""
    counter = 1
    current = 0
    cols = []
    final_cols = []
    for x in path.split(separator)[::-1]:
        col, _ = Collection.objects.get_or_create(
            has_title=x
        )
        cols.append(col)
    while counter != len(cols):
        current_col = cols[current]
        parent_col = cols[counter]
        current_col.part_of = parent_col
        current_col.save()
        counter += 1
        current += 1
        final_cols.append(current_col)

    return final_cols
