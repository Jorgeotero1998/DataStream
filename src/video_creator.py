from moviepy import ImageClip, CompositeVideoClip, concatenate_videoclips
from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import numpy as np
import datetime

class VideoCreator:
    @staticmethod
    def create_process_slide(step_name, detail, sub_detail, progress):
        img = Image.new('RGB', (1280, 720), color=(10, 10, 10))
        draw = ImageDraw.Draw(img)
        
        try:
            font_main = ImageFont.truetype("arial.ttf", 40)
            font_code = ImageFont.truetype("lucon.ttf", 25) # Lucida Console
        except:
            font_main = ImageFont.load_default()
            font_code = ImageFont.load_default()

        # Interfaz de "Sistema"
        draw.rectangle([50, 50, 1230, 670], outline="green", width=2)
        draw.text((70, 70), "INDUSTRIAL-SCRAPER v2.0 - SYSTEM LOG", fill="green", font=font_code)
        draw.text((1000, 70), datetime.datetime.now().strftime("%H:%M:%S"), fill="green", font=font_code)

        # Contenido Central
        draw.text((640, 250), f"> EJECUTANDO: {step_name}", fill="white", anchor="mm", font=font_main)
        draw.text((640, 320), detail, fill="lightgray", anchor="mm", font=font_code)
        draw.text((640, 360), sub_detail, fill="gray", anchor="mm", font=font_code)

        # Barra de progreso
        draw.rectangle([340, 450, 940, 480], outline="green", width=1)
        draw.rectangle([345, 455, 345 + (6 * progress), 475], fill="green")
        draw.text((640, 510), f"PROGRESS: {progress}%", fill="green", anchor="mm", font=font_code)

        return np.array(img)

    @staticmethod
    def create_demo(csv_path, output_path="proceso_robot.mp4"):
        print("[*] Generando video del proceso (Making-of)...")
        
        # Definimos las "escenas" de lo que hizo el robot
        escenas = [
            ("INICIALIZACION", "Cargando modulos de Python...", "Engine, Parser, VideoCreator cargados.", 20),
            ("CONEXION REMOTA", "Accediendo a https://news.ycombinator.com/", "User-Agent: Chrome/120.0 (Windows)", 45),
            ("EXTRACCION DE DATOS", "Parseando HTML y limpiando etiquetas...", "30 registros encontrados.", 70),
            ("GENERACION DE REPORTES", "Guardando data/scraped_data.csv", "Formato: Excel/CSV (Latin-1)", 90),
            ("FINALIZADO", "Proceso completado con exito.", "Video generado satisfactoriamente.", 100)
        ]
        
        clips = []
        for i, (step, det, sub, prog) in enumerate(escenas):
            frame = VideoCreator.create_process_slide(step, det, sub, prog)
            clip = ImageClip(frame).with_duration(3) # 3 segundos por etapa
            clips.append(clip)
        
        if clips:
            print(f"[*] Renderizando Making-of: {output_path}...")
            video_final = concatenate_videoclips(clips, method="compose")
            video_final.write_videofile(output_path, fps=24, codec='libx264', audio=False)
