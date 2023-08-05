from io import BytesIO
from PIL import Image
from django.core.files import File


def compress_image(image, quality_value):
    uploaded_image = Image.open(image)

    if uploaded_image.mode != "RGB":
        uploaded_image = uploaded_image.convert("RGB")

    output_image = BytesIO()
    uploaded_image.save(output_image, "JPEG", quality=quality_value)

    compressed_image = File(output_image, name=image.name)

    return compressed_image
