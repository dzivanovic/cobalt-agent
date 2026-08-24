"""Daily Report Card PDF builder — SMB template layout, landscape A4."""
import base64
import io

from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.colors import HexColor, white, black
from reportlab.lib.units import mm
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas

NAVY = HexColor("#1e2153")
GREY = HexColor("#efefef")
DGREY = HexColor("#555555")
PURPLE = HexColor("#4a3c8c")

PAGE_W, PAGE_H = landscape(A4)
M = 12 * mm  # margin


def _img_from_b64(data_url: str):
    """data:image/png;base64,... → ImageReader or None."""
    if not data_url:
        return None
    try:
        b64 = data_url.split(",", 1)[-1]
        return ImageReader(io.BytesIO(base64.b64decode(b64)))
    except Exception:
        return None


def _box(c, x, y, w, h, label=None, fill=GREY):
    c.setFillColor(fill)
    c.rect(x, y, w, h, stroke=0, fill=1)
    if label:
        c.setFillColor(PURPLE)
        c.setFont("Helvetica-BoldOblique", 7.5)
        c.drawString(x + 2 * mm, y + h - 4.5 * mm, label)


def _wrap_text(c, text, x, y, w, font="Helvetica", size=8, leading=10, color=black):
    """Simple word-wrap inside width w, drawing downward from y."""
    c.setFont(font, size)
    c.setFillColor(color)
    for raw_line in (text or "").split("\n"):
        words = raw_line.split(" ")
        line = ""
        for word in words:
            test = (line + " " + word).strip()
            if c.stringWidth(test, font, size) <= w:
                line = test
            else:
                c.drawString(x, y, line)
                y -= leading
                line = word
        c.drawString(x, y, line)
        y -= leading
    return y


