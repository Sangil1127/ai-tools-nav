#!/usr/bin/env python3
"""
生成AI工具导航网页预览图
"""
from PIL import Image, ImageDraw, ImageFont
import os

# 创建画布 (1280x1800 模拟网页高度)
width, height = 1280, 1800
img = Image.new('RGB', (width, height), color='#0f172a')
draw = ImageDraw.Draw(img)

# 尝试加载字体
try:
    font_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 48)
    font_header = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 32)
    font_text = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 20)
    font_small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 16)
    font_tag = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 14)
except:
    font_title = ImageFont.load_default()
    font_header = font_title
    font_text = font_title
    font_small = font_title
    font_tag = font_title

# 颜色定义
purple = '#6366f1'
accent = '#06b6d4'
white = '#ffffff'
gray = '#94a3b8'
card_bg = '#1e293b'

# ===== 导航栏 =====
draw.rectangle([0, 0, width, 70], fill='#0f172a')
draw.text([30, 20], "🚀 AI工具导航", fill=white, font=font_header)
draw.text([350, 25], "AI写作    AI绘画    AI编程    AI视频    办公效率", fill=gray, font=font_text)
draw.text([1000, 25], "收录 500+ 工具", fill=accent, font=font_text)

# ===== Hero区域 =====
# 渐变背景效果（用矩形模拟）
for i in range(300):
    alpha = int(255 * (1 - i/300))
    color = f'#{alpha//16:02x}{alpha//8:02x}{alpha//4:02x}'
    draw.rectangle([0, 70+i*1, width, 70+i*1+1], fill='#1e1b4b')

draw.text([450, 120], "✨ 每日更新 · 持续收录最新AI工具", fill=accent, font=font_small)
draw.text([320, 170], "发现最优质的", fill=white, font=font_title)
draw.text([420, 230], "AI人工智能工具", fill=purple, font=font_title)
draw.text([350, 310], "精选全球优质AI工具，助你提升10倍工作效率", fill=gray, font=font_text)

# 搜索框
draw.rounded_rectangle([240, 380, 1040, 440], radius=15, outline='#6366f1', width=2)
draw.text([270, 400], "🔍  搜索AI工具，如：ChatGPT、Midjourney...", fill=gray, font=font_text)
draw.rounded_rectangle([900, 388, 1030, 432], radius=10, fill='#6366f1')
draw.text([930, 402], "搜索", fill=white, font=font_text)

# 筛选标签
tags = ["全部", "免费", "付费", "热门", "最新", "国产"]
for i, tag in enumerate(tags):
    x = 340 + i * 100
    color = '#6366f1' if i == 0 else card_bg
    draw.rounded_rectangle([x, 480, x+80, 515], radius=20, fill=color)
    draw.text([x+20, 490], tag, fill=white, font=font_tag)

# ===== 统计卡片 =====
stats = [("🛠️", "500+", "收录工具"), ("📂", "50+", "分类目录"), 
         ("👥", "10万+", "月活跃用户"), ("⭐", "98%", "用户好评")]
for i, (icon, num, label) in enumerate(stats):
    x = 80 + i * 300
    draw.rounded_rectangle([x, 560, x+260, 680], radius=15, fill=card_bg, outline='#334155')
    draw.text([x+20, 580], icon, fill=white, font=font_header)
    draw.text([x+20, 610], num, fill=white, font=font_title)
    draw.text([x+20, 650], label, fill=gray, font=font_text)

# ===== AI写作工具分类 =====
y_offset = 720
draw.text([80, y_offset], "✍️", fill=white, font=font_header)
draw.text([140, y_offset+5], "AI写作工具", fill=white, font=font_header)
draw.rounded_rectangle([1180, y_offset+10, 1200, 35], radius=10, fill='#6366f1')
draw.text([1140, y_offset+15], "6 个工具", fill=accent, font=font_small)

# 工具卡片 (3列2行)
tools_writing = [
    ("📝", "ChatGPT", "对话AI · 通用", "OpenAI开发的对话式AI...", "免费 / $20月付", True),
    ("🤖", "Claude", "长文写作 · 文档分析", "Anthropic开发的AI助手...", "免费 / Pro$20", True),
    ("🌙", "Kimi Chat", "长文档 · 国产", "月之暗面开发，支持超长文本...", "免费", True),
    ("🇨🇳", "文心一言", "中文AI · 百度", "百度推出的中文对话AI...", "免费", False),
    ("✨", "通义千问", "阿里AI · 电商", "阿里巴巴推出的AI大模型...", "免费", False),
    ("🎵", "豆包", "字节AI · 抖音", "字节跳动推出的AI助手...", "免费", False),
]

for i, (icon, name, tags, desc, price, is_hot) in enumerate(tools_writing):
    row, col = i // 3, i % 3
    x, y = 80 + col * 400, y_offset + 80 + row * 200
    
    # 卡片背景
    draw.rounded_rectangle([x, y, x+380, y+180], radius=15, fill=card_bg, outline='#334155')
    
    # HOT标签
    if is_hot:
        draw.rounded_rectangle([x+300, y+10, x+370, y+30], radius=5, fill='#f59e0b')
        draw.text([x+310, y+13], "HOT", fill=white, font=font_tag)
    
    # 图标和标题
    draw.text([x+15, y+15], icon, fill=white, font=font_header)
    draw.text([x+70, y+20], name, fill=white, font=font_text)
    draw.text([x+70, y+50], tags, fill=accent, font=font_tag)
    
    # 描述
    draw.text([x+15, y+85], desc[:25]+"...", fill=gray, font=font_small)
    
    # 价格和按钮
    draw.text([x+15, y+130], "价格", fill=gray, font=font_tag)
    draw.text([x+15, y+145], price, fill='#10b981', font=font_small)
    draw.rounded_rectangle([x+280, y+140, x+370, y+170], radius=8, fill='#6366f1')
    draw.text([x+305, y+148], "访问 →", fill=white, font=font_tag)

# ===== 广告位 =====
y_ad = y_offset + 500
draw.rounded_rectangle([80, y_ad, 1200, y_ad+80], radius=15, outline='#475569', width=2)
draw.text([550, y_ad+30], "📢 广告位招租", fill=gray, font=font_text)

# ===== AI绘画工具分类 =====
y_paint = y_ad + 120
draw.text([80, y_paint], "🎨", fill=white, font=font_header)
draw.text([140, y_paint+5], "AI绘画工具", fill=white, font=font_header)
draw.text([1140, y_paint+15], "6 个工具", fill=accent, font=font_small)

# 继续添加更多内容... (简化为Footer)
y_footer = height - 150
draw.rectangle([0, y_footer, width, height], fill='#0f172a')
draw.text([80, y_footer+30], "🚀 AI工具导航", fill=white, font=font_header)
draw.text([80, y_footer+70], "精选全球优质AI工具，助你提升工作效率", fill=gray, font=font_text)
draw.text([80, height-40], "© 2026 AI工具导航. All rights reserved.", fill=gray, font=font_small)

# 保存图片
output_path = '/root/.openclaw/workspace/projects/ai-tools-nav/preview.png'
img.save(output_path, 'PNG')
print(f"预览图已保存: {output_path}")
print(f"图片尺寸: {img.size}")
