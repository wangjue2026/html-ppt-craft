import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

def create_deck():
    prs = Presentation()
    # 16:9 widescreen
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]
    slide = prs.slides.add_slide(blank_layout)

    # Palette
    C_BG = RGBColor(248, 249, 250)
    C_WHITE = RGBColor(255, 255, 255)
    C_TITLE = RGBColor(17, 24, 39)
    C_SUB = RGBColor(100, 116, 139)
    C_BODY = RGBColor(51, 65, 85)
    C_MUTED = RGBColor(148, 163, 184)
    C_BLUE = RGBColor(37, 99, 235)
    C_BLUE_LIGHT = RGBColor(239, 246, 255)
    C_PURPLE = RGBColor(79, 70, 229)
    C_PURPLE_LIGHT = RGBColor(238, 242, 255)
    C_BORDER = RGBColor(226, 232, 240)
    C_CARD_BG = RGBColor(250, 250, 251)
    C_TAG_DELAY_BG = RGBColor(254, 243, 199)
    C_TAG_DELAY_TXT = RGBColor(146, 64, 14)
    C_TAG_PROG_BG = RGBColor(239, 246, 255)
    C_TAG_PROG_TXT = RGBColor(30, 64, 175)
    C_TAG_WATCH_BG = RGBColor(241, 245, 249)
    C_TAG_WATCH_TXT = RGBColor(71, 85, 105)

    # Top accent line
    top_line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(0.08))
    top_line.fill.solid()
    top_line.fill.fore_color.rgb = C_BLUE
    top_line.line.color.rgb = C_BLUE

    # Header Box
    header_box = slide.shapes.add_textbox(Inches(0.6), Inches(0.4), Inches(10.5), Inches(1.1))
    tf = header_box.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

    # Badge / Category
    p0 = tf.paragraphs[0]
    p0.text = "MID-YEAR REVIEW · 年中工作复盘"
    p0.font.size = Pt(9.5)
    p0.font.bold = True
    p0.font.color.rgb = C_BLUE

    # Main Title
    p1 = tf.add_paragraph()
    p1.text = "业务方向聚焦与落地攻坚 · AI 工程化探索沉淀"
    p1.font.size = Pt(20)
    p1.font.bold = True
    p1.font.color.rgb = C_TITLE
    p1.space_before = Pt(4)

    # Subtitle
    p2 = tf.add_paragraph()
    p2.text = "围绕核心业务场景打通可用性闭环与体验规范；持续推进 AI 从原型验证到统一工具链、规范代码资产的高效演进"
    p2.font.size = Pt(11)
    p2.font.color.rgb = C_SUB
    p2.space_before = Pt(3)

    # Header Right Badge
    right_badge = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(11.2), Inches(0.45), Inches(1.5), Inches(0.35))
    right_badge.fill.solid()
    right_badge.fill.fore_color.rgb = RGBColor(243, 244, 246)
    right_badge.line.color.rgb = C_BORDER
    rtf = right_badge.text_frame
    rtf.word_wrap = False
    rp = rtf.paragraphs[0]
    rp.alignment = PP_ALIGN.CENTER
    rp.text = "2024 年中总结"
    rp.font.size = Pt(10)
    rp.font.color.rgb = C_SUB
    rp.font.bold = True

    # Divider line under header
    line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.6), Inches(1.55), Inches(12.133), Inches(0.015))
    line.fill.solid()
    line.fill.fore_color.rgb = C_BORDER
    line.line.color.rgb = C_BORDER

    # ================= LEFT COLUMN: 业务项目部分 (width: 7.2 in) =================
    col_left_x = Inches(0.6)
    col_left_w = Inches(7.3)

    # Section Title Left
    sec_left = slide.shapes.add_textbox(col_left_x, Inches(1.68), col_left_w, Inches(0.35))
    stf = sec_left.text_frame
    stf.word_wrap = True
    stf.margin_left = stf.margin_top = stf.margin_right = stf.margin_bottom = 0
    sp = stf.paragraphs[0]
    sp.text = "01  业务项目部分  |  方向变更与聚焦 · 落地周期拉长"
    sp.font.size = Pt(12)
    sp.font.bold = True
    sp.font.color.rgb = C_TITLE

    # Card 1: SMG 1.0 (Top)
    smg_card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, col_left_x, Inches(2.08), col_left_w, Inches(2.65))
    smg_card.fill.solid()
    smg_card.fill.fore_color.rgb = C_CARD_BG
    smg_card.line.color.rgb = C_BORDER
    smg_card.line.width = Pt(1)

    smg_tf = smg_card.text_frame
    smg_tf.word_wrap = True
    smg_tf.margin_left = Inches(0.2)
    smg_tf.margin_right = Inches(0.2)
    smg_tf.margin_top = Inches(0.15)
    smg_tf.margin_bottom = Inches(0.15)

    p = smg_tf.paragraphs[0]
    p.text = "SMG 1.0   移动办公、组网等场景 Job 能力融合管理平台"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = C_TITLE

    # Delay status tag on the top right of SMG card
    smg_tag = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, col_left_x + col_left_w - Inches(1.7), Inches(2.18), Inches(1.5), Inches(0.28))
    smg_tag.fill.solid()
    smg_tag.fill.fore_color.rgb = C_TAG_DELAY_BG
    smg_tag.line.color.rgb = RGBColor(252, 211, 77)
    smg_tag.line.width = Pt(0.5)
    st = smg_tag.text_frame.paragraphs[0]
    st.alignment = PP_ALIGN.CENTER
    st.text = "预计 10.16 预发布"
    st.font.size = Pt(9.5)
    st.font.bold = True
    st.font.color.rgb = C_TAG_DELAY_TXT

    # Metrics inside SMG card
    metrics = [
        ("900+", "自检/演示检视问题"),
        ("70%", "问题整体闭环率"),
        ("100%", "核心体验缺陷已闭环")
    ]
    mw = Inches(2.18)
    for i, (val, lbl) in enumerate(metrics):
        mx = col_left_x + Inches(0.2) + i * (mw + Inches(0.15))
        my = Inches(2.55)
        m_box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, mx, my, mw, Inches(0.62))
        m_box.fill.solid()
        m_box.fill.fore_color.rgb = C_WHITE
        m_box.line.color.rgb = C_BORDER
        m_box.line.width = Pt(0.8)
        mtf = m_box.text_frame
        mtf.margin_top = Inches(0.06)
        mtf.margin_bottom = 0
        mtf.margin_left = Inches(0.1)
        vp = mtf.paragraphs[0]
        vp.text = val
        vp.font.size = Pt(14)
        vp.font.bold = True
        vp.font.color.rgb = C_BLUE
        lp = mtf.add_paragraph()
        lp.text = lbl
        lp.font.size = Pt(8.5)
        lp.font.color.rgb = C_SUB

    # Bullet points inside SMG card (text box below metrics)
    smg_bullets = slide.shapes.add_textbox(col_left_x + Inches(0.2), Inches(3.25), col_left_w - Inches(0.4), Inches(1.35))
    btf = smg_bullets.text_frame
    btf.word_wrap = True
    btf.margin_left = btf.margin_right = btf.margin_top = btf.margin_bottom = 0

    bp1 = btf.paragraphs[0]
    bp1.text = "• 高保真业务 Demo 与可用性闭环：覆盖设备管理与全球安全核心页面，完成 2 个 AF 专家可用性测试，识别 33 个问题，关键体验问题（接入地址配置不合理、接入码无法导出、前置后置策略不理解等）与规划同步并在研发闭环。"
    bp1.font.size = Pt(9.5)
    bp1.font.color.rgb = C_BODY
    bp1.space_before = Pt(2)

    bp2 = btf.add_paragraph()
    bp2.text = "• 9+ 业务规范统一定义：主导高级搜索、对象选择器、权限管理、批量导入、配置下发、表格操作、导航栏、时间展示、空状态及文案等规范落地，部分已沉淀为 AI 资产技能。"
    bp2.font.size = Pt(9.5)
    bp2.font.color.rgb = C_BODY
    bp2.space_before = Pt(4)

    # Bottom Row of Left: GA and GEN AI
    card_sub_w = Inches(3.55)
    sub_y = Inches(4.85)
    sub_h = Inches(2.05)

    # Sub-card 1: 全球加速 GA
    ga_card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, col_left_x, sub_y, card_sub_w, sub_h)
    ga_card.fill.solid()
    ga_card.fill.fore_color.rgb = C_CARD_BG
    ga_card.line.color.rgb = C_BORDER
    ga_card.line.width = Pt(1)

    ga_tf = ga_card.text_frame
    ga_tf.word_wrap = True
    ga_tf.margin_left = Inches(0.18)
    ga_tf.margin_right = Inches(0.18)
    ga_tf.margin_top = Inches(0.14)
    ga_tf.margin_bottom = Inches(0.1)

    gp0 = ga_tf.paragraphs[0]
    gp0.text = "全球加速 GA   [国庆后 Beta]"
    gp0.font.size = Pt(11)
    gp0.font.bold = True
    gp0.font.color.rgb = C_TITLE

    gp_sub = ga_tf.add_paragraph()
    gp_sub.text = "让全球办公员工快速访问跨境业务"
    gp_sub.font.size = Pt(8.5)
    gp_sub.font.color.rgb = C_SUB
    gp_sub.space_before = Pt(1)

    gp1 = ga_tf.add_paragraph()
    gp1.text = "• 前期完成竞品分析、AI 静态图发散与交付调研举措；"
    gp1.font.size = Pt(9)
    gp1.font.color.rgb = C_BODY
    gp1.space_before = Pt(5)

    gp2 = ga_tf.add_paragraph()
    gp2.text = "• 输出高保真 AI Demo 通过 TR1 需求评审，部分需求（天枢全球一张网）直接复用 AI 代码交付；"
    gp2.font.size = Pt(9)
    gp2.font.color.rgb = C_BODY
    gp2.space_before = Pt(3)

    gp3 = ga_tf.add_paragraph()
    gp3.text = "• 已完成立项与迭代一开发，当前检视中。"
    gp3.font.size = Pt(9)
    gp3.font.color.rgb = C_BODY
    gp3.space_before = Pt(3)

    # Sub-card 2: GEN AI
    gen_card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, col_left_x + card_sub_w + Inches(0.2), sub_y, card_sub_w, sub_h)
    gen_card.fill.solid()
    gen_card.fill.fore_color.rgb = C_CARD_BG
    gen_card.line.color.rgb = C_BORDER
    gen_card.line.width = Pt(1)

    gen_tf = gen_card.text_frame
    gen_tf.word_wrap = True
    gen_tf.margin_left = Inches(0.18)
    gen_tf.margin_right = Inches(0.18)
    gen_tf.margin_top = Inches(0.14)
    gen_tf.margin_bottom = Inches(0.1)

    gen0 = gen_tf.paragraphs[0]
    gen0.text = "GEN AI   [审慎投入 · 保持观察]"
    gen0.font.size = Pt(11)
    gen0.font.bold = True
    gen0.font.color.rgb = C_TITLE

    gen_sub = gen_tf.add_paragraph()
    gen_sub.text = "保障端侧 AI 安全使用与行为管控"
    gen_sub.font.size = Pt(8.5)
    gen_sub.font.color.rgb = C_SUB
    gen_sub.space_before = Pt(1)

    gen1 = gen_tf.add_paragraph()
    gen1.text = "• 目前仅支持审计看清管控，筑牢安全合规底线；"
    gen1.font.size = Pt(9)
    gen1.font.color.rgb = C_BODY
    gen1.space_before = Pt(5)

    gen2 = gen_tf.add_paragraph()
    gen2.text = "• 430 Beta 测试后，针对无感隔离与零信任动态授权产线暂缓投入，无感沙箱方案搁置；"
    gen2.font.size = Pt(9)
    gen2.font.color.rgb = C_BODY
    gen2.space_before = Pt(3)

    gen3 = gen_tf.add_paragraph()
    gen3.text = "• 核心成因：企业侧成熟 GenAI 使用场景短期尚不明确，理性控本待时机成熟。"
    gen3.font.size = Pt(9)
    gen3.font.color.rgb = C_BODY
    gen3.space_before = Pt(3)

    # ================= RIGHT COLUMN: AI 探索部分 (width: 4.6 in) =================
    col_right_x = Inches(8.15)
    col_right_w = Inches(4.58)

    # Section Title Right
    sec_right = slide.shapes.add_textbox(col_right_x, Inches(1.68), col_right_w, Inches(0.35))
    srtf = sec_right.text_frame
    srtf.word_wrap = True
    srtf.margin_left = srtf.margin_top = srtf.margin_right = srtf.margin_bottom = 0
    srp = srtf.paragraphs[0]
    srp.text = "02  AI 深度探索部分  |  常态化推进 · 提效沉淀"
    srp.font.size = Pt(12)
    srp.font.bold = True
    srp.font.color.rgb = C_TITLE

    # AI Card 1: Token & SD 技能 (h = 1.5 in)
    ai1_y = Inches(2.08)
    ai1_h = Inches(1.48)
    ai1 = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, col_right_x, ai1_y, col_right_w, ai1_h)
    ai1.fill.solid()
    ai1.fill.fore_color.rgb = C_CARD_BG
    ai1.line.color.rgb = C_BORDER
    ai1.line.width = Pt(1)

    ai1_tf = ai1.text_frame
    ai1_tf.word_wrap = True
    ai1_tf.margin_left = Inches(0.18)
    ai1_tf.margin_right = Inches(0.18)
    ai1_tf.margin_top = Inches(0.12)
    ai1_tf.margin_bottom = Inches(0.1)

    ap1 = ai1_tf.paragraphs[0]
    ap1.text = "SD 高保真技能突破   [标准 Token 体系]"
    ap1.font.size = Pt(11)
    ap1.font.bold = True
    ap1.font.color.rgb = C_PURPLE

    ap1_stat = ai1_tf.add_paragraph()
    ap1_stat.text = "直出还原率 80% ~ 90%（微调达 90%）"
    ap1_stat.font.size = Pt(10)
    ap1_stat.font.bold = True
    ap1_stat.font.color.rgb = RGBColor(5, 150, 105)
    ap1_stat.space_before = Pt(2)

    ap1_desc = ai1_tf.add_paragraph()
    ap1_desc.text = "• 提取全局视觉样式 Token、基础组件 Token、公用页面模板 Token 等输出 SD 高保真技能，多案例打磨下在基础表单表格页实现高准确度快速直出。"
    ap1_desc.font.size = Pt(9)
    ap1_desc.font.color.rgb = C_BODY
    ap1_desc.space_before = Pt(3)

    # AI Card 2: 统一交付工具链演进 (h = 1.6 in)
    ai2_y = Inches(3.68)
    ai2_h = Inches(1.58)
    ai2 = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, col_right_x, ai2_y, col_right_w, ai2_h)
    ai2.fill.solid()
    ai2.fill.fore_color.rgb = C_CARD_BG
    ai2.line.color.rgb = C_BORDER
    ai2.line.width = Pt(1)

    ai2_tf = ai2.text_frame
    ai2_tf.word_wrap = True
    ai2_tf.margin_left = Inches(0.18)
    ai2_tf.margin_right = Inches(0.18)
    ai2_tf.margin_top = Inches(0.12)
    ai2_tf.margin_bottom = Inches(0.1)

    ap2 = ai2_tf.paragraphs[0]
    ap2.text = "统一交付工具链演进   [协同 UEDC]"
    ap2.font.size = Pt(11)
    ap2.font.bold = True
    ap2.font.color.rgb = C_PURPLE

    ap2_1 = ai2_tf.add_paragraph()
    ap2_1.text = "• 路径演进：探索 Vue+Ant 到 HTML+IDUX、Vue+IDUX 多种实现路径；"
    ap2_1.font.size = Pt(9)
    ap2_1.font.color.rgb = C_BODY
    ap2_1.space_before = Pt(4)

    ap2_2 = ai2_tf.add_paragraph()
    ap2_2.text = "• 协同赋能：辅助 UEDC 进行统建工具调试与整改，已有业务项目基于统一工具交付中；"
    ap2_2.font.size = Pt(9)
    ap2_2.font.color.rgb = C_BODY
    ap2_2.space_before = Pt(3)

    ap2_3 = ai2_tf.add_paragraph()
    ap2_3.text = "• 前沿孵化：输出体验目标量化、检视评估等 MVP 阶段技能。"
    ap2_3.font.size = Pt(9)
    ap2_3.font.color.rgb = C_BODY
    ap2_3.space_before = Pt(3)

    # AI Card 3: 业务规范代码资产沉淀 (h = 1.5 in)
    ai3_y = Inches(5.38)
    ai3_h = Inches(1.52)
    ai3 = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, col_right_x, ai3_y, col_right_w, ai3_h)
    ai3.fill.solid()
    ai3.fill.fore_color.rgb = C_CARD_BG
    ai3.line.color.rgb = C_BORDER
    ai3.line.width = Pt(1)

    ai3_tf = ai3.text_frame
    ai3_tf.word_wrap = True
    ai3_tf.margin_left = Inches(0.18)
    ai3_tf.margin_right = Inches(0.18)
    ai3_tf.margin_top = Inches(0.12)
    ai3_tf.margin_bottom = Inches(0.1)

    ap3 = ai3_tf.paragraphs[0]
    ap3.text = "业务规范代码资产沉淀   [持续提效支撑]"
    ap3.font.size = Pt(11)
    ap3.font.bold = True
    ap3.font.color.rgb = C_PURPLE

    ap3_1 = ai3_tf.add_paragraph()
    ap3_1.text = "• 代码资产库建设：基于多项目 AI Demo 实战，沉淀 SMG、SASE 系列产品业务规范代码资产；"
    ap3_1.font.size = Pt(9)
    ap3_1.font.color.rgb = C_BODY
    ap3_1.space_before = Pt(4)

    ap3_2 = ai3_tf.add_paragraph()
    ap3_2.text = "• 长效复用赋能：从孤立 Demo 走向规范组件库复用，为后续 SMG 版本的 AI Demo 迭代输出形成显著的提效与质量保障。"
    ap3_2.font.size = Pt(9)
    ap3_2.font.color.rgb = C_BODY
    ap3_2.space_before = Pt(3)

    # Footer
    footer = slide.shapes.add_textbox(Inches(0.6), Inches(7.05), Inches(12.133), Inches(0.3))
    ftf = footer.text_frame
    ftf.word_wrap = True
    ftf.margin_left = ftf.margin_right = ftf.margin_top = ftf.margin_bottom = 0
    fp = ftf.paragraphs[0]
    fp.text = "2024 年中总结与复盘  |  聚焦核心体验 · 稳健推进迭代  |  AI 效能工程化实践"
    fp.font.size = Pt(8.5)
    fp.font.color.rgb = C_MUTED

    import os
    output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../slides_output"))
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "midyear_summary_slide.pptx")
    prs.save(output_path)
    print(f"PPTX saved successfully to {output_path}")

if __name__ == "__main__":
    create_deck()
