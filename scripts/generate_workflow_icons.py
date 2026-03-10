#!/usr/bin/env python3

from __future__ import annotations

import subprocess
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
ASSETS_DIR = ROOT / "assets" / "workflow-icons"

ICONSET_FILES = [
    ("icon_16x16.png", 16),
    ("icon_16x16@2x.png", 32),
    ("icon_32x32.png", 32),
    ("icon_32x32@2x.png", 64),
    ("icon_128x128.png", 128),
    ("icon_128x128@2x.png", 256),
    ("icon_256x256.png", 256),
    ("icon_256x256@2x.png", 512),
    ("icon_512x512.png", 512),
    ("icon_512x512@2x.png", 1024),
]

WORKFLOWS = [
    {
        "slug": "compress-image",
        "bundle": "Compress Image.workflow",
        "primary": "#8AF2AA",
        "secondary": "#129168",
        "glow": "#D9FFE5",
        "ink": "#0E4B3A",
        "kind": "compress_image",
    },
    {
        "slug": "compress-pdf",
        "bundle": "Compress PDF.workflow",
        "primary": "#FFB28F",
        "secondary": "#E64B4B",
        "glow": "#FFE0D2",
        "ink": "#7B1E2F",
        "kind": "compress_pdf",
    },
    {
        "slug": "convert-to-png",
        "bundle": "Convert to PNG.workflow",
        "primary": "#88DBFF",
        "secondary": "#2968F0",
        "glow": "#D8F2FF",
        "ink": "#173D7A",
        "kind": "convert_png",
    },
    {
        "slug": "open-in-vscode",
        "bundle": "Open in VSCode.workflow",
        "primary": "#72DDFF",
        "secondary": "#2B57F6",
        "glow": "#D8F1FF",
        "ink": "#17356E",
        "kind": "open_code",
    },
    {
        "slug": "trim-transparent-pixels",
        "bundle": "Trim Transparent Pixels.workflow",
        "primary": "#C0D7FF",
        "secondary": "#7A6AFF",
        "glow": "#E8EDFF",
        "ink": "#40379D",
        "kind": "trim_transparency",
    },
]


def run(*args: str) -> None:
    subprocess.run(args, check=True)


def ensure_directories() -> None:
    ASSETS_DIR.mkdir(parents=True, exist_ok=True)
    for workflow in WORKFLOWS:
        bundle_root = ROOT / workflow["bundle"] / "Contents"
        (bundle_root / "QuickLook").mkdir(parents=True, exist_ok=True)
        (bundle_root / "Resources").mkdir(parents=True, exist_ok=True)


def backdrop_svg(primary: str, secondary: str, glow: str, symbol_svg: str) -> str:
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="1024" height="1024" viewBox="0 0 1024 1024" fill="none">
  <defs>
    <linearGradient id="bg" x1="164" y1="124" x2="882" y2="910" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="{primary}"/>
      <stop offset="100%" stop-color="{secondary}"/>
    </linearGradient>
    <radialGradient id="orb" cx="0" cy="0" r="1" gradientUnits="userSpaceOnUse" gradientTransform="translate(276 220) rotate(39) scale(488 442)">
      <stop offset="0%" stop-color="{glow}" stop-opacity="0.96"/>
      <stop offset="100%" stop-color="{glow}" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="glass" x1="252" y1="190" x2="794" y2="860" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#FFFFFF" stop-opacity="0.34"/>
      <stop offset="100%" stop-color="#FFFFFF" stop-opacity="0.09"/>
    </linearGradient>
    <linearGradient id="surface" x1="272" y1="246" x2="728" y2="784" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#FFFFFF"/>
      <stop offset="100%" stop-color="#E7F0FF"/>
    </linearGradient>
    <linearGradient id="surfaceShade" x1="384" y1="290" x2="684" y2="764" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#FFFFFF" stop-opacity="0"/>
      <stop offset="100%" stop-color="#B9C9E3" stop-opacity="0.55"/>
    </linearGradient>
    <filter id="baseShadow" x="24" y="24" width="976" height="976" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
      <feDropShadow dx="0" dy="22" stdDeviation="26" flood-color="#14243B" flood-opacity="0.18"/>
    </filter>
    <filter id="objectShadow" x="120" y="120" width="784" height="784" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
      <feDropShadow dx="0" dy="16" stdDeviation="18" flood-color="#11243F" flood-opacity="0.18"/>
    </filter>
    <clipPath id="iconClip">
      <rect x="80" y="80" width="864" height="864" rx="216"/>
    </clipPath>
  </defs>
  <g filter="url(#baseShadow)">
    <rect x="80" y="80" width="864" height="864" rx="216" fill="url(#bg)"/>
    <rect x="98" y="98" width="828" height="828" rx="198" stroke="#FFFFFF" stroke-opacity="0.34" stroke-width="12"/>
  </g>
  <g clip-path="url(#iconClip)">
    <circle cx="308" cy="246" r="300" fill="url(#orb)"/>
    <ellipse cx="762" cy="856" rx="312" ry="174" fill="#0A1730" fill-opacity="0.08"/>
    <path d="M136 168C246 116 414 92 596 112C738 128 832 164 892 210V342C796 294 646 266 484 266C328 266 198 292 136 326V168Z" fill="#FFFFFF" fill-opacity="0.16"/>
    <rect x="184" y="184" width="656" height="656" rx="176" fill="url(#glass)"/>
    <rect x="184" y="184" width="656" height="656" rx="176" stroke="#FFFFFF" stroke-opacity="0.22" stroke-width="10"/>
  </g>
  {symbol_svg}
