/**
 * AI工具导航 v5.0 - 交互功能
 */

// 当前打开的工具
let currentModalTool = null;

/**
 * 初始化
 */
document.addEventListener('DOMContentLoaded', () => {
    initNavigation();
    initCategoryFilters();
    initModal();
    initSearch();
});

/**
 * 导航功能
 */
function initNavigation() {
    // 滚动时更新导航
    window.addEventListener('scroll', () => {
        const sections = document.querySelectorAll('.category-section');
        const scrollPos = window.scrollY + 150;
        
        sections.forEach(section => {
            const top = section.offsetTop;
            const height = section.offsetHeight;
            const id = section.getAttribute('id');
            
            if (scrollPos >= top && scrollPos < top + height) {
                document.querySelectorAll('.cat-filter').forEach(filter => {
                    filter.classList.remove('active');
                    if (filter.dataset.category === id) {
                        filter.classList.add('active');
                    }
                });
            }
        });
    });
}

/**
 * 分类筛选功能
 */
function initCategoryFilters() {
    const filters = document.querySelectorAll('.cat-filter');
    
    filters.forEach(filter => {
        filter.addEventListener('click', () => {
            filters.forEach(f => f.classList.remove('active'));
            filter.classList.add('active');
            
            const category = filter.dataset.category;
            filterTools(category);
        });
    });
}

function filterTools(category) {
    const cards = document.querySelectorAll('.tool-card');
    const sections = document.querySelectorAll('.category-section');
    
    if (category === 'all') {
        cards.forEach(card => {
            card.style.display = 'block';
            card.closest('.category-section').style.display = 'block';
        });
        sections.forEach(section => section.style.display = 'block');
    } else {
        sections.forEach(section => {
            const sectionId = section.getAttribute('id');
            if (sectionId === category) {
                section.style.display = 'block';
                section.scrollIntoView({ behavior: 'smooth', block: 'start' });
            } else {
                section.style.display = 'none';
            }
        });
    }
}

/**
 * 打开工具详情浮窗
 */
function openToolModal(card) {
    if (!card) return;
    
    // 获取工具数据
    const tool = {
        name: card.querySelector('.tool-name')?.textContent || '未知工具',
        category: card.querySelector('.tool-category span:last-child')?.textContent || 'AI工具',
        description: card.querySelector('.tool-desc')?.textContent || '暂无描述',
        logo: card.querySelector('.tool-logo')?.src || '',
        heat: card.dataset.heat || '80',
        url: card.querySelector('a')?.href || '#',
        price: card.dataset.price || 'freemium'
    };
    
    currentModalTool = tool;
    
    // 填充数据
    document.getElementById('modalLogo').src = tool.logo;
    document.getElementById('modalLogo').alt = tool.name;
    document.getElementById('modalTitle').textContent = tool.name;
    document.getElementById('modalCategory').textContent = tool.category;
    document.getElementById('modalDesc').textContent = tool.description;
    document.getElementById('modalHeatFill').style.width = tool.heat + '%';
    document.getElementById('modalHeatValue').textContent = tool.heat + '%';
    document.getElementById('modalVisitBtn').href = tool.url;
    
    // 价格标签
    const priceBadge = document.getElementById('modalPrice');
    priceBadge.className = 'pricing-type pricing-' + tool.price;
    priceBadge.textContent = getPriceLabel(tool.price);
    
    // 优缺点（示例数据）
    const prosList = document.getElementById('modalPros');
    const consList = document.getElementById('modalCons');
    
    prosList.innerHTML = `
        <li>功能强大，使用便捷</li>
        <li>界面友好，易于上手</li>
        <li>持续更新，功能完善</li>
    `;
    
    consList.innerHTML = `
        <li>部分功能需要付费</li>
        <li>对网络环境有一定要求</li>
    `;
    
    // 功能特性
    const featuresGrid = document.getElementById('modalFeatures');
    featuresGrid.innerHTML = `
        <div class="feature-item"><span class="feature-icon">✓</span><span class="feature-text">智能生成</span></div>
        <div class="feature-item"><span class="feature-icon">✓</span><span class="feature-text">多语言支持</span></div>
        <div class="feature-item"><span class="feature-icon">✓</span><span class="feature-text">云端同步</span></div>
        <div class="feature-item"><span class="feature-icon">✓</span><span class="feature-text">API接口</span></div>
    `;
    
    // 显示模态框
    document.getElementById('toolModal').classList.add('show');
    document.body.style.overflow = 'hidden';
}

/**
 * 关闭工具详情浮窗
 */
function closeToolModal() {
    document.getElementById('toolModal').classList.remove('show');
    document.body.style.overflow = '';
    currentModalTool = null;
}

function getPriceLabel(price) {
    const labels = {
        free: '免费',
        paid: '付费',
        freemium: '免费增值'
    };
    return labels[price] || price;
}

/**
 * 模态框初始化
 */
function initModal() {
    const overlay = document.getElementById('toolModal');
    
    // 点击遮罩关闭
    overlay.addEventListener('click', (e) => {
        if (e.target === overlay) {
            closeToolModal();
        }
    });
    
    // ESC键关闭
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') {
            closeToolModal();
        }
    });
}

/**
 * 搜索功能
 */
function initSearch() {
    const searchInput = document.getElementById('navSearch');
    if (!searchInput) return;
    
    let searchTimeout;
    
    searchInput.addEventListener('input', (e) => {
        clearTimeout(searchTimeout);
        const query = e.target.value.trim().toLowerCase();
        
        searchTimeout = setTimeout(() => {
            if (query) {
                searchTools(query);
            } else {
                filterTools('all');
            }
        }, 300);
    });
}

function searchTools(query) {
    const cards = document.querySelectorAll('.tool-card');
    const sections = document.querySelectorAll('.category-section');
    let hasResult = false;
    
    cards.forEach(card => {
        const name = card.querySelector('.tool-name')?.textContent?.toLowerCase() || '';
        const desc = card.querySelector('.tool-desc')?.textContent?.toLowerCase() || '';
        
        if (name.includes(query) || desc.includes(query)) {
            card.style.display = 'block';
            card.closest('.category-section').style.display = 'block';
            hasResult = true;
        } else {
            card.style.display = 'none';
        }
    });
    
    // 隐藏没有匹配工具的分类
    sections.forEach(section => {
        const visibleCards = section.querySelectorAll('.tool-card[style*="block"]').length;
        if (visibleCards === 0) {
            section.style.display = 'none';
        }
    });
}

// 导出全局函数
window.openToolModal = openToolModal;
window.closeToolModal = closeToolModal;
window.filterTools = filterTools;
