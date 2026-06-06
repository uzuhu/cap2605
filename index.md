---
layout: default
title: 首页
breadcrumb_title: Home
description: 南通华裕电子有限公司 - 专注特规类铝电解电容器研发生产，主营牛角型和螺栓型电解电容
keywords: 铝电解电容, 牛角型电容, 螺栓型电容, Snap-in capacitor, Screw terminal capacitor
---
<section class="home-hero">
  <h1>{{ site.title }}</h1>
  <p class="tagline">
    始建于1987年，专注<span class="highlight">特规类铝电解电容器</span>的研发与生产。
    主营牛角型(Snap-in)和螺栓型(Screw Terminal)电解电容。
  </p>
  <p class="tagline" style="font-size:0.9375rem;color:var(--c-text-light);">定位<span class="highlight">"小而精，专而强"</span>，致力于为中大型设备提供高品质电容解决方案。</p>
</section>

<section class="home-features">
  <div class="feature-card">
    <h3>38年技术沉淀</h3>
    <p>自1987年建厂，深耕铝电解电容领域，积累了丰富的研发与制造经验。</p>
  </div>
  <div class="feature-card">
    <h3>中大型特规定制</h3>
    <p>专注中大型特规类电容，满足各种特殊应用场景的定制化需求。</p>
  </div>
  <div class="feature-card">
    <h3>全系列产品覆盖</h3>
    <p>17大产品系列，电压范围10V~500V，容量覆盖100μF~470,000μF。</p>
  </div>
  <div class="feature-card">
    <h3>快速响应服务</h3>
    <p>技术支持团队快速响应，提供选型指导与应用方案建议。</p>
  </div>
</section>

<section class="home-products">
  <h2>产品系列</h2>

  <h3 style="margin-top:24px;">牛角型 Snap-in Type</h3>
  <div class="product-card-grid">
    {% assign snap_products = "CD292LC,CD293LD,CD294LE,CD295LF,CD296LG,CD297LH,CD298LI,CD17FXFX" | split: "," %}
    {% assign snap_names = "标准品,Low ESR,长寿命,高纹波,大容量,高电压,超高压,特殊品" | split: "," %}
    {% for p in snap_products %}
    {% assign p_slug = p | slice: 0,5 | downcase %}
    {% capture p_url %}/products/snap-in/{{ p_slug }}/{% endcapture %}
    <a href="{{ p_url | relative_url }}" class="product-card">
      <strong>{{ p | slice: 0,5 }}</strong>
      <span>{{ p | slice: 5,2 }}型 - {{ snap_names[forloop.index0] }}</span>
    </a>
    {% endfor %}
  </div>

  <h3 style="margin-top:24px;">螺栓型 Screw Terminal Type</h3>
  <div class="product-card-grid">
    {% assign screw_products = "CD135BP,CD136PK,CD13NGC,CD13NHGE,CD13LGF,CD13HLGG,CD92GA,CD92LGD,CD98SKGK" | split: "," %}
    {% assign screw_names = "标准品,高纹波,标准品,高温品,长寿命,超长寿命,低压大容量,长寿命低压,超级电容" | split: "," %}
    {% for p in screw_products %}
    {% assign p_slug = p | slice: 0,5 | downcase %}
    {% capture p_url %}/products/screw/{{ p_slug }}/{% endcapture %}
    <a href="{{ p_url | relative_url }}" class="product-card">
      <strong>{{ p | slice: 0,5 }}</strong>
      <span>{{ p | slice: 5,2 }}型 - {{ screw_names[forloop.index0] }}</span>
    </a>
    {% endfor %}
  </div>
</section>
