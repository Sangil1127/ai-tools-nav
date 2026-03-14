#!/usr/bin/env python3
"""
网站截图工具 - 使用Playwright
"""
import asyncio
from playwright.async_api import async_playwright
import sys

async def screenshot(url, output_path="/tmp/screenshot.png", width=1280, height=800):
    """截取网站截图"""
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={'width': width, 'height': height})
        await page.goto(url, wait_until='networkidle')
        await page.screenshot(path=output_path, full_page=True)
        await browser.close()
        print(f"截图已保存: {output_path}")

if __name__ == "__main__":
    url = sys.argv[1] if len(sys.argv) > 1 else "http://127.0.0.1:8080/"
    output = sys.argv[2] if len(sys.argv) > 2 else "/tmp/screenshot.png"
    asyncio.run(screenshot(url, output))
