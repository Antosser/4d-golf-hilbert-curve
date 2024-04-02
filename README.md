# 4D Golf Hilbert's Curve Track
The code in this repository was used to generate the 24x24 and 8x8x8 Hilbert's Curve maps for the [4D Golf](https://store.steampowered.com/app/2147950/4D_Golf/) game

## Links to maps
### Flat
- [Discord Post](https://discord.com/channels/731857424805527633/1224319434093498479)
- [Steam Workshop](https://steamcommunity.com/sharedfiles/filedetails/?id=3208859834)

### 3D curve in 4D space
- [Discord Post](https://discord.com/channels/731857424805527633/1224818080060805221)
- [Steam Workshop](https://steamcommunity.com/sharedfiles/filedetails/?id=3210437890)

## Generate your own
**Numpy has to be installed**

### 2D
```bash
python3 2d.py {width} {height}
```
Width and height must be divisible by 2

### 3D
```bash
python3 3d.py {width} {height} {depth}
```
Width, height, and depth must be divisible by 2
