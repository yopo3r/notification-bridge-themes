# Notification Bridge Themes

Theme files for **Notification Bridge**, organized by their primary appearance:

- `themes/light/`
- `themes/dark/`

Every `.theme` file is import-ready and intentionally contains both a light and dark palette,
because Notification Bridge theme format version 1 requires all seven colors for both appearances.
The folder indicates the variant the file is designed to emphasize.

## Included themes

### Light
- Alucard Light
- Gruvbox Light
- Nord Snow
- Solarized Light
- Tokyo Day
- Turquoise Light

### Dark
- Dracula
- Gruvbox Dark
- Nord Polar Night
- Solarized Dark
- Tokyo Night
- Turquoise Dark

## Install

1. Download an individual `.theme` file.
2. Open Notification Bridge.
3. Go to **Settings -> Theme**.
4. Import the file.
5. Select System, Light, or Dark appearance as desired.

## Theme format

```text
version: 1
name: Example
light.foreground: #RRGGBB
light.background: #RRGGBB
light.highlight: #RRGGBB
light.highlight-foreground: #RRGGBB
light.secondary: #RRGGBB
light.surface: #RRGGBB
light.error: #RRGGBB
dark.foreground: #RRGGBB
dark.background: #RRGGBB
dark.highlight: #RRGGBB
dark.highlight-foreground: #RRGGBB
dark.secondary: #RRGGBB
dark.surface: #RRGGBB
dark.error: #RRGGBB
```

Blank lines and comments beginning with `#` are allowed by the app, but the distributed files
stay minimal for easy inspection.

## Validation

Run:

```bash
python3 scripts/validate_themes.py
```

The validator checks required keys, version, duplicate keys, hex colors, and folder contents.

## Licensing and attribution

The repository's original packaging, documentation, and validation script use the MIT License.
Some palettes are adapted from separately licensed open-source themes. Their names, upstream
projects, licenses, and notices are listed in `THIRD_PARTY_NOTICES.md`. Keep that file when
redistributing the full collection.

Theme names remain associated with their respective upstream projects. This repository is an
independent Notification Bridge port and is not an official upstream distribution.

## Contributing

Pull requests are welcome. New files must:

- use theme format version 1;
- contain all required light and dark keys;
- pass `scripts/validate_themes.py`;
- include upstream attribution and license information when based on another palette;
- be placed according to the intended primary appearance.
