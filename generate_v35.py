#!/usr/bin/env python3
"""
解析index-part1.html到index-part8.html中的所有工具卡片
生成新的index.html v3.5版本
"""

import re
import os
from html import escape

# 工具数据结构
tools_data = {
    'writing': {'name': 'AI写作工具', 'icon': '✍️', 'tools': []},
    'art': {'name': 'AI绘画工具', 'icon': '🎨', 'tools': []},
    'coding': {'name': 'AI编程工具', 'icon': '💻', 'tools': []},
    'video': {'name': 'AI视频工具', 'icon': '🎬', 'tools': []},
    'audio': {'name': 'AI音乐工具', 'icon': '🎵', 'tools': []},
    'design': {'name': 'AI设计工具', 'icon': '🎭', 'tools': []},
    'office': {'name': 'AI办公效率', 'icon': '📊', 'tools': []},
}

def extract_domain(url):
    """从URL中提取域名"""
    url = url.strip()
    if not url or url == '#':
        return ''
    if url.startswith('http://'):
        url = url[7:]
    elif url.startswith('https://'):
        url = url[8:]
    url = url.split('/')[0]
    url = url.split(':')[0]
    return url

def parse_tool_card(line):
    """解析单行工具卡片"""
    tool = {}
    
    # 提取data属性
    m = re.search(r'data-category="([^"]*)"', line)
    tool['data_category'] = m.group(1) if m else ''
    
    m = re.search(r'data-name="([^"]*)"', line)
    tool['data_name'] = m.group(1) if m else ''
    
    # 提取badges
    tool['badges'] = []
    if 'badge-hot' in line or 'HOT' in line:
        tool['badges'].append('hot')
    if 'badge-featured' in line:
        tool['badges'].append('featured')
    if 'badge-new' in line:
        tool['badges'].append('new')
    
    tool['is_china'] = 'badge-china' in line
    
    # 提取名称
    m = re.search(r'<h3>([^<]+)</h3>', line)
    if not m:
        return None
    tool['name'] = m.group(1).strip()
    
    # 提取描述 - <div class="tool-desc">...</div>
    m = re.search(r'<div class="tool-desc">([^<]+)</div>', line)
    if m:
        tool['description'] = m.group(1).strip()
    else:
        tool['description'] = ''
    
    # 提取价格 - <span class="value...">...</span>
    m = re.search(r'<span class="value[^"]*">([^<]+)</span>', line)
    if m:
        price = m.group(1).strip()
        # 清理价格文本
        price = price.replace('价格', '').strip()
        tool['price'] = price
    else:
        tool['price'] = '免费'
    
    # 提取URL - 从btn-primary链接
    m = re.search(r'href="(https?://[^"]+)"[^>]*class="[^"]*btn-primary', line)
    if not m:
        m = re.search(r'class="[^"]*btn-primary[^"]*"[^>]*href="(https?://[^"]+)"', line)
    if m:
        tool['url'] = m.group(1)
    else:
        tool['url'] = '#'
    
    # 计算热度值
    heat = 75
    if 'hot' in tool['badges']:
        heat = 98
    elif 'featured' in tool['badges']:
        heat = 93
    elif 'new' in tool['badges']:
        heat = 88
    if '免费' in tool['price'] or '开源' in tool['price']:
        heat += 2
    if tool['is_china']:
        heat += 1
    tool['heat'] = min(heat, 100)
    
    return tool

def parse_html_file(filepath):
    """解析HTML文件，提取工具卡片"""
    if not os.path.exists(filepath):
        return []
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    tools = []
    # 查找所有tool-card div
    for line in content.split('\n'):
        if 'class="tool-card"' in line:
            tool = parse_tool_card(line)
            if tool and tool['name']:
                tools.append(tool)
    
    return tools

def main():
    base_dir = '/root/.openclaw/workspace/projects/ai-tools-nav/'
    
    # 解析各分类工具
    tools_data['writing']['tools'] = parse_html_file(os.path.join(base_dir, 'index-part2.html'))
    tools_data['art']['tools'] = parse_html_file(os.path.join(base_dir, 'index-part3.html'))
    tools_data['coding']['tools'] = parse_html_file(os.path.join(base_dir, 'index-part4.html'))
    tools_data['video']['tools'] = parse_html_file(os.path.join(base_dir, 'index-part5.html'))
    tools_data['audio']['tools'] = parse_html_file(os.path.join(base_dir, 'index-part6.html'))
    tools_data['design']['tools'] = parse_html_file(os.path.join(base_dir, 'index-part7.html'))
    tools_data['office']['tools'] = parse_html_file(os.path.join(base_dir, 'index-part8.html'))
    
    # 统计工具数量
    total_count = sum(len(cat['tools']) for cat in tools_data.values())
    print(f"共提取 {total_count} 个工具")
    
    for cat_id, cat_data in tools_data.items():
        print(f"  {cat_data['name']}: {len(cat_data['tools'])} 个")
        if cat_data['tools']:
            t = cat_data['tools'][0]
            print(f"    示例: {t['name']} | URL: {t['url'][:40]} | Desc: {t['description'][:40]}")
    
    # 生成HTML
    generate_html(tools_data, total_count, base_dir)
    
    return total_count

