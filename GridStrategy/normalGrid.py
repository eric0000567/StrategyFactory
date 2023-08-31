# 一個簡單的網格策略
# 依照等比或等差的方式生成网格

import numpy as np
import pandas as pd

# createGrids: 生成网格
# use factory pattern

class Grids:
  def __init__(self, upperLimit, lowerLimit, gridNumber) -> None:
    self.upperLimit = upperLimit
    self.lowerLimit = lowerLimit
    self.gridNumber = gridNumber

