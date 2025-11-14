# Image Optimization Guide

## Images to Optimize

### High Priority (Large Files)

1. **data/XinLI_profile.jpg** (2.3MB)
   - Current: 2.3MB
   - Target: ~100-200KB
   - Recommended dimensions: 400x400px (displayed at 140px, 2x for retina)

2. **images/XinLi.png** (293KB)
   - Current: 293KB
   - Target: ~50-100KB
   - Used for Open Graph/social sharing

3. **images/icon.png** (250KB)
   - Current: 250KB
   - Target: ~20-50KB
   - Favicon and Apple touch icon

## Optimization Methods

### Option 1: Online Tools (Easiest)
1. Visit https://squoosh.app/ or https://tinypng.com/
2. Upload each image
3. Adjust quality slider to ~80-85% for JPG, use lossy compression for PNG
4. Download and replace original files

### Option 2: Command Line (ImageMagick)
```bash
# Install ImageMagick
sudo apt-get install imagemagick

# Optimize JPG (profile photo)
convert data/XinLI_profile.jpg -strip -interlace Plane -quality 85% -resize 400x400 data/XinLI_profile_optimized.jpg

# Optimize PNG files
convert images/XinLi.png -strip -quality 85 images/XinLi_optimized.png
convert images/icon.png -strip -quality 85 -resize 192x192 images/icon_optimized.png
```

### Option 3: Python with Pillow
```bash
# Install Pillow
pip install Pillow

# Run optimization script
python3 scripts/optimize_images.py
```

### Option 4: Modern Formats (WebP)
Consider converting to WebP format for even better compression:
```bash
# Convert to WebP
cwebp -q 85 data/XinLI_profile.jpg -o data/XinLI_profile.webp
cwebp -q 85 images/XinLi.png -o images/XinLi.webp
```

Then use `<picture>` element for fallback:
```html
<picture>
  <source srcset="data/XinLI_profile.webp" type="image/webp">
  <img src="data/XinLI_profile.jpg" alt="...">
</picture>
```

## Expected Impact
- **Page Load Time**: Reduce by 2-3 seconds on 3G connections
- **Bandwidth**: Save ~2MB per page load
- **SEO**: Improved Core Web Vitals (LCP score)
- **User Experience**: Faster initial render
