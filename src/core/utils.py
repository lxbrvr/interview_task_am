def find_latest_id_for_model(model):
    try:
        latest_inserted_id = model.objects.latest('id').id
    except model.DoesNotExist:
        latest_inserted_id = None

    return latest_inserted_id