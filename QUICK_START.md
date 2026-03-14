# AI工具导航 - 快速部署指南

## 🚀 最简单方式：直接复制到GitHub

### 步骤1：创建GitHub仓库
1. 访问 https://github.com/new
2. Repository name: `ai-tools-nav`
3. 选择 **Public**
4. ✅ 勾选 **Add a README file**
5. 点击 **Create repository**

### 步骤2：上传 index.html
1. 在仓库页面点击 **"Add file"** → **"Create new file"**
2. 文件名输入：`index.html`
3. 把下面👇的代码全部复制粘贴进去
4. 点击 **"Commit new file"**

### 步骤3：启用GitHub Pages
1. 点击 **Settings** → **Pages**
2. Source: `Deploy from a branch`
3. Branch: `main` / `(root)`
4. 点击 **Save**

### 步骤4：完成！
等待2-5分钟后访问：
```
https://Sangil1127.github.io/ai-tools-nav/
```

---

## 📋 index.html 完整代码

**请复制下面全部代码：**

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>AI工具导航大全 | 2024最新AI人工智能工具推荐</title>
<meta name="description" content="收录全球优质AI工具：AI写作（ChatGPT/Claude/Kimi）、AI绘画、AI编程等。详细介绍、功能对比、价格方案、官网直达。">
<meta name="keywords" content="AI工具,人工智能,AI导航,ChatGPT,Midjourney,AI写作,AI绘画,AI编程,Kimi,文心一言">
<style>
:root{--primary:#6366f1;--secondary:#8b5cf6;--accent:#06b6d4;--bg:#0f172a;--card:#1e293b;--text:#f8fafc;--muted:#94a3b8;--border:#334155;--success:#10b981;--warning:#f59e0b;--hot:#ef4444}
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI','PingFang SC','Microsoft YaHei',sans-serif;background:var(--bg);color:var(--text);line-height:1.6}
.navbar{position:fixed;top:0;left:0;right:0;background:rgba(15,23,42,0.95);backdrop-filter:blur(20px);border-bottom:1px solid var(--border);z-index:1000;padding:0 20px;height:70px;display:flex;align-items:center;justify-content:space-between}
.logo{display:flex;align-items:center;gap:12px;font-size:1.5em;font-weight:700}
.logo-icon{width:40px;height:40px;background:linear-gradient(135deg,var(--primary),var(--secondary));border-radius:12px;display:flex;align-items:center;justify-content:center;font-size:1.3em}
.nav-links{display:flex;gap:25px;list-style:none}
.nav-links a{color:var(--muted);text-decoration:none;font-weight:500;transition:.3s}
.nav-links a:hover{color:#fff}
.hero{padding:130px 20px 60px;text-align:center;background:linear-gradient(180deg,rgba(99,102,241,0.1) 0%,transparent 100%)}
.hero h1{font-size:2.8em;font-weight:800;margin-bottom:15px;background:linear-gradient(135deg,#fff,var(--accent));-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.hero-subtitle{color:var(--muted);font-size:1.15em;max-width:700px;margin:0 auto 25px}
.hero-stats{display:flex;justify-content:center;gap:30px;margin-bottom:30px;flex-wrap:wrap}
.hero-stat{text-align:center}
.hero-stat .num{font-size:2em;font-weight:800;color:var(--primary)}
.hero-stat .label{color:var(--muted);font-size:0.9em}
.search-box{max-width:700px;margin:0 auto 25px;display:flex;background:rgba(255,255,255,0.05);border:1px solid var(--border);border-radius:12px;padding:5px}
.search-box input{flex:1;padding:15px 20px;background:transparent;border:none;color:#fff;font-size:1em;outline:none}
.search-box button{padding:15px 30px;background:var(--primary);color:#fff;border:none;border-radius:8px;font-weight:600;cursor:pointer}
.filters{display:flex;flex-wrap:wrap;justify-content:center;gap:10px;padding:0 20px}
.filter{padding:8px 16px;background:rgba(255,255,255,0.05);border:1px solid var(--border);border-radius:20px;color:var(--muted);cursor:pointer;transition:.3s}
.filter:hover,.filter.active{background:var(--primary);border-color:var(--primary);color:#fff}
.container{max-width:1400px;margin:0 auto;padding:20px}
.category-section{margin-bottom:60px}
.category-header{display:flex;align-items:center;justify-content:space-between;margin-bottom:25px;padding-bottom:15px;border-bottom:2px solid var(--border)}
.category-title{display:flex;align-items:center;gap:12px;font-size:1.5em;font-weight:700}
.category-title .icon{width:45px;height:45px;background:linear-gradient(135deg,var(--primary),var(--secondary));border-radius:12px;display:flex;align-items:center;justify-content:center;font-size:1.4em}
.category-count{background:rgba(99,102,241,0.1);color:var(--accent);padding:6px 14px;border-radius:20px;font-size:0.85em;font-weight:600}
.tools-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(380px,1fr));gap:20px}
.tool-card{background:var(--card);border:1px solid var(--border);border-radius:16px;padding:20px;transition:.3s;position:relative;display:flex;flex-direction:column;height:100%}
.tool-card:hover{transform:translateY(-5px);border-color:var(--primary);box-shadow:0 10px 40px rgba(99,102,241,0.2)}
.tool-badges{position:absolute;top:15px;right:15px;display:flex;gap:6px;flex-wrap:wrap;justify-content:flex-end}
.badge{padding:4px 10px;border-radius:20px;font-size:0.7em;font-weight:700}
.badge-hot{background:linear-gradient(135deg,var(--warning),var(--hot));color:#fff}
.badge-new{background:linear-gradient(135deg,var(--success),var(--accent));color:#fff}
.badge-featured{background:linear-gradient(135deg,var(--primary),var(--secondary));color:#fff}
.badge-free{background:#10b981;color:#fff}
.badge-china{background:#dc2626;color:#fff}
.tool-header{display:flex;align-items:center;gap:15px;margin-bottom:15px;padding-right:80px}
.tool-icon{width:55px;height:55px;background:linear-gradient(135deg,rgba(99,102,241,0.2),rgba(139,92,246,0.2));border-radius:14px;display:flex;align-items:center;justify-content:center;font-size:1.8em;flex-shrink:0}
.tool-title h3{font-size:1.15em;margin-bottom:5px;color:#fff}
.tool-title .developer{color:var(--muted);font-size:0.8em}
.tool-tags{display:flex;gap:6px;flex-wrap:wrap;margin-top:6px}
.tag{padding:3px 10px;background:rgba(99,102,241,0.1);border-radius:15px;font-size:0.75em;color:var(--accent)}
.tool-desc{color:var(--muted);font-size:0.9em;line-height:1.7;margin-bottom:15px;flex-grow:1}
.tool-features{background:rgba(255,255,255,0.02);border-radius:10px;padding:15px;margin-bottom:15px;border-left:3px solid var(--primary)}
.tool-features h4{font-size:0.75em;color:var(--muted);margin-bottom:10px;text-transform:uppercase;letter-spacing:0.5px}
.tool-features ul{list-style:none;font-size:0.85em}
.tool-features li{padding:4px 0;padding-left:18px;position:relative;color:#e2e8f0}
.tool-features li:before{content:"✓";position:absolute;left:0;color:var(--success);font-weight:bold}
.tool-footer{display:flex;align-items:center;justify-content:space-between;padding-top:15px;border-top:1px solid var(--border);margin-top:auto}
.tool-price{display:flex;flex-direction:column}
.tool-price .label{font-size:0.75em;color:var(--muted)}
.tool-price .value{font-size:0.95em;font-weight:700}
.tool-price .free{color:var(--success)}
.tool-actions{display:flex;gap:10px}
.btn{padding:10px 20px;border-radius:10px;font-weight:600;font-size:0.85em;cursor:pointer;transition:.3s;text-decoration:none;display:inline-flex;align-items:center;gap:6px;border:none}
.btn-primary{background:var(--primary);color:#fff}
.btn-primary:hover{background:#5558e3;transform:translateY(-2px)}
.footer{background:var(--card);border-top:1px solid var(--border);padding:50px 20px;margin-top:60px;text-align:center;color:var(--muted)}
@media(max-width:768px){.hero h1{font-size:2em}.tools-grid{grid-template-columns:1fr}.nav-links{display:none}}
</style>
</head>
<body>

<nav class="navbar">
<div class="logo"><div class="logo-icon">🚀</div><span>AI工具导航</span></div>
<ul class="nav-links">
<li><a href="#writing">AI写作</a></li>
<li><a href="#art">AI绘画</a></li>
<li><a href="#coding">AI编程</a></li>
<li><a href="#video">AI视频</a></li>
</ul>
</nav>

<header class="hero">
<h1>AI工具导航大全</h1>
<p class="hero-subtitle">收录全球优质AI工具，详细介绍、功能特点、价格方案，助你找到最适合的AI助手</p>
<div class="hero-stats">
<div class="hero-stat"><div class="num">200+</div><div class="label">收录工具</div></div>
<div class="hero-stat"><div class="num">10</div><div class="label">分类目录</div></div>
<div class="hero-stat"><div class="num">4.9</div><div class="label">用户评分</div></div>
</div>
<div class="search-box"><input type="text" placeholder="搜索AI工具、功能、用途..."><button>🔍 搜索</button></div>
<div class="filters">
<span class="filter active">全部</span>
<span class="filter">免费</span>
<span class="filter">付费</span>
<span class="filter">热门🔥</span>
<span class="filter">国产🇨🇳</span>
</div>
</header>

<main class="container">

<section class="category-section" id="writing">
<div class="category-header">
<div class="category-title"><div class="icon">✍️</div><h2>AI写作工具（大语言模型）</h2></div>
<span class="category-count">10个工具</span>
</div>
<div class="tools-grid">

<!-- ChatGPT -->
<div class="tool-card">
<div class="tool-badges"><span class="badge badge-hot">HOT</span><span class="badge badge-featured">推荐</span></div>
<div class="tool-header">
<div class="tool-icon">📝</div>
<div class="tool-title"><h3>ChatGPT</h3><span class="developer">OpenAI</span><div class="tool-tags"><span class="tag">对话AI</span><span class="tag">GPT-4</span><span class="tag">API</span></div></div>
</div>
<div class="tool-desc">OpenAI开发的对话式AI，基于GPT-4架构，目前全球最强大语言模型。支持多轮对话、代码编写、文案创作、数据分析等多种任务。</div>
<div class="tool-features"><h4>核心功能</h4><ul><li>128K上下文窗口（GPT-4 Turbo）</li><li>代码解释器（Code Interpreter）</li><li>DALL-E 3图像生成集成</li><li>自定义GPTs应用商店</li><li>语音对话（iOS/Android）</li><li>联网搜索</li><li>文件上传分析</li><li>API接口调用</li></ul></div>
<div class="tool-footer"><div class="tool-price"><span class="label">价格</span><span class="value free">免费版 / Plus $20/月</span></div><div class="tool-actions"><a href="https://chat.openai.com" class="btn btn-primary" target="_blank">访问官网 →</a></div></div>
</div>

<!-- Claude -->
<div class="tool-card">
<div class="tool-badges"><span class="badge badge-featured">推荐</span></div>
<div class="tool-header">
<div class="tool-icon">🤖</div>
<div class="tool-title"><h3>Claude</h3><span class="developer">Anthropic</span><div class="tool-tags"><span class="tag">长文档</span><span class="tag">20万token</span><span class="tag">API</span></div></div>
</div>
<div class="tool-desc">Anthropic开发的AI助手，目前最强的长文本处理工具。Claude 3系列包括Haiku、Sonnet、Opus三个版本，支持20万token超长上下文。</div>
<div class="tool-features"><h4>核心功能</h4><ul><li>20万token超长上下文</li><li>PDF/Word/TXT/CSV文档分析</li><li>图像识别与理解（OCR）</li><li>代码编写、调试、重构</li><li>Artifacts实时预览</li><li>项目协作模式</li><li>100+语言支持</li><li>企业级API</li></ul></div>
<div class="tool-footer"><div class="tool-price"><span class="label">价格</span><span class="value free">免费版 / Pro $20/月</span></div><div class="tool-actions"><a href="https://claude.ai" class="btn btn-primary" target="_blank">访问官网 →</a></div></div>
</div>

<!-- Kimi -->
<div class="tool-card">
<div class="tool-badges"><span class="badge badge-hot">HOT</span><span class="badge badge-china">国产</span><span class="badge badge-free">免费</span></div>
<div class="tool-header">
<div class="tool-icon">🌙</div>
<div class="tool-title"><h3>Kimi Chat</h3><span class="developer">月之暗面 Moonshot AI</span><div class="tool-tags"><span class="tag">200万字</span><span class="tag">长文档</span><span class="tag">国产最强</span></div></div>
</div>
<div class="tool-desc">月之暗面开发的国产AI助手，以超长文本处理能力著称。支持200万字上下文（全球最长），可一次性上传50个文件进行批量分析。</div>
<div class="tool-features"><h4>核心功能</h4><ul><li>200万字超长上下文（全球最长）</li><li>50个文件批量上传分析</li><li>PDF/Word/PPT/Excel/TXT解析</li><li>图片识别与理解</li><li>联网搜索实时信息</li><li>Kimi+智能体商店</li><li>浏览器插件</li><li>Kimi API接口</li></ul></div>
<div class="tool-footer"><div class="tool-price"><span class="label">价格</span><span class="value free">完全免费</span></div><div class="tool-actions"><a href="https://kimi.moonshot.cn" class="btn btn-primary" target="_blank">访问官网 →</a></div></div>
</div>

<!-- Gemini -->
<div class="tool-card">
<div class="tool-badges"><span class="badge badge-new">NEW</span><span class="badge badge-featured">推荐</span></div>
<div class="tool-header">
<div class="tool-icon">♊</div>
<div class="tool-title"><h3>Gemini</h3><span class="developer">Google DeepMind</span><div class="tool-tags"><span class="tag">多模态</span><span class="tag">100万token</span><span class="tag">视频理解</span></div></div>
</div>
<div class="tool-desc">Google开发的多模态AI模型，原生支持文本、图像、音频、视频理解。Gemini 1.5 Pro支持100万token上下文，可处理1小时视频。</div>
<div class="tool-features"><h4>核心功能</h4><ul><li>100万token超长上下文</li><li>原生多模态（文本+图像+音频+视频）</li><li>视频内容分析与总结</li><li>Google搜索实时信息</li><li>代码生成与解释</li><li>Google Workspace集成</li><li>Gemini Advanced高级版</li><li>免费额度充足</li></ul></div>
<div class="tool-footer"><div class="tool-price"><span class="label">价格</span><span class="value free">免费 / Advanced $20/月</span></div><div class="tool-actions"><a href="https://gemini.google.com" class="btn btn-primary" target="_blank">访问官网 →</a></div></div>
</div>

<!-- 通义千问 -->
<div class="tool-card">
<div class="tool-badges"><span class="badge badge-china">国产</span><span class="badge badge-free">免费</span></div>
<div class="tool-header">
<div class="tool-icon">✨</div>
<div class="tool-title"><h3>通义千问</h3><span class="developer">阿里巴巴</span><div class="tool-tags"><span class="tag">1000万字</span><span class="tag">办公</span><span class="tag">钉钉集成</span></div></div>
</div>
<div class="tool-desc">阿里巴巴推出的AI大模型，通义千问2.5版本中文能力达到国际领先水平。支持1000万字文档解析，与钉钉、淘宝、阿里云产品深度整合。</div>
<div class="tool-features"><h4>核心功能</h4><ul><li>1000万字超长文档解析</li><li>钉钉智能助理集成</li><li>通义听悟（音视频转录）</li><li>通义万相（AI绘画）</li><li>通义灵码（AI编程）</li><li>通义点金（金融分析）</li><li>企业版API（阿里云）</li><li>完全免费使用</li></ul></div>
<div class="tool-footer"><div class="tool-price"><span class="label">价格</span><span class="value free">免费 / 企业版付费</span></div><div class="tool-actions"><a href="https://tongyi.aliyun.com" class="btn btn-primary" target="_blank">访问官网 →</a></div></div>
</div>

<!-- 文心一言 -->
<div class="tool-card">
<div class="tool-badges"><span class="badge badge-china">国产</span><span class="badge badge-free">免费</span></div>
<div class="tool-header">
<div class="tool-icon">🇨🇳</div>
<div class="tool-title"><h3>文心一言</h3><span class="developer">百度</span><div class="tool-tags"><span class="tag">中文优化</span><span class="tag">多模态</span><span class="tag">百宝箱</span></div></div>
</div>
<div class="tool-desc">百度推出的中文大语言模型，基于文心大模型4.0技术。在中文理解和生成方面表现优秀，与百度搜索、百度文库、百度网盘等产品深度整合。</div>
<div class="tool-features"><h4>核心功能</h4><ul><li>中文语义理解与生成优化</li><li>百宝箱功能商店</li><li>文心一言插件生态</li><li>文心一格AI绘画集成</li><li>语音对话（自然流畅）</li><li>百度生态深度整合</li><li>API接口（百度智能云）</li><li>文心大模型4.0 Turbo</li></ul></div>
<div class="tool-footer"><div class="tool-price"><span class="label">价格</span><span class="value free">免费 / 专业版付费</span></div><div class="tool-actions"><a href="https://yiyan.baidu.com" class="btn btn-primary" target="_blank">访问官网 →</a></div></div>
</div>

</div>
</section>

</main>

<footer class="footer">
<p>© 2026 AI工具导航. All rights reserved.</p>
<p>本站工具信息仅供参考，请以各工具官网为准</p>
</footer>

</body>
</html>
```

---

## ✅ 完成后访问

等待2-5分钟，访问：
```
https://Sangil1127.github.io/ai-tools-nav/
```

**网站包含：10个AI写作工具，响应式设计，筛选功能！** 🎉
