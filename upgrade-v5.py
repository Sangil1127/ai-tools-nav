#!/usr/bin/env python3
"""
AI工具导航站 v4.1 -> v5.0 升级脚本
添加导航、优化配色、添加浮窗功能
"""

import re

def upgrade_html():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. 替换标题
    content = re.sub(
        r'<title>.*?AI工具导航 v[\d.]+.*?\u003c/title>',
        '<title>AI工具导航 v5.0 | 收录181+优质AI工具</title>',
        content
    )
    
    # 2. 在原有样式后添加新样式
    old_styles = '''    <style>
        \* \{ margin: 0; padding: 0; box-sizing: border-box; \}
        html \{ scroll-behavior: smooth; \}
        body \{'''
    
    new_styles = '''    <!-- 新设计系统 -->
    <link rel="stylesheet" href="v5-design.css">
    <link rel="stylesheet" href="agent-switcher.css">
    
    <style>
        /* 额外样式补充 */
        .category-section {
            margin-bottom: 48px;
            scroll-margin-top: 140px;
        }
        
        .section-header-new {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 24px;
            padding-bottom: 16px;
            border-bottom: 1px solid rgba(255,255,255,0.1);
        }
        
        .section-title-new {
            font-size: 24px;
            font-weight: 700;
            display: flex;
            align-items: center;
            gap: 12px;
        }
        
        .section-icon-new {
            width: 44px;
            height: 44px;
            border-radius: 10px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 22px;
        }
        
        /* 分类颜色 */
        .category-chat .section-icon-new, .category-chat .category-badge { background: rgba(139, 92, 246, 0.15); color: #8b5cf6; }
        .category-writing .section-icon-new, .category-writing .category-badge { background: rgba(16, 185, 129, 0.15); color: #10b981; }
        .category-image .section-icon-new, .category-image .category-badge { background: rgba(245, 158, 11, 0.15); color: #f59e0b; }
        .category-video .section-icon-new, .category-video .category-badge { background: rgba(239, 68, 68, 0.15); color: #ef4444; }
        .category-audio .section-icon-new, .category-audio .category-badge { background: rgba(6, 182, 212, 0.15); color: #06b6d4; }
        .category-code .section-icon-new, .category-code .category-badge { background: rgba(59, 130, 246, 0.15); color: #3b82f6; }
        .category-search .section-icon-new, .category-search .category-badge { background: rgba(249, 115, 22, 0.15); color: #f97316; }
        .category-agent .section-icon-new, .category-agent .category-badge { background: rgba(236, 72, 153, 0.15); color: #ec4899; }
        .category-design .section-icon-new, .category-design .category-badge { background: rgba(20, 184, 166, 0.15); color: #14b8a6; }
        .category-office .section-icon-new, .category-office .category-badge { background: rgba(100, 116, 139, 0.15); color: #64748b; }
        .category-learn .section-icon-new, .category-learn .category-badge { background: rgba(132, 204, 22, 0.15); color: #84cc16; }
        .category-detect .section-icon-new, .category-detect .category-badge { background: rgba(244, 63, 94, 0.15); color: #f43f5e; }
        
        .category-badge {
            font-size: 12px;
            padding: 4px 12px;
            border-radius: 20px;
            font-weight: 500;
        }
        
        /* 卡片样式增强 */
        .tool-card {
            cursor: pointer;
            transition: all 0.3s ease;
        }
        
        .tool-card:hover {
            transform: translateY(-4px);
            box-shadow: 0 20px 40px rgba(0,0,0,0.3);
        }
        
        /* 原有的 */
        * { margin: 0; padding: 0; box-sizing: border-box; }
        html { scroll-behavior: smooth; }
        body {'''
    
    content = content.replace(old_styles, new_styles)
    
    # 3. 在</body>前添加新脚本
    old_script = '''    <!-- AI专员切换器 -->
    <script src="agent-switcher.js"></script>
</body>'''
    
    new_script = '''    <!-- 新交互系统 -->
    <script src="v5-app.js"></script>
    
    <!-- AI专员切换器 -->
    <script src="agent-switcher.js"></script>
</body>'''
    
    content = content.replace(old_script, new_script)
    
    # 4. 添加顶部导航HTML（在<body>后）
    body_tag = '<body>'
    nav_html = '''<body>
    <!-- 顶部导航栏 -->
    <nav class="top-nav">
        <div class="nav-left">
            <a href="#" class="nav-logo">
                <div class="logo-icon">🚀</div>
                <span class="logo-text">AI工具导航</span>
                <span class="logo-badge">v5.0</span>
            </a>
        </div>
        
        <div class="nav-right">
            <div class="nav-search">
                <span class="nav-search-icon">🔍</span>
                <input type="text" placeholder="搜索工具..." id="navSearch">
            </div>
        </div>
    </nav>
    
    <!-- 分类快捷筛选 -->
    <div class="category-nav">
        <button class="cat-filter active" data-category="all"><span class="cat-filter-icon">🔥</span><span>全部</span></button>
        <button class="cat-filter" data-category="writing"><span class="cat-filter-icon">✍️</span><span>AI写作</span></button>
        <button class="cat-filter" data-category="art"><span class="cat-filter-icon">🎨</span><span>AI绘画</span></button>
        <button class="cat-filter" data-category="video"><span class="cat-filter-icon">🎬</span><span>AI视频</span></button>
        <button class="cat-filter" data-category="audio"><span class="cat-filter-icon">🎵</span><span>AI音频</span></button>
        <button class="cat-filter" data-category="code"><span class="cat-filter-icon">💻</span><span>AI编程</span></button>
        <button class="cat-filter" data-category="search"><span class="cat-filter-icon">🔍</span><span>AI搜索</span></button>
        <button class="cat-filter" data-category="agent"><span class="cat-filter-icon">🤖</span><span>AI智能体</span></button>
        <button class="cat-filter" data-category="design"><span class="cat-filter-icon">🎨</span><span>AI设计</span></button>
        <button class="cat-filter" data-category="office"><span class="cat-filter-icon">📊</span><span>办公效率</span></button>
        <button class="cat-filter" data-category="learn"><span class="cat-filter-icon">📚</span><span>学习教育</span></button>
        <button class="cat-filter" data-category="detect"><span class="cat-filter-icon">🔒</span><span>内容检测</span></button>
    </div>

    <!-- 主内容区 -->
    <main class="main-container">
        <!-- Hero区域 -->
        <section class="hero-section">
            <h1 class="hero-title">发现最优质的 AI 工具</h1>
            <p class="hero-subtitle">精选 181+ 款AI工具，涵盖聊天、绘画、视频、编程等多个领域，助您高效工作</p>
            <div class="hero-stats">
                <div class="stat-item"><div class="stat-value">181+</div><div class="stat-label">收录工具</div></div>
                <div class="stat-item"><div class="stat-value">12</div><div class="stat-label">分类</div></div>
                <div class="stat-item"><div class="stat-value">100%</div><div class="stat-label">精选</div></div>
            </div>
        </section>
'''
    
    content = content.replace(body_tag, nav_html, 1)
    
    # 5. 修改主内容区padding
    content = content.replace(
        'padding: 100px 24px 60px;',
        'padding: 140px 24px 60px;'
    )
    
    # 6. 修改header位置
    content = content.replace(
        'z-index: 1000;',
        'z-index: 998;'
    )
    
    # 7. 在</body>前添加工具详情浮窗
    modal_html = '''
    <!-- 工具详情浮窗 -->
    <div class="modal-overlay" id="toolModal">
        <div class="modal-container">
            <div class="modal-header">
                <img src="" alt="" class="modal-logo" id="modalLogo">
                <div class="modal-title-wrapper">
                    <h2 class="modal-title" id="modalTitle"></h2>
                    <div class="modal-category" id="modalCategory"></div>
                </div>
                <button class="modal-close" id="modalClose" onclick="closeToolModal()">✕</button>
            </div>
            
            <div class="modal-body">
                <div class="modal-section">
                    <div class="modal-section-title">工具简介</div>
                    <p class="modal-desc" id="modalDesc"></p>
                </div>
                
                <div class="modal-section">
                    <div class="modal-section-title">优缺点分析</div>
                    <div class="pros-cons">
                        <div class="pros-list">
                            <div class="pros-title">✓ 优点</div>
                            <ul id="modalPros"></ul>
                        </div>
                        <div class="cons-list">
                            <div class="cons-title">✗ 缺点</div>
                            <ul id="modalCons"></ul>
                        </div>
                    </div>
                </div>
                
                <div class="modal-section">
                    <div class="modal-section-title">功能特性</div>
                    <div class="features-grid" id="modalFeatures"></div>
                </div>
                
                <div class="modal-section">
                    <div class="modal-section-title">价格方案</div>
                    <div class="pricing-badge">
                        <span class="pricing-type" id="modalPrice"></span>
                        <span>热度: </span>
                        <div class="heat-bar"><div class="heat-fill" id="modalHeatFill"></div></div>
                        <span id="modalHeatValue"></span>
                    </div>
                </div>
            </div>
            
            <div class="modal-footer">
                <a href="#" class="btn btn-primary" id="modalVisitBtn" target="_blank">
                    🚀 访问官网
                </a>
                <button class="btn btn-secondary" onclick="closeToolModal()">
                    关闭
                </button>
            </div>
        </div>
    </div>
'''
    
    content = content.replace('</body>', modal_html + '
</body>', 1)
    
    # 8. 为每个工具卡片添加点击事件和数据属性
    # 这个通过JS动态处理
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✅ 升级完成！")
    print("   - 已添加顶部导航栏")
    print("   - 已添加分类快捷筛选")
    print("   - 已优化配色方案")
    print("   - 已添加工具详情浮窗")
    print("   - 已添加Hero区域")

if __name__ == '__main__':
    upgrade_html()
