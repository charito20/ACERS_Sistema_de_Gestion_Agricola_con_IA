#!/usr/bin/env python3
"""
generar_exif_inventario.py
Genera 10_Autoria/exif_inventario.csv exigido en A11 de la Guia de desarrollo ACERS.

Para cada fotografia en las carpetas indicadas produce una fila con:
  nombre, fecha_captura_exif, dispositivo, hash_sha256

Requisito de la guia: "Las fotografias deben conservar sus metadatos originales."
Este script NO modifica ni re-comprime las imagenes; solo las lee.

Uso:
    pip install --break-system-packages pillow
    python3 generar_exif_inventario.py <carpeta1> [<carpeta2> ...] -o exif_inventario.csv

Ejemplo (segun la estructura A2/A6 de la guia):
    python3 generar_exif_inventario.py 10_Autoria/capturas 10_Autoria/fotos_equipo \
        02_Evidencias/Fotos_Entorno -o 10_Autoria/exif_inventario.csv
"""
import argparse
import csv
import hashlib
import sys
from pathlib import Path

try:
    from PIL import Image
    from PIL.ExifTags import TAGS
except ImportError:
    sys.exit("Falta Pillow. Instala con: pip install --break-system-packages pillow")

IMG_EXT = {".jpg", ".jpeg", ".png", ".heic", ".tiff", ".tif"}

DATETIME_TAGS = ("DateTimeOriginal", "DateTime", "DateTimeDigitized")
DEVICE_TAGS_MAKE = "Make"
DEVICE_TAGS_MODEL = "Model"


def sha256_of(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def read_exif(path: Path):
    """Devuelve (fecha_captura, dispositivo) o ('', '') si no hay EXIF."""
    fecha = ""
    dispositivo = ""
    try:
        img = Image.open(path)
        exif = img.getexif()
        if exif:
            tags = {TAGS.get(k, k): v for k, v in exif.items()}
            for t in DATETIME_TAGS:
                if t in tags and tags[t]:
                    fecha = str(tags[t])
                    break
            make = str(tags.get(DEVICE_TAGS_MAKE, "")).strip()
            model = str(tags.get(DEVICE_TAGS_MODEL, "")).strip()
            dispositivo = f"{make} {model}".strip()
    except Exception as e:
        print(f"  [aviso] no se pudo leer EXIF de {path.name}: {e}", file=sys.stderr)
    return fecha, dispositivo


def main():
    ap = argparse.ArgumentParser(description="Genera exif_inventario.csv (A11)")
    ap.add_argument("carpetas", nargs="+", help="Carpetas con fotografias a inventariar")
    ap.add_argument("-o", "--output", default="exif_inventario.csv", help="CSV de salida")
    args = ap.parse_args()

    filas = []
    sin_exif = []

    for carpeta in args.carpetas:
        base = Path(carpeta)
        if not base.exists():
            print(f"[aviso] carpeta no existe, se omite: {base}", file=sys.stderr)
            continue
        for p in sorted(base.rglob("*")):
            if p.is_file() and p.suffix.lower() in IMG_EXT:
                fecha, dispositivo = read_exif(p)
                h = sha256_of(p)
                if not fecha:
                    sin_exif.append(str(p))
                filas.append({
                    "nombre_archivo": str(p),
                    "fecha_captura_exif": fecha,
                    "dispositivo": dispositivo,
                    "hash_sha256": h,
                })

    if not filas:
        sys.exit("No se encontraron fotografias en las carpetas indicadas.")

    with open(args.output, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["nombre_archivo", "fecha_captura_exif", "dispositivo", "hash_sha256"])
        w.writeheader()
        w.writerows(filas)

    print(f"OK: {len(filas)} fotografias inventariadas -> {args.output}")
    if sin_exif:
        print("\nADVERTENCIA (viola A11 - 'deben conservar sus metadatos originales'):")
        print("Las siguientes fotos NO tienen fecha EXIF:")
        for s in sin_exif:
            print(f"  - {s}")
        print("\nSolucion: comparte las fotos por USB/cable o Drive en su formato original,")
        print("nunca por WhatsApp/Telegram, que eliminan el EXIF al recomprimir.")


if __name__ == "__main__":
    main()
