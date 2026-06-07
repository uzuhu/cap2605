---
layout: default
title: 使用注意事项
breadcrumb_title: Guidelines for Using
description: 铝电解电容使用注意事项 — Guidelines for Using
nav_order: 2
---

# 使用注意事项 Guidelines for Using

为使您获得电解电容器的最佳性能和延长电解电容器的使用寿命，在使用电解电容器前，请务必阅读本注意事项。

## 1. 极性确认 DC electrolytic capacitors are polarized.

确定极性，极性标志在电容器的基体上。以免因极性反可能引起电路短路或电容器损坏，当极性不固定或不确定的，使用双极性电容器。**注意直流电解电容器不能使用于交流。**

## 2. 双极性电容器 Bipolar capacitors

只适用于脉动电路和极性反转电路中，**不适用于纯交流和高纹波电路中**。

## 3. 使用电压 DO NOT apply voltage greater than rated voltage.

使用电压大于额定电压，漏电流会增大，可能损坏电容器。**建议工作电压为额定电压的70%~80%**，电容器在建议的工作电压下使用可延长电容器的寿命。

## 4. 纹波电流 DO NOT allow excessive ripple current.

流过电容器的纹波电流超过许可值，将会引起电容器发热，电容量减少，损害电容器。通过电容器的纹波电流**一般不超过额定值的80%**。

## 5. 快速充放电 Use especially designed capacitors.

在经受快速的周期性充放电电路中，电容器可能受损害，它的寿命因容量下降、温升等原因而缩短。**在这种电路中，一定要使用专门设计的电容器**。

## 6. 工作温度范围 Operating temperature range.

电容器的特性随工作温度而变化：
- **高温** → 容量、漏电流增大，tgδ减少
- **低温** → 容量和漏电流下降，tgδ增大

电容器在较低的温度下使用会确保延长寿命。

## 7. 使用温度与寿命 Relationship between temperature and life.

电容器的寿命与其使用的温度有关，**使用温度每降低10℃，其寿命是额定温度下的2倍**。

计算公式：

<div class="formula-block">
  <code>L₂ = L₁ × 2^((T₁ − T₂) / 10)</code>
</div>

| 变量 | 含义 |
|------|------|
| L₁ | 额定温度下的寿命 |
| L₂ | 实际温度下的寿命 |
| T₁ | 额定使用温度 (°C) |
| T₂ | 实际使用温度 (°C) |

## 8. 核对工作频率 Check operating frequency.

电解电容器的电容量通常是在100Hz或120Hz下测得的。容量随频率的升高而下降，tgδ随频率的升高而增大。

## 9. 长时间存放后的处理 Apply rated DC voltage treatment.

长时间存放后的电容器处理：**首先逐渐施加直流电压至额定电压，然后再使用**。

## 10. 电容器外壳绝缘 The capacitor case is not insulated.

电容器的外壳与阴极端是通过电解液连接的。如果电容器的外壳必须与线路绝缘，则在电容器的安装位置处，**一定要采取绝缘措施**。

## 11. 端子和引线 DO NOT apply excessive force.

过大的力施加到端子或引线上，可能引起引线的断裂或端子分裂，进而引起内部连接的破坏。

## 12. 线路板清洗 Cleaning of the circuit board.

**禁止**使用卤化物或类似溶剂（如三氯乙烯、二甲苯、酮类等）清洗电容器。

**推荐清洗溶剂**：甲醇、异丙醇、乙醇、异丁醇、石油醚、丙醇和一般的洗涤剂。

## 13. 焊接注意事项 Be cautious of the temperature and duration.

- 烙铁应与电容器的塑料绝缘套管保持一定的距离
- 浸焊时：**温度260℃以内，时间不超过10秒**

## 14. 印刷线路板上孔的布局 Hole positions.

设计印刷线路板时，安装孔距应等于引线间距。当孔距大于或小于引线间距时，安装电容器时将有应力作用到引线上，可能引起短路、电路损坏、漏电流增大。
