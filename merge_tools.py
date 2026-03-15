#!/usr/bin/env python3
"""
合并 index-part1.html 到 index-part8.html 中的工具数据到主文件 index.html
"""

import re
from pathlib import Path

WORKSPACE = Path("/root/.openclaw/workspace/projects/ai-tools-nav")

def extract_tool_cards(content):
    """提取所有 tool-card div"""
    pattern = r'<div class="tool-card"[^>]*>.*?</div>\s*</div>\s*</div>'
    cards = re.findall(pattern, content, re.DOTALL)
    return cards

def extract_category_sections(content):
    """提取分类section的内容（包括工具卡片）"""
    # 匹配 category-section
    pattern = r'<section class="category-section" id="([^"]+)">.*?<div class="tools-grid">(.*?)</div>\s*</section>'
    sections = re.findall(pattern, content, re.DOTALL)
    return {cat_id: tools.strip() for cat_id, tools in sections}

def count_tools_in_grid(tools_grid_content):
    """计算tools-grid中的工具数量"""
    return len(re.findall(r'<div class="tool-card"', tools_grid_content))

def main():
    # 读取主文件 index.html
    index_path = WORKSPACE / "index.html"
    with open(index_path, 'r', encoding='utf-8') as f:
        index_content = f.read()
    
    # 收集所有part文件中的工具数据，按分类组织
    category_tools = {}
    category_counts = {}
    
    # 读取所有part文件
    for i in range(1, 9):
        part_path = WORKSPACE / f"index-part{i}.html"
        if part_path.exists():
            with open(part_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 提取分类section
            sections = extract_category_sections(content)
            for cat_id, tools_grid in sections.items():
                if cat_id not in category_tools:
                    category_tools[cat_id] = []
                
                # 提取该分类下的所有工具卡片
                cards = re.findall(r'(<div class="tool-card"[^>]*>.*?</div>\s*</div>\s*</div>)', tools_grid, re.DOTALL)
                category_tools[cat_id].extend(cards)
    
    # 统计每个分类的工具数量
    for cat_id, cards in category_tools.items():
        category_counts[cat_id] = len(cards)
        print(f"分类 {cat_id}: {len(cards)} 个工具")
    
    total_tools = sum(category_counts.values())
    print(f"\n总工具数量: {total_tools}")
    
    # 分类ID到标题的映射
    category_info = {
        'writing': {'title': 'AI写作工具', 'icon': '✍️', 'desc': 'AI写作工具能够辅助创作文章、编写代码、回答问题、翻译文档等。以下是最优秀的AI大语言模型和写作助手。'},
        'art': {'title': 'AI绘画工具', 'icon': '🎨', 'desc': 'AI绘画工具可以根据文字描述生成图像，或进行图像编辑、修复、风格转换等操作。'},
        'coding': {'title': 'AI编程工具', 'icon': '💻', 'desc': 'AI编程工具可以辅助代码编写、自动补全、Bug修复、代码重构等，大幅提升开发效率。'},
        'video': {'title': 'AI视频工具', 'icon': '🎬', 'desc': 'AI视频工具可以生成视频、编辑视频、数字人播报、自动剪辑等，革新视频创作流程。'},
        'audio': {'title': 'AI音乐工具', 'icon': '🎵', 'desc': 'AI音乐工具可以生成原创音乐、伴奏、音效等，革新音乐创作方式。'},
        'design': {'title': 'AI设计工具', 'icon': '🎭', 'desc': 'AI设计工具可以辅助UI设计、Logo设计、海报设计、3D建模等，提升设计效率。'},
        'office': {'title': 'AI办公效率工具', 'icon': '📊', 'desc': 'AI办公效率工具可以自动化处理文档、表格、邮件、会议记录等，大幅提升工作效率。'},
    }
    
    # 构建新的分类sections
    new_sections = []
    for cat_id, info in category_info.items():
        if cat_id in category_tools and category_tools[cat_id]:
            count = len(category_tools[cat_id])
            cards_html = '\n'.join(category_tools[cat_id])
            
            section_html = f'''<!-- {info['title']} -->
<section class="category-section" id="{cat_id}">
<div class="category-header">
<div class="category-title"><div class="icon">{info['icon']}</div><h2>{info['title']}</h2></div>
<span class="category-count">{count}个工具</span>
</div>
<p class="category-desc">{info['desc']}</p>
<div class="tools-grid">

{cards_html}

</div>
</section>'''
            new_sections.append(section_html)
    
    # 构建新的目录导航
    toc_items = []
    for cat_id, info in category_info.items():
        if cat_id in category_counts:
            toc_items.append(f'<li><a href="#{cat_id}">{info["icon"]} {info["title"]}({category_counts[cat_id]})</a></li>')
    
    new_toc = f'''<nav class="toc">
<h2>📑 快速导航</h2>
<ul>
{chr(10).join(toc_items)}
</ul>
</nav>'''
    
    # 找到index.html中需要替换的部分
    # 1. 找到并替换目录导航
    toc_pattern = r'<nav class="toc">.*?</nav>'
    index_content = re.sub(toc_pattern, new_toc, index_content, flags=re.DOTALL)
    
    # 2. 找到并替换所有分类section（从AI写作到AI音乐）
    # 先找到<main class="container">之后的所有category-section，直到footer
    main_pattern = r'(<main class="container">)\s*<nav class="toc">.*?</nav>\s*(.*?)\s*(</main>)'
    
    # 构建新的main内容
    new_main_content = f'''<main class="container">

{new_toc}

{chr(10).join(new_sections)}

</main>'''
    
    # 替换main内容
    index_content = re.sub(
        r'<main class="container">.*?</main>',
        new_main_content,
        index_content,
        flags=re.DOTALL
    )
    
    # 3. 更新hero统计
    # 更新收录工具数量
    index_content = re.sub(
        r'<div class="hero-stat"><div class="num">\d+\+?</div><div class="label">收录工具</div></div>',
        f'<div class="hero-stat"><div class="num">{total_tools}+</div><div class="label">收录工具</div></div>',
        index_content
    )
    
    # 更新分类数量
    category_num = len([c for c in category_counts.values() if c > 0])
    index_content = re.sub(
        r'<div class="hero-stat"><div class="num">\d+\+?</div><div class="label">分类目录</div></div>',
        f'<div class="hero-stat"><div class="num">{category_num}</div><div class="label">分类目录</div></div>',
        index_content
    )
    
    # 更新标题
    index_content = re.sub(
        r'<h1>AI工具导航大全 - 收录\d+\+?优质人工智能工具</h1>',
        f'<h1>AI工具导航大全 - 收录{total_tools}+优质人工智能工具</h1>',
        index_content
    )
    
    # 更新footer中的描述
    index_content = re.sub(
        r'收录\d+\+?全球优质AI工具',
        f'收录{total_tools}+全球优质AI工具',
        index_content
    )
    
    # 保存合并后的文件
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(index_content)
    
    print(f"\n✅ 合并完成！")
    print(f"   - 总工具数量: {total_tools}")
    print(f"   - 分类数量: {category_num}")
    print(f"   - 文件已保存到: {index_path}")

if __name__ == '__main__':
    main()
