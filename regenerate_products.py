#!/usr/bin/env python3
"""
重新生成产品页 - 干净版本
从 PDF 提取内容，生成格式清晰的产品 MD 文件
"""

import pdfplumber
import re
import os

def clean_text(text):
    """清理 PDF 提取的文字粘连"""
    if not text:
        return ""
    # 修复常见的英文粘连
    fixes = [
        (r'([a-z])([A-Z])', r'\1 \2'),  # 小写后面跟大写，加空格
        (r'(\d)([A-Z])', r'\1 \2'),      # 数字后面跟大写，加空格
        (r'([A-Z])([A-Z][a-z])', r'\1 \2'),  # 连续大写后跟小写，加空格
    ]
    for pattern, repl in fixes:
        text = re.sub(pattern, repl, text)
    # 修复特定的粘连词
    glue_fixes = {
        'OperatingTemperature': 'Operating Temperature',
        'RatedVoltage': 'Rated Voltage',
        'NominalCapacitance': 'Nominal Capacitance',
        'LeakageCurrent': 'Leakage Current',
        'DissipationFactor': 'Dissipation Factor',
        'CapacitanceChange': 'Capacitance Change',
        'LoadLife': 'Load Life',
        'ShelfLife': 'Shelf Life',
        'whicheverissmaller': 'whichever is smaller',
        'Aftertest': 'After test',
        'After test:UR': 'After test: UR',
        '24to48hours': '24 to 48 hours',
        'Lessthan': 'Less than',
        'I≤0.01CV': 'I ≤ 0.01CV',
        'I≤0.03CV': 'I ≤ 0.03CV',
        'OperatingTemperatureRange': 'Operating Temperature Range',
        'NominalCapacitance(μF)': 'Nominal Capacitance (μF)',
        'LeakageCurrent(μA)': 'Leakage Current (μA)',
        'DissipationFactor(20℃)': 'Dissipation Factor (20℃)',
    }
    for old, new in glue_fixes.items():
        text = text.replace(old, new)
    return text.strip()

def extract_product_info(pdf_path):
    """从 PDF 提取产品基本信息"""
    info = {
        'series': '',
        'type': '',
        'features': [],
        'specs': {},
        'rating_table': [],  # 额定值表 (Table 3)
        'frequency_table': [],  # 频率系数表
        'dimensions': [],  # 尺寸表
    }
    
    with pdfplumber.open(pdf_path) as pdf:
        # 提取第一页文字（通常包含产品特点）
        first_page_text = pdf.pages[0].extract_text() or ""
        
        # 尝试识别系列名
        series_match = re.search(r'(CD\d+[A-Z]*)', first_page_text)
        if series_match:
            info['series'] = series_match.group(1)
        
        # 提取所有表格
        all_tables = []
        for page in pdf.pages:
            tables = page.extract_tables()
            if tables:
                all_tables.extend(tables)
        
        # 处理表格数据
        for table in all_tables:
            if not table or len(table) < 2:
                continue
            
            # 检查是否是额定值表（有 WV, Cap, Size 等列）
            header_row = [str(c or '').lower() for c in table[0]]
            header_str = ' '.join(header_row)
            
            if 'wv' in header_str or 'rated' in header_str or 'size' in header_str:
                # 这是额定值表
                info['rating_table'] = table
            elif 'frequency' in header_str or '50' in header_str or '120' in header_str:
                # 这是频率系数表
                info['frequency_table'] = table
                
    return info

