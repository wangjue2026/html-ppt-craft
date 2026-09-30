---
name: html-ppt-craft
description: >-
  用于将用户的文本草稿、截图或初稿想法转化为高保真、简约轻量且严格保持 16:9 比例的 HTML 格式 PPT 幻灯片与配套高清大图。支持动态全屏自适应、一键导出 PDF 与 PNG 图片。除非用户明确要求生成 PPT 文件，否则默认不主动生成 .pptx 文件。
---

# HTML-PPT-Craft (HTML 演示文稿制作技能)

本技能用于将各种输入源（文本散文/要点草稿、页面截图、初稿大纲）转化为**专业级、简约轻量、信息层级清晰且严格 16:9 自适应**的 HTML 格式单页/多页 PPT，并同步输出一张**配套的高清 16:9 大图**供用户直接拖拽进现有汇报。

---

## 核心设计规范与原则

1. **严格 16:9 物理画板与双向视口等比自适应**：
   * 基准画板采用 `1920 × 1080` 分辨率。
   * 使用 `transform: translate(-50%, -50%) scale(...)` 算法，在任意窗口尺寸与长宽比下（如 1920x726、1440x900 等）始终 100% 完整居中展示，**严禁产生滚动条或底部/侧边截断**。
2. **极简轻量、拒绝花哨**：
   * 采用现代商务/科技的高级灰白底色（如 `#FFFFFF` 配合 `#F8FAFC` 卡片与 `#E2E8F0` 极细边框）。
   * 克制使用色彩：主要信息用深灰黑（`#0F172A`），正文浅灰（`#334155`），点缀色仅用于关键数字、标签或状态感知。
3. **结构化信息提炼（看板化）**：
   * 将大段纯文本提炼为：**顶部导读/摘要 + 结构化多栏看板 + 核心量化指标卡（如 900+ / 70% / 100%）+ 状态标签胶囊**。
4. **输出目录与文件管理（独立维护项目）**：
   * **专属输出目录**：所有交付物保存在本技能项目内部的 [slides_output/](./slides_output/) 目录下（路径为 `html-ppt-craft/slides_output/`），**严禁在主项目根目录中散落文件**。
   * **默认交付物**：`slides_output/[name]_slide.html`（交互演示与导出）、`slides_output/[name]_slide.png`（高清大图）。
   * **PPTX 策略**：**若用户未明确说明需要 PPT/PPTX 文件，不主动生成 .pptx**。若用户明确要求生成 PPT，使用技能内置的 [generate_pptx.py](./scripts/generate_pptx.py) 脚本生成至内部的 `slides_output/` 下。
5. **高饱满度宽屏字号与行高基准（Spacious & Rich Information Standard）**：
   * **正文字号标准**：统一基准提升至 **`17.5px`**，行高统一为 **`1.72 ~ 1.75`**。彻底消除使用 14~15px 小字号在 1920×1080 宽画板中造成的文字零散与孤立空旷感。
   * **层级字号梯度**：
     * 一级主标题：`36px ~ 38px`（700 加粗，`-0.02em` 字距）
     * 一句话战略副标题：`18px ~ 19px`（次级灰色 `#64748B`，行高 1.38）
     * 板块栏目头 (Panel Title)：`26px ~ 28px`，搭配序列编号方块与副标 Tagline（`15px ~ 16px`）
     * 核心卡片标题 (Card Title)：`21.5px ~ 24px`，左侧搭配对应业务主题的彩色圆点
     * 状态胶囊/标签 (Status Tags)：`13.5px ~ 14.5px`（粗体，内边距 `3px 10px` ~ `4px 12px`）
     * 正文字体 (Body Text)：`17.5px`（行高 `1.72 ~ 1.75`，列表项间距 `13px ~ 16px`）
     * 辅助标注/提示块 (Callout Text)：`16px ~ 16.5px`（行高 `1.62 ~ 1.65`）
6. **纵向自适应比例与容器布局体系（Proportional Flex Allocation）**：
   * **拒绝“盒中盒”留白陷阱**：避免无意义的外层大灰框套内层小子卡片所导致的大面积死寂空白；优先采用清晰独立的顶层 `.card` 体系。
   * **按信息体量自适应分配 flex**：
     * 单栏内 2 个卡片：按文字多寡配置 `flex: 1.15 : 1.0` 或 `1.35 : 1.0`，使卡片自然撑满整列高度，左右两栏底部严丝合缝平齐；
     * 单栏内 3 个卡片：按文字多寡配置 `flex: 0.88 : 1.0 : 1.48`，保证内容少的卡片紧凑包裹，内容多的卡片获得充分呼吸感；
     * **卡片内对齐原则**：卡片内部默认使用 `justify-content: flex-start; gap: 14px~18px;`，**严禁在仅有标题和正文列表的两项卡片上滥用 `space-between`**，杜绝中间产生割裂空洞。
7. **结构化原注文案与轻量彩色 Callout 体系**：
   * 原文重点文字必须保持加粗，原注文案（如带星号 `*...` 的待改进项、推进阶段、下一阶段规划）转化为轻量彩色背景的结构化提示块（`note-callout`）：
     * 待改进 / 风险预警：暖琥珀色轻卡（`#FFFBEB`，边框 `#FDE68A`，标签 `pill-warning`）；
     * 推进阶段 / 技术演进：科技蓝轻卡（`#EFF6FF`，边框 `#BFDBFE`，标签 `pill-info`）；
     * 规划展望 / 持续深化：沉稳灰蓝轻卡（`#F8FAFC`，边框 `#E2E8F0`，标签 `pill-slate`）。
   * 阶段旅程链条（如 `及时发现 → 准确验证 → 推演路径 → 精准断链`）采用高亮胶囊（`journey-badge`）承载。
