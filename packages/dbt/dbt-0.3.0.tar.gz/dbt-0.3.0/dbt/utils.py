
def find_model_by_name(models, name, package_namespace=None):
    found = []
    for model in models:
        if model.name == name:
            if package_namespace is None:
                found.append(model)
            elif package_namespace is not None and package_namespace == model.project['name']:
                found.append(model)

    nice_package_name = 'ANY' if package_namespace is None else package_namespace
    if len(found) == 0:
        raise RuntimeError("Can't find a model named '{}' in package '{}' -- does it exist?".format(name, nice_package_name))
    elif len(found) == 1:
        return found[0]
    else:
        raise RuntimeError("Model specification is ambiguous: model='{}' package='{}' -- {} models match criteria: {}".format(name, nice_package_name, len(found), found))
