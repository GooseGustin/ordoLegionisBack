import cloudinary
import cloudinary.uploader
from django.conf import settings
import re

cloudinary.config(
    cloud_name=settings.CLOUDINARY_STORAGE["CLOUD_NAME"],
    api_key=settings.CLOUDINARY_STORAGE["API_KEY"],
    api_secret=settings.CLOUDINARY_STORAGE["API_SECRET"]
)

def upload_file_to_server(file, folder="announcements"):
    result = cloudinary.uploader.upload(file, folder=folder)
    return {
        "secure_url": result["secure_url"],
        "public_id": result["public_id"]
    }

def delete_file_from_cloudinary(image_url):
    """
    Extracts the file name (without extension) from the image_url
    and constructs the full public_id using the given folder name.
    Then deletes the file from Cloudinary.
    """
    folder_name = "announcements"
    match = re.search(r'/upload/.+?/([^/]+)\.(jpg|jpeg|png|gif|webp)$', image_url)
    if match:
        file_name = match.group(1)
        public_id = f"{folder_name}/{file_name}"
        print(f"Deleting public_id: {public_id}")
        result = cloudinary.uploader.destroy(public_id)
        return result
    else:
        print("Could not extract file name from URL.")
        return None
    # print("public id for deleting", public_id)
    # return cloudinary.uploader.destroy(public_id)