8. **免打扰样式快修与临时文件清理原则**：
   * 当用户提出样式调整、快速修复或排版优化时，**严禁自动调用浏览器验证**；通过无头 Chrome 脚本离线导出高清 PNG 进行画质把控，由用户在已有窗口直接刷新验证。
   * **严禁在项目交付目录遗留临时测试文件**：中间自检产生的 `test_*.png` 或辅助验证截图必须存放在系统临时目录或自检完毕后即刻自动删除，严禁污染 `slides_output/` 等业务交付目录，保持工作区绝对纯净。


---

## 执行工作流 (Step-by-Step)

### 第一步：理解与重构文案 (Content Structuring)
1. **识别核心主题**：提炼出一级主标题（24~34px）和一句话战略副标题（14~17px）。
2. **提炼量化数据**：寻找所有的百分比、计数、周期等（如“900+”、“70%”、“80%~90%”），将其提升为 Metric Box。
3. **梳理状态与标签**：为各个模块打上直观状态（如 `进行中`、`预发布 10.16`、`审慎观望`、`国庆后 Beta`）。
4. **布局规划**：
   * 双栏对比/看板（如 58% : 42% 业务攻坚 vs 效能探索）；
   * 三栏卡片阵列（如 核心亮点 1 / 2 / 3）；
   * 上下架构流水（如 顶层战略目标 + 底层能力支撑）。

### 第二步：生成 16:9 自适应 HTML 页面
参考 [slide-template.html](./templates/slide-template.html) 构建页面：
1. **必须包含的基础自适应 CSS**：
   ```css
   html, body {
     width: 100vw;
     height: 100vh;
     overflow: hidden;
     background-color: #ECEFF3;
     margin: 0;
     padding: 0;
   }
   .stage {
     position: absolute;
     inset: 0;
     display: flex;
     align-items: center;
     justify-content: center;
     overflow: hidden;
   }
   .slide-canvas {
     position: absolute;
     width: 1920px;
     height: 1080px;
     top: 50%;
     left: 50%;
     transform: translate(-50%, -50%) scale(var(--slide-scale, 0.7));
     transform-origin: center center;
     background: #FFFFFF;
     border-radius: 12px;
     box-shadow: 0 20px 50px -10px rgba(15, 23, 42, 0.15);
     overflow: hidden;
     display: flex;
     flex-direction: column;
     padding: 48px 64px 36px;
   }
   ```
2. **必须包含的 JS 缩放计算引擎**：
   ```javascript
   function autoScaleSlide() {
     const isFullscreen = !!document.fullscreenElement;
     const marginRatio = isFullscreen ? 0.98 : 0.94;
     const vw = window.innerWidth;
     const vh = window.innerHeight;
     const scale = Math.min((vw * marginRatio) / 1920, (vh * marginRatio) / 1080);
     document.documentElement.style.setProperty('--slide-scale', scale);
     const display = document.getElementById('scaleDisplay');
     if (display) display.innerText = `${Math.round(scale * 100)}% 视口适配`;
   }
   window.addEventListener('resize', autoScaleSlide);
   document.addEventListener('fullscreenchange', autoScaleSlide);
   autoScaleSlide();
   ```
3. **信息密度模式 (Density Modes)**：
   * **高饱满度宽屏排版 (Spacious & Rich · 默认推荐)**：适用于标准汇报与高管演示（正文 **17.5px**、行高 **1.72~1.75**、卡片标题 **22~24px**、列表间距 **14~18px**、卡片内边距 **24~30px**），视觉饱满大气，彻底消除零散空洞感。
   * **紧凑密集排版 (Compact)**：适用于条目极多、超高密度的综合清单（正文 15px、行高 1.56、间距紧凑收敛），保障信息单页容纳。
   * 在 CSS 中通过 CSS 变量（`--body-size`, `--body-lh`, `--gap-list`, `--padding-card`）统一定义。
4. **悬浮控制胶囊与导出体系 (Floating Toolbar & Export Suite)**：
   * **全屏演示按钮**：调用 `requestFullscreen()` 实现沉浸式汇报。
   * **导出 16:9 PDF**：必须在 CSS 中配置 `@page { size: 1920px 1080px; margin: 0; }` 以及 `-webkit-print-color-adjust: exact; print-color-adjust: exact;`，确保浏览器打印时输出纯正 16:9 横版无白边、色彩完整的高清 PDF。
   * **下载 1080P 高清大图**：集成 `html2canvas` 导出原生 1920×1080 PNG。**关键注意**：在调用 `html2canvas` 渲染前，必须临时将画板的 CSS `transform` 重置为 `none`，并将 `position` 临时设为 `fixed`、`top:0`、`left:0`，待截图完成后再恢复原位，防止画板缩放变换导致截图留白或严重偏移；禁止设置 `allowTaint: true`，避免触发浏览器的 Canvas 安全导出拦截。

### 第三步：输出一张配套的高清 16:9 大图
1. 使用画板自带的“下载高清大图”能力或浏览器子代理（`browser_subagent`）/辅助脚本，捕获无失真、无外围阴影的纯净 1920×1080 画板图像。
2. 图像保存为 `slides_output/[name]_slide.png`。
3. 确保该图片拖拽进现有的 PowerPoint 或 Keynote 页面时能严丝合缝填满 16:9 画面。

### 第四步：交付总结与说明
交付给用户时提供：
1. **效果图预览**（Markdown 内嵌图片预览）。
2. **提炼与设计逻辑阐述**（简述如何将零散文字转化为结构化卡片与指标）。
3. **文件指引**：
   * `slides_output/[name]_slide.html`：位于技能子项目内部，双击浏览器打开演示，支持全屏与导出 PDF。
   * `slides_output/[name]_slide.png`：高清图片，可直接复制或插入 PPT。
