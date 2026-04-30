from PIL import Image
import os

# Caminho da pasta onde estão suas imagens
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "static", "img")


def convert_to_webp(filename, quality=85):
    """Converte uma imagem PNG ou JPG para WebP."""
    src_path = os.path.join(IMG_DIR, filename)
    dst_path = os.path.splitext(src_path)[0] + ".webp"

    img = Image.open(src_path)
    img.save(dst_path, format="WEBP", quality=quality)
    print(f"✅ Convertido: {dst_path}")


def batch_convert():
    """Converte todas as imagens PNG/JPG da pasta para WebP."""
    for file in os.listdir(IMG_DIR):
        if file.lower().endswith((".png", ".jpg", ".jpeg")):
            convert_to_webp(file)


if __name__ == "__main__":
    batch_convert()
