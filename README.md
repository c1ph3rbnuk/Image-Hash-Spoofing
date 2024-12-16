# Image-Hash-Spoofing
This tool takes an image and an arbitray hexstring and outputs an adjusted file that displays identically to the human eye but has a SHA1 hash that begins with the given hexstring.

## Usage
`python3 spoof.py 0x2e original.png altered.png`

## Background
Hash functions are cryptographic algorithms that take an input file,text or data and map it to a fixed-length hexstring called digest(or a hash).

Some of the properties of a hash include:
* Determinism - the same input always produces the same hash
* Avalanche effect - a small change is the input produces a vastly difefrent hash

`c1ph3rbnuk@DESKTOP-D97OINA:$ echo "Let's hash this text" | sha1sum 
11c2b22fbc012e6b7b4630b16904f2ec7acdfd78`

`c1ph3rbnuk@DESKTOP-D97OINA:$ echo "Let's hash this text." | sha1sum 
c92ed79b4d0f811e990de0272f2223e3627a2888`

* One way(Irreversibility) - it is computational infeasible to reconstruct the original input from its hash.


## Approach
The goal is to manipulate an image without affecting it's visual appearance while achieving a hash that starts with a specific prefix.

1. **Understanding PNG Structure**: In order to achieve that, we need to start by understanding how images are formated. I chose the PNG formart because it has a clear and simple structure. PNG files consist of a series of chunks which convey different information about the image. A header chunk that identifies the file as an image, other critical chunks like IHDR, that contain image properties like width, depth, and color, IDAT that holds the actual image and IEND that marks the end of the PNG file and optional chuks that holds information such as the metadata of the image file.
2. **Appending Bytes**: Since the IEND chunk marks the end of an image data, any data added after this chunk is ignored by the image decoders. We could take advantage of that and keep appending random bytes after the IEND chunk while recalculating the hash to check if it meets the desired prefix. This prevents us from interefing with critical image information that could corrupt its visual appearance while achieving our objective.


## Challenges and How they were adressed.
- **Ensuring FIle Integrity**: The biggest challenge was modifying the file without corrupting it or making it unreadable by image viewers. **The tools addresses this by adding extra bytes after the IEND chunk which is outside the critical content of the file.**