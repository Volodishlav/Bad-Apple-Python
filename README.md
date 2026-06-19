# Bad Apple Python

This project reproduces the [Bad Apple!!](https://youtu.be/FtutLA63Cp8?si=_QNjj4ybEjiaY_qa) video in your terminal using Python, with all graphics rendered in ASCII art.

## Requirements

- Python 3.13.x: [Python Downloads](https://www.python.org/downloads/)
- Pygame. If you don't have pygame installed:

1.- Create a virtual enviroment:
```bash
python3.13 -m venv .venv
source .venv/bin/activate
```

2.- Install pygame
```bash
pip install pygame
```

## Usage Instructions

1.- Clone the repository:
```bash
git clone https://github.com/Volodishlav/Bad-Apple-Python
```

2.- Navigate to the project directory:
```bash
cd Bad-Apple-Python
```

3.- Run the script:
```bash
py -3.13 main.py
```

## Parameters

You can change **line 61** to asjust the volume of the song:
```python
pygame.mixer.music.set_volume(0.25)  # 25%
```

## Credits

The assets are not mine. Special thanks to [FelipeFMA](https://github.com/FelipeFMA/BadAppleBash) and [Trung-Kieen](https://github.com/Trung-Kieen/bad-apple-ascii) for the ASCII art.
