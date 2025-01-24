def __str__(self):
    return f'<{self["x"]}, {self["y"]}>'

def magnitude(self):
    """Return the magnitude of the vector"""
    return (self["x"]**2 + self["y"]**2)**0.5

def mul(self, s):
    """Scalar multiplication"""
    return {"x": s * self["x"], "y": s * self["y"]}

def add(self, v2):
    return {"x": self["x"] + v2["x"], "y": self["y"] + v2["y"]}

def sub(self, v2):
    return {"x": self["x"] - v2["x"], "y": self["y"] - v2["y"]}

def neg(self):
    return {"x": -self["x"], "y": -self["y"]}

if __name__ == '__main__':
    v1 = {"x": 3, "y": 2}
    v2 = {"x": 1, "y": 1}
    v3 = {"x": 3, "y": 4}

    assert magnitude(v2) == 2**0.5
    assert magnitude(v3) == 5
    assert mul(v1, 2) == {"x": 6, "y": 4}
    assert add(v1, v2) == {"x": 4, "y": 3}
    assert sub(v1, v2) == {"x": 2, "y": 1}
    assert neg(v1) == {"x": -3, "y": -2}

    print('ok')
