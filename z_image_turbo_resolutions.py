class ZImageTurboResolutions:
    """
    A custom node for selecting turbo-optimized image resolutions
    """
    
    # Resolution mappings with all ratio options
    RESOLUTIONS = {
        "1024": [
            "1024x1024 (1:1)",
            "1152x896 (9:7)",
            "896x1152 (7:9)",
            "1152x864 (4:3)",
            "864x1152 (3:4)",
            "1248x832 (3:2)",
            "832x1248 (2:3)",
            "1280x720 (16:9)",
            "720x1280 (9:16)",
            "1344x576 (21:9)",
            "576x1344 (9:21)"
        ],
        "1280": [
            "1280x1280 (1:1)",
            "1440x1120 (9:7)",
            "1120x1440 (7:9)",
            "1472x1104 (4:3)",
            "1104x1472 (3:4)",
            "1536x1024 (3:2)",
            "1024x1536 (2:3)",
            "1536x864 (16:9)",
            "864x1536 (9:16)",
            "1680x720 (21:9)",
            "720x1680 (9:21)"
        ],
        "1536": [
            "1536x1536 (1:1)",
            "1728x1344 (9:7)",
            "1344x1728 (7:9)",
            "1728x1296 (4:3)",
            "1296x1728 (3:4)",
            "1872x1248 (3:2)",
            "1248x1872 (2:3)",
            "2048x1152 (16:9)",
            "1152x2048 (9:16)",
            "2016x864 (21:9)",
            "864x2016 (9:21)"
        ]
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        # Get all resolution options
        resolution_options = list(cls.RESOLUTIONS.keys())
        
        # Get all ratio options (we'll show all, but filter in JS if needed)
        all_ratios = []
        for ratios in cls.RESOLUTIONS.values():
            all_ratios.extend(ratios)
        # Remove duplicates while preserving order
        all_ratios = list(dict.fromkeys(all_ratios))
        
        return {
            "required": {
                "resolution": (resolution_options, {"default": "1024"}),
                "ratio": (all_ratios, {"default": "1024x1024 (1:1)"}),
            },
        }
    
    RETURN_TYPES = ("INT", "INT", "INT")
    RETURN_NAMES = ("resolution", "width", "height")
    FUNCTION = "get_dimensions"
    CATEGORY = "image/resolution"
    
    def get_dimensions(self, resolution, ratio):
        """
        Parse the selected resolution and ratio to return dimensions
        """
        # Extract width and height from the ratio string (format: "1024x1024 (1:1)")
        dimensions = ratio.split(" ")[0]  # Get "1024x1024" part
        width, height = dimensions.split("x")
        
        # Convert to integers
        resolution_int = int(resolution)
        width_int = int(width)
        height_int = int(height)
        
        return (resolution_int, width_int, height_int)


# Node registration
NODE_CLASS_MAPPINGS = {
    "ZImageTurboResolutions": ZImageTurboResolutions
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ZImageTurboResolutions": "Z-Image-Turbo Resolutions"
}