def generate_html(tools_data, total_count, base_dir):
    """生成v3.5样式HTML"""
    
    html = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI工具导航 v3.5 | 极简高级版</title>
    <meta name="description" content="收录81+优质AI工具，极简设计，高效导航">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        html { scroll-behavior: smooth; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'PingFang SC', 'Microsoft YaHei', sans-serif;
            background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
            color: #f8fafc;
            line-height: 1.6;
            min-height: 100vh;
        }
        
        /* Header */
        .header {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            background: rgba(15, 23, 42, 0.95);
            backdrop-filter: blur(20px);
            border-bottom: 1px solid rgba(255, 255, 255, 0.1);
            z-index: 1000;
            padding: 16px 24px;
        }
        .header-content {
            max-width: 1400px;
            margin: 0 auto;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 20px;
            flex-wrap: wrap;
        }
        .logo {
            font-size: 1.25rem;
            font-weight: 700;
            color: #f8fafc;
            display: flex;
            align-items: center;
            gap: 10px;
        }
        .logo-icon {
            width: 36px;
            height: 36px;
            background: linear-gradient(135deg, #6366f1, #8b5cf6);
            border-radius: 10px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1rem;
        }
        
        /* Search */
        .search-box {
            flex: 1;
            max-width: 400px;
            position: relative;
        }
        .search-box input {
            width: 100%;
            padding: 12px 16px 12px 44px;
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 10px;
            color: #f8fafc;
            font-size: 0.9rem;
            outline: none;
            transition: all 0.3s;
        }
        .search-box input:focus {
            border-color: rgba(99, 102, 241, 0.5);
            background: rgba(255, 255, 255, 0.08);
        }
        .search-box::before {
            content: "🔍";
            position: absolute;
            left: 16px;
            top: 50%;
            transform: translateY(-50%);
            opacity: 0.5;
            font-size: 0.9rem;
        }
        
        /* Filters */
        .filters {
            display: flex;
            gap: 8px;
        }
        .filter {
            padding: 8px 16px;
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 20px;
            color: #94a3b8;
            font-size: 0.85rem;
            cursor: pointer;
            transition: all 0.3s;
            white-space: nowrap;
            border: none;
        }
        .filter:hover {
            background: rgba(255, 255, 255, 0.1);
            color: #f8fafc;
        }
        .filter.active {
            background: rgba(99, 102, 241, 0.2);
            border: 1px solid rgba(99, 102, 241, 0.5);
            color: #6366f1;
        }
        
        /* Main Content */
        .main {
            max-width: 1400px;
            margin: 0 auto;
            padding: 100px 24px 60px;
        }
        
        /* Category */
        .category {
            margin-bottom: 48px;
        }
        .category-header {
            display: flex;
            align-items: center;
            gap: 12px;
            margin-bottom: 20px;
            padding-bottom: 12px;
            border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        }
        .category-title {
            font-size: 1.2rem;
            font-weight: 700;
            color: #f8fafc;
            display: flex;
            align-items: center;
            gap: 8px;
        }
        .category-count {
            font-size: 0.8rem;
            color: #64748b;
            background: rgba(255, 255, 255, 0.05);
            padding: 4px 12px;
            border-radius: 12px;
        }
        
        /* Tools Grid */
        .tools-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(380px, 1fr));
            gap: 16px;
        }
        
        /* Tool Card v3.5 */
        .tool-card {
            background: rgba(30, 41, 59, 0.6);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 16px;
            padding: 16px;
            transition: all 0.3s;
            position: relative;
            display: flex;
            flex-direction: column;
        }
        .tool-card:hover {
            transform: translateY(-3px);
            border-color: rgba(99, 102, 241, 0.3);
            box-shadow: 0 10px 40px rgba(99, 102, 241, 0.15);
        }
        .tool-card.hidden {
            display: none;
        }
        
        /* Tool Main */
        .tool-main {
            display: flex;
            gap: 14px;
            flex: 1;
        }
        
        /* Tool Logo */
        .tool-logo {
            width: 48px;
            height: 48px;
            border-radius: 12px;
            flex-shrink: 0;
            object-fit: cover;
            background: rgba(255, 255, 255, 0.1);
        }
        
        /* Tool Info */
        .tool-info {
            flex: 1;
            min-width: 0;
        }
        
        /* Tool Header Row */
        .tool-header-row {
            display: flex;
            align-items: center;
            gap: 8px;
            margin-bottom: 8px;
            flex-wrap: wrap;
        }
        .tool-name {
            font-size: 1rem;
            font-weight: 700;
            color: #f8fafc;
            margin: 0;
        }
        
        /* Tool Tags */
        .tool-tag {
            font-size: 0.65rem;
            padding: 2px 8px;
            border-radius: 10px;
            font-weight: 600;
        }
        .tool-tag.free {
            background: linear-gradient(135deg, #10b981, #059669);
            color: #fff;
        }
        .tool-tag.hot {
            background: linear-gradient(135deg, #f59e0b, #ef4444);
            color: #fff;
        }
        .tool-tag.new {
            background: linear-gradient(135deg, #06b6d4, #6366f1);
            color: #fff;
        }
        .tool-tag.china {
            background: linear-gradient(135deg, #dc2626, #b91c1c);
            color: #fff;
        }
        
        /* Heat Bar */
        .heat-bar {
            height: 4px;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 2px;
            overflow: hidden;
            margin-bottom: 10px;
            position: relative;
        }
        .heat-fill {
            height: 100%;
            background: linear-gradient(90deg, #6366f1, #8b5cf6);
            border-radius: 2px;
            transition: width 0.5s ease;
        }
        .heat-fill.high {
            background: linear-gradient(90deg, #f59e0b, #ef4444);
        }
        .heat-text {
            position: absolute;
            right: 0;
            top: -16px;
            font-size: 0.7rem;
            color: #64748b;
        }
        
        /* Tool Desc */
        .tool-desc {
            font-size: 0.85rem;
            color: #94a3b8;
            line-height: 1.6;
            margin: 0;
            display: -webkit-box;
            -webkit-line-clamp: 2;
            -webkit-box-orient: vertical;
            overflow: hidden;
        }
        
        /* Tool Footer */
        .tool-footer {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-top: 12px;
            padding-top: 12px;
            border-top: 1px solid rgba(255, 255, 255, 0.05);
        }
        .tool-price {
            font-size: 0.8rem;
            color: #64748b;
        }
        
        .btn {
            padding: 8px 18px;
            background: linear-gradient(135deg, #6366f1, #8b5cf6);
            border: none;
            border-radius: 8px;
            color: #fff;
            font-size: 0.8rem;
            font-weight: 600;
            text-decoration: none;
            transition: all 0.3s;
            cursor: pointer;
        }
        .btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 20px rgba(99, 102, 241, 0.4);
        }
        
        /* No Results */
        .no-results {
            display: none;
            text-align: center;
            padding: 60px 20px;
            color: #64748b;
        }
        .no-results.show {
            display: block;
        }
        
        /* Footer */
        .footer {
            text-align: center;
            padding: 40px 24px;
            border-top: 1px solid rgba(255, 255, 255, 0.1);
            color: #64748b;
            font-size: 0.85rem;
        }
        
        /* Responsive */
        @media (max-width: 768px) {
            .header-content {
                flex-direction: column;
                align-items: stretch;
            }
            .search-box {
                max-width: 100%;
                order: 2;
            }
            .filters {
                order: 3;
                justify-content: center;
            }
            .main {
                padding-top: 160px;
            }
            .tools-grid {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <header class="header">
        <div class="header-content">
            <div class="logo">
                <div class="logo-icon">🚀</div>
                <span>AI工具导航 v3.5</span>
            </div>
            <div class="search-box">
                <input type="text" id="searchInput" placeholder="搜索AI工具名称、功能...">
            </div>
            <div class="filters">
                <button class="filter active" data-filter="all">全部</button>
                <button class="filter" data-filter="free">免费</button>
                <button class="filter" data-filter="paid">付费</button>
                <button class="filter" data-filter="hot">热门</button>
                <button class="filter" data-filter="china">国产</button>
            </div>
        </div>
    </header>

    <main class="main">
'''
    
    # 生成各分类内容
    for cat_id, cat_data in tools_data.items():
        if not cat_data['tools']:
            continue
            
        html += f'''
        <!-- {cat_data['name']} -->
        <section class="category" id="{cat_id}">
            <div class="category-header">
                <h2 class="category-title">{cat_data['icon']} {cat_data['name']}</h2>
                <span class="category-count">{len(cat_data['tools'])} 个工具</span>
            </div>
            <div class="tools-grid">
'''
        
        for tool in cat_data['tools']:
            # 构建data-category属性
            data_cats = [cat_id]
            if 'free' in tool.get('price', '').lower() or '开源' in tool.get('price', ''):
                data_cats.append('free')
            if tool.get('is_china'):
                data_cats.append('china')
            if 'hot' in tool.get('badges', []):
                data_cats.append('hot')
            if '付费' in tool.get('price', '') or '$' in tool.get('price', ''):
                if '免费' not in tool.get('price', ''):
                    data_cats.append('paid')
            
            data_category = ' '.join(data_cats)
            
            # 构建标签HTML
            tags_html = ''
            if 'hot' in tool.get('badges', []):
                tags_html += '<span class="tool-tag hot">推荐</span>'
            if tool.get('is_china'):
                tags_html += '<span class="tool-tag china">国产</span>'
            if '免费' in tool.get('price', '') or '开源' in tool.get('price', ''):
                tags_html += '<span class="tool-tag free">免费</span>'
            
            # 热度条样式
            heat_value = tool.get('heat', 75)
            heat_class = 'high' if heat_value >= 90 else ''
            
            # 获取favicon
            domain = extract_domain(tool.get('url', ''))
            if domain:
                favicon_url = f"https://www.google.com/s2/favicons?domain={domain}&sz=64"
            else:
                favicon_url = "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Ctext y='.9em' font-size='90'%3E🚀%3C/text%3E%3C/svg%3E"
            
            desc = escape(tool.get('description', '')[:120])
            
            html += f'''                <div class="tool-card" data-category="{data_category}" data-name="{tool.get('data_name', tool['name'].lower())}">
                    <div class="tool-main">
                        <img class="tool-logo" src="{favicon_url}" alt="{tool['name']}" loading="lazy">
                        <div class="tool-info">
                            <div class="tool-header-row">
                                <h3 class="tool-name">{tool['name']}</h3>
                                {tags_html}
                            </div>
                            <div class="heat-bar">
                                <div class="heat-fill {heat_class}" style="width: {heat_value}%"></div>
                                <span class="heat-text">{heat_value}°</span>
                            </div>
                            <p class="tool-desc">{desc}</p>
                        </div>
                    </div>
                    <div class="tool-footer">
                        <span class="tool-price">{tool.get('price', '')}</span>
                        <a href="{tool.get('url', '#')}" class="btn" target="_blank" rel="noopener">访问</a>
                    </div>
                </div>
'''
        
        html += '''            </div>
        </section>
'''
    
    # 添加底部和JS
    html += '''
        <div class="no-results" id="noResults">
            <p>😕 没有找到匹配的工具</p>
            <p>试试其他关键词？</p>
        </div>
    </main>

    <footer class="footer">
        <p>AI工具导航 v3.5 | 收录81+优质AI工具 | 持续更新中</p>
    </footer>

    <script>
        // 搜索功能
        const searchInput = document.getElementById('searchInput');
        const toolCards = document.querySelectorAll('.tool-card');
        const noResults = document.getElementById('noResults');
        
        searchInput.addEventListener('input', (e) => {
            const keyword = e.target.value.toLowerCase().trim();
            let visibleCount = 0;
            
            toolCards.forEach(card => {
                const name = card.querySelector('.tool-name').textContent.toLowerCase();
                const desc = card.querySelector('.tool-desc').textContent.toLowerCase();
                const category = card.dataset.category.toLowerCase();
                
                if (name.includes(keyword) || desc.includes(keyword) || category.includes(keyword)) {
                    card.classList.remove('hidden');
                    visibleCount++;
                } else {
                    card.classList.add('hidden');
                }
            });
            
            noResults.classList.toggle('show', visibleCount === 0 && keyword !== '');
        });
        
        // 筛选功能
        const filterBtns = document.querySelectorAll('.filter');
        
        filterBtns.forEach(btn => {
            btn.addEventListener('click', () => {
                // 更新按钮状态
                filterBtns.forEach(b => b.classList.remove('active'));
                btn.classList.add('active');
                
                const filter = btn.dataset.filter;
                
                toolCards.forEach(card => {
                    if (filter === 'all') {
                        card.classList.remove('hidden');
                    } else {
                        const categories = card.dataset.category.toLowerCase().split(' ');
                        if (categories.includes(filter.toLowerCase())) {
                            card.classList.remove('hidden');
                        } else {
                            card.classList.add('hidden');
                        }
                    }
                });
                
                noResults.classList.add('show');
                document.querySelectorAll('.tool-card:not(.hidden)').forEach(() => {
                    noResults.classList.remove('show');
                });
            });
        });
    </script>
</body>
</html>
'''
    
    # 保存文件
    output_path = os.path.join(base_dir, 'index.html')
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"已生成 index.html ({len(html)} 字符)")

if __name__ == '__main__':
    count = main()
    print(f"\n完成！共 {count} 个工具")