def generate_clean_product_md(series, pdf_path, output_dir):
    """生成干净的产品 MD 文件"""
    
    # 先尝试从现有 MD 文件读取已丰富的内容
    existing_md = os.path.join(output_dir, 'index.md')
    existing_content = {}
    if os.path.exists(existing_md):
        with open(existing_md, 'r', encoding='utf-8') as f:
            content = f.read()
            # 提取 front matter
            fm_match = re.search(r'^---\n(.*?)\n---', content, re.DOTALL)
            if fm_match:
                fm_text = fm_match.group(1)
                for line in fm_text.split('\n'):
                    if ':' in line:
                        key, val = line.split(':', 1)
                        existing_content[key.strip()] = val.strip()
    
    # 提取 PDF 信息
    info = extract_product_info(pdf_path)
    
    # 确定产品类型
    series_lower = series.lower()
    if 'snap' in output_dir.lower() or series in ['CD292', 'CD293', 'CD294', 'CD295', 'CD296', 'CD297', 'CD298', 'CD17FX']:
        prod_type = 'snap-in'
        type_cn = '牛角型'
        type_en = 'Snap-in'
    else:
        prod_type = 'screw'
        type_cn = '螺栓型'
        type_en = 'Screw Terminal'
    
    # 生成 MD 内容
    md = f"""---
layout: default
title: {series} {type_cn}铝电解电容
breadcrumb_title: {series}
description: {series}系列为华裕电子{type_cn}铝电解电容器，广泛应用于光伏逆变器、UPS、工业电源等领域。
keywords: {series}电容,{type_cn}电解电容,铝电解电容器
series: "{series}"
type: "{prod_type}"
nav_order: 1
---

<div class="product-header">
  <h1>{series} 系列 {type_cn}铝电解电容</h1>
  <p class="product-type">{type_en} Type</p>
  <p class="product-subtitle">{series}系列为华裕电子{type_cn}铝电解电容器，具有优异的电气性能和可靠性，广泛应用于光伏逆变器、UPS、工业电源、变频器等对可靠性要求较高的场合。</p>
</div>

<div class="product-image-placeholder">
  <span class="placeholder-text">{series} series — product photo</span>
  <span class="placeholder-size">建议尺寸: 600×400px, 透明背景 PNG</span>
</div>

<section class="product-content">

## 产品特点

<ul>
  <li><strong>高可靠性</strong> — 严格的品质控制和全流程追溯</li>
  <li><strong>宽温度范围</strong> — 适应各种工作环境</li>
  <li><strong>低 ESR</strong> — 优异的高频特性</li>
  <li><strong>长寿命设计</strong> — 高温下保证长时间可靠工作</li>
</ul>

## 技术规格

<div class="table-responsive">
<table class="spec-table">
  <thead>
    <tr>
      <th>项目 Item</th>
      <th>规格 Specifications</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>使用温度范围 Operating Temperature</td><td>-40~+105℃</td></tr>
    <tr><td>额定电压 Rated Voltage</td><td>详见额定值表</td></tr>
    <tr><td>标称容量 Nominal Capacitance</td><td>详见额定值表</td></tr>
    <tr><td>容量偏差 Tolerance</td><td>±20% (M)</td></tr>
    <tr><td>保证寿命 Load Life</td><td>2000~10000小时</td></tr>
  </tbody>
</table>
</div>

"""

    # 如果有额定值表，添加
    if info['rating_table']:
        md += """
## 额定值表 Rated Values

<div class="table-responsive">
<table class="spec-data-table">
"""
        # 表头
        table = info['rating_table']
        if len(table) > 0:
            md += "  <thead>\n    <tr>\n"
            for cell in table[0]:
                cell_str = str(cell or '').strip()
                md += f"      <th>{cell_str}</th>\n"
            md += "    </tr>\n  </thead>\n  <tbody>\n"
            
            # 数据行（只取前30行，避免过长）
            for row in table[1:31]:
                md += "    <tr>\n"
                for cell in row:
                    cell_str = str(cell or '').strip()
                    md += f"      <td>{cell_str}</td>\n"
                md += "    </tr>\n"
            md += "  </tbody>\n</table>\n</div>\n"
    
    # 如果有频率系数表，添加
    if info['frequency_table']:
        md += """
## 频率系数 Frequency Coefficient

<div class="table-responsive">
<table class="spec-data-table">
"""
        table = info['frequency_table']
        if len(table) > 0:
            md += "  <thead>\n    <tr>\n"
            for cell in table[0]:
                cell_str = str(cell or '').strip()
                md += f"      <th>{cell_str}</th>\n"
            md += "    </tr>\n  </thead>\n  <tbody>\n"
            
            for row in table[1:10]:
                md += "    <tr>\n"
                for cell in row:
                    cell_str = str(cell or '').strip()
                    md += f"      <td>{cell_str}</td>\n"
                md += "    </tr>\n"
            md += "  </tbody>\n</table>\n</div>\n"
    
    # 应用场景和选型指南
    md += """
## 应用场景

本系列电容器凭借其优异的性能参数，广泛应用于以下领域：

<ul>
  <li>光伏逆变器 PV Inverter</li>
  <li>不间断电源 UPS</li>
  <li>工业电源 Industrial Power</li>
  <li>变频器 Inverter</li>
</ul>

## 选型指南

<ol>
  <li><strong>额定电压：</strong>建议工作电压不超过额定电压的80%</li>
  <li><strong>容量选择：</strong>根据实际电路需求选择合适容量</li>
  <li><strong>纹波电流：</strong>流过电容器的纹波电流有效值不应超过额定值</li>
  <li><strong>工作温度：</strong>在低于额定最高温度的环境下使用，可显著延长电容器使用寿命</li>
</ol>

## 相关资源

<ul>
  <li><a href="/technical/guidelines/">使用注意事项</a></li>
  <li><a href="/technical/part-number-system/">型号命名规则</a></li>
  <li><a href="/technical/terminal-dimensions/">端子尺寸图</a></li>
</ul>

</section>
"""
    
    # 写入文件
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, 'index.md')
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(md)
    
    print(f"Generated: {output_path}")
    return output_path

