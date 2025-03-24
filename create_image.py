from PIL import Image

# 1x1の透明なPNGを作成
img = Image.new("RGBA", (1, 1), (0, 0, 0, 0))
img.save("beacon.png")