</svg>
"""


def paper_group(ink: str, extra: str = "", transform: str = "") -> str:
    transform_attr = f' transform="{transform}"' if transform else ""
    return f"""
  <g filter="url(#objectShadow)"{transform_attr}>
    <path d="M304 248H560L714 402V704C714 744 682 776 642 776H304C264 776 232 744 232 704V320C232 280 264 248 304 248Z" fill="url(#surface)"/>
    <path d="M560 248V358C560 390 586 416 618 416H714" fill="#F4F8FF"/>
    <path d="M560 248V358C560 390 586 416 618 416H714" stroke="#D8E4F6" stroke-width="18" stroke-linejoin="round"/>
    <path d="M304 248H560L714 402V704C714 744 682 776 642 776H304C264 776 232 744 232 704V320C232 280 264 248 304 248Z" stroke="#FFFFFF" stroke-width="12"/>
    <path d="M320 330H484" stroke="{ink}" stroke-opacity="0.12" stroke-width="22" stroke-linecap="round"/>
    <path d="M320 382H512" stroke="{ink}" stroke-opacity="0.12" stroke-width="22" stroke-linecap="round"/>
    <path d="M320 434H468" stroke="{ink}" stroke-opacity="0.12" stroke-width="22" stroke-linecap="round"/>
    <rect x="232" y="248" width="482" height="528" rx="72" fill="url(#surfaceShade)"/>
    {extra}
  </g>
"""


def image_group(accent: str, ink: str, extra: str = "", transform: str = "") -> str:
    transform_attr = f' transform="{transform}"' if transform else ""
    return f"""
  <g filter="url(#objectShadow)"{transform_attr}>
    <rect x="246" y="298" width="532" height="428" rx="104" fill="url(#surface)"/>
    <rect x="246" y="298" width="532" height="428" rx="104" stroke="#FFFFFF" stroke-width="12"/>
    <circle cx="630" cy="420" r="44" fill="{accent}" fill-opacity="0.64"/>
    <path d="M318 618L430 488L528 572L632 446L706 618H318Z" fill="{accent}" fill-opacity="0.88"/>
    <path d="M318 618L430 488L528 572L632 446L706 618" stroke="{ink}" stroke-opacity="0.18" stroke-width="18" stroke-linejoin="round"/>
    <rect x="246" y="298" width="532" height="428" rx="104" fill="url(#surfaceShade)"/>
    {extra}
  </g>
