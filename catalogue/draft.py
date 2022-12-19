from catalogue.models import Kayak
kayaks = Kayak.kayaks.all()


fields = [
    "id",
    "brand",
    "model_name",
    "material",
    "description",
    "key_features",
    "model_code",
    "web_page",
    "youtube",
    "steering",
    "paddling",
    "length",
    "width",
    "height",
    "weight",
    "load_capacity",
    "outer_cockpit_dimensions",
    "ideal_paddler_size",
    "beluga_skirt_size",
    "impulse_drive",
    "is_new",
    "in_stock",
    "slug",
    "top_view",
    "side_view",
    "angle_view",
    "action_shot_1",
    "action_shot_2",
]

for k in kayaks:
    if k.brand:
        brand = k.brand.replace("″", '"').replace('′', "'")
        k.brand = brand
        k.save()
    if k.model_name:
        model_name = k.model_name.replace("″", '"').replace('′', "'")
        k.model_name = model_name
        k.save()
    if k.material:
        material = k.material.replace("″", '"').replace('′', "'")
        k.material = material
        k.save()
    if k.description:
        description = k.description.replace("″", '"').replace('′', "'")
        k.description = description
        k.save()
    if k.key_features:
        key_features = k.key_features.replace("″", '"').replace('′', "'")
        k.key_features = key_features
        k.save()
    if k.model_code:
        model_code = k.model_code.replace("″", '"').replace('′', "'")
        k.model_code = model_code
        k.save()
    if k.web_page:
        web_page = k.web_page.replace("″", '"').replace('′', "'")
        k.web_page = web_page
        k.save()
    if k.youtube:
        youtube = k.youtube.replace("″", '"').replace('′', "'")
        k.youtube = youtube
        k.save()
    if k.steering:
        steering = k.steering.replace("″", '"').replace('′', "'")
        k.steering = steering
        k.save()
    if k.paddling:
        paddling = k.paddling.replace("″", '"').replace('′', "'")
        k.paddling = paddling
        k.save()
    if k.length:
        length = k.length.replace("″", '"').replace('′', "'")
        k.length = length
        k.save()
    if k.width:
        width = k.width.replace("″", '"').replace('′', "'")
        k.width = width
        k.save()
    if k.height:
        height = k.height.replace("″", '"').replace('′', "'")
        k.height = height
        k.save()
    if k.weight:
        weight = k.weight.replace("″", '"').replace('′', "'")
        k.weight = weight
        k.save()
    if k.load_capacity:
        load_capacity = k.load_capacity.replace("″", '"').replace('′', "'")
        k.load_capacity = load_capacity
        k.save()
    if k.outer_cockpit_dimensions:
        outer_cockpit_dimensions = k.outer_cockpit_dimensions.replace("″", '"').replace('′', "'")
        k.outer_cockpit_dimensions = outer_cockpit_dimensions
        k.save()
    if k.ideal_paddler_size:
        ideal_paddler_size = k.ideal_paddler_size.replace("″", '"').replace('′', "'")
        k.ideal_paddler_size = ideal_paddler_size
        k.save()
    if k.beluga_skirt_size:
        beluga_skirt_size = k.beluga_skirt_size.replace("″", '"').replace('′', "'")
        k.beluga_skirt_size = beluga_skirt_size
        k.save()
    if k.impulse_drive:
        impulse_drive = k.impulse_drive.replace("″", '"').replace('′', "'")
        k.impulse_drive = impulse_drive
        k.save()
    if k.slug:
        slug = k.slug.replace("″", '"').replace('′', "'")
        k.slug = slug
        k.save()


# if k.top_view:
#     top_view = k.top_view.replace("″", '"').replace('′', "'")
#     k.top_view = top_view
#     k.save()
# if k.side_view:
#     side_view = k.side_view.replace("″", '"').replace('′', "'")
#     k.side_view = side_view
#     k.save()
# if k.angle_view:
#     angle_view = k.angle_view.replace("″", '"').replace('′', "'")
#     k.angle_view = angle_view
#     k.save()
# if k.action_shot_1:
#     action_shot_1 = k.action_shot_1.replace("″", '"').replace('′', "'")
#     k.action_shot_1 = action_shot_1
#     k.save()
# if k.action_shot_2:
#     action_shot_2 = k.action_shot_2.replace("″",'"'".replace('′', "'"))
#     k.action_shot_2 = action_shot_2
#     k.save()