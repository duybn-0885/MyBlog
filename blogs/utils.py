import inflect
engine = inflect.engine()

def custom_model_name(model_name):
    return engine.plural(model_name).title()+'Admin'
