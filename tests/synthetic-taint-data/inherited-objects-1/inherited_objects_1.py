from sub_class_a import SubClassA
import sys
import helper
from sub_class_b import SubClassB


if __name__ == '__main__':
    condition = 10 + 1
    super = None
    if condition == 10:
        super = SubClassA()
        super.set_path(sys.argv[1])
    else:
        super = SubClassB()
        super.set_path(sys.argv[1])
    helper.run_cmd(super.get_info())
