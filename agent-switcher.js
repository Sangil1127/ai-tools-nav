/**
 * AI专员切换器 - 集成版
 * 集成到AI工具导航站
 */

// 专员数据
const AGENTS_DATA = {
    xiaoanzi: {
        id: 'xiaoanzi',
        avatar: '🎯',
        name: '小安子',
        role: '总指挥 · 池总秘书',
        shortRole: '总指挥',
        desc: '统筹协调所有专员工作，上传下达，确保任务高效完成',
        status: 'online',
        color: '#6366f1'
    },
    youxiaoguang: {
        id: 'youxiaoguang',
        avatar: '📧',
        name: '邮小广',
        role: '邮件推广专员',
        shortRole: '邮件',
        desc: '负责邮件发送、收件箱检查、退订处理等工作',
        status: 'standby',
        color: '#10b981'
    },
    duanxiaoying: {
        id: 'duanxiaoying',
        avatar: '🎬',
        name: '短小影',
        role: '短视频专员',
        shortRole: '视频',
        desc: '负责短视频制作、多平台发布等工作',
        status: 'standby',
        color: '#f59e0b'
    },
    shuxiaoxin: {
        id: 'shuxiaoxin',
        avatar: '📊',
        name: '数小昕',
        role: '数据分析专员',
        shortRole: '数据',
        desc: '负责日报生成、数据分析、可视化等工作',
        status: 'standby',
        color: '#8b5cf6'
    },
    kexiaofu: {
        id: 'kexiaofu',
        avatar: '💬',
        name: '客小服',
        role: '客服专员',
        shortRole: '客服',
        desc: '负责询盘回复、客户咨询、投诉处理等工作',
        status: 'standby',
        color: '#ec4899'
    },
    niuxiaoma: {
        id: 'niuxiaoma',
        avatar: '🐂🐴',
        name: '牛小马',
        role: '天选牛马专员',
        shortRole: '牛马',
        desc: '负责数字产品生成、平台上传、被动收益等工作',
        status: 'standby',
        color: '#f97316'
    },
    yinxiaolv: {
        id: 'yinxiaolv',
        avatar: '🎵',
        name: '音小律',
        role: '音乐天才专员',
        shortRole: '音乐',
        desc: '负责BGM制作、配音、音频素材等工作',
        status: 'standby',
        color: '#06b6d4'
    }
};

// 当前专员
let currentAgent = 'xiaoanzi';

/**
 * 初始化专员切换器
 */
function initAgentSwitcher() {
    createAgentSwitcherHTML();
    bindAgentEvents();
    updateCurrentAgentDisplay();
}

/**
 * 创建专员切换器HTML
 */
function createAgentSwitcherHTML() {
    const html = `
        <!-- 专员切换按钮 -->
        <button class="agent-toggle-btn" id="agentToggleBtn" title="切换AI专员">
            ${AGENTS_DATA[currentAgent].avatar}
        </button>
        
        <!-- 遮罩层 -->
        <div class="agent-overlay" id="agentOverlay"></div>
        
        <!-- 专员面板 -->
        <div class="agent-panel" id="agentPanel">
            <div class="agent-panel-header">
                <div class="agent-panel-title">
                    🤖 AI专员团队
                </div>
                <div class="agent-panel-subtitle">点击切换不同专员</div>
                <button class="agent-panel-close" id="agentPanelClose">✕</button>
            </div>
            
            <div class="agent-current-card" id="agentCurrentCard">
                <!-- 动态填充 -->
            </div>
            
            <div class="agent-list">
                <div class="agent-list-title">选择专员</div>
                <div id="agentListContainer">
                    <!-- 动态填充 -->
                </div>
            </div>
            
            <div class="agent-panel-footer">
                <button class="agent-action-btn" id="agentActionBtn">
                    联系当前专员
                </button>
            </div>
        </div>
    `;
    
    // 插入到body末尾
    const div = document.createElement('div');
    div.innerHTML = html;
    document.body.appendChild(div);
}

/**
 * 绑定事件
 */
function bindAgentEvents() {
    const toggleBtn = document.getElementById('agentToggleBtn');
    const panel = document.getElementById('agentPanel');
    const overlay = document.getElementById('agentOverlay');
    const closeBtn = document.getElementById('agentPanelClose');
    
    // 打开面板
    toggleBtn.addEventListener('click', () => {
        panel.classList.add('open');
        overlay.classList.add('show');
        toggleBtn.classList.add('active');
        renderAgentList();
        updateCurrentAgentCard();
    });
    
    // 关闭面板
    const closePanel = () => {
        panel.classList.remove('open');
        overlay.classList.remove('show');
        toggleBtn.classList.remove('active');
    };
    
    closeBtn.addEventListener('click', closePanel);
    overlay.addEventListener('click', closePanel);
    
    // 操作按钮
    document.getElementById('agentActionBtn').addEventListener('click', () => {
        const agent = AGENTS_DATA[currentAgent];
        alert(`正在联系 ${agent.name} (${agent.role})...\n\n功能开发中，敬请期待！`);
    });
}

