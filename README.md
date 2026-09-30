# HTML-PPT-Craft (HTML 演示文稿制作技能与沉淀仓库)

这是一个可独立维护、直接推送到 Git 云端存储与团队共享的 **高保真 16:9 HTML 演示文稿制作规范与交付工程**。

---

## 目录结构

```text
html-ppt-craft/
├── SKILL.md                 # 核心规范与制作标准文档 (字号、行高、留白、卡片体系等)
├── README.md                # 项目与使用说明文档
├── .gitignore               # Git 忽略配置
├── templates/               # 基础 16:9 画板与模板文件
│   └── slide-template.html
├── scripts/                 # 自动化构建与 PPTX 辅助生成脚本
│   └── generate_pptx.py
├── references/              # 参考资料与设计样例
│   └── example-output.md
└── slides_output/           # 演示文稿成果与配套 16:9 高清大图
    ├── midyear_slide_presentation.html   # 垂直长卷多页完整演示文稿 (Page 01~05)
    ├── midyear_summary_slide.png         # Page 01 高清大图 (1920x1080)
    ├── visual_team_summary_slide.png     # Page 02 高清大图 (1920x1080)
    ├── ai_secops_summary_slide.png       # Page 03 高清大图 (1920x1080)
    ├── sec_group2_summary_slide.png      # Page 04 高清大图 (1920x1080)
    └── ai_native_evolution_slide.png     # Page 05 高清大图 (1920x1080)
```

---

## 核心设计规范速查

1. **严格 16:9 物理画板与双向视口等比自适应**：
   - 基准分辨率 `1920 × 1080`，任意屏幕下居中展示，绝无横向/纵向断层滚动。
2. **高饱满度宽屏排版标准（Spacious & Rich）**：
   - **正文字号**：统一为 `17.5px`，行高统一为 `1.72 ~ 1.75`。
   - **标题梯次**：主标题 `38px`、一句话战略副标 `19px`、板块栏目头 `28px`、卡片标题 `21.5~24px`。
   - **留白控制**：卡片内统一 `justify-content: flex-start; gap: 14~18px`，杜绝滥用 `space-between`。
3. **结构化 Callout 体系**：
   - 待改进/预警：暖琥珀色卡（`#FFFBEB`）
   - 推进阶段/技术：科技蓝轻卡（`#EFF6FF`）
   - 规划展望：沉稳灰蓝卡（`#F8FAFC`）

---

## 快速使用与查看

1. **直接双击查看长卷**：
   双击用浏览器打开 `slides_output/midyear_slide_presentation.html` 即可在全屏/窗口下以流式垂直长卷浏览所有 5 页总结。
2. **直接使用高清图片**：
   `slides_output/*.png` 均为 1920×1080 原生无损图片，拖拽进 PowerPoint 或 Keynote 页面即可严丝合缝填满 16:9。

---

## Git 仓库与协作

本技能与规范仓库已托管于 GitHub：
- **仓库地址**：[https://github.com/wangjue2026/html-ppt-craft](https://github.com/wangjue2026/html-ppt-craft)
- **克隆与安装**：

```bash
# 作为独立项目克隆
git clone https://github.com/wangjue2026/html-ppt-craft.git

# 或软链接挂载到任意工程的 AI Agent 技能库中：
# ln -s /path/to/html-ppt-craft /your-project/.agents/skills/html-ppt-craft
```