"""


def folder_group(accent: str, ink: str) -> str:
    return f"""
  <g filter="url(#objectShadow)">
    <path d="M252 398C252 354 288 318 332 318H470C494 318 516 328 532 348L570 394H692C740 394 778 432 778 480V668C778 728 730 776 670 776H354C294 776 246 728 246 668V474C246 432 280 398 322 398H252Z" fill="url(#surface)"/>
    <path d="M252 398H690C738 398 778 436 778 484V668C778 728 730 776 670 776H354C294 776 246 728 246 668V474C246 432 280 398 322 398H252Z" fill="url(#surfaceShade)"/>
    <path d="M252 398C252 354 288 318 332 318H470C494 318 516 328 532 348L570 394H692C740 394 778 432 778 480V668C778 728 730 776 670 776H354C294 776 246 728 246 668V474C246 432 280 398 322 398H692" stroke="#FFFFFF" stroke-width="12" stroke-linejoin="round"/>
    <rect x="284" y="438" width="456" height="266" rx="74" fill="{accent}" fill-opacity="0.18"/>
    <path d="M436 486L360 572L436 652" stroke="{ink}" stroke-width="34" stroke-linecap="round" stroke-linejoin="round"/>
    <path d="M590 486L666 572L590 652" stroke="{ink}" stroke-width="34" stroke-linecap="round" stroke-linejoin="round"/>
    <path d="M494 472L456 672" stroke="{ink}" stroke-width="28" stroke-linecap="round"/>
  </g>
"""


def inward_side_arrows(ink: str) -> str:
    return f"""
  <g filter="url(#objectShadow)">
    <path d="M186 512H286" stroke="{ink}" stroke-width="32" stroke-linecap="round"/>
    <path d="M248 468L292 512L248 556" stroke="{ink}" stroke-width="32" stroke-linecap="round" stroke-linejoin="round"/>
    <path d="M838 512H738" stroke="{ink}" stroke-width="32" stroke-linecap="round"/>
    <path d="M776 468L732 512L776 556" stroke="{ink}" stroke-width="32" stroke-linecap="round" stroke-linejoin="round"/>
  </g>
"""


def convert_symbol(accent: str, ink: str) -> str:
    picture_badge = f"""
      <g filter="url(#objectShadow)" transform="translate(454 470)">
        <rect x="0" y="0" width="320" height="232" rx="72" fill="url(#surface)"/>
        <rect x="0" y="0" width="320" height="232" rx="72" stroke="#FFFFFF" stroke-width="10"/>
        <circle cx="232" cy="62" r="26" fill="{accent}" fill-opacity="0.64"/>
        <path d="M38 194L116 108L172 162L232 100L286 194H38Z" fill="{accent}" fill-opacity="0.88"/>
        <path d="M38 194L116 108L172 162L232 100L286 194" stroke="{ink}" stroke-opacity="0.18" stroke-width="12" stroke-linejoin="round"/>
        <rect x="0" y="0" width="320" height="232" rx="72" fill="url(#surfaceShade)"/>
      </g>
    """
    arrow = f"""
      <g filter="url(#objectShadow)">
        <path d="M450 470C488 420 558 404 618 420" stroke="{ink}" stroke-width="26" stroke-linecap="round"/>
        <path d="M592 382L636 422L584 450" fill="none" stroke="{ink}" stroke-width="26" stroke-linecap="round" stroke-linejoin="round"/>
      </g>
    """
    return paper_group(ink, extra="", transform="rotate(-7 472 512)") + picture_badge + arrow


def compress_image_symbol(accent: str, ink: str) -> str:
    badge = f"""
      <g filter="url(#objectShadow)">
        <rect x="320" y="338" width="384" height="128" rx="64" fill="#FFFFFF" fill-opacity="0.24"/>
      </g>
    """
    return image_group(accent, ink, extra=badge) + inward_side_arrows(ink)


def compress_pdf_symbol(accent: str, ink: str) -> str:
    badge = f"""
      <rect x="322" y="548" width="302" height="96" rx="48" fill="{accent}" fill-opacity="0.20"/>
      <path d="M356 596H588" stroke="{ink}" stroke-opacity="0.18" stroke-width="18" stroke-linecap="round"/>
    """
    return paper_group(ink, extra=badge) + inward_side_arrows(ink)


def open_code_symbol(accent: str, ink: str) -> str:
    return folder_group(accent, ink)


def trim_transparency_symbol(accent: str, ink: str) -> str:
    squares = []
    size = 76
    start_x = 342
    start_y = 342
    for row in range(4):
        for col in range(4):
            fill = "#FFFFFF" if (row + col) % 2 == 0 else accent
            opacity = "0.96" if (row + col) % 2 == 0 else "0.30"
            x = start_x + col * size
            y = start_y + row * size
            squares.append(
                f'<rect x="{x}" y="{y}" width="{size}" height="{size}" fill="{fill}" fill-opacity="{opacity}"/>'
            )
    checkerboard = "".join(squares)
    return f"""
  <g filter="url(#objectShadow)">
    <rect x="304" y="304" width="416" height="416" rx="104" fill="url(#surface)"/>
    <rect x="304" y="304" width="416" height="416" rx="104" stroke="#FFFFFF" stroke-width="12"/>
    <g clip-path="url(#trimGrid)">
      {checkerboard}
    </g>
    <rect x="304" y="304" width="416" height="416" rx="104" fill="url(#surfaceShade)"/>
    <path d="M292 430V330C292 308 310 290 332 290H432" stroke="{ink}" stroke-width="30" stroke-linecap="round" stroke-linejoin="round"/>
    <path d="M732 430V330C732 308 714 290 692 290H592" stroke="{ink}" stroke-width="30" stroke-linecap="round" stroke-linejoin="round"/>
    <path d="M292 594V694C292 716 310 734 332 734H432" stroke="{ink}" stroke-width="30" stroke-linecap="round" stroke-linejoin="round"/>
    <path d="M732 594V694C732 716 714 734 692 734H592" stroke="{ink}" stroke-width="30" stroke-linecap="round" stroke-linejoin="round"/>
    <path d="M650 290L736 204" stroke="{ink}" stroke-opacity="0.28" stroke-width="24" stroke-linecap="round"/>
  </g>
