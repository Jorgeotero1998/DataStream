from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import os

class DataParser:
    @staticmethod
    def parse_hacker_news(html_content):
        if not html_content: return []
        soup = BeautifulSoup(html_content, 'html.parser')
        articles = []
        rows = soup.find_all('tr', class_='athing')
        
        for row in rows:
            title_line = row.find('span', class_='titleline')
            if not title_line: continue
            link = title_line.find('a')
            site_str = title_line.find('span', class_='sitestr')
            subtext = row.find_next_sibling('tr')
            
            if link and subtext:
                score_tag = subtext.find('span', class_='score')
                score_val = int(score_tag.text.split()[0]) if score_tag else 0
                
                articles.append({
                    "Importancia": "CRITICA" if score_val > 200 else "NORMAL",
                    "Titulo": link.text,
                    "Fuente": site_str.text if site_str else "YCombinator",
                    "Puntos": score_val
                })
        return articles

    @staticmethod
    def run_analysis(data):
        if not data: return
        df = pd.DataFrame(data)
        print("\n" + "="*40)
        print("RESUMEN EJECUTIVO")
        print("="*40)
        print(f"Total: {len(df)} | Criticas: {len(df[df['Importancia'] == 'CRITICA'])}")
        print(f"Fuente Top: {df['Fuente'].mode()[0]}")
        print("="*40 + "\n")

    @staticmethod
    def save_results(data, filename="data/scraped_data.csv", overwrite=False):
        if not data: return False
        df = pd.DataFrame(data)
        try:
            with open(filename, 'w', encoding='latin-1', errors='replace') as f:
                f.write("sep=;\n")
                df.to_csv(f, index=False, sep=';', encoding='latin-1')
            return True
        except PermissionError:
            print("\n[!] ERROR: Cierra el Excel.\n")
            return False
