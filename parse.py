import common

def FGItemDescriptor_hook(dct: dict) -> common.FGItemDescriptor | None:
    ret_val = None
    keys = [
        'ClassName',
        'mDisplayName',
        'mDescription' 
    ]

    if all([key in dct for key in keys]):
        params = [dct[key] for key in keys]
        ret_val = common.FGItemDescriptor(*params)

    return ret_val