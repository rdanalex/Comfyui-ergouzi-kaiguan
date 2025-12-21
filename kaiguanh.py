import torch
import random
import json

class EGRWGL:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "hidden": {
                "run_count": ("INT", {
                    "default": 1,
                    "min": 1,
                    "max": 1000
                }),
            }
        }

    RETURN_TYPES = ()
    RETURN_NAMES = ("remaining_run_count",)
    FUNCTION = "manage_tasks"
    CATEGORY = "2🐕 Switch"
    
    def manage_tasks(self, run_count):
        return (run_count,)
NODE_CLASS_MAPPINGS = {
    "EGRWGL": EGRWGL
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "EGRWGL": "2🐕 Task Manager"
}