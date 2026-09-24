"""Renderiza a PDF (A4) los HTML de dist/guias con Chromium (Playwright).
Uso: python3 tools/render_pdf.py [archivo.html ...]   (sin argumentos: todos los de dist/guias)
"""
import asyncio, pathlib, sys
from playwright.async_api import async_playwright
BASE = pathlib.Path(__file__).resolve().parents[1]
files = [pathlib.Path(a) for a in sys.argv[1:]] or sorted((BASE / 'dist/guias').glob('*.html'))
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        for f in files:
            pg = await b.new_page()
            await pg.goto(f.resolve().as_uri()); await pg.wait_for_timeout(500)
            await pg.pdf(path=str(f.with_suffix('.pdf')), format='A4', print_background=True,
                         margin={'top': '16mm', 'bottom': '16mm', 'left': '14mm', 'right': '14mm'})
            await pg.close(); print('ok', f.with_suffix('.pdf').name)
        await b.close()
asyncio.run(main())
