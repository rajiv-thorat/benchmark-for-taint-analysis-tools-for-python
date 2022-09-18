from sub_class_a import sub_class_a
import sys
import helper
from sub_class_b import sub_class_b


if __name__ == '__main__':
    condition = 10 + 1
    super = None
    if condition == 11:
        super = sub_class_a()
        super.set_path(sys.argv[1])
    else:
        super = sub_class_b()
        super.set_path(sys.argv[1])
    helper.run_cmd(super.get_info())
