import re

# 读取文件
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 工具详情浮窗HTML
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

# 在</body>前插入浮窗
content = content.replace('</body>', modal_html + '\n</body>')

# 写入文件
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('✅ 工具详情浮窗添加完成')