if __name__ == '__main__':
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 处理牛角型
    snap_in_dir = os.path.join(base_dir, 'products', 'snap-in')
    snap_in_pdfs = {
        'CD292': os.path.join(base_dir, 'pdf', 'snap-in', 'CD292.pdf'),
        'CD293': os.path.join(base_dir, 'pdf', 'snap-in', 'CD293.pdf'),
        'CD294': os.path.join(base_dir, 'pdf', 'snap-in', 'CD294.pdf'),
        'CD295': os.path.join(base_dir, 'pdf', 'snap-in', 'CD295.pdf'),
        'CD296': os.path.join(base_dir, 'pdf', 'snap-in', 'CD296.pdf'),
        'CD297': os.path.join(base_dir, 'pdf', 'snap-in', 'CD297.pdf'),
        'CD298': os.path.join(base_dir, 'pdf', 'snap-in', 'CD298.pdf'),
        'CD17FX': os.path.join(base_dir, 'pdf', 'snap-in', 'CD17FX.pdf'),
    }
    
    for series, pdf_path in snap_in_pdfs.items():
        if os.path.exists(pdf_path):
            output_dir = os.path.join(snap_in_dir, series.lower())
            generate_clean_product_md(series, pdf_path, output_dir)
        else:
            print(f"PDF not found: {pdf_path}")
    
    # 处理螺栓型
    screw_dir = os.path.join(base_dir, 'products', 'screw')
    screw_pdfs = {
        'CD135': os.path.join(base_dir, 'pdf', 'screw', 'CD135.pdf'),
        'CD136': os.path.join(base_dir, 'pdf', 'screw', 'CD136.pdf'),
        'CD13N': os.path.join(base_dir, 'pdf', 'screw', 'CD13N.pdf'),
        'CD13NH': os.path.join(base_dir, 'pdf', 'screw', 'CD13NH.pdf'),
        'CD13L': os.path.join(base_dir, 'pdf', 'screw', 'CD13L.pdf'),
        'CD13HL': os.path.join(base_dir, 'pdf', 'screw', 'CD13HL.pdf'),
        'CD92': os.path.join(base_dir, 'pdf', 'screw', 'CD92.pdf'),
        'CD92L': os.path.join(base_dir, 'pdf', 'screw', 'CD92L.pdf'),
        'CD98SK': os.path.join(base_dir, 'pdf', 'screw', 'CD98SK.pdf'),
    }
    
    for series, pdf_path in screw_pdfs.items():
        if os.path.exists(pdf_path):
            output_dir = os.path.join(screw_dir, series.lower().replace('cd', 'cd'))
            # 特殊处理 CD13N -> cd13n
            output_dir = os.path.join(screw_dir, series.lower())
            generate_clean_product_md(series, pdf_path, output_dir)
        else:
            print(f"PDF not found: {pdf_path}")
    
    print("\nDone! All product pages regenerated.")
