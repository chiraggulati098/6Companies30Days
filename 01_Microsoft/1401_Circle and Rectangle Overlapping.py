class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        x_nearest = max(x1, min(x2, xCenter))
        y_nearest = max(y1, min(y2, yCenter))

        dx = x_nearest - xCenter
        dy = y_nearest - yCenter

        return (dx * dx) + (dy * dy) <= (radius * radius)