def build_drc_pdf(data: dict) -> bytes:
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=landscape(A4))

    # ── Header bar ────────────────────────────────────────────────
    c.setFillColor(NAVY)
    c.rect(0, PAGE_H - 22 * mm, PAGE_W, 22 * mm, stroke=0, fill=1)
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 20)
    c.drawString(M, PAGE_H - 15 * mm, "DAILY REPORT CARD")

    y = PAGE_H - 30 * mm

    # ── Date / Grade ──────────────────────────────────────────────
    half = (PAGE_W - 2 * M - 4 * mm) / 2
    _box(c, M, y - 8 * mm, half, 8 * mm)
    _box(c, M + half + 4 * mm, y - 8 * mm, half, 8 * mm)
    c.setFillColor(black)
    c.setFont("Helvetica-Bold", 9)
    c.drawString(M + 2 * mm, y - 5.5 * mm, "DATE:  " + (data.get("date") or ""))
    c.drawString(M + half + 6 * mm, y - 5.5 * mm, "GRADE:  " + (data.get("grade") or ""))

    # ── Goal ──────────────────────────────────────────────────────
    y -= 12 * mm
    _box(c, M, y - 14 * mm, PAGE_W - 2 * M, 14 * mm)
    c.setFillColor(black)
    c.setFont("Helvetica-Bold", 8.5)
    c.drawString(M + 2 * mm, y - 4.5 * mm, "GOAL:")
    _wrap_text(c, data.get("goal") or "", M + 2 * mm, y - 9 * mm,
               PAGE_W - 2 * M - 4 * mm, size=8.5)

    # ── Reminders / aphorisms row ─────────────────────────────────
    y -= 18 * mm
    reminders = [r.strip() for r in (data.get("reminders") or "").split("\n") if r.strip()]
    if reminders:
        c.setFillColor(PURPLE)
        c.setFont("Helvetica-Bold", 7.5)
        col_w = (PAGE_W - 2 * M) / 3
        for i, rem in enumerate(reminders[:6]):
            cx = M + (i % 3) * col_w
            cy = y - (i // 3) * 4.5 * mm
            txt = "\u2713 " + rem
            while c.stringWidth(txt, "Helvetica-Bold", 7.5) > col_w - 4 * mm and len(txt) > 5:
                txt = txt[:-1]
            c.drawString(cx, cy, txt)
        y -= ((min(len(reminders), 6) - 1) // 3) * 4.5 * mm + 4 * mm

    # ── Segments table ────────────────────────────────────────────
    y -= 4 * mm
    headers = ["Segment", "Grade", "PTD Only", "Sizing", "In My Favor", "Comments"]
    widths = [0.10, 0.08, 0.16, 0.14, 0.16, 0.36]
    widths = [w * (PAGE_W - 2 * M) for w in widths]
    row_h = 9 * mm

    x = M
    c.setFillColor(NAVY)
    c.rect(M, y - row_h, PAGE_W - 2 * M, row_h, stroke=0, fill=1)
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 8.5)
    for htxt, wcol in zip(headers, widths):
        c.drawString(x + 2 * mm, y - row_h + 3 * mm, htxt)
        x += wcol

    segments = data.get("segments") or []
    seg_names = ["Temp", "9:30-11", "11-12", "12-2", "2-4"]
    for i, name in enumerate(seg_names):
        y -= row_h
        seg = segments[i] if i < len(segments) else {}
        c.setFillColor(GREY if i % 2 == 0 else white)
        c.rect(M, y - row_h, PAGE_W - 2 * M, row_h, stroke=0, fill=1)
        x = M
        vals = [name, seg.get("grade", ""), seg.get("ptd", ""), seg.get("sizing", ""),
                seg.get("favor", ""), seg.get("comments", "")]
        c.setFillColor(black)
        for j, (val, wcol) in enumerate(zip(vals, widths)):
            c.setFont("Helvetica-Bold" if j == 0 else "Helvetica", 8)
            txt = str(val)
            while c.stringWidth(txt, "Helvetica", 8) > wcol - 4 * mm and len(txt) > 3:
                txt = txt[:-1]
            c.drawString(x + 2 * mm, y - row_h + 3 * mm, txt)
            x += wcol

    # ── Bottom row: 6 boxes ───────────────────────────────────────
    y -= row_h + 6 * mm
    box_h = y - M - 8 * mm
    gap = 3 * mm
    bw = (PAGE_W - 2 * M - 5 * gap) / 6
    labels = ["What I learned / improved upon today:", "Changes I need to make from today:", "Overview:", "Easiest $50k:"]
    texts = [data.get("learned"), data.get("changes"), data.get("overview"), data.get("easiest")]

    for i, (lab, txt) in enumerate(zip(labels, texts)):
        bx = M + i * (bw + gap)
        _box(c, bx, M + 8 * mm, bw, box_h, label=lab)
        _wrap_text(c, txt or "", bx + 2 * mm, M + 8 * mm + box_h - 9 * mm,
                   bw - 4 * mm, size=7.5, leading=9)

    # Ticker boxes with chart image
    tickers = data.get("tickers") or []
    for i in range(2):
        t = tickers[i] if i < len(tickers) else {}
        bx = M + (4 + i) * (bw + gap)
        label = f"Ticker: {t.get('ticker','')}  {t.get('pnl','')}".strip()
        _box(c, bx, M + 8 * mm, bw, box_h, label=label or "Ticker: +/-$")
        ty = _wrap_text(c, t.get("writeup") or "", bx + 2 * mm,
                        M + 8 * mm + box_h - 9 * mm, bw - 4 * mm, size=7.5, leading=9)
        img = _img_from_b64(t.get("chart"))
        if img:
            iw, ih = img.getSize()
            max_w, max_h = bw - 4 * mm, max(10 * mm, ty - (M + 10 * mm))
            scale = min(max_w / iw, max_h / ih)
            c.drawImage(img, bx + 2 * mm, M + 10 * mm,
                        iw * scale, ih * scale, preserveAspectRatio=True, mask="auto")

    # ── Footer ────────────────────────────────────────────────────
    c.setFillColor(DGREY)
    c.setFont("Helvetica", 7)
    c.drawCentredString(PAGE_W / 2, M / 2 + 2 * mm,
                        "TRADE REPORTER — DAILY REPORT CARD (SMB format)")

    c.showPage()
    c.save()
    return buf.getvalue()
