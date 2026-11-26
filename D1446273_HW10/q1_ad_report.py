# 學號：D1446273


def ad_report(impressions, clicks, target=3.0):
    """計算點擊率 (CTR) 與是否達標，回傳 (ctr, passed)。"""
    if impressions == 0:
        return (None, False)
    if clicks == 0:
        ctr = 0.0
    else:
        ctr = (clicks / impressions) * 100
    passed = ctr >= target
    return (ctr, passed)


if __name__ == "__main__":
    student_id = input("請輸入完整學號：").strip().upper()
    tail = student_id[-3:]
    a = int(student_id[-3])
    b = int(student_id[-2])
    c = int(student_id[-1])
    s = a + b + c

    target = 2.5 + 0.1 * c
    ads = [
        ("主視覺", 800 + 100 * a, 25 + 3 * b),
        ("限時優惠", 1200 + 100 * b, 40 + 4 * c),
        ("再行銷", 600 + 100 * c, 20 + 2 * a),
    ]

    print(f"學號：{student_id}（末三碼：{tail}，a={a}, b={b}, c={c}, s={s}）")
    print(f"達標門檻 CTR：{target:.2f}%")

    passed_count = 0
    for name, imp, clk in ads:
        ctr, passed = ad_report(imp, clk, target=target)
        if passed:
            passed_count += 1
        status = "達標" if passed else "未達標"
        ctr_text = "無曝光" if ctr is None else f"{ctr:.2f}%"
        print(f"- {name}：曝光 {imp}、點擊 {clk}、CTR {ctr_text}、{status}")

    print(f"達標廣告數：{passed_count} / {len(ads)}")

    # 邊界測試
    print("測試 ad_report(1000, 30)：", ad_report(1000, 30))
    print("測試 ad_report(1000, 0)：", ad_report(1000, 0))
