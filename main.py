from src.engine import WebEngine
from src.parser import DataParser
from src.video_creator import VideoCreator
import time
import random

def run_industrial_pipeline():
    engine = WebEngine()
    parser = DataParser()
    video = VideoCreator()
    all_data = []
    
    print("[*] Iniciando Extraccion Masiva (Objetivo: 100 noticias)...")
    
    # Navegamos por 4 paginas para juntar los 100
    for page in range(1, 5):
        url = f"https://news.ycombinator.com/news?p={page}"
        print(f"[*] Escaneando fuente real - Pagina {page}...")
        
        html = engine.get_html(url)
        if html:
            page_data = parser.parse_hacker_news(html)
            all_data.extend(page_data)
            if len(all_data) >= 100: break
        
        # Pausa para no ser bloqueado
        time.sleep(random.uniform(1.0, 2.0))

    final_data = all_data[:100]
    
    if parser.save_results(final_data, overwrite=True):
        parser.run_analysis(final_data)
        
        print("[*] Generando reporte visual de respaldo...")
        try:
            video.create_demo("data/scraped_data.csv")
            print("[+] PROCESO COMPLETO: 100 noticias y video listos.")
        except Exception as e:
            print(f"[!] Error visual: {e}")

if __name__ == "__main__":
    run_industrial_pipeline()
