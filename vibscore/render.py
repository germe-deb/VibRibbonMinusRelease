from PIL import Image

scorevals = (
    [0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [8, 7, 6, 5, 4, 3, 2],
    [36, 28, 21, 15, 10, 6, 3],
    [120, 84, 56, 35, 20, 10, 4],
    [330, 210, 126, 70, 35, 15, 5],
    [792, 462, 252, 126, 56, 21, 6],
    [1716, 924, 462, 210, 84, 28, 7],
    [3432, 1716, 792, 330, 120, 36, 8],
    [6435, 3003, 1287, 495, 165, 45, 9],
    [11440, 5005, 2002, 715, 220, 55, 10],
    [19448, 8008, 3003, 1001, 286, 66, 11],
    [31824, 12376, 4368, 1365, 364, 78, 12],
    [50388, 18564, 6188, 1820, 455, 91, 13],
    [77520, 27132, 8568, 2380, 560, 105, 14],
    [116280, 38760, 11628, 3060, 680, 120, 15],
    [170544, 54264, 15504, 3876, 816, 136, 16],
    [245157, 74613, 20349, 4845, 969, 153, 17],
    [346104, 100947, 26334, 5985, 1140, 171, 18],
    [480700, 134596, 33649, 7315, 1330, 190, 19],
    [657800, 177100, 42504, 8855, 1540, 210, 20]
)


def calculate(num):
    global scorevals
    curval = num
    res = ""
    for place in range(0, 7):
        for compval in reversed(range(0,len(scorevals))):
            if curval < scorevals[compval][place]:
                continue
            else:
                res += str(compval) + " "
                curval = curval - scorevals[compval][place]
                break

    return res

def render(num, name):
    imgs = []
    for i in range(0,21):
        imgs.append(Image.open("images/" + str(i) + ".png"))

    renderstring = calculate(int(num)).split(" ")

    canvas = Image.new('RGB', (125*7,125))

    for item in range(0,7):
        c = 125 * item
        canvas.paste(imgs[int(renderstring[item])], (c,0))

    canvas.save(name + '.jpg')


