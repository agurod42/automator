# Automator

A collection of macOS Automator services designed to simplify everyday tasks.

## Installation

1. Clone this repository to your macOS Automator Services directory:

   ```sh
   git clone <repository_url> $HOME/Library/Services
   ```

   Ensure the `README.md` file is located at `$HOME/Library/Services/README.md`.

2. The services will now be available in the context menu when you right-click files or within the **Services** section of macOS.

## Services Overview

Every service except **Open in VSCode** posts a completion notification via `osascript`. The first time one fires, macOS may prompt you to grant notification permission to **Script Editor** (System Settings → Notifications → Script Editor).

### Compress Image

This service compresses JPEG and PNG images with ImageMagick, writing a new file beside each original with a `_compressed` suffix.

#### Requirements

Install ImageMagick via Homebrew:

```sh
brew install imagemagick
```

### Compress PDF

This service reduces the file size of PDFs using Ghostscript.

#### Requirements

Install Ghostscript via Homebrew:

```sh
brew install ghostscript
```

### Compress Video

This service compresses video files with ffmpeg (H.264 + AAC, CRF 28), writing a new MP4 beside each original with a `_compressed.mp4` suffix.

#### Requirements

Install ffmpeg via Homebrew:

```sh
brew install ffmpeg
```

### Convert to PNG

This service converts each page of a PDF into PNG files using ImageMagick and Ghostscript.

#### Requirements

Install ImageMagick and Ghostscript via Homebrew:

```sh
brew install imagemagick ghostscript
```

### Copy Contents to Clipboard

This service copies the contents of the selected text file(s) to the clipboard. When multiple files are selected, their contents are concatenated in selection order.

### Open in VSCode

This service opens the selected folder (or the parent directory of the selected file) in a new VSCode window via the `code` CLI.

#### Requirements

Install the `code` CLI from within VSCode: open the Command Palette and run **Shell Command: Install 'code' command in PATH**.

### Trim Transparent Pixels

This service trims fully transparent borders from images and saves a new PNG beside the original with a `_trimmed.png` suffix so transparency is preserved.

#### Requirements

Install ImageMagick via Homebrew:

```sh
brew install imagemagick
```

## Development

Regenerate the workflow icon set with:

```sh
python3 scripts/generate_workflow_icons.py
```
