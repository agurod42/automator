# Automator

A collection of macOS Automator services designed to simplify everyday tasks.

## Installation

1. Clone this repository to your macOS Automator Services directory:

   ```sh
   git clone <repository_url> /Users/agurodriguez/Library/Services
   ```

   Ensure the `README.md` file is located at `/Users/agurodriguez/Library/Services/README.md`.

2. The services will now be available in the context menu when you right-click files or within the **Services** section of macOS.

## Services Overview

### Compress PDF

This service reduces the file size of PDFs using Ghostscript.

#### Requirements

Install Ghostscript via Homebrew:

```sh
brew install ghostscript
```

### Convert to PNG

This service converts each page of a PDF into PNG files using ImageMagick and Ghostscript.

#### Requirements

Install ImageMagick and Ghostscript via Homebrew:

```sh
brew install imagemagick ghostscript
```