/**
 * 渲染专员列表
 */
function renderAgentList() {
    const container = document.getElementById('agentListContainer');
    container.innerHTML = Object.values(AGENTS_DATA).map(agent => `
        <div class="agent-item ${agent.id === currentAgent ? 'active' : ''}" 
             data-agent="${agent.id}"
             onclick="selectAgent('${agent.id}')">
            <div class="agent-item-avatar">${agent.avatar}</div>
            <div class="agent-item-info">
                <div class="agent-item-name">${agent.name}</div>
                <div class="agent-item-role">${agent.role}</div>
            </div>
            <div class="agent-item-badge">${agent.shortRole}</div>
        </div>
    `).join('');
}

/**
 * 更新当前专员卡片
 */
function updateCurrentAgentCard() {
    const agent = AGENTS_DATA[currentAgent];
    const card = document.getElementById('agentCurrentCard');
    card.innerHTML = `
        <div class="agent-current-header">
            <div class="agent-current-avatar">${agent.avatar}</div>
            <div class="agent-current-info">
                <div class="agent-current-name">${agent.name}</div>
                <div class="agent-current-role">${agent.role}</div>
                <div class="agent-current-desc">${agent.desc}</div>
                <div class="agent-current-status">
                    ${agent.status === 'online' ? '● 在线' : '○ 待命'}
                </div>
            </div>
        </div>
    `;
}

/**
 * 选择专员
 */
function selectAgent(agentId) {
    currentAgent = agentId;
    
    // 更新列表高亮
    document.querySelectorAll('.agent-item').forEach(item => {
        item.classList.toggle('active', item.dataset.agent === agentId);
    });
    
    // 更新当前卡片
    updateCurrentAgentCard();
    
    // 更新切换按钮
    document.getElementById('agentToggleBtn').innerHTML = AGENTS_DATA[agentId].avatar;
    
    // 触发切换事件
    onAgentSwitch(agentId);
}

/**
 * 更新当前专员显示
 */
function updateCurrentAgentDisplay() {
    const agent = AGENTS_DATA[currentAgent];
    document.getElementById('agentToggleBtn').innerHTML = agent.avatar;
}

/**
 * 专员切换回调
 */
function onAgentSwitch(agentId) {
    const agent = AGENTS_DATA[agentId];
    console.log(`[Agent Switcher] 切换到专员: ${agent.name} (${agent.role})`);
    
    // 可以在这里添加自定义逻辑
    // 例如：切换工具推荐、改变主题色等
    
    // 显示切换提示
    showAgentSwitchToast(agent);
}

/**
 * 显示切换提示
 */
function showAgentSwitchToast(agent) {
    // 创建提示元素
    const toast = document.createElement('div');
    toast.style.cssText = `
        position: fixed;
        top: 100px;
        left: 50%;
        transform: translateX(-50%) translateY(-20px);
        background: linear-gradient(135deg, ${agent.color}, ${agent.color}dd);
        color: #fff;
        padding: 12px 24px;
        border-radius: 25px;
        font-size: 14px;
        font-weight: 500;
        z-index: 9999;
        opacity: 0;
        transition: all 0.3s;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
        display: flex;
        align-items: center;
        gap: 8px;
    `;
    toast.innerHTML = `
        <span style="font-size: 18px;">${agent.avatar}</span>
        <span>已切换到 ${agent.name}</span>
    `;
    
    document.body.appendChild(toast);
    
    // 动画显示
    requestAnimationFrame(() => {
        toast.style.opacity = '1';
        toast.style.transform = 'translateX(-50%) translateY(0)';
    });
    
    // 3秒后移除
    setTimeout(() => {
        toast.style.opacity = '0';
        toast.style.transform = 'translateX(-50%) translateY(-20px)';
        setTimeout(() => toast.remove(), 300);
    }, 3000);
}

/**
 * 获取当前专员
 */
function getCurrentAgent() {
    return AGENTS_DATA[currentAgent];
}

/**
 * 按职责获取专员
 */
function getAgentByRole(role) {
    return Object.values(AGENTS_DATA).find(agent => 
        agent.role.includes(role) || agent.shortRole === role
    );
}

// 初始化
document.addEventListener('DOMContentLoaded', initAgentSwitcher);
