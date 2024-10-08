class ImageUtils:
  
    @staticmethod
    def calculate_resized_dimensions(img, max_height: int, max_width: int):
        width, height = img.size
        if height > max_height:
            # Calculate the scaling factor
            scale_factor = max_height / height
            # Calculate new dimensions
            new_width = int(width * scale_factor)
            new_height = int(height * scale_factor)
        elif width > max_width:
            scale_factor = max_width / width
            new_width = int(width * scale_factor)
            new_height = int(height * scale_factor)
        else:
            new_width = width
            new_height = height
            
        return new_width, new_height