"""


def build_svg(workflow: dict[str, str]) -> str:
    accent = workflow["primary"]
    ink = workflow["ink"]
    symbol = {
        "compress_image": compress_image_symbol,
        "compress_pdf": compress_pdf_symbol,
        "convert_png": convert_symbol,
        "open_code": open_code_symbol,
        "trim_transparency": trim_transparency_symbol,
    }[workflow["kind"]](accent, ink)

    svg = backdrop_svg(workflow["primary"], workflow["secondary"], workflow["glow"], symbol)
    trim_clip = """
    <clipPath id="trimGrid">
      <rect x="332" y="332" width="360" height="360" rx="84"/>
    </clipPath>
"""
    return svg.replace("</defs>", trim_clip + "\n  </defs>", 1)


def render_master_png(svg_path: Path, destination: Path) -> None:
    run(
        "magick",
        "-background",
        "none",
        "-density",
        "384",
        str(svg_path),
        "PNG32:" + str(destination),
    )


def resize_png(source: Path, destination: Path, size: int) -> None:
    run(
        "magick",
        str(source),
        "-resize",
        f"{size}x{size}",
        str(destination),
    )


def generate_icons() -> None:
    ensure_directories()

    for workflow in WORKFLOWS:
        bundle_root = ROOT / workflow["bundle"] / "Contents"
        svg_path = ASSETS_DIR / f"{workflow['slug']}.svg"
        master_png_path = ASSETS_DIR / f"{workflow['slug']}.png"
        svg_path.write_text(build_svg(workflow), encoding="utf-8")
        render_master_png(svg_path, master_png_path)

        thumbnail_path = bundle_root / "QuickLook" / "Thumbnail.png"
        resize_png(master_png_path, thumbnail_path, 512)

        with tempfile.TemporaryDirectory() as tmpdir:
            iconset_dir = Path(tmpdir) / "WorkflowIcon.iconset"
            iconset_dir.mkdir(parents=True, exist_ok=True)
            for filename, size in ICONSET_FILES:
                resize_png(master_png_path, iconset_dir / filename, size)

            run(
                "iconutil",
                "-c",
                "icns",
                str(iconset_dir),
                "-o",
                str(bundle_root / "Resources" / "WorkflowIcon.icns"),
            )


if __name__ == "__main__":
    generate_icons()